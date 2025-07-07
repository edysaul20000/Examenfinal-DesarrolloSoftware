from fastapi import FastAPI, HTTPException

app = FastAPI()

usuarios = {}
usuarios_id_seq = 1

@app.post("/usuarios")
def creacion_usuario(nombre: str):
    global usuario_id_seq
    usuario = {"id": usuario_id_seq, "nombre": nombre}
    usuarios[usuario_id_seq] = usuario
    usuario_id_seq += 1
    return usuario

@app.get("/usuarios")
def lista_usuarios():
    return list(usuarios.values())

@app.delete("/usuarios/{usuario_id}")
def eliminar_usuario(usuario_id: int):
    if usuario_id in usuarios:
        del usuarios[usuario_id]
        return {"mensaje": "Usuario eliminado"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
