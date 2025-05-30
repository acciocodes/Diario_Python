from datetime import datetime
import os

class DiarioModel:
    def __init__(self, arquivo='diario.txt'):
        self.arquivo = arquivo

    def adicionar_entrada(self, texto):
        data_hora = datetime.now().strftime("[%d/%m/%Y %H:%M:%S]")
        with open(self.arquivo, 'a', encoding='utf-8') as f:
            f.write(f"{data_hora} {texto}\n")

    def ler_entradas(self):
        if not os.path.exists(self.arquivo):
            return None
        with open(self.arquivo, 'r', encoding='utf-8') as f:
            return f.readlines()
