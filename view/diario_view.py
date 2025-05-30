def exibir_menu():
    print("\n--- Diário Digital ---")
    print("1. Escrever nova anotação")
    print("2. Ler anotações")
    print("3. Sair")

def obter_entrada():
    return input("Digite sua escolha: ")

def exibir_mensagem(msg):
    print(msg)

def exibir_anotacoes(anotacoes):
    if not anotacoes:
        print("O diário está vazio.")
    else:
        for data_hora, texto in anotacoes:
            print(f"[{data_hora}] {texto}")

def obter_texto_anotacao():
    return input("Digite sua anotação: ")
