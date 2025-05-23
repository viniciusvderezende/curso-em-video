recebe_valor = float(input('Digite o valor em reais: R$ '))

converter_dolar = recebe_valor / 5.67
converter_euro = recebe_valor / 6.44
converter_libra_esterlina = recebe_valor / 7.67
converter_iene = recebe_valor / 0.040
converter_yuan = recebe_valor / 0.79
covnerter_won = recebe_valor / 0.0042

print(f'''R$ {recebe_valor:.2f} correspondem a:
      US$   {converter_dolar:.2f}    (Dólar Norte Americano);
      €     {converter_euro:.2f}    (Euro);
      £     {converter_libra_esterlina:.2f}    (Libra Esterlina);
      ¥    {converter_iene:.2f}    (Iene Japonês);
      ¥     {converter_yuan:.2f}    (Yuan Chinês);
      ₩   {covnerter_won:.2f}    (Won Sul-Coreano)      
      ''')