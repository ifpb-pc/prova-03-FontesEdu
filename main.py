def q1(cidades):
    nova_lista = []

    for i in cidades:
        idade = cidades[i]
        if idade > 100:
            nova_lista.append(i)

    return nova_lista

def q2(lista1, lista2):
    nova_lista = []
    soma = 0

    for i in lista1:
        if i > 0:
            soma +=i
            nova_lista.append(i)

    for j in lista2:
        if j >0:
            soma +=j
            nova_lista.append(j)

    nova_lista.sort()

    return soma, nova_lista

def q3(valores):
    return [],[]

def q4(valores):
    return []

def main():
    # Teste as questões que você desenvolveu manualmente:
    idades = {
        "João Pessoa": 432,
        "Campina Grande": 325,
        "Santa Rita": 68,
        "Patos": 289,
        "Bayeux": 54,
        "Sousa": 178,
        "Cajazeiras": 201,
        "Cabedelo": 45,
        "Guarabira": 122,
        "Areia": 177,
    }
    resultado = q1(idades)
    print("q1:", resultado)


    lista1 = [3, -5, 12, 0, -8, 7]
    lista2 = [-2, 10, -1, 6, -4, 9]
    resultado = q2(lista1, lista2)
    print("q2:", resultado)



if __name__ == "__main__":
    main()


