import os
from contextlib import asynccontextmanager

import dill
from apscheduler.jobstores.memory import MemoryJobStore
from fastapi import FastAPI
import uvicorn
from fastapi_app.api_v1.routers import router_v1
from fastapi_app.core.config import settings
from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler()
scheduler.add_jobstore(jobstore=MemoryJobStore(), alias='memory')


@asynccontextmanager
async def lifespan(app: FastAPI):
    print(os.stat('data.pkl').st_size)
    if os.stat('data.pkl').st_size != 0:
        with open('data.pkl', 'rb') as file:
            loaded_object = dill.load(file)
            print(loaded_object)
        for job in loaded_object:
            scheduler.add_job(func=job.func,
                              jobstore="memory",
                              trigger=job.trigger,
                              args=job.args)
        scheduler.start()
    yield
    if os.stat('data.pkl').st_size != 0:
        with open('data.pkl', 'wb') as file:
            pass
    with open('data.pkl', 'wb') as file:
        dill.dump(scheduler.get_jobs('memory'), file)
    if scheduler.state == 1:
        scheduler.shutdown()


app = FastAPI(lifespan=lifespan)


app.include_router(router=router_v1, prefix=settings.API_V1_PREFIX)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
