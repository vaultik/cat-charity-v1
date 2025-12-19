from sqlalchemy import CheckConstraint, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base, CommonMixin


class CharityProject(CommonMixin, Base):
    name: Mapped[str] = mapped_column(
        String(100),
        CheckConstraint('length(name) >= 5'),
        unique=True
    )
    description: Mapped[str] = mapped_column(
        Text,
        CheckConstraint('LENGTH(description) >= 10')
    )
