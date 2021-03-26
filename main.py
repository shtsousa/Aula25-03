def terceira_parte():
    set_a = {'apple', 'orange', 'banana', 'lime'}
    set_b = {'grapefruit', 'lime', 'banana'}

    print(f'Union: {set_a | set_b}')
    print(f'Intersection: {set_a & set_b}')
    print(f'Difference: {set_a - set_b}')
    print(f'Symetric Difference: {set_a ^ set_b}')


def quarta_parte():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(type(data))
    print(f'list_data: {data}')

    data_filtered = list(filter(lambda i: i % 2 == 0, data))

    print(f'date_filtered: {data_filtered}')

    def is_even(i):
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                29]
        print(data)
        print(f'list_data: {data}')

        data_filtered = list(filter(lambda i: i % 2 == 0, data))

        print(f'date_filtered: {data_filtered}')
        return i % 2 == 0

    data_filtered = list(filter(is_even, data))
    print(f'data_filtered(even numbers)(função de baixa ordem) = {data_filtered}')

    person_data = [person('Fabricio', 39), person('Pollyana', 22), person('Samuel', 25), person('Nayara', 23)]
    print('\n')
    print('-' * 25)
    for person in person_data:
        print(person, end=', ')

    person_filtered = list(filter
                           (lambda person: person.age >= 18,
                            person_data

                            ))
    print(person_data)


terceira_parte()
quarta_parte()
is_even()

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
