from auxiliares.normalizar_strings import normalizar_string
from datos.obtener_datos import obtener_lista_objetos
from modelos.comuna import Comuna


def obtener_listado_comunas():
    lista_comunas = obtener_lista_objetos(Comuna)
    if lista_comunas:
        return lista_comunas


def obtener_comuna_nombre(buscar_comuna):
    listado_comunas = obtener_lista_objetos(Comuna)
    if listado_comunas:
        for comuna in listado_comunas:
            if normalizar_string(comuna.nombre_comuna) == normalizar_string(buscar_comuna):
                return comuna
