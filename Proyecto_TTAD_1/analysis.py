
# FUNCIONALIDADES

# TOTAL FACTURADO
def calcular_total_facturado(ventas: list[dict]) -> float:
    """Calcula el importe total facturado en todas las ventas."""
    return sum(v["cantidad"] * v["precio_unitario"] for v in ventas)

# VENTAS POR CATEGORÍA
def calcular_ventas_por_categoria(ventas: list[dict]) -> dict[str, float]:
    """Agrupa y suma el importe facturado por categoría."""
    totales: dict[str, float] = {}
    for v in ventas:
        categoria = v["categoria"]
        importe = v["cantidad"] * v["precio_unitario"]
        totales[categoria] = totales.get(categoria, 0.0) + importe
    return dict(sorted(totales.items(), key=lambda item: item[1], reverse=True))

# PRODUCTO MÁS VENDIDO
def obtener_producto_mas_vendido(ventas: list[dict], criterio: str = "unidades") -> tuple[str, float] | None:
    """
    Devuelve (producto, valor) del más vendido.
    `criterio`: 'unidades' (por cantidad) o 'ingresos' (por importe facturado).
    """
    if not ventas:
        return None

    acumulado: dict[str, float] = {}
    for v in ventas:
        producto = v["producto"]
        valor = v["cantidad"] if criterio == "unidades" else v["cantidad"] * v["precio_unitario"]
        acumulado[producto] = acumulado.get(producto, 0.0) + valor

    return max(acumulado.items(), key=lambda item: item[1])


