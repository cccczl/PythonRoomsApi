from fastapi import FastAPI

from api.users import users_router
from api.courses import courses_router
from api.sections import sections_router

app = FastAPI(
    title="Fast API LMS",
    description="LMS for managing students and courses.",
    version="0.0.1",
    contact={
        "name": "Paulo",
        "email": "paulosilvadosreis2057@gmail.com",
    },
    license_info={
        "name": "MIT",
    },
)

app.include_router(users_router)
app.include_router(courses_router)
app.include_router(sections_router)
