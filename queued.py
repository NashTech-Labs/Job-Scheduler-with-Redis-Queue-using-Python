from rq import Queue
from redis import Redis
from myfile import schedule_my_msg
from datetime import datetime
redis_conn = Redis(host="localhost",port=6379)
q = Queue(connection=redis_conn)  

def schedular():
    # this message will schedule for 2024 10 september at 12:30
    job = q.enqueue_at(datetime(2024, 10, 9, 12, 30),schedule_my_msg)

    return job.get_id()

def get_status_of_job(job_id):
    job = q.fetch_job(job_id)
    return {"Job ID":job._status , "result":job.result}
