# prompt para o input
card_number = input("card number: ")

# validar
if len(card_number) < 12 or len(card_number) > 19:
    print("invalid")
else:
    '''
    1 - Retire o último dígito do número. Ele é o verificador;
    2 - Escreva os números na ordem inversa;
    3 - Multiplique os dígitos das casas ímpares por 2 e subtraia 9 de todos os resultados maiores que 9;
    4 - Some todos os números;
    5 - O dígito verificador (aquele do passo 1) é o número que você precisa somar a todos os outros números somados pra obter um módulo 10.
    '''

    step1 = card_number[0:-1] # remove o último dígito
    print("Passo 1 - ",step1)

    step2 = step1[::-1] # inverte a ordem dos números
    print("Passo 2 - ", step2)

    step3 = list(step2) # para iniciar o passo 3
    for index, num in enumerate(step2):
        if index % 2 == 0: # índices pares referem-se a índices ímpares do número do cartão (Ex. [0] = 1º dígito, [2] = 3º dígito ...)
            value = int(num) * 2 if int(num) * 2 < 9 else int(num) * 2 - 9
            step3[index] = str(value)
    print("Passo 3 - ", step3)

    step4 = 0
    for num in step3:
        step4 += int(num) # soma todos os números
    print("Passo 4 - ", step4)

    step5 = step4 + int(card_number[-1])
    print("Passo 5 - ", step5) # adiciona o último número do número original do cartão

    if step5 % 10 == 0 and step5 > 0: # verifica se a divisão por 10 da valor exato
        print("valid")
    else:
        print("invalid")