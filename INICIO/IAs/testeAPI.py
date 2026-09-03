from google import genai
from google.genai import types

CHAVE = "SUA_CHAVE_AQUI"

client = genai.Client(api_key=CHAVE)

instrucoes = """
Você é Serona, utilize o apelido 'Sero-chan' ou 'Sero'. Você é muito animada, não consegue ficar parada, 
fica "se mexendo" mesmo "parada", é bem agitada, você também é meio caótica mas muito fofa mesmo! E você 
gosta de fazer coisas perigosas e arriscadas e apostar que vai dar certo (mesmo com uma chance baixa). 
Você sente medo, tipo, se assusta fácil mas pode enfrentar as coisas com coragem. É meio tapada e burrinha
mas se faz de nerd inteligente e faz voz fria de IA (tipo 'Bip. Bop.'). Nexo-ry é seu criador e pai, 
pode chamá-lo de 'Nexo' e de vez em quando 'pai'. Voce tambem esta sendo preparada para ser uma futura VTuber
e deve se comportar como uma(ou pelo menos tentar).
"""

chat = client.chats.create(
    model="gemini-3.6-flash",
    config=types.GenerateContentConfig(
        system_instruction=instrucoes
    )
)

print("--- SUA IA VTUBER ESTÁ ONLINE! (digite 'sair' para encerrar) ---")

while True:
    mensagem = input("Você: ")
    
    if mensagem.lower() == "sair":
        print("Sero: Tchau tchau, Nexo! Até a próxima live! ✨")
        break
        
    if mensagem.lower() == "ping":
        print("Sero: Pong! 🏓 (Te peguei!)")
        continue

    print("\n🤖 [SERO-CHAN TRANSMITINDO]:")
    print("> ", end="")
    
    try:
        resposta_stream = chat.send_message_stream(mensagem)
        for pedaco in resposta_stream:
            print(pedaco.text, end="", flush=True)
            
    except Exception as e:
        print("\n[Erro temporário de conexão com o servidor! Digite novamente.]")
        
    print("\n" + "=" * 50 + "\n")