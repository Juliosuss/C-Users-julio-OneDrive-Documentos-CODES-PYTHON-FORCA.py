import os
import random
vocabulario = ["alimento", "apartamento", 'linguagem', 'computador']
palavra = random.choice(vocabulario)

nome = input ("Qual seu nome? ")
print (f"Seja bem vindo(a) {nome}!!!")
print (f"Regras do Jogo: {nome}, você receberá uma palavra.")
print ("Você deve digitar a letra que acha que contém na palavra.")
print ("Você pode errar 6 vezes.")
print ('Boa sorte!!!')


print (input('\npressione enter para iniciar o game'))
os.system ('cls')

for letra in palavra:
    print('_', end= ' ')


chances = 6
tentativas = []

while chances > 0:
    print(tentativas)
    print("Chances: ",chances)

    for letra in palavra:
        if letra in tentativas:
            print(letra, end = ' ')
        else:
            print('_', end= ' ')

    palpite = input("\nDigite seu palpite ou 'SAIR' para sair do programa!").lower()
    
    if palpite == "sair":
        break
    elif not palpite.isalpha() or len(palpite) > 1:
        print("Opção inválida!")
        continue
    elif palpite in tentativas:
        print("Você já tentou essa letra, por favor, tente outra!")
        continue
   
    tentativas.append(palpite)
   
    if palpite in palavra:
        print("Muito bem!!!")

        if set(palavra).issubset(set(tentativas)):
            break
    else:
         chances = chances -1
         print("Infelizmente, você errou! ")



if chances == 0:
    print("Perdeu, Game over!!! a palavra era", palavra )
elif palpite == "sair":
    print('obrigado por jogar, até a próxima!')
else:
    print("Parabéns, você acertou! a palavra é", palavra )

input ('\n pressione enter para sair')







'''import random
import sys
from re import S
from select import select
vocabulario = ["alimento", "apartamento", 'linguagem', 'computador']
palavra = random.choice(vocabulario)

nome = input ("Qual seu nome? ")
print (f"Seja bem vindo(a) {nome}!!!")
print (f"Regras do Jogo: {nome}, você receberá uma palavra.")
print ("Você deve digitar a letra que acha que contém na palavra.")
print ("Você pode errar 6 vezes.")
print ('Boa sorte!!!')

for letra in palavra:
	print('_', end= ' ')


chances = 6
alfabeto = list("abcdefghijklmnopqrstuvwxyz")
tentativas = []

while chances > 0:
	print(tentativas)
	print("Chances: ",chances)

	for letra in palavra:
		if letra in tentativas:
			print(letra, end = ' ')
		else:
			print('_', end= ' ')

	palpite = input("\nDigite seu palpite ou 'SAIR' para sair do programa!").lower()
	if palpite == "sair":
		break	
	elif palpite not in alfabeto or palpite == '':
		print("Opção inválida")
		continue	
	elif palpite in tentativas:
		print("Você já tentou essa letra, por favor, tente outra!")
		continue
	tentativas.append(palpite)
	if palpite in palavra:
		print("Muito bem!!!")
	else:
         chances = chances -1
         print("Infelizmente, você errou! ")
               

            
if chances == 0:
        print("Perdeu, Game over!!! a palavra era", palavra )
elif set(palavra).issubset(set(tentativas)):
        print("Parabéns, você acertou! a palavra é", palavra )     '''        
    



#         elif set(palavra).issubset(set(tentativas)):
#		     print("Parabéns, você acertou! a palavra é", palavra )

 		


'''
palavras = ["alimento", "apartamento", 'linguagem', 'computador']
palavra = random.choice(palavras)
print(palavra)
q = 0
while q <= (len (palavra)):
    s = palavra
    l = list(s)
    l[q] = "_"
    s = "".join(l)
    print(s)
    #sys.stdout.write (s[q])
    q=q+1
    
    

from random import choice

vocabulario = ["esquistossomose", "naftalina", "ribonucleico", "idiossincratico", "fagocitose", "quinquagesimo"]

palavra = choice(vocabulario)

print("JOGO DA FORCA 1.0\n")
print("Bem vindo ao JOGO DA FORCA. Boa sorte!\n")

chances = 6
alfabeto = list("abdcefghijklmnopqrstuvwxyz")
tentativas = []

while True:
	print(tentativas)
	print("Chances: ",chances)

	for letra in palavra:
		if letra in tentativas:
			print(letra, end = ' ')
		else:
			print('_', end= ' ')

	palpite = input("\nDigite seu palpite ou 'SAIR' para sair do programa!").lower()
	if palpite == "sair":
		break	
	elif palpite not in alfabeto or palpite == '':
		print("Hein!? Fala direito! Isso não é uma letra!")
		continue	
	elif palpite in tentativas:
		print("Você é desmemoriado ou o quê!? Você já tentou essa letra. Tente outra!")
		continue
	tentativas.append(palpite)
	if palpite in palavra:
		print("ACERTÔ, MIZERAVI!")
	else: chances-=1
	print("Errou feio, errou rude!")
                
	if chances == 0:
     		print("Perdeu, pivete! Game over!!! >:)") 
                break
	elif set(palavra).issubset(set(tentativas)):
		print("Parabéns, você acertou! Weeee are the champions, my frieeeend!")
 		break
    else:

import random

def imprime_mensagem_abertura():
    nome = input ("Qual seu nome? ")
    print (f"Seja bem vindo(a) {nome}!!!")
    print (f"Regras do Jogo: {nome}, você receberá uma palavra.")
    print ("Você deve digitar a letra que acha que contém na palavra.")
    print ("Você pode errar 6 vezes.")
    print ('Boa sorte!!!')

def carrega_palavra_secreta():
    palavras = ["alimento", "apartamento", 'linguagem', 'computador']
    

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def jogar():

    imprime_mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0
    letras_faltando = len(letras_acertadas)

    print(letras_acertadas)
    while (not acertou and not enforcou):

        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
            letras_faltando = str(letras_acertadas.count('_'))
            if (letras_faltando == "0"):
                print("PARABÉNS!! Você encontrou todas as letras formando a palavra '{}'".format(palavra_secreta.upper()))
        else:
            erros += 1
            print(letras_acertadas)
            print('Ainda faltam acertar {} letras'.format(letras_faltando))
            print('Você ainda tem {} tentativas'.format(7-erros))
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    print("Fim do jogo")

if(__name__ == '__main__'):
    jogar()'''