"""Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
• SP : R$67.836,43
• RJ : R$36.678,66
• MG : R$29.229,88
• ES : R$27.165,48
• Outros : R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora."""

def representacao_estados():
    faturamento_SP = 67836.43
    faturamento_RJ = 36678.66
    faturamento_MG = 29229.88
    faturamento_ES = 27165.48
    faturamento_outros = 19849.53
    faturamento_total = faturamento_SP + faturamento_RJ + faturamento_MG + faturamento_ES + faturamento_outros
    
    percentual_SP = (faturamento_SP/faturamento_total)*100
    percentual_RJ = (faturamento_RJ/faturamento_total)*100
    percentual_MG = (faturamento_MG/faturamento_total)*100
    percentual_ES = (faturamento_ES/faturamento_total)*100
    percentual_outros = (faturamento_outros/faturamento_total)*100

    print(f'SP representou {percentual_SP:.2f} do faturamento total da empresa.')
    print(f'RJ representou {percentual_RJ:.2f} do faturamento total da empresa.')
    print(f'MG representou {percentual_MG:.2f} do faturamento total da empresa.')
    print(f'ES representou {percentual_ES:.2f} do faturamento total da empresa.')
    print(f'Outros estados representaram {percentual_outros:.2f} do faturamento total da empresa.')

representacao_estados()