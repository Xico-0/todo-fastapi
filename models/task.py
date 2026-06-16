from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime, Boolean, String
from datetime import datetime, timezone
from core.database import Base


class Task(Base):
    __tablename__ = "tasks"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    description: Mapped[str | None] = mapped_column(String(256))
    completed: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(
                DateTime, 
                default=lambda: datetime.now(timezone.utc))
    
