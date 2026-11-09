
from sqlalchemy import text
from config.database import engine

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version()"))

        print("Connection successful!")
        print(result.scalar())

except Exception as e:
    print("Connection failed:", e)

finally:
    engine.dispose()
