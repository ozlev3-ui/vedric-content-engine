import os
import time


def run() -> None:
    interval = int(os.getenv("WORKER_INTERVAL_SECONDS", "10"))
    while True:
        print("Worker heartbeat", flush=True)
        time.sleep(interval)


if __name__ == "__main__":
    run()
