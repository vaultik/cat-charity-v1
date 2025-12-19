from datetime import datetime as dt
from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import CharityProject, Donation
from app.schemas import CharityProjectUpdate


def closed_obj(obj) -> None:
    obj.invested_amount = obj.full_amount
    obj.fully_invested = True
    obj.close_date = dt.now()


async def get_objs(
        model, session: AsyncSession
) -> List['CharityProject | Donation']:
    data = await session.execute(
        select(model)
        .where(model.fully_invested.is_(False))
        .order_by(model.create_date, model.id)
    )
    return data.scalars().all()


async def investing_process(
        session: AsyncSession
):
    donations = await get_objs(Donation, session)
    projects = await get_objs(CharityProject, session)
    while projects and donations:
        free_donation = donations[0].full_amount - donations[0].invested_amount
        need_project = projects[0].full_amount - projects[0].invested_amount
        if free_donation > need_project:
            closed_obj(projects[0])
            projects.pop(0)
            donations[0].invested_amount += need_project
        elif free_donation == need_project:
            closed_obj(projects[0])
            projects.pop(0)
            closed_obj(donations[0])
            donations.pop(0)
        else:
            projects[0].invested_amount += free_donation
            closed_obj(donations[0])
            donations.pop(0)
    await session.commit()


def process_edit_project(
        project: CharityProject,
        obj_in: CharityProjectUpdate
) -> None:
    if project.invested_amount == obj_in.full_amount:
        closed_obj(project)
