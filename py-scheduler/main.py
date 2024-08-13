from fastapi import FastAPI
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores.memory import MemoryJobStore

# Create a FastAPI app instance
app = FastAPI()


# configuration

jobstores = {
    'default': MemoryJobStore()
}

# Initialize an AsyncIOScheduler with the jobstore
scheduler = AsyncIOScheduler(jobstores=jobstores,)

# defining Scheduler
# Defining Scheduled Jobs We define sample scheduled jobs using different scheduling methods:

# job running every 10 seconds


@scheduler.scheduled_job(trigger='interval', seconds=10)
def scheduled_job() -> None:
    print('This job is run every 10 seconds.')


# Job running at a specific date and time
@scheduler.scheduled_job(trigger='date', run_date='2024-07-21 13:16:00')
def scheduled_job_2() -> None:
    print("scheduled_job_2")

# Job running daily at 23:44:00


@scheduler.scheduled_job(trigger='cron', day_of_week='mon-sun', hour=23, minute=44, second=0)
def scheduled_job_3() -> None:
    print("scheduled_job_3")


# Handling

# Handling Application Events We register event handlers for application startup and shutdown to manage the scheduler’s lifecycle:

@app.on_event("startup")
async def startup_event():
    scheduler.start()


@app.on_event("shutdown")
async def shutdown_event():
    scheduler.shutdown()


# Endpoint and putting all together

@app.get(path="/")
async def read_root() -> dict[str, str]:
    return {"message": " Hello, World!"}
