class Musica:
    def __init__(self, id, titulo, artista, genero, bpm): # Cria cada faixa
        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.genero = genero
        self.bpm = bpm
   
    def __str__(self): # __str__ --> Faz com que o objeto criado vire texto
        return (f"• {self.id} | {self.titulo} | {self.artista} | {self.genero} | {self.bpm}") # os () não são obrigatórios