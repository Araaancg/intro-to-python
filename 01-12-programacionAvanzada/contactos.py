"""
python contactos.py agregar Arancha 666666666

1. Agregar
- nombre 
- tlf
"""

import sys

contactos = [{'nombre': 'Arancha', 'tlf': '77'}]
# { nombre: "", tlf: "" }

def agregarContacto(lista: list, nombre: str, tlf:str) -> None:
    contacto = { "nombre": nombre, "tlf": tlf }

    contactoNuevo = True

    for contacto in lista:
        for v in contacto.values():
            if tlf == v:
                print("Contacto ya agregado")
                contactoNuevo = False
                
    if contactoNuevo:
        lista.append(contacto)
        print("Contacto agregado!")

    

# clave = sys.argv[1]

# if clave == "agregar":
#     # 1. PILLAR LA INFO
#     nombre_ = sys.argv[2]
#     tlf_ = sys.argv[3]

#     # 2. AGREGAR CONTACTO
#     agregarContacto(contactos, nombre_, tlf_)

# print(contactos)


