from app.database.database import engine

try:

    connection = engine.connect()

    print("Connexion PostgreSQL réussie")

    connection.close()

except Exception as e:

    print(e)