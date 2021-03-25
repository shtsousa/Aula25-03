if __name__ == '__main__':
    # criando dicionarios

    estados_capitais = {'Maranhão': 'São Luiz',
                        'Mato Grosso': 'Cuiaba',
                        'Mato Grosso do Sul': 'Campo Grande',
                        'Minas Gerais': 'Belo Horizonte',
                        }

print(estados_capitais)

# as chaves nao são strings
dict_01 = dict(mg='BH', MT='CB', MS='CG')
print(f'dict_01 {dict_01}')

# as chaves valor são tuplas
dict_02 = dict([('MG', 'BH'), ('MT', 'CB'), ('MS', 'CG')])
print(f'dict_02 {dict_02}')

# par chaves são listas
dict_03 = dict((['MG', 'BH'], ['MT', 'CB'], ['MS', 'CG']))
print(f'dict_02 {dict_03}')

print(f'dict_03 [MG] = {dict_03["MG"]}')

'''dict()#construtor
    1)dict (**kwargs) -> seq K : valve
    2)dict (mapping, **kwargs)'''
