from thread_pool import ThreadPool
from tasks import sample_task, fast_task
import time

if __name__ == "__main__":
    print("Initializing Thread Pool with 4 threads...")

    pool = ThreadPool(4)

    # Submitting CPU-bound tasks
    for i in range(10):
        pool.submit(sample_task, i)

    # Submitting I/O-bound tasks
    for msg in ["Task A", "Task B", "Task C"]:
        pool.submit(fast_task, msg)

    time.sleep(5)

    print("\nScaling up to 6 threads...")
    pool.scale_threads(6)

    # Adding more tasks
    for i in range(10, 15):
        pool.submit(sample_task, i)

    time.sleep(5)

    print("\nShutting down the pool...")
    pool.shutdown()
