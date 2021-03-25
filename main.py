def terceira_parte():
    set_a = {'apple', 'orange', 'banana', 'lime'}
    set_b = {'grapefruit', 'lime', 'banana'}

    print(f'Union: {set_a | set_b}')
    print(f'Intersection: {set_a & set_b}')
    print(f'Difference: {set_a - set_b}')
    print(f'Symetric Difference: {set_a ^ set_b}')


terceira_parte()

# if __name__ == '__main__':
#     # criando dicionarios
#
#     estados_capitais = {'Maranhão': 'São Luiz',
#                         'Mato Grosso': 'Cuiaba',
#                         'Mato Grosso do Sul': 'Campo Grande',
#                         'Minas Gerais': 'Belo Horizonte',
#                         }
#
# print(estados_capitais)
#
# # as chaves nao são strings
# dict_01 = dict(mg='BH', MT='CB', MS='CG')
# print(f'dict_01 {dict_01}')
#
# # as chaves valor são tuplas
# dict_02 = dict([('MG', 'BH'), ('MT', 'CB'), ('MS', 'CG')])
# print(f'dict_02 {dict_02}')
#
# # par chaves são listas
# dict_03 = dict((['MG', 'BH'], ['MT', 'CB'], ['MS', 'CG']))
# print(f'dict_02 {dict_03}')
#
# print(f'dict_03 [MG] = {dict_03["MG"]}')
#
# print(f'dict_03 [MG] "teste" = {dict_03["MG"]}')
#
#
# print(dict_03)
# print(dict_03.popitem())
# print(f' popitem: {dict_03}')
# print(dict_03.pop('MG'))
# dict_03.pop('MG')
# print(dict_03)
# del dict_03['MT']
# print(f'del: {dict_03}')
#
#
#
# #criar um dicionario alinhando, onde a chave é a região, e os valores são os estados pertencentes
#
#
#
#
#
#
#
# '''dict()#construtor
#     1)dict (**kwargs) -> seq K : valve
#     2)dict (mapping, **kwargs)'''
