#Alumnos Edgar Solos Cuadros(23151263) y Jose Antonio Cedeño Cabrera(23151209)

Titulo="";
Autor="";
URL="";
Activo=False;
Respuesta="Si";
MiLista=[];
RespuestaActivado=False;
Columnas=1;

#Respuesta = input("¿Desea ingresar datos?");

while Respuesta.upper() == "SI":
    Titulo=input("Ingrese el Titulo: ");
    MiLista.append(Titulo);
    Autor=input("Ingrese el nombre del autor: ");
    MiLista.append(Autor);
    URL=input("Ingrese un enlace: ");
    MiLista.append(URL)

    RespuestaActivado=input("¿Esa activado?: ")
    if RespuestaActivado.upper() =="SI":
        Activo = True;
        MiLista.append(Activo);
    elif RespuestaActivado.upper()=="NO":
        Activo=False;
        MiLista.append(Activo);
    Respuesta=input("¿Desea Ingresar mas datos ?")
    Columnas=Columnas+1;


print(MiLista)