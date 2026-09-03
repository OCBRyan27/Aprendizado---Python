meus_jogos = [
    {"título": "Undertale", "zerado": True},
    {"título": "Deltarune", "zerado": False},
    {"título": "Zenless Zone Zero", "zerado": False}
]

for jogo in meus_jogos:
    print(f"O jogo {jogo['título']}, está zerado? {jogo['zerado']}")