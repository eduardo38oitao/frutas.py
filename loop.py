
print ("*************************")
print ("AS MELHORES 4 FRUTAS")
print ("*************************")

def listar_invertida(lista):


    for indice, valor in enumerate(reversed(lista)):
        print(f"Posição {indice}: {valor}")


        
    print("***********")
    print("Fim")
    print("***********")

frutas = ["Maçã", "Banana", "Caju", "Manga"]


listar_invertida(frutas)

        