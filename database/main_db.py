import asyncpg

from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST


class AsyncpgDB:

    @staticmethod
    async def __executor(query, *args):
        connection = await asyncpg.connect(
            database=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
        await connection.execute(query, *args)
        await connection.close()

