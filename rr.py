def escalonar_rr(processos):
    tempo_atual = 0
    tempo_resposta = 0
    tempo_retorno = 0
    tempo_espera = 0
    quantidade_processos = len(processos)
    fila = []
    processos_copia = processos[:]
    duracao_restante = {(chegada, duracao): duracao for chegada, duracao in processos}
    primeira_execucao = {}
    quantum = 2

    while processos_copia or fila:
        # O algoritmo começa não adicionando nenhum
        if fila:
            processo_atual = fila.pop(0)
            chegada, duracao = processo_atual

            # Verifica se é a primeira execução do processo
            if processo_atual not in primeira_execucao:
                primeira_execucao[processo_atual] = tempo_atual
                tempo_resposta += tempo_atual - chegada

            # Calcula o tempo de execução real (mínimo entre quantum e duração restante)
            tempo_execucao = min(quantum, duracao_restante[processo_atual])

            # Atualiza o tempo atual e a duração restante do processo
            tempo_atual += tempo_execucao
            duracao_restante[processo_atual] -= tempo_execucao

            # Se o processo terminou, calcula o tempo de retorno e de espera
            if duracao_restante[processo_atual] == 0:
                tempo_retorno += tempo_atual - chegada
                tempo_espera += tempo_atual - chegada - duracao
            else:
                # Adiciona processos à fila de prontos
                while processos_copia and processos_copia[0][0] <= tempo_atual:
                    fila.append(processos_copia.pop(0))

                # Se o processo não terminou, adiciona-o de volta ao final da fila
                fila.append(processo_atual)
        else:
            # Se a fila estiver vazia, avança o tempo até o próximo processo chegar
            if processos_copia:
                tempo_atual = processos_copia[0][0]

            # Adiciona processos à fila de prontos
            while processos_copia and processos_copia[0][0] <= tempo_atual:
                fila.append(processos_copia.pop(0))

    # Calcula as médias
    tempo_resposta_media = tempo_resposta / quantidade_processos
    tempo_retorno_media = tempo_retorno / quantidade_processos
    tempo_espera_media = tempo_espera / quantidade_processos

    return tempo_retorno_media, tempo_resposta_media, tempo_espera_media
