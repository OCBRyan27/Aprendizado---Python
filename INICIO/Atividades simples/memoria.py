historico_conversas = []


print("--- CHAT COM MEMORIA (digite 'sair' para encerrar) ---")
while True:
    mensagem = input("Voce: ")

    if mensagem.lower() == "sair":
        print("Tchau mestre! Salvei todas as conversas na memoria")
        break

    elif mensagem.lower() == "memoria":
        if len(historico_conversas) == 0:
            print("Sys: Ainda nao tenho nada na memoria, mestre.")
        else:
            for item in historico_conversas:
                print("-", item)
                print("============================\n")

    else:
        historico_conversas.append(mensagem)
        print("Sys: Entendi! Guardei isso na memoria, mestre!")