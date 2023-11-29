import sqlite3

base = sqlite3.connect("server.db")

curs = base.cursor()

curs.execute("""CREATE TABLE IF NOT EXISTS users (
             user_id BIGINT,
             registred INT
)""")

base.commit()

curs.execute(f"SELECT user_id FROM users WHERE user_id = {234706554}")
if curs.fetchone() is None:
    curs.execute("INSERT INTO users VALUES (?, ?)", (234706554, 1))
    base.commit()


async def get_reg(user_id):
    values = curs.execute(f"SELECT registred FROM users WHERE user_id = {user_id}")
    for value in values:
        return value[0]
    return 0