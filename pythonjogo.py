nome = input("Digite o nome do herói: ")
xp = int(input("Digite a quantidade de XP do herói: "))

class input:
    def __init__(self):
        pass

    def method(self):
        raise NotImplementedError

classe = input("Digite a classe do herói: ")
moedas = int(input("Digite a quantidade de moedas do herói: "))

while xp < 0:
    print("A quantidade de XP não pode ser negativa.")
    xp = int(input("Digite novamente a quantidade de XP: "))

while moedas < 0:
    print("A quantidade de moedas não pode ser negativa.")
    moedas = int(input("Digite novamente suas moedas: "))

if xp <= 1000:
    nivel = "Ferro"
elif xp <= 2000:
    nivel = "Bronze"
elif xp <= 5000:
    nivel = "Prata e Ouro"
elif xp <= 8000:
    nivel = "Platina e Diamante"
elif xp <= 9000:
    nivel = "Ascendente"
elif xp >= 10000:
    nivel = "Radiante"
else:
    nivel = "Não classificado"

niveis = {
    "Ferro": 1,
    "Bronze": 2,
    "Prata e Ouro": 3,
    "Platina e Diamante": 4,
    "Ascendente": 5,
    "Radiante": 6
}

loja = [
    {"nome": "Pocao de vida", "preco": 20, "nivel": "Ferro"},
    {"nome": "Espada de ferro", "preco": 50, "nivel": "Bronze"},
    {"nome": "Escudo reforcado", "preco": 100, "nivel": "Prata e Ouro"},
    {"nome": "Armadura de diamante", "preco": 250, "nivel": "Platina e Diamante"},
    {"nome": "Espada lendaria", "preco": 500, "nivel": "Ascendente"},
    {"nome": "Arma divina", "preco": 1000, "nivel": "Radiante"}
]

print(f"\nO heroi de nome {nome} da classe {classe} "
      f"esta no nivel {nivel} com {moedas} moedas.")

entrar = input("\nGostaria de entrar na loja? (sim/nao): ").lower()

while entrar == "sim":

    print("\n========== LOJA DO HEROI ==========")
    print(f"Suas moedas: {moedas}")
    print(f"Seu nivel: {nivel}")
    print("\nItens disponiveis:")

    for i, item in enumerate(loja, start=1):
        print(
            f"{i} - {item['nome']} | "
            f"Preco: {item['preco']} moedas | "
            f"Nivel necessario: {item['nivel']}"
        )

    print("0 - Sair da loja")

    try:
        escolha = int(input("\nDigite o numero do item que deseja comprar: "))
    except ValueError:
        print("Digite um numero valido.")
        continue

    if escolha == 0:
        print("Voce saiu da loja.")
        break

    elif escolha < 1 or escolha > len(loja):
        print("Opcao invalida.")

    else:
        item = loja[escolha - 1]

        nivel_heroi = niveis.get(nivel, 0)
        nivel_necessario = niveis[item["nivel"]]

        if nivel_heroi < nivel_necessario:
            print(
                f"Voce precisa ser nivel {item['nivel']} "
                f"para comprar esse item."
            )

        elif moedas >= item["preco"]:
            moedas -= item["preco"]

            print(f"\nCompra realizada: {item['nome']}!")
            print(f"Voce gastou {item['preco']} moedas.")
            print(f"Saldo atualizado: {moedas} moedas.")

        else:
            print("Voce nao tem moedas suficientes.")
            print(f"Preco do item: {item['preco']} moedas.")
            print(f"Suas moedas: {moedas}.")

    entrar = input(
        "\nDeseja continuar comprando? (sim/nao): "
    ).lower()

print("\n========== RESUMO DO HEROI ==========")
print(f"Nome: {nome}")
print(f"Classe: {classe}")
print(f"Nivel: {nivel}")
print(f"XP: {xp}")
print(f"Moedas restantes: {moedas}")
print("Siga em frente em sua jornada!")