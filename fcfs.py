# tempo resposta = tempo chegada - lugar onde começou

# tempo retorno = lugar onde terminou - tempo de chegada

# tempo espera = soma quanto tempo ele parou no processo antes da ultima chamada,
# subtrai com o valor do último lugar onde ele aparece e subtrai o tempo de chegada.

def escalonar_fcfs(processos):
    # declaração de variáveis
    tempo_atual = 0
    tempo_resposta = 0
    tempo_retorno = 0
    tempo_espera = 0
    quantidade_processos = len(processos)

    for chegada, duracao in processos:
        # Ajusta o tempo atual se for menor que o tempo de chegada do processo
        if tempo_atual < chegada:
            tempo_atual = chegada

        # armazena o tempo de resposta
        tempo_resposta += tempo_atual - chegada
        # soma a duração do processo ao tempo_atual, simulando o escalonador
        tempo_atual += duracao
        # armazena o tempo de retorno, o tempo_atual agora sendo o valor após adicionar o processo
        tempo_retorno += tempo_atual - chegada
        # como o fcfs não tem preempção, o tempo de espera vai ser igual ao tempo de resposta
        tempo_espera = tempo_resposta

    tempo_resposta_media = tempo_resposta / quantidade_processos
    tempo_retorno_media = tempo_retorno / quantidade_processos
    tempo_espera_media = tempo_espera / quantidade_processos

    return tempo_retorno_media, tempo_resposta_media, tempo_espera_media
