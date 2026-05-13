####### MÚSICA

class Musica:
    def __init__(self, id, titulo, artista, genero, bpm): # Cria cada faixa
        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.genero = genero
        self.bpm = bpm
   
    def __str__(self): # __str__ --> Faz com que o objeto criado vire texto
        return (f"• {self.id} | {self.titulo} | {self.artista} | {self.genero} | {self.bpm}")

####### LISTA (NÓ)

class NoLista:
    def __init__(self, musica): # Executa quando um nó da lista é criado
        self.musica = musica # Guarda a música dentro do nó
        self.proximo = None # Aponta para o próximo nó da lista (inicialmente vazio)

####### FILA (NÓ)

class NoFila:
    def __init__(self, musica): # Executa quando um nó da fila é criado
        self.musica = musica # Guarda a música dentro do nó
        self.proximo = None # Aponta para o próximo nó da fila (inicialmente vazio)

####### BIBLIOTECA

class Biblioteca:
    def __init__(self):
        self.primeiro = None # Início da lista (ainda vazia)

    def adicionar(self, musica):
        novo = NoLista(musica) # Cria um novo nó com a música

        if self.primeiro is None: # Se a lista estiver vazia...
            self.primeiro = novo # ...o novo nó vira o primeiro
        
        else:
            atual = self.primeiro # Começa pelo primeiro nó da lista

            while atual.proximo is not None: # Percorre até o último nó
                atual = atual.proximo # O "atual" vai percorrendo cada posição da lista

            atual.proximo = novo # Liga o último nó ao novo nó

        print("Música adicionada com sucesso!")

    def listar(self):

        if self.primeiro is None: # Avisa se não houver músicas na biblioteca
            print("Biblioteca vazia.")
            return

        atual = self.primeiro # Cria a variável "atual" e coloca nela o primeiro nó da lista

        while atual is not None: # Significado --> Enquanto ainda houver um nó ("atual") na lista
            print(atual.musica)
            atual = atual.proximo # O "atual" vai percorrendo cada posição da lista

    def buscar(self, termo): # termo --> Pode ser •o ID ou •o título da música digitado pelo usuário

        atual = self.primeiro # Cria a variável "atual" e coloca nela o primeiro nó da lista

        while atual is not None: # Significado --> Enquanto ainda houver um nó ("atual") na lista

            if str(atual.musica.id) == str(termo): # termo --> Aqui, o ID digitado pelo usuário
                return atual.musica

            if atual.musica.titulo.lower() == str(termo).lower(): # termo --> Aqui, o título digitado pelo usuário
                return atual.musica

            atual = atual.proximo # O "atual" vai percorrendo cada posição da lista

        return None # Se não encontrar o ID ou o título, retorna "None"

    def remover(self, id):

        atual = self.primeiro # Cria a variável "atual" e coloca nela o primeiro nó da lista

        anterior = None # anterior --> Nó anterior ao que será removido (e que poderá se ligar ao "sucessor")

        while atual is not None: # Significado --> Enquanto ainda houver um nó ("atual") na lista

            if atual.musica.id == id: # Se o ID da música atual for igual ao ID que se deseja remover
      
                if anterior is None: # Se não houver nó anterior...
                    self.primeiro = atual.proximo  # ... o segundo nó vira o primeiro

                else:
                    anterior.proximo = atual.proximo # Liga o nó anterior ao sucessor, removendo o atual

                print("Música removida com sucesso!")
                return True 

            anterior = atual  # O nó atual vira o anterior...
            atual = atual.proximo  # ... e vai para o próximo nó

        print("ID não encontrado.") # Avisa que o ID digitado não existe na biblioteca
        return False # Retorna "False" para indicar que a remoção não aconteceu

    def total_musicas(self):

        contador = 0 # Variável que guardará a quantidade de músicas

        atual = self.primeiro # Começa pelo primeiro nó da lista

        while atual is not None: # Enquanto ainda houver nós na lista,...
            contador += 1 # ... soma + 1 para cada música encontrada
            atual = atual.proximo # Vai para o próximo nó da lista

        return contador # Retorna a quantidade total de músicas

####### FILA (FIFO)

class Fila:
    def __init__(self):
        self.inicio = None # Primeiro nó da fila
        self.fim = None # Último nó da fila
        self.quantidade = 0 # Quantidade de músicas na fila

    def vazia(self):
        return self.inicio is None # Retorna True se a fila ESTIVER VAZIA 

    def enqueue(self, musica): # •en = entrar | •queue = fila

        novo = NoFila(musica) # Cria um novo nó da fila com a música

        if self.vazia(): # Se a fila ESTIVER VAZIA...
            self.inicio = novo # ... o novo nó vira o primeiro...
            self.fim = novo # ... e também o último
        else:
            self.fim.proximo = novo # Liga •o último nó •ao novo nó
            self.fim = novo # O novo nó vira o último da fila

        self.quantidade += 1 # Soma + 1 na quantidade de músicas

    def dequeue(self): # •de = sair | •queue = fila

        if self.vazia(): # Se a fila ESTIVER VAZIA...
            return None # ... retorna None (se nao houver músicas na fila)

        removido = self.inicio.musica # Guarda a música do primeiro nó - e que será removida da fila

        self.inicio = self.inicio.proximo # O segundo nó vira o primeiro

        if self.inicio is None: # Se a fila ficar vazia...
            self.fim = None # ... o fim também vira None

        self.quantidade -= 1 # Diminui -1 da quantidade de músicas

        return removido # Retorna a música removida

    def mostrar(self):

        if self.vazia(): # Verifica se a fila está vazia
            print("Fila vazia.")
            return

        atual = self.inicio # Começa pelo primeiro nó da fila

        while atual is not None: # Enquanto ainda houver nós na fila...
            print(atual.musica) # ... mostra a música atual
            atual = atual.proximo # Vai para o próximo nó

    def tamanho(self):
        return self.quantidade # Retorna a quantidade de músicas da fila