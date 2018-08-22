def jogar():
	print("Bem vindo ao Jogo da Forca!")
	print("")

	palavra_secreta = "cachorro"

	enforcou = False
	acertou = False

	contador = 0

	while(not enforcou and not acertou and contador != 5):

		chute = input("Qual a letra? ").strip()

		index = 0
		for letra in palavra_secreta:
			if(chute.lower() == letra):
				print("Você acertou a letra: {}, na posição {}".format(chute, index))
			index = index + 1

		contador = contador + 1

		print("")
		print("Jogando...")
		print("")

		if(contador == 5):
			reposta = input("Digite a Palavra Final: ").strip()
			print("")
			if(reposta == palavra_secreta):
				print("Parabéns, a palavra secreta é {}".format(palavra_secreta))
			else:
				print("Você errou, volte depois!")
				

	print("Fim do jogo!")

if(__name__ == "__main__"):
	jogar()