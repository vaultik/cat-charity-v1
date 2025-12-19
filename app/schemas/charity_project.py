from datetime import datetime as dt
from typing import Optional

from pydantic import (
    BaseModel, ConfigDict, Field, NonNegativeInt, PositiveInt
)


class CharityProjectBase(BaseModel):
    name: str = Field(..., min_length=5, max_length=100)
    description: str = Field(..., min_length=10)
    full_amount: PositiveInt

    model_config = ConfigDict(extra='forbid')


class CharityProjectCreate(CharityProjectBase):
    pass


class CharityProjectDB(CharityProjectBase):
    id: int
    invested_amount: NonNegativeInt
    fully_invested: bool
    create_date: dt
    close_date: Optional[dt] = None

    model_config = ConfigDict(from_attributes=True)


class CharityProjectUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=5, max_length=100)
    description: Optional[str] = Field(None, min_length=10)
    full_amount: Optional[PositiveInt] = None

    model_config = ConfigDict(extra='forbid')
