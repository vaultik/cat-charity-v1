from datetime import datetime as dt
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import charity_project_crud, donation_crud
from app.models import CharityProject, Donation
from app.schemas import CharityProjectUpdate


async def run_investing_process(
        obj: 'CharityProject | Donation',
        session: AsyncSession
):
    await session.flush()
    projects = await charity_project_crud.get_objs_for_investing(session)
    donations = await donation_crud.get_objs_for_investing(session)

    investing_process(projects, donations)

    await session.commit()
    await session.refresh(obj)
    return obj


def closed_obj(obj) -> None:
    obj.invested_amount = obj.full_amount
    obj.fully_invested = True
    obj.close_date = dt.now()


def investing_process(
        projects: List[CharityProject],
        donations: List[Donation]
):
    while donations and projects:
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


def process_edit_project(
        project: CharityProject,
        obj_in: CharityProjectUpdate
) -> None:
    if project.invested_amount == obj_in.full_amount:
        closed_obj(project)
