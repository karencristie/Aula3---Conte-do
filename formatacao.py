nome = "Karen"
altura = 1.63
peso = 62
IMC=peso / altura**2
print(nome, "tem", altura, "de altura,", "pesa", peso,"kg e seu IMC é de",  IMC)

print(f'{nome} tem {altura} de altura, pesa {peso} kg e seu IMC é de {IMC:.2f}') #.2f formarta a quantidade de casas decimais - o f no inicio formata o texto 
print(f'{nome} tem {altura} de altura\npesa {peso} kg e seu IMC é de {IMC:.2f}') #.2f formarta a quantidade de casas decimais - o f no inicio formata o texto