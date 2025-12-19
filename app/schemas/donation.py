from datetime import datetime as dt
from typing import Optional

from pydantic import (
    BaseModel, ConfigDict, NonNegativeInt, PositiveInt
)


class DonationBase(BaseModel):
    full_amount: PositiveInt
    comment: Optional[str] = None

    model_config = ConfigDict(extra='forbid')


class DonationCreate(DonationBase):
    pass


class DonationDB(DonationBase):
    id: int
    create_date: dt

    model_config = ConfigDict(from_attributes=True)


class DonationFullInfoDB(DonationDB):
    invested_amount: NonNegativeInt
    fully_invested: bool
    close_date: Optional[dt] = None
