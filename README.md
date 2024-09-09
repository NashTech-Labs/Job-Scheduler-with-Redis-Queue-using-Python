# Job Scheduler with Redis Queue

This project demonstrates how to use Redis Queue (RQ) to schedule jobs in a Python application. The provided code schedules a message to be displayed at a specified time and allows you to check the status of the scheduled job.

## Requirements

- Python 3.x
- Redis server
- `rq` Python library
- `redis` Python library

You can install the required Python libraries using pip:

```bash
pip install rq redis
```

## Running the Script

1. **Start Redis Server**: Make sure the Redis server is running.
2. **Run rq worked with schedular**: 
```bash
rq worker --with-scheduler
```
3. **Run the Scheduler Script**: Execute the `queued.py` script to schedule jobs and check their status.

```bash
python queued.py
```