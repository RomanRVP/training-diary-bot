from database.main_db import AsyncpgDB


class AsyncpgGymTable(AsyncpgDB):

    @staticmethod
    async def create_categories_table():
        await AsyncpgGymTable.__executor(
            """
            CREATE TABLE IF NOT EXISTS gym_categories 
            (
            category_id serial PRIMARY KEY,
            category_name VARCHAR (50) NOT NULL,
            category_parent_id BIGINT REFERENCES gym_categories (category_id),
            category_is_active BOOLEAN DEFAULT TRUE,
            user_tg_id BIGINT NOT NULL 
            )
            """
        )

    @staticmethod
    async def create_exercises_table():
        await AsyncpgGymTable.__executor(
            """
            CREATE TABLE IF NOT EXISTS gym_exercises
            (
            exercise_id serial PRIMARY KEY,
            exercise_name VARCHAR (50) NOT NULL,
            category_id BIGINT REFERENCES gym_categories (category_id),
            exercise_is_active BOOLEAN DEFAULT TRUE,
            user_tg_id BIGINT NOT NULL 
            )
            """
        )

    @staticmethod
    async def create_completed_exercises_table():
        await AsyncpgGymTable.__executor(
            """
            CREATE TABLE IF NOT EXISTS gym_completed_exercises
            (
            specific_exercise_id serial PRIMARY KEY,
            exercise_id BIGINT REFERENCES gym_exercises (exercise_id),
            exercise_name VARCHAR (50),
            specific_exercise_repeat NUMERIC (2, 1),
            specific_exercise_weight NUMERIC (3, 2),
            specific_exercise_date DATE NOT NULL,
            specific_exercise_time TIME NOT NULL,
            user_tg_id BIGINT NOT NULL 
            )
            """
        )
