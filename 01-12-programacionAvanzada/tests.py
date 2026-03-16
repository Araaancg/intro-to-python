from contactos import agregarContacto

lista = []
cuantosContactos = len(lista)

agregarContacto(lista, "Arancha", "77")

assert len(lista) == 1, "El primer contacto no se ha añadido"

agregarContacto(lista, "Arancha", "77")

assert len(lista) == 1, "Ha fallado"

agregarContacto(lista, "Arancha", "76")

assert len(lista) == 2, "Ha fallado"

print("  ✓ OK")