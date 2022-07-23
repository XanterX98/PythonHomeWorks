"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import asyncio
from typing import List

import aiohttp
from loguru import logger

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(session: aiohttp.ClientSession, url: str) -> List[dict]:
    async with session.get(url) as response:
        data: List[dict] = await response.json()
        logger.info("got response for {} with status {} and data {}", url, response.status, data)
        return data


# async def get_users_data() -> List[dict]:
#     async with aiohttp.ClientSession() as session:
#         data = await fetch_json(session, USERS_DATA_URL)
#         return data
#
#
# async def get_posts_data() -> List[dict]:
#     async with aiohttp.ClientSession() as session:
#         data = await fetch_json(session, POSTS_DATA_URL)
#         return data
#
#
# async def main():
#     users = await get_users_data()
#     posts = await get_posts_data()
#     logger.info("done, users {!r}", users)
#     logger.info("done, posts {!r}", posts)
#
#
# if __name__ == '__main__':
#     # asyncio.run(demo_gather_results())
#
#     asyncio.run(main())
