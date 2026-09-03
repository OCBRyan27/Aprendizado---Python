saldo = 100.0

while saldo > 0:
    preco = 30.0
    if saldo >= preco:
        saldo = saldo - preco
        print(f"Compra feita! Saldo restante: {saldo}")
    else:
        print("Saldo insuficiente para a compra.")
        break