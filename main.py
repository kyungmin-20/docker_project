import uvicorn
from fastapi import FastAPI

from courses import course_router

app = FastAPI(title="수강기록 API")

app.include_router(course_router)


@app.get("/")
async def welcome():
    return {"msg": "수강기록 API 서버입니다."}


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
