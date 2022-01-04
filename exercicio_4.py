def fat_total(receita_estados: dict):
    return sum(receita_estados.values())

def repr_percentual(receita_estados: dict):
    receita_total = fat_total(receita_estados)
    for estado, faturamento in receita_estados.items():
        repr_percentual = (faturamento/receita_total)*100
        print(
            f"{estado} teve uma representação percentual de aproximadamente {repr_percentual:.2f}% " 
            f"em relação ao faturamento total"
            ) 

def main():
    faturamento_estados = {'SP': 67836.43, 'RJ': 36678.66, 'MG': 29229.88, 'ES': 27165.48, 'Outros': 19849.53}
    repr_percentual(faturamento_estados)

if __name__ == '__main__':
    main()