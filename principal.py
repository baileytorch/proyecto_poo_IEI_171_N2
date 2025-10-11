from datos.obtener_datos import obtener_lista_objetos
from modelos.comuna import Comuna
from modelos.marca import Marca


def obtener_listado_comunas():
    comuna = Comuna
    lista_comunas = obtener_lista_objetos(comuna)
    if lista_comunas:
        for comuna in lista_comunas:
            print(f'{comuna.id} {comuna.codigo_comuna} {comuna.nombre_comuna}')


def obtener_listado_marcas():
    marca = Marca
    lista_marcas = obtener_lista_objetos(marca)
    if lista_marcas:
        for marca in lista_marcas:
            print(f'{marca.id} {marca.nombre_marca} {marca.pais_origen}')


obtener_listado_comunas()
