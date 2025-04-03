# Scalable-Thread-Management-Library
This project implements a Scalable Thread Pool in Python to efficiently manage and execute multiple tasks in parallel. It is useful for handling both CPU-bound (e.g., calculations, data processing) and I/O-bound (e.g., file operations, network requests) tasks. The thread pool allows dynamic scaling, meaning we can increase or decrease the number of worker threads based on demand.

How the Project Works

    1. Initialization of the Thread Pool
    The ThreadPool class is created with a specified number of worker threads.
    
    A task queue is maintained to store incoming tasks.
    
    Each worker thread continuously fetches and executes tasks from the queue.
    
    Example: Creating a Thread Pool
    
    pool = ThreadPool(4)  # Creates a thread pool with 4 threads
    Here, 4 threads are created, and each thread waits for tasks to process.
