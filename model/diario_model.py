import sqlite3
from datetime import datetime

def inicializar_banco():
    conn = sqlite3.connect("diario.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS anotacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_hora TEXT,
            texto TEXT
        )
    ''')
    conn.commit()
    conn.close()

def adicionar_anotacao(texto):
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    conn = sqlite3.connect("diario.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO anotacoes (data_hora, texto) VALUES (?, ?)", (data_hora, texto))
    conn.commit()
    conn.close()

def ler_anotacoes():
    conn = sqlite3.connect("diario.db")
    cursor = conn.cursor()
    cursor.execute("SELECT data_hora, texto FROM anotacoes ORDER BY id ASC")
    registros = cursor.fetchall()
    conn.close()
    return registros
