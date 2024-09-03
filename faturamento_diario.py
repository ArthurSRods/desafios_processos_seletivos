import json
with open('faturamento.json', 'r') as file:
    data = json.load(file)

faturamento = data['faturamento_diario']

faturamento_sem_zero = [valor for valor in faturamento if valor > 0]

menor_faturamento = min(faturamento_sem_zero)
maior_faturamento = max(faturamento_sem_zero)

faturamento_medio = sum(faturamento_sem_zero) / len(faturamento_sem_zero)

dias_acima_da_media = sum(1 for valor in faturamento_sem_zero if valor > faturamento_medio)

print(f"Menor valor de faturamento: {menor_faturamento}")
print(f"Maior valor de faturamento: {maior_faturamento}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
