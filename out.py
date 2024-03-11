import os
lista = os.listdir()
for pasta in lista:
    if pasta == 'in.py':
        pass
    elif pasta == 'out.py':
        pass
    else:
        listamenor = os.path.join(os.getcwd(), pasta)
        arquivos = os.listdir(listamenor)
        for arquivo in arquivos:
            if pasta == 'py':
                os.rename(f'py/{arquivo}', arquivo)
            elif pasta == 'csv':
                os.rename(f'csv/{arquivo}', arquivo)
            elif pasta == 'pdf':
                os.rename(f'pdf/{arquivo}', arquivo)
            elif pasta == 'json':
                os.rename(f'json/{arquivo}', arquivo)
            elif pasta == 'jpg':
                os.rename(f'jpg/{arquivo}', arquivo)
            elif pasta == 'txt':
                os.rename(f'txt/{arquivo}', arquivo)
            elif pasta == 'png':
                os.rename(f'png/{arquivo}', arquivo)
        os.rmdir(pasta)
