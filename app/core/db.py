from datetime import datetime as dt
from typing import Optional

from sqlalchemy import (
    Boolean, CheckConstraint, DateTime, Integer
)
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import (
    DeclarativeBase, Mapped, declared_attr, mapped_column
)

from app.core.config import settings


class Base(DeclarativeBase):
    pass


class CommonMixin:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    full_amount: Mapped[int] = mapped_column(
        Integer,
        CheckConstraint('full_amount > 0')
    )
    invested_amount: Mapped[int] = mapped_column(Integer, default=0)
    fully_invested: Mapped[bool] = mapped_column(Boolean, default=False)
    create_date: Mapped[dt] = mapped_column(
        DateTime, index=True, default=dt.now
    )
    close_date: Mapped[Optional[dt]] = mapped_column(DateTime)
    __abstract__ = True


engine = create_async_engine(settings.database_url)
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session():
    async with AsyncSessionLocal() as async_session:
        yield async_session
