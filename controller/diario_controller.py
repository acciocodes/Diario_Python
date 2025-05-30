from model import diario_model
from view import diario_view
import requests

def frase_motivacional():
    try:
        resposta = requests.get("https://zenquotes.io/api/random")
        if resposta.status_code == 200:
            dados = resposta.json()
            return f"Frase do dia: \"{dados[0]['q']}\" - {dados[0]['a']}"
    except:
        return "Não foi possível carregar a frase do dia."
    return ""

def executar():
    diario_model.inicializar_banco()
    print(frase_motivacional())
    while True:
        diario_view.exibir_menu()
        opcao = diario_view.obter_entrada()

        if opcao == "1":
            texto = diario_view.obter_texto_anotacao()
            diario_model.adicionar_anotacao(texto)
            diario_view.exibir_mensagem("Anotação salva com sucesso.")
        elif opcao == "2":
            anotacoes = diario_model.ler_anotacoes()
            diario_view.exibir_anotacoes(anotacoes)
        elif opcao == "3":
            diario_view.exibir_mensagem("Encerrando o programa.")
            break
        else:
            diario_view.exibir_mensagem("Opção inválida. Tente novamente.")
