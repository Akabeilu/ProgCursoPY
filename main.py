import random

# Define o intervalo de números possíveis
min_num = 1
max_num = 50

# Gera um número aleatório dentro do intervalo
secret_num = random.randint(min_num, max_num)

# Inicializa o contador de tentativas
num_guesses = 0

# Loop principal do jogo
while True:
    # Pede ao jogador para adivinhar um número
    print(f"Adivinhe um número entre {min_num} e {max_num} (ou digite 'desistir' para sair): ")
    guess = input()

    # Verifica se o jogador desistiu
    if guess.lower() == 'desistir':
        print(f"O número secreto era {secret_num}. Obrigado por jogar!")
        break
    
    # Converte a entrada do jogador em um número inteiro
    guess = int(guess)
    
    # Verifica se o número adivinhado é igual ao número secreto
    if guess == secret_num:
        print("Parabéns, você acertou!")
        break
    else:
        # Dá uma dica para o jogador depois de duas tentativas
        num_guesses += 1
        if num_guesses == 2:
            if secret_num % 2 == 0:
                print("Dica: O número secreto é par.")
            else:
                print("Dica: O número secreto é ímpar.")
                
        # Dá uma dica para o jogador se o número adivinhado é maior ou menor
        if guess < secret_num:
            print("Mais")
        else:
            print("Menos")
