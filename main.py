from classes import Biblioteca, Fila, Musica

# # # # # # #   M E N U   P R I N C I P A L

def menu():

    biblioteca = Biblioteca() # Cria a biblioteca de músicas

    # Humor
    #   •Relaxar        - Tranquilo     --> 1 até 80 BPM
    #   •Concentração   - Focar         --> 81 até 120 BPM
    #   •Agitado        - Animar        --> 121 até 160 BPM
    #   •Intenso        - Treinar       --> 161 BPM ou mais

### Músicas bônus
    
    biblioteca.adicionar(Musica(1, "The Album", "Jive Bunny and The Mastermixers", "Agitado", 140))
                                
    biblioteca.adicionar(Musica(2, "It's Oh So Quiet", "Björk", "Agitado", 130))

    biblioteca.adicionar(Musica(3, "Alright", "Supergrass", "Agitado", 145))

    biblioteca.adicionar(Musica(4, "El Noi de la Mare", "Miguel Llobet", "Tranquilo", 60))

    biblioteca.adicionar(Musica(5, "Margarida", "Toninho Carrasqueira (Pixinguinha)", "Tranquilo", 72))

    biblioteca.adicionar(Musica(6, "Mariana", "Yamandu Costa", "Tranquilo", 78))

    biblioteca.adicionar(Musica(7, "Prelude C Major", "Bobby McFerrin (Johann Sebastian Bach)", "Tranquilo", 65))

    biblioteca.adicionar(Musica(8, "Gonna Fly Now", "Bill Conti", "Concentração", 95))
    
    biblioteca.adicionar(Musica(9, "What a Feeling", "Irene Cara", "Concentração", 104))

    biblioteca.adicionar(Musica(10, "(I've Had) The Time of My Life", "Bill Medley e Jennifer Warnes", "Intenso", 170))

    biblioteca.adicionar(Musica(11, "One", "Apocalyptica Inquisition Symphony (Metallica)", "Intenso", 180))


    fila_relax = Fila() # Cria as filas de humor
    fila_foco = Fila()
    fila_animada = Fila()
    fila_treino = Fila()

       
    historico = Fila() # Guarda músicas reproduzidas
    
    proximo_codigo = 12 # Próximo ID das músicas adicionadas

    while True: # Loop principal do sistema
        
        print("\n========== PLAYLIST ==========") # Mostra o menu
        print("1 - Adicionar música")
        print("2 - Remover música")
        print("3 - Buscar música")
        print("4 - Exibir biblioteca")
        print("5 - Criar filas por humor")
        print("6 - Reproduzir música")
        print("7 - Mostrar fila")
        print("8 - Histórico")
        print("9 - Estatísticas")
        print("0 - Sair")

        opcao = input("Escolha: ")

# # # # # # #   1 - A D I C I O N A R   M Ú S I C A

        if opcao == "1":

            titulo = input("Título: ") # Pede os dados da música
            
            artista = input("Artista: ")

            genero = input("Gênero: ")

            bpm_texto = input("BPM: ")

           
            if not bpm_texto.isdigit():
            # •bpm_texto --> valor digitado pelo usuário | •isdigit --> Verifica se o texto contém apenas números
                print("Digite um BPM válido.")
                continue

            bpm = int(bpm_texto)

            if bpm <= 0: # Verifica se o BPM é maior que zero
                print("O BPM deve ser maior que zero.")
                continue
           
            musica = Musica( # Cria a música
                proximo_codigo,
                titulo,
                artista,
                genero,
                bpm
            )

            biblioteca.adicionar(musica) # Adiciona a música criada acima na biblioteca
           
            proximo_codigo += 1 # Atualiza o próximo ID

# # # # # # #   2 - R E M O V E R   M Ú S I C A

        elif opcao == "2":

            codigo = input("Digite o ID: ") # Pede o ID da música que será removida

            if codigo.isdigit(): # Verifica se o usuário digitou apenas números
                biblioteca.remover(int(codigo)) # Converte o texto para número e remove a música
            
            else:
                print("ID inválido.") # Mostra erro se o usuário digitar letras ou caracteres inválidos

# # # # # # #   3 - B U S C A R   M Ú S I C A

        elif opcao == "3":

            termo = input("Digite o ID ou título: ") # Pede •o ID ou •o título da música

            resultado = biblioteca.buscar(termo) # Busca a música (termo) na biblioteca

            if resultado: # Verifica se a música foi encontrada
        
                print("\nMúsica encontrada:")
                print(resultado) # Mostra os dados da música encontrada

            else:
                print("Música não encontrada.")

# # # # # # #   4 - E X I B I R   B I B L I O T E C A
        
        elif opcao == "4":

            biblioteca.listar() # Mostra todas as músicas

# # # # # # #   5 - C R I A R   F I L A S   P O R   H U M O R

        elif opcao == "5":

            fila_relax = Fila() # Reinicia as filas
            fila_foco = Fila()
            fila_animada = Fila()
            fila_treino = Fila()

            atual = biblioteca.primeiro # Começa pelo primeiro nó da biblioteca

            if atual is None:
                print("Biblioteca vazia.")
            
            else:

                while atual is not None: # Enquanto ainda houver músicas na biblioteca

                    musica = atual.musica # Guarda a música atual

                    if musica.bpm <= 80: # Se BPM de 1 até 80...
                        fila_relax.enqueue(musica) # ... adiciona na fila Relaxar

                    elif musica.bpm <= 120: # Se BPM de 81 até 120...
                        fila_foco.enqueue(musica) # ... adiciona na fila Focar

                    elif musica.bpm <= 160: # Se BPM de 121 até 160...
                        fila_animada.enqueue(musica) # ... adiciona na fila Animar

                    else: # Se BPM acima de 160...
                        fila_treino.enqueue(musica) # ... adiciona na fila Treinar

                    atual = atual.proximo # Vai para o próximo nó da lista

                print("Filas criadas com sucesso!")

# # # # # # #   6 - R E P R O D U Z I R   M Ú S I C A
        
        elif opcao == "6":

            print("\n1 - Relaxar") # Escolha da fila
            print("2 - Focar")
            print("3 - Animar")
            print("4 - Treinar")

            escolha = input("Escolha a fila: ")

            fila = None

            if escolha == "1": # Qual fila será usada???
                fila = fila_relax

            elif escolha == "2":
                fila = fila_foco

            elif escolha == "3":
                fila = fila_animada

            elif escolha == "4":
                fila = fila_treino


            if fila is None: # Verifica se a opção existe
                print("Opção inválida.")
                    
            elif fila.vazia(): # Verifica se a fila está vazia
                print("Fila vazia.")


            else:
                tocando = fila.dequeue() # Remove a primeira música da fila (•de = sair | •queue = fila)

                print("\nTocando agora:")
                print(tocando)

                historico.enqueue(tocando) # Guarda no histórico (•en = entrar | •queue = fila)

# # # # # # #   7 - M O S T R A R   F I L A

        elif opcao == "7":

            print("\n1 - Relaxar") # Mostra opções de filas para o usuário
            print("2 - Focar")
            print("3 - Animar")
            print("4 - Treinar")

            escolha = input("Escolha: ") # Usuário escolhe qual fila quer ver

            if escolha == "1":
                fila_relax.mostrar() # Mostra músicas da fila Relaxar

            elif escolha == "2":
                fila_foco.mostrar() # Mostra músicas da fila Focar

            elif escolha == "3":
                fila_animada.mostrar() # Mostra músicas da fila Animar

            elif escolha == "4":
                fila_treino.mostrar() # Mostra músicas da fila Treinar

            else:
                print("Opção inválida.") # Caso o usuário digite algo errado


# # # # # # #   8 - H I S T Ó R I C O

        elif opcao == "8":

            print("\n===== HISTÓRICO =====")

            if historico.vazia(): # Verifica se existe histórico
                print("Nenhuma música reproduzida.")

            else:
                historico.mostrar() # Mostra todas as músicas já tocadas

# # # # # # #   9 - E S T A T Í S T I C A S

        elif opcao == "9":

            print("\n===== ESTATÍSTICAS =====")

            print("Músicas cadastradas:",
                biblioteca.total_musicas()) # Total de músicas na biblioteca

            print("Fila Relaxar:",
                fila_relax.tamanho()) # Quantidade na fila Relaxar

            print("Fila Focar:",
                fila_foco.tamanho()) # Quantidade na fila Focar

            print("Fila Animar:",
                fila_animada.tamanho()) # Quantidade na fila Animar

            print("Fila Treinar:",
                fila_treino.tamanho()) # Quantidade na fila Treinar

            print("Músicas reproduzidas:",
                historico.tamanho()) # Total de músicas já tocadas

# # # # # # #   0 - S A I R

        elif opcao == "0":

            print("Sistema encerrado.")  # Mensagem de saída do sistema
            break  # Encerra o loop do menu

        else:
            print("Escolha inválida.")  # Caso o usuário digite uma opção que não existe

### EXECUÇÃO

if __name__ == "__main__": 
    menu()