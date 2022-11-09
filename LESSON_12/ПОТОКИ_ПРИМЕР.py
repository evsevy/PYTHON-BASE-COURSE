"""
# СИНХРОННЫЙ ВАРИАНТ

import queue
 
def task(name, work_queue):
    if work_queue.empty():
        print(f"Task {name} nothing to do")
    else:
        while not work_queue.empty():
            count = work_queue.get()
            total = 0
            print(f"Task {name} running")
            for x in range(count):
                total += 1
            print(f"Task {name} total: {total}")
 
def main():
    
    # Создание очереди работы
    work_queue = queue.Queue()
 
    # Помещение работы в очередь
    for work in [15, 10, 5, 2]:
        work_queue.put(work)
 
    # Создание нескольких синхронных задач
    tasks = [(task, "One", work_queue), (task, "Two", work_queue)]
 
    # Запуск задач
    for t, n, q in tasks:
        t(n, q)
 
if __name__ == "__main__":
    main()
    
#Task one and Task two не комбинированы! Отсутствует переключение
    
# С ПЕРЕКЛЮЧЕНИЕМ

import queue
 
 
def task(name, queue):
    while not queue.empty():
        count = queue.get()
        total = 0
        print(f"Task {name} running")
        for x in range(count):
            total += 1
            yield
        print(f"Task {name} total: {total}")
 
 
def main():
    
   # Это основная точка входа в программу
    
    # Создание очереди работы
    work_queue = queue.Queue()
 
    # Размещение работы в очереди
    for work in [15, 10, 5, 2]:
        work_queue.put(work)
 
    # Создание задач
    tasks = [task("One", work_queue), task("Two", work_queue)]
 
    # Запуск задач
    done = False
    while not done:
        for t in tasks:
            try:
                next(t)
            except StopIteration:
                tasks.remove(t)
            if len(tasks) == 0:
                done = True
 
 
if __name__ == "__main__":
    main()

# АСИНХРОННЫЙ ВАРИАНТ

import asyncio
from codetiming import Timer
 
 
async def task(name, work_queue):
    timer = Timer(text=f"Task {name} elapsed time: {{:.1f}}")
    while not work_queue.empty():
        delay = await work_queue.get()
        print(f"Task {name} running")
        timer.start()
        await asyncio.sleep(delay)
        timer.stop()

 
 
async def main():
    
    #Это главная точка входа для главной программы
    
    # Создание очереди работы
    work_queue = asyncio.Queue()
 
    # Помещение работы в очередь
    for work in [15, 10, 5, 2]:
        await work_queue.put(work)
 
    # Запуск задач
    with Timer(text="\nTotal elapsed time: {:.1f}"):
        await asyncio.gather(
            asyncio.create_task(task("One", work_queue)),
            asyncio.create_task(task("Two", work_queue)),
        )
 
 
if __name__ == "__main__":
    asyncio.run(main())
    
#################################
    
import asyncio
import aiohttp
from codetiming import Timer
 
 
async def task(name, work_queue):
    timer = Timer(text=f"Task {name} elapsed time: {{:.1f}}")
    async with aiohttp.ClientSession() as session:
        while not work_queue.empty():
            url = await work_queue.get()
            print(f"Task {name} getting URL: {url}")
            timer.start()
            
            async with session.get(url) as response:
                await response.text()
            timer.stop()
 
 
async def main():
    
    # Создание очереди работы
    work_queue = asyncio.Queue()
 
    # Помещение работы в очередь
    for url in [
        "http://google.com",
        "http://yahoo.com",
        "http://linkedin.com",
        "http://apple.com",
        "http://microsoft.com",
        "http://facebook.com",
        "http://twitter.com",
    ]:
        await work_queue.put(url)
 
    # Запуск задач
    with Timer(text="\nTotal elapsed time: {:.1f}"):
        await asyncio.gather(
            asyncio.create_task(task("One", work_queue)),
            asyncio.create_task(task("Two", work_queue)),
        )
 
 
if __name__ == "__main__":
    asyncio.run(main())
    """
