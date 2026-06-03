from pydantic import BaseModel


class Course(BaseModel):
    course_name: str
    year: str
    semester: str
    grade: str
