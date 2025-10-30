from datos.conexion import sesion


def insertar_objeto(objeto):
    sesion.add(objeto)
    try:
        sesion.commit()
        print("El objeto se ha guardado correctamente.")
    except Exception as e:
        sesion.rollback()
        print(f"Error al guardar la marca: {e}")
    finally:
        sesion.close()

def actualizar_objeto(objeto):
    sesion.merge(objeto)
    try:
        sesion.commit()
        print("El objeto se ha actualizado correctamente.")
    except Exception as e:
        sesion.rollback()
        print(f"Error al actualizar el objeto: {e}")
    finally:
        sesion.close()
