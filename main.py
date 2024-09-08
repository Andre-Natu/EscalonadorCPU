import fcfs
import sjf
import rr

nome_arquivo = "entrada.txt"


def ler_entrada():
    valores = []
    with open(nome_arquivo, "r") as entrada:
        for linha in entrada:
            chegada, duracao = map(int, linha.split())
            valores.append((chegada, duracao))
    return valores


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    processos = ler_entrada()
    # chama a função fcfs e formata os resultados dela para os requisitados no projeto.
    resultado_fcfs = ' '.join(f'{x:.1f}'.replace('.', ',') for x in fcfs.escalonar_fcfs(processos))
    print("FCFS", resultado_fcfs)

    resultado_sjf = ' '.join(f'{x:.1f}'.replace('.', ',') for x in sjf.escalonar_sjf(processos))
    print("SJF", resultado_sjf)

    resultado_rr = ' '.join(f'{x:.1f}'.replace('.', ',') for x in rr.escalonar_rr(processos))
    print("RR", resultado_rr)
