from typing import List

from fastapi import APIRouter, Depends, Body, Path, Query, Response, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from api.config.connection import get_db
from pydantic_schemas.course import Course, CourseCreate, CoursePatch
from pydantic_schemas.sections import Section
from api.utils.sections import get_course_sections
from api.utils.users import get_user_by_id
from api.utils.courses import (
    create_db_course,
    delete_db_course,
    get_course_by_id,
    get_course_by_title,
    get_courses,
    patch_db_course,
)

courses_router = APIRouter()


@courses_router.get("/courses", response_model=List[Course])
async def read_courses(
    skip: int = Query(0, description="skip items in pagination"),
    limit: int = Query(100, description="limit items in pagination"),
    db_session: AsyncSession = Depends(get_db),
):
    """Get all courses list"""

    courses = await get_courses(db_session, skip=skip, limit=limit)

    return courses


@courses_router.get("/courses/{course_id}", response_model=Course)
async def find_course(
    course_id: int = Path(..., description="Course id to retrieve", gt=0),
    db_session: AsyncSession = Depends(get_db),
):
    """Get a course"""

    check_course_exists = await get_course_by_id(db_session, course_id=course_id)

    if check_course_exists is None:
        raise HTTPException(status_code=404, detail="Course not found")

    return check_course_exists


@courses_router.get("/courses/sections/{course_id}", response_model=List[Section])
async def read_course_sections(
    course_id: int = Path(..., description="Course id to retrieve sections", gt=0),
    db_session: AsyncSession = Depends(get_db),
):
    """Get course's sections"""

    check_course_exists = await get_course_by_id(db_session, course_id=course_id)

    if check_course_exists is None:
        raise HTTPException(status_code=404, detail="Course not found")

    course_sections_response = await get_course_sections(
        db_session, course_id=course_id
    )

    return course_sections_response


@courses_router.post("/courses", response_model=bool, status_code=201)
async def create_course(
    course: CourseCreate = Body(..., description="Course data to create"),
    db_session: AsyncSession = Depends(get_db),
):
    """Create a course"""

    check_course_exists = await get_course_by_title(
        db_session, course_title=course.title
    )

    if check_course_exists:
        raise HTTPException(status_code=400, detail="Course already exists!")

    check_user_exists = await get_user_by_id(db_session, user_id=course.user_id)

    if check_user_exists is None:
        raise HTTPException(status_code=404, detail="User not found")

    create_db_course_response = await create_db_course(db_session, course=course)

    return create_db_course_response


@courses_router.patch("/courses/{course_id}", status_code=204)
async def patch_course(
    course_id: int = Path(..., description="Course id to patch", gt=0),
    course: CoursePatch = Body(..., description="Course data to patch"),
    db_session: AsyncSession = Depends(get_db),
):
    """Patch a course"""

    check_course_exists = await get_course_by_id(db_session, course_id=course_id)

    if check_course_exists is None:
        raise HTTPException(status_code=404, detail="Course not found")

    await patch_db_course(db_session, course_id=course_id, course=course)

    return Response(status_code=204)


@courses_router.delete("/courses/{course_id}", status_code=204)
async def delete_course(
    course_id: int = Path(..., description="Course id to delete", gt=0),
    db_session: AsyncSession = Depends(get_db),
):
    """Delete a course"""

    check_course_exists = await get_course_by_id(db_session, course_id=course_id)

    if check_course_exists is None:
        raise HTTPException(status_code=404, detail="Course not found")

    await delete_db_course(db_session, course_id=course_id)

    return Response(status_code=204)
