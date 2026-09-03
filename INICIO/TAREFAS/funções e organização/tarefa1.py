def checar_saldo(saldo, preco):
    if saldo >= preco:
        return True
    else:
        return False

aprovado = checar_saldo(200, 150)
print(aprovado)