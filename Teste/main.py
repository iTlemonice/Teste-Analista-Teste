import numpy as np

valor = np.random.randint(1000000, size=365)
# CRIAÇÃO DOS VALORES DIÁRIOS DA EMPRESA, DEFINIDO O TAMANHO DELA, OU SEJA, A QUANTIDADE DE DIAS.

print(f'O valor mínimo desse ano foi de: R${valor.min():.2f}')
print(f'O valor máximo desse ano foi de: R${valor.max():.2f}')
#PEGAMOOS O VALOR MÁXIMO, PEGO AGORA POIS COMO FOI REQUERIDO PARA DESCONTAR OS VALORES NULOS DE FIM DE SEMANA.

k = 0   # O VALOR DE DIAS QUE O RENDIMENTO FOI MAIOR QUE A MÉDIA ANUAL.
fs = 1  # VALOR PARA DEFINIÇÃO DOS FIM DE SEMANA.
valor_fs = np.arange(0)     # ARRAY NP PARA FAZER A CÓPIA DOS VALORES DE DIAS, E A SUBSTITUIÇÃO QUE OS FIM DE SEMANA NÃO TERÃO RENDIMENTO.

for dia in valor:
    if fs == 6:
        dia = 0
    elif fs == 7:
        dia = 0
        fs = 0
    elif dia >= (valor.sum())/len(valor):
        k += 1
    fs += 1
    valor_fs = np.append(arr=valor_fs, values=dia)

print(f'A média anual é de: R${(valor_fs.sum())/len(valor):.2f}')

print(f'A quantidade de dias em que o faturamento foi maior que a média anual é {k}.')

print(valor_fs)