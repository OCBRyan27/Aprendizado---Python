print("--- CHAT INICIADO (digite 'sair' para encerrar) ---")
while True:
    mensagem = input("Você: ")
    if mensagem.lower() == "sair":
        print("Sys: Ate logo! Foi muito legal conversar com voce!")
        break
    elif "quem e voce?" in mensagem.lower():
        print("Sys: Eu sou Sys, seu prototipo da sua futura VTuber!")
    else:
        print("Sys: Desculpe, mestre. Ainda estou aprendendo a responder a isso!")