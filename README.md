# 📝 Projeto: Diário Digital

Este projeto foi desenvolvido como atividade prática da disciplina de Programação com o professor **Ranyere Lima** no curso de **Engenharia de Software**.

O **Diário Digital** é um programa em Python que permite ao usuário escrever anotações do dia a dia, salvando tudo com data e hora. A cada início do programa, uma **frase motivacional** é exibida para deixar o uso mais leve e divertido. Tudo foi desenvolvido com organização em **MVC** e aplicação de boas práticas de programação.

---

## 🚀 Funcionalidades

✅ Escrever novas entradas no diário  
✅ Visualizar todas as entradas salvas  
✅ Exibir uma frase motivacional ao iniciar  
✅ Salvar todas as anotações em `diario.txt` com data e hora  
✅ Código separado em camadas (MVC)

---

## 🧱 Estrutura do Projeto

```bash
diario_python/
├── main.py
├── controller/
│   └── diario_controller.py
├── model/
│   └── diario_model.py
├── view/
│   └── diario_view.py
└── diario.txt  # arquivo gerado automaticamente
