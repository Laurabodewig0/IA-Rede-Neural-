import sqlite3

# Conecta ao banco de dados (ou cria um novo arquivo)
conn = sqlite3.connect("test.db")

# Cria um cursor para executar comandos SQL
cursor = conn.cursor()

# Cria uma tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
)
""")

# Insere dados
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alexandre", 30))

# Salva as alterações
conn.commit()

# Consulta os dados
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

# Fecha a conexão
conn.close()
