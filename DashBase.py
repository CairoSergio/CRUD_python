import sqlite3

banco = sqlite3.connect('DashBase.db')

cursor = banco.cursor() 

cursor.execute("""
CREATE TABLE IF NOT EXISTS pessoas(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    senha TEXT NOT NULL,
    numero_conta TEXT NOT NULL,
    password_reset  NUMERIC NOT NULL,
    status TEXT NOT NULL
);
""")


print('conectado ao banco de dados')


banco.commit()

