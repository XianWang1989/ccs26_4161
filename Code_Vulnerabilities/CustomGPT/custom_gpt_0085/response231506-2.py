
import threading

def process_jobs(queue):
    while True:
        job = queue.get()
        if job is None:  # Exit condition
            break
        print(f"Processing job: {job}")

# In the start_client function, right after initializing job_queue
threading.Thread(target=process_jobs, args=(job_queue,), daemon=True).start()
