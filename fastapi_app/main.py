from contextlib import asynccontextmanager
from apscheduler.jobstores.redis import RedisJobStore
from fastapi import FastAPI
import uvicorn
from fastapi_app.api_v1.routers import router_v1
from fastapi_app.core.config import settings
from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler(
    jobstores={'redis': RedisJobStore(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=1,
                                      jobs_key="apschedulers.default_jobs",
                                      run_times_key="apschedulers.default_run_times")}
)

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    scheduler.shutdown()


app.include_router(router=router_v1, prefix=settings.API_V1_PREFIX)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
