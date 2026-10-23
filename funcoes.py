def conversor(valor_em_dolar, valor_dolar_atual):
    return round(valor_em_dolar * valor_dolar_atual, 2)


dolar = float(input("Digite o valor em dólar: "))

valor_dolar = float(input("Digite o valor atual do dólar: "))

valor_convertido = conversor(dolar, valor_dolar)

print(f'Valor em reais: R$ {valor_convertido}')

print(f'Valor do conversor com outros parâmetros: {round(conversor(5.00, 5.05), 2)}')