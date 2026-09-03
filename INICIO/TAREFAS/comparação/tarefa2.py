saldo = 100.0
preco_produto = 40.0
cupom_desconto = 10.0

preco_final = preco_produto - cupom_desconto
if saldo >= preco_final:
    saldo = saldo - preco_final
    print(f"Compra realizada com sucesso! Saldo restante: {saldo}")
else:
    print("Saldo insuficiente.")