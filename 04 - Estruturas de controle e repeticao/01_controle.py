idade = input("Digite sua idade: ")
sexo = input(
    "Escolha uma opção:\n"
    "(M) - Masculino\n"
    "(F) - Feminino\n"
    "Sua resposta: "
)

if sexo.upper() == "M":
    if int(idade) >= 65:
        print("Parabéns! Sua aposentadoria será concedida.")
    else:
        print(
            f"Sua vez ainda não chegou. Aguarde mais {65 - int(idade)} anos.")
elif sexo.upper() == "F":
    if int(idade) >= 60:
        print("Parabéns! Sua aposentadoria será concedida.")
    else:
        print(
            f"Sua vez ainda não chegou. Aguarde mais {60 - int(idade)} anos.")
else:
    print("Resposta inválida! Tente novamente.")
