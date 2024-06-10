cidadão = input("digite o nome do cidadão:")
idade = int(input("digite a idade do cidadão:"))
if idade >= 16 :
    print (f'{cidadão} pode emitir')
elif idade < 16 :
    print (f'{cidadão} não pode emitir')