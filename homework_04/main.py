"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio
import aiohttp
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

import models
from jsonplaceholder_requests import fetch_json, USERS_DATA_URL, POSTS_DATA_URL


async def create_tables():

    async with models.async_engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.drop_all)
        await conn.run_sync(models.Base.metadata.create_all)


async def create_users(session: AsyncSession, users: List[dict]) -> None:
    for user in users:
        user_model = models.User(
            id=user['id'],
            name=user['name'],
            username=user['username'],
            email=user['email'],
        )
        session.add(user_model)


async def create_posts(session: AsyncSession, posts: List[dict]) -> None:
    for post in posts:
        post_model = models.Post(
            id=post['id'],
            user_id=post['userId'],
            title=post['title'],
            body=post['body'],
        )
        session.add(post_model)


async def async_main():
    await create_tables()

    async with aiohttp.ClientSession() as ClientSession:  # type: ClientSession
        users_data, posts_data = await asyncio.gather(
            fetch_json(ClientSession, USERS_DATA_URL),
            fetch_json(ClientSession, POSTS_DATA_URL),
        )

    async with models.Session() as session:   # type: AsyncSession
        await create_users(session, users_data)
        await create_posts(session, posts_data)
        await session.commit()
        await session.close()


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
