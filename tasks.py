import time

def sample_task(n):
    """Simulates a CPU-bound task."""
    print(f"Processing task with value: {n}")
    time.sleep(1)

def fast_task(msg):
    """Simulates a fast I/O-bound task."""
    print(f"Message: {msg}")
    time.sleep(0.5)
