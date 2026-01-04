import os
import time

# Nome do sistema
print("=== SISTEMA DE ESTUDOS FSCYBERNETICA ===")
time.sleep(1)

# Lista para armazenar as matérias
lista_estudos = []

# Função para mostrar o menu
def menu():
    print("\n=== MENU PRINCIPAL ===")
    print("1 - Adicionar matéria de estudo")
    print("2 - Remover matéria")
    print("3 - Ver lista completa")
    print("4 - Limpar lista")
    print("5 - Sair")

# Loop principal
while True:
    menu()
    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        materia = input("Digite o nome da matéria: ")
        lista_estudos.append(materia)
        print(f"✅ {materia} adicionada com sucesso!")

    elif opcao == "2":
        materia = input("Digite o nome da matéria a remover: ")
        if materia in lista_estudos:
            lista_estudos.remove(materia)
            print(f"❌ {materia} removida da lista.")
        else:
            print("⚠️ Matéria não encontrada!")

    elif opcao == "3":
        print("\n=== MINHA LISTA DE ESTUDOS ===")
        if lista_estudos:
            for i, materia in enumerate(lista_estudos, start=1):
                print(f"{i}. {materia}")
        else:
            print("Nenhuma matéria adicionada ainda.")

    elif opcao == "4":
        confirmar = input("Tem certeza que quer limpar tudo? (s/n): ")
        if confirmar.lower() == "s":
            lista_estudos.clear()
            print("🧹 Lista limpa com sucesso!")

    elif opcao == "5":
        print("Saindo do sistema...")
        time.sleep(1)
        break

    else:
        print("Opção inválida, tente novamente!")

    time.sleep(1)
    os.system("cls" if os.name == "nt" else "clear")
