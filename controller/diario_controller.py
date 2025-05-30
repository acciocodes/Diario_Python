from model.diario_model import DiarioModel
from view.diario_view import DiarioView

class DiarioController:
    def __init__(self):
        self.model = DiarioModel()
        self.view = DiarioView()
        self.view.mostrar_frase_motivacional()  # Mostra a frase ao iniciar o diário

    def executar(self):
        while True:
            self.view.mostrar_menu()
            opcao = input("Escolha uma opção: ")
            if opcao == '1':
                texto = self.view.solicitar_entrada()
                self.model.adicionar_entrada(texto)
                print("Entrada salva com sucesso!")
            elif opcao == '2':
                entradas = self.model.ler_entradas()
                self.view.mostrar_entradas(entradas)
            elif opcao == '3':
                print("Encerrando o diário. Até logo!")
                break
            else:
                print("Opção inválida.")
