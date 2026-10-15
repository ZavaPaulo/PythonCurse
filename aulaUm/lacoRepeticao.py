#LACO DE REPETICAO
contador = 10
while contador >= 1:
    print(f"Coontagem autual: {contador}")
    contador -= 1

senha = "senha"
tentativa_senha = ""
while senha != tentativa_senha:
    tentativa_senha = input("Digite sua senha: ")
    if tentativa_senha != senha:
        print("SENHA INCORRETA!")
    else:
        print("Acertou")

compras = ["Arroz", "Feijão", "Leite", "Pão"]
for item in compras:
    print(f"Você precisa comprar: {item}")

numeros = [2, 4, 7, 1, 87, 3, 12, 7, 4, 2]
for numero in numeros:
    if numero % 2 == 0:
        continue
    print(numero)