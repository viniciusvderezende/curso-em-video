temperatura_celcius = float(input('Digite a temperatura em graus Celcius: '))
converter_temperatura_fahrenheit = temperatura_celcius * 1.8 + 32
converter_temperatura_kelvin = temperatura_celcius + 273.15

print(f'{temperatura_celcius}°C corresponde(m) a:')
print(f'{converter_temperatura_fahrenheit}°F;')
print(f'{converter_temperatura_kelvin}°K;')