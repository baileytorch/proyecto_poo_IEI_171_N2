from datos.obtener_datos import obtener_lista_objetos
from datos.insertar_datos import insertar_marca
from prettytable import PrettyTable
from modelos.comuna import Comuna
from modelos.marca import Marca


def obtener_listado_comunas():
    tabla_comunas = PrettyTable()
    tabla_comunas.field_names = ['Id', 'Código Comuna', 'Nombre Comuna']
    lista_comunas = obtener_lista_objetos(Comuna)
    if lista_comunas:
        for comuna in lista_comunas:
            tabla_comunas.add_row(
                [comuna.id, comuna.codigo_comuna, comuna.nombre_comuna])
            # print(f'{comuna.id} {comuna.codigo_comuna} {comuna.nombre_comuna}')
        print(tabla_comunas)


def obtener_listado_marcas():
    tabla_marcas = PrettyTable()
    tabla_marcas.field_names = ['Id', 'Nombre Marca', 'País de Origen']
    lista_marcas = obtener_lista_objetos(Marca)
    if lista_marcas:
        for marca in lista_marcas:
            tabla_marcas.add_row(
                [marca.id, marca.nombre_marca, marca.pais_origen])
            # print(f'{marca.id} {marca.nombre_marca} {marca.pais_origen}')
        print(tabla_marcas)


def guardar_nueva_marca():
    marca = input('Ingrese nombre de marca: ')
    pais = input('Ingrese país de origen: ')
    if marca != '':
        insertar_marca(marca, pais)


# obtener_listado_marcas()
# print()
# obtener_listado_comunas()
guardar_nueva_marca()
