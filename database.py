from environs import Env
from pymysql import connect, cursors

env = Env()
env.read_env()

DB_NAME=env.str("DB_NAME")
DB_USER=env.str("DB_USER")   
DB_PASSWORD=env.str("DB_PASSWORD")
DB_PORT=env.int("DB_PORT") 
DB_HOST=env.str("DB_HOST")

def execute(sql: str, params: tuple = ()):
    connection = connect(
        db=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT,
        host=DB_HOST,
        cursorclass=cursors.DictCursor
    )
    cursor = connection.cursor()
    cursor.execute(sql, params)
    connection.commit()
    connection.close()


def register_user(telegram_id: str, fullname: str) -> None:
    sql = """
        INSERT INTO users (telegram_id, fullname)
        VALUES (%s, %s)
    """
    execute(sql, (telegram_id, fullname))
