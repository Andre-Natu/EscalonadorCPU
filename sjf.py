def escalonar_sjf(processos):
    # declaração de variáveis
    tempo_atual = 0
    tempo_resposta = 0
    tempo_retorno = 0
    tempo_espera = 0
    quantidade_processos = len(processos)
    fila = []
    processos_copia = processos[:]

    while processos_copia or fila:
        # Adiciona processos à fila de prontos
        while processos_copia and processos_copia[0][0] <= tempo_atual:
            fila.append(processos_copia.pop(0))

        if fila:
            # Obtém o processo com a menor duração
            menor_duracao = min(fila, key=lambda x: x[1])

            chegada, duracao = menor_duracao

            # armazena o tempo de resposta
            tempo_resposta += tempo_atual - chegada
            # soma a duração do processo ao tempo_atual, simulando o escalonador
            tempo_atual += duracao
            # armazena o tempo de retorno, o tempo_atual agora sendo o valor após adicionar o processo
            tempo_retorno += tempo_atual - chegada
            # como o fcfs não tem preempção, o tempo de espera vai ser igual ao tempo de resposta
            tempo_espera = tempo_resposta

            # remove o processo da fila
            fila.remove(menor_duracao)
        else:
            # Se a fila estiver vazia, avança o tempo até o próximo processo chegar
            tempo_atual = processos_copia[0][0]

    # Calcula as médias
    tempo_resposta_media = tempo_resposta / quantidade_processos
    tempo_retorno_media = tempo_retorno / quantidade_processos
    tempo_espera_media = tempo_espera / quantidade_processos

    return tempo_retorno_media, tempo_resposta_media, tempo_espera_media