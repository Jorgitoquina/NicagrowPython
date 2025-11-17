import pyodbc

try:
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=NicaGrowDB;trusted_connection=yes"
    )
    print("✅ Conexión exitosa")
    conn.close()
except Exception as e:
    print("❌ Error:", e)