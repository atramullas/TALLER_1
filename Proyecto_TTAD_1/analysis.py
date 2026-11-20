
import json

with open("data.json", "r", encoding="utf-8") as file:                  
    data = json.load(file)

ventas = data["ventas"]

#TOTAL FACTURADO
def total_facturado(ventas):
    total = 0
    for venta in ventas:
        total += venta["cantidad"] * venta["precio_unitario"]
    
    return total

print("Total facturado:", total_facturado(ventas))

# VENTAS POR CATEGORÍA
def ventas_por_categoria(ventas):
    categorias = {}
    for venta in ventas:
        categoria = venta["categoria"]
        importe = venta["cantidad"] * venta["precio_unitario"]
        if categoria not in categorias:
            categorias[categoria] = 0
        categorias[categoria] += importe
    
    return categorias
print("Ventas por categoría:", ventas_por_categoria(ventas))

# PRODUCTO MÁS VENDIDO
def producto_mas_vendido(ventas):
    productos = {}
    for venta in ventas:
        producto = venta["producto"]
        cantidad = venta["cantidad"]
        if producto not in productos:
            productos[producto] = 0
        productos[producto] += cantidad
    
    max_producto = max(productos, key=productos.get)
    return max_producto, productos[max_producto]

print("Producto más vendido:", producto_mas_vendido(ventas))