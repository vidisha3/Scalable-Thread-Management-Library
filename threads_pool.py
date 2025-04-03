import threading
import queue

class ThreadPool:
    def __init__(self, num_threads):
        """Initialize the ThreadPool with the given number of worker threads."""
        self.num_threads = num_threads
        self.task_queue = queue.Queue()
        self.threads = []
        self.shutdown_flag = threading.Event()

        # Create worker threads
        for _ in range(num_threads):
            thread = threading.Thread(target=self.worker)
            thread.start()
            self.threads.append(thread)

    def worker(self):
        """Worker function that picks tasks from the queue and executes them."""
        while not self.shutdown_flag.is_set():
            try:
                task, args = self.task_queue.get(timeout=1)
                print(f"[{threading.current_thread().name}] Executing {task.__name__} with args {args}")
                task(*args)
                self.task_queue.task_done()
            except queue.Empty:
                continue

    def submit(self, func, *args):
        """Add a new task to the queue."""
        self.task_queue.put((func, args))

    def scale_threads(self, new_thread_count):
        """Scale the number of threads dynamically."""
        if new_thread_count > self.num_threads:
            for _ in range(new_thread_count - self.num_threads):
                thread = threading.Thread(target=self.worker)
                thread.start()
                self.threads.append(thread)
        elif new_thread_count < self.num_threads:
            for _ in range(self.num_threads - new_thread_count):
                self.shutdown_flag.set()
                self.threads.pop().join()

        self.num_threads = new_thread_count
        self.shutdown_flag.clear()

    def shutdown(self):
        """Gracefully shut down the thread pool."""
        self.shutdown_flag.set()
        for thread in self.threads:
            thread.join()
        print("Thread pool shut down successfully.")
