class Usuario():
    def __init__(self, nombre: str, apellido: str, email: str, genero: str) -> None:
        self.nombre = nombre
        self.apellidos = apellido
        self.email = email
        self.genero = genero
             
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
            linea=usuarios.readline()
        except Exception as e:
            with open("error.log", "a+") as log:
                log.write(f'ERROR!!!:{linea.strip()} -> {str(e)}\n')
                
        linea = usuarios.readline()        
            
print("""::::::::::::::::::::: Detalle de usuarios::::::::::::::::::::::::::::::
      
Nombre          Apellido             Email                     Genero 
""")
for usuario in instancias:
    print(f"{usuario.nombre:15} {usuario.apellidos:20} {usuario.email:25} {usuario.genero}")
     