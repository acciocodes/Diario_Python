import requests

class DiarioView:
    @staticmethod
    def mostrar_frase_motivacional():
        try:
            resposta = requests.get("https://zenquotes.io/api/random")
            if resposta.status_code == 200:
                dados = resposta.json()[0]
                frase = f'"{dados["q"]}" — {dados["a"]}'
                print("\n✨ Frase do dia:\n" + frase + "\n")
            else:
                print("Não foi possível carregar a frase motivacional.")
        except Exception as e:
            print(f"Erro ao buscar frase motivacional: {e}")

    @staticmethod
    def mostrar_menu():
        print("\n=== MENU DO DIÁRIO ===")
        print("1 - Escrever nova entrada")
        print("2 - Ler todas as entradas")
        print("3 - Sair")

    @staticmethod
    def solicitar_entrada():
        return input("Digite sua anotação: ")

    @staticmethod
    def mostrar_entradas(entradas):
        if not entradas:
            print("O diário está vazio.")
        else:
            print("\n=== ENTRADAS DO DIÁRIO ===")
            for linha in entradas:
                print(linha.strip())
