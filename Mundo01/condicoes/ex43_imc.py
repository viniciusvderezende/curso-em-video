peso = float(input('Digite o seu peso atual: '))
altura = float(input('Digite a sua altura: '))
imc = peso / altura ** 2
if imc < 18.5:
    print(f'Seu IMC é de {imc:.1f}. Você está abaixo do peso ideal.')
elif imc <= 24.9:
    print(f'Seu IMC é de {imc:.1f}. Você está no seu peso ideal.')
elif imc <= 29.9:
    print(f'Seu IMC é de {imc:.1f}. Você está com sobrepeso.')
elif imc <= 34.9:
    print(f'Seu IMC é de {imc:.1f}. Você está com obesidade grau I.')
elif imc <= 39.9:
    print(f'Seu IMC é de {imc:.1f}. Você está com obesidade grau II.')
else:
    print(f'Seu IMC é de {imc:.1f}. Você está com obesidade grau III.')