aluno = input("digite o nome do aluno:")
disciplina = input("digite a disciplina:")
nota1 = int(input("digite a nota 1:"))
nota2 = int(input("digite a nota 2:"))
média = (nota1 + nota2 /2)
if média >=6 :
    print(f'{aluno} está aprovado em {disciplina}')
elif média <6 :
    print(f'{aluno} está reprovado em {disciplina}')