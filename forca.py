def jogar():
	print("Bem vindo ao Jogo da Forca!")
	print("")

	palavra_secreta = "cachorro"

	enforcou = False
	acertou = False

	while(not enforcou and not acertou):

		chute = input("Qual a letra? ")

		index = 0
		for letra in palavra_secreta:
			if(chute == letra):
				print("Você acertou a letra: {}, na posição {}".format(chute, index))
			index = index + 1			

		print("")
		print("Jogando...")

	print("Fim do jogo!")

if(__name__ == "__main__"):
	jogar()