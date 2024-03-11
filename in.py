import os
lista = os.listdir()
pastas = []
def criar_pastas(lista, pastas):
    for arquivo in lista:
        if arquivo == 'in.py':
            pass
        elif arquivo == 'out.py':
            pass
        else:
            y = arquivo.split('.')[-1]
            if y not in pastas:
                os.mkdir(y)
                pastas.append(y)
                mover(arquivo)
            else:
                mover(arquivo)

def mover(arquivo):
        if 'txt' in arquivo:
            os.rename(arquivo, f'txt/{arquivo}')
        elif 'json' in arquivo:
            os.rename(arquivo, f'json/{arquivo}')
        elif 'py' in arquivo:
            os.rename(arquivo, f'py/{arquivo}')
        elif 'csv' in arquivo:
            os.rename(arquivo, f'csv/{arquivo}')
        elif 'jpg' in arquivo:
            os.rename(arquivo, f'jpg/{arquivo}')
        elif 'pdf' in arquivo:
            os.rename(arquivo, f'pdf/{arquivo}')
        elif 'png' in arquivo:
            os.rename(arquivo, f'png/{arquivo}')




criar_pastas(lista, pastas)