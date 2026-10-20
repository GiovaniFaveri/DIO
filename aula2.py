
def calcular_rankeadas(vitorias, derrotas):
    saldo_vitorias = vitorias - derrotas

    if vitorias <= 10:
        nivel = "Ferro"
    elif vitorias <= 20:
        nivel = "Bronze"
    elif vitorias <= 50:
        nivel = "Prata"
    elif vitorias <= 80:
        nivel = "Ouro"
    elif vitorias <= 90:
        nivel = "Diamante"
    elif vitorias <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"

    return saldo_vitorias, nivel


while True:
    try:
        vitorias = int(input("Digite a quantidade de vitórias: "))
        derrotas = int(input("Digite a quantidade de derrotas: "))

        if vitorias < 0 or derrotas < 0:
            print("Digite valores iguais ou maiores que zero.")
            continue

        break

    except ValueError:
        print("Digite apenas números inteiros.")

saldo, nivel = calcular_rankeadas(vitorias, derrotas)

print(f"O Herói tem de saldo de {saldo} está no nível de {nivel}")
