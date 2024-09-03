from usuario import Usuario
from datetime import datetime
import json 
instancias = []

with open('usuarios.txt') as usuarios:
    linea = usuarios.readline()
    while linea:
        try:
            usuario = json.loads(linea)
            instancias.append(
                Usuario(usuario.get("nombre"), usuario.get("apellido"),usuario.get("email"), usuario.get("genero"))
            )
        
        except Exception as e:
            with open("error.log", "a+") as log:
                log.seek(0)
                print(log.read())
                now = datetime.now()
                log.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] ERROR: {type(e)}, Linea{linea}")
                log.seek(0)
                print(log.read())
                
        linea = usuarios.readline()        
            
print("""::::::::::::::::::::: Detalle de usuarios::::::::::::::::::::::::::::::
      
Nombre          Apellido             Email                     Genero 
""")
for usuario in instancias:
    print(f"{usuario.nombre:15} {usuario.apellidos:20} {usuario.email:25} {usuario.genero}")
     