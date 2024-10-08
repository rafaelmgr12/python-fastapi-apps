import asyncio
from aiocache import cached, SimpleMemoryCache


@cached(ttl=10, cache=SimpleMemoryCache)
async def get_factorial(n: int):
    await asyncio.sleep(2)
    if n == 1:
        return 1
    return n * await get_factorial(n-1)