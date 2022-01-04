import json

def dados_faturamento(json_arquivo):
    with open(json_arquivo, 'r') as arq_dados:
        dados = json.load(arq_dados)
        val_dias_com_fat = [dict['valor'] for dict in dados
                            if dict['valor'] != 0
                            ]

        def menor_valor():
            menor_valor = min(val_dias_com_fat)
            for dict in dados:
                if dict['valor'] == menor_valor:
                    msg_menor_valor = (f"O menor valor de R${dict['valor']:.2f} "
                                       f"ocorreu no dia {dict['dia']}"
                                       )
                else:
                    pass

            return print(msg_menor_valor)

        def maior_valor():
            maior_valor = max(val_dias_com_fat)
            for dict in dados:
                if dict['valor'] == maior_valor:
                    msg_maior_valor = (f"O maior valor de R${dict['valor']:.2f} " 
                                       f"ocorreu no dia {dict['dia']}"
                                       )
                else:
                    pass

            return print(msg_maior_valor)
    
        def sup_media_mensal():
            media_mensal = sum(val_dias_com_fat)/len(val_dias_com_fat)
            dias_fat_sup_media = len([(dict['dia'],dict['valor']) 
                                      for dict in dados 
                                      if dict['valor'] > media_mensal])
        
            return print((f"{dias_fat_sup_media} dias tiveram o faturamento "
                          f"diário superior à média mensal"
                          ))
        
    menor_valor()
    maior_valor()
    sup_media_mensal()

def main():
    dados_faturamento('dados.json')

if __name__ == '__main__':
    main()