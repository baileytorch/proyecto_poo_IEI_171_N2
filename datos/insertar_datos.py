from modelos.marca import Marca
from modelos.comuna import Comuna
from modelos.direccion import Direccion
from datos.conexion import Session

sesion = Session()


def insertar_marca(marca, pais):
    nueva_marca = Marca(
        nombre_marca=marca.title(),
        pais_origen=pais.title())
    sesion.add(nueva_marca)
    try:
        sesion.commit()
        print(
            f"La marca '{nueva_marca.nombre_marca}' se ha guardado correctamente.")
    except Exception as e:
        sesion.rollback()
        print(f"Error al guardar la marca: {e}")
    finally:
        sesion.close()


def insertar_comuna(codigo, comuna):
    nueva_comuna = Comuna(
        codigo_comuna=codigo.title(),
        nombre_comuna=comuna.title())
    sesion.add(nueva_comuna)
    try:
        sesion.commit()
        print(
            f"La comuna '{nueva_comuna.nombre_marca}' se ha guardado correctamente.")
    except Exception as e:
        sesion.rollback()
        print(f"Error al guardar la comuna: {e}")
    finally:
        sesion.close()


def insertar_direccion(dir_calle, dir_numero, dir_departamento, dir_detalles, dir_id_comuna):
    nueva_direccion = Direccion(
        calle=dir_calle.title(),
        numero=dir_numero.title(),
        departamento=dir_departamento,
        detalles=dir_detalles,
        id_comuna=dir_id_comuna)
    sesion.add(nueva_direccion)
    try:
        sesion.commit()
        print("La dirección se ha guardado correctamente.")
    except Exception as e:
        sesion.rollback()
        print(f"Error al guardar la direccion: {e}")
    finally:
        sesion.close()
