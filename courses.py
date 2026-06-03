import json
import os

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from model import Course

course_router = APIRouter()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "courses.json")


def load_courses():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, list):
            return []
        return data
    except (json.JSONDecodeError, OSError):
        return []


def save_courses(courses):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(courses, f, ensure_ascii=False, indent=2)


@course_router.get("/courses")
async def get_courses():
    return load_courses()


@course_router.post("/courses")
async def add_course(course: Course):
    try:
        courses = load_courses()
        courses.append(course.model_dump())
        save_courses(courses)
        return {"message": "과목이 추가되었습니다.", "course": course.model_dump()}
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"message": "과목 추가 중 오류가 발생했습니다.", "detail": str(e)},
        )
