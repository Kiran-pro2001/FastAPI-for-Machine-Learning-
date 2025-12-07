# Asynchronoys Programming 

import time 
from timeit import default_timer as timer 
import asyncio



async def run_task(name, seconds):
    print(f"{name} started at : {timer()}")
    await asyncio.sleep(seconds) # delay
    print(f"{name} completed at : {timer()}")



async def main():
    start = timer()
    # all asynchronous tasks 
    await asyncio.gather(
        run_task("Task 1", 2),
        run_task("Task 2", 1),
        run_task("Task 3",3)
    )
    print(f"\nTotal Time Taken : {timer() - start:.2f} Seconds")


asyncio.run(main())