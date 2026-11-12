import json

with open('data.json', 'r') as file:
    data = json.load(file)

print(data)

import csv

# Diccionario inicial con las compras de cada usuario
usuarios = {
    "ana_gomez": [
        {"producto": "Ratón inalámbrico", "categoria": "Informática", "precio": 25.50},
        {"producto": "Teclado mecánico", "categoria": "Informática", "precio": 89.99},
        {"producto": "Alfombrilla XXL", "categoria": "Accesorios", "precio": 15.00}
    ],
    "carlos_ruiz": [
        {"producto": "Monitor 24 pulgadas", "categoria": "Informática", "precio": 145.00},
        {"producto": "Cable HDMI", "categoria": "Accesorios", "precio": 9.95}
    ],
    "laura_m": [
        {"producto": "Silla ergonómica", "categoria": "Mobiliario", "precio": 210.00},
        {"producto": "Lámpara LED", "categoria": "Iluminación", "precio": 32.50},
        {"producto": "Soporte portátil", "categoria": "Accesorios", "precio": 22.00},
        {"producto": "Webcam HD", "categoria": "Informática", "precio": 55.00}
    ],
    "david_perez": []
}


# 1. GASTO TOTAL POR USUARIO

gastos = {}

for usuario, productos in usuarios.items():
    total = sum(producto["precio"] for producto in productos)
    gastos[usuario] = total

print("1. GASTO TOTAL POR USUARIO")

for usuario, total in gastos.items():
    print(f"{usuario}: {total:.2f} €")


# 2. CLIENTE VIP (MAYOR GASTO)

cliente_vip = max(gastos, key=gastos.get)

print("\n2. CLIENTE VIP")
print(f"Cliente: {cliente_vip}")
print(f"Gasto total: {gastos[cliente_vip]:.2f} €")


# 3. CLIENTE CON MÁS ARTÍCULOS

cantidad_productos = {}

for usuario, productos in usuarios.items():
    cantidad_productos[usuario] = len(productos)

cliente_mas_articulos = max(
    cantidad_productos,
    key=cantidad_productos.get
)

print("\n3. CLIENTE CON MÁS ARTÍCULOS")
print(f"Cliente: {cliente_mas_articulos}")
print(f"Artículos comprados: {cantidad_productos[cliente_mas_articulos]}")


# 4. PRODUCTO MÁS CARO Y MÁS BARATO

todas_compras = []

for usuario, productos in usuarios.items():
    for producto in productos:
        compra = producto.copy()
        compra["usuario"] = usuario
        todas_compras.append(compra)

producto_caro = max(todas_compras, key=lambda p: p["precio"])
producto_barato = min(todas_compras, key=lambda p: p["precio"])

print("\n4. PRODUCTO MÁS CARO Y MÁS BARATO")

print(f"Más caro: {producto_caro['producto']}")
print(f"Precio: {producto_caro['precio']:.2f} €")
print(f"Comprador: {producto_caro['usuario']}")

print(f"\nMás barato: {producto_barato['producto']}")
print(f"Precio: {producto_barato['precio']:.2f} €")
print(f"Comprador: {producto_barato['usuario']}")


# 5. RESUMEN DINÁMICO POR CATEGORÍAS

gastos_categorias = {}

for productos in usuarios.values():
    for producto in productos:
        categoria = producto["categoria"]
        precio = producto["precio"]

        if categoria not in gastos_categorias:
            gastos_categorias[categoria] = 0

        gastos_categorias[categoria] += precio

print("\n5. GASTOS POR CATEGORÍAS")

for categoria, total in gastos_categorias.items():
    print(f"{categoria}: {total:.2f} €")


# 6. AÑADIR PRECIO CON IVA (21%)

for productos in usuarios.values():
    for producto in productos:
        producto["precioIVA"] = round(producto["precio"] * 1.21, 2)

print("\n6. PRODUCTOS CON IVA")

for usuario, productos in usuarios.items():
    for producto in productos:
        print(
            f"{producto['producto']}: "
            f"{producto['precioIVA']:.2f} €"
        )


# 7. CREAR FICHERO CSV

with open("contabilidad_a.csv", "w", newline="", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo, delimiter=";")

    # Cabecera del CSV
    escritor.writerow(["producto", "precioIVA"])

    # Escribir todos los productos
    for productos in usuarios.values():
        for producto in productos:
            escritor.writerow([
                producto["producto"],
                f"{producto['precioIVA']:.2f}"
            ])

print("\n7. FICHERO CSV")
print("Archivo contabilidad_a.csv creado correctamente.")
