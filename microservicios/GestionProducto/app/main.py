from fastapi import FastAPI, HTTPException

app = FastAPI()

productos = {}
producto_id_seq = 1

@app.post("/productos")
def create_product(nombre: str, precio: float):
    global producto_id_seq
    producto = {"id": producto_id_seq, "nombre": nombre, "precio": precio}
    productos[producto_id_seq] = producto
    producto_id_seq += 1
    return producto

@app.get("/productos/{producto_id}")
def get_producto(producto_id: int):
    if producto_id in productos:
        return productos[producto_id]
    raise HTTPException(status_code=404, detail="Producto no encontrado")

@app.put("/productos/{producto_id}")
def update_producto(producto_id: int, nombre: str = None, precio: float = None):
    if producto_id not in productos:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    if nombre:
        productos[producto_id]["nombre"] = nombre
    if precio is not None:
        productos[producto_id]["precio"] = precio
    return productos[producto_id]
