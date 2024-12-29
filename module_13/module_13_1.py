import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    for i in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {i} шар')
    print(f'Силач {name} закончил соревнования')

async def start_tournament():
    await asyncio.gather(start_strongman('Вася', 3),
                         start_strongman('Костя', 4),
                         start_strongman('Егор', 5))

asyncio.run(start_tournament())