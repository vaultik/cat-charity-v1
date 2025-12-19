from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud import donation_crud
from app.schemas import (
    DonationCreate, DonationDB, DonationFullInfoDB
)
from app.services import run_investing_process

router = APIRouter()
SessionDep = Annotated[AsyncSession, Depends(get_async_session)]


@router.get(
    '/',
    response_model=list[DonationFullInfoDB],
    response_model_exclude_none=True,
    summary='Получить список всех пожертвований',
    description='Получает список всех пожертвований '
                'в проекты для сбора средств.',
    response_description='Список пожертвований'
)
async def get_all_donations(
        session: SessionDep
):
    return await donation_crud.get_multi(session)


@router.post(
    '/',
    response_model=DonationDB,
    response_model_exclude_none=True,
    summary='Создать пожертвование',
    description='Создает новое пожертвование в проекты для сбора средств.',
    response_description='Данные созданного проекта'
)
async def create_donation(
        donation: DonationCreate,
        session: SessionDep
):
    new_donation = await donation_crud.create(
        donation, session, True
    )
    new_donation = await run_investing_process(new_donation, session)
    return new_donation
