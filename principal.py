from datos.obtener_datos import obtener_lista_objetos
from datos.insertar_datos import insertar_objeto,actualizar_objeto
from prettytable import PrettyTable
from modelos.comuna import Comuna
from modelos.marca import Marca
from modelos.direccion import Direccion
from auxiliares.normalizar_strings import normalizar_string
from negocio.negocio_comunas import obtener_comuna_nombre


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


def obtener_marca_nombre(buscar_marca):
    lista_marcas = obtener_lista_objetos(Marca)
    if lista_marcas:
        for marca in lista_marcas:
            if normalizar_string(marca.nombre_marca) == normalizar_string(buscar_marca):
                return marca


def guardar_nueva_marca():
    while True:
        marca = input('Ingrese nombre de marca: ')
        pais = input('Ingrese país de origen: ')
        if marca != '':
            buscar_marca = obtener_marca_nombre(marca)
            if buscar_marca == None:
                nueva_marca = Marca(nombre_marca=marca, pais_origen=pais.title())
                insertar_objeto(nueva_marca)
                break
            else:
                print('La marca YA existe.')
                break
        else:
            print('Ingrese el nombre de la marca.')


def actualizar_marca():
    marca = input('Ingrese nombre de marca: ')
    if marca != '':
        buscar_marca = obtener_marca_nombre(marca)
        if buscar_marca!=None:            
            nuevo_nombre_marca = input('Ingrese NUEVO nombre de marca: ')
            nuevo_pais_origen = input('Ingrese NUEVO país de origen: ')
            if nuevo_nombre_marca!='':
                buscar_marca.nombre_marca = nuevo_nombre_marca
            if nuevo_pais_origen!='':
                buscar_marca.pais_origen = nuevo_pais_origen
            actualizar_objeto(buscar_marca)

def eliminar_marca():
    marca = input('Ingrese nombre de marca: ')
    if marca != '':
        buscar_marca = obtener_marca_nombre(marca)
        if buscar_marca!=None:
            buscar_marca.habilitado = 0
            actualizar_objeto(buscar_marca)

def guardar_nueva_direccion():
    while True:
        buscar_comuna = input('Ingrese nombre de comuna: ')
        comuna_encontrada = obtener_comuna_nombre(buscar_comuna)

        if comuna_encontrada:
            while True:
                nueva_calle = input('Ingrese calle: ')
                nuevo_numero = input('Ingrese número: ')
                nuevo_departamento = input('Ingrese departamento: ')
                nuevo_detalles = input('Ingrese detalles necesarios: ')

                if nueva_calle != '':
                    nueva_direccion = Direccion(
                        calle=nueva_calle,
                        numero=nuevo_numero,
                        departamento=nuevo_departamento,
                        detalles=nuevo_detalles,
                        id_comuna=comuna_encontrada.id)
                    insertar_objeto(nueva_direccion)
                    break
                else:
                    print('Nombre de calle no ingresado, intente nuevamente.')
            break
        else:
            print('Comuna NO encontrada, intente nuevamente.')


# obtener_listado_marcas()
# print()
# obtener_listado_comunas()
obtener_listado_marcas()
# guardar_nueva_marca()
# actualizar_marca()
# eliminar_marca()
# guardar_nueva_direccion()
