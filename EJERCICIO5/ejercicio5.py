import hashlib
from hashlib import sha256
#La alianza rebelde necesita comunicarse de manera segura pero el imperio galáctico interviene todas las comunicaciones, por lo que la princesa Leia nos encarga el desarrollo de un algoritmo de encriptación para las comunicaciones rebeldes, que contemple los siguientes requerimientos:
#cada carácter deberá ser encriptado a ocho caracteres;



#se deberá generar dos tablas hash para encriptar y desencriptar, para los caracteres desde el “ ” hasta el “}” –es decir desde el 32 al 125 de la tabla ASCII.



def encriptar(texto):

    texto= sha256(texto.encode('utf-8')).hexdigest()[:8]
    with open("encriptado.txt", "w") as file:
        file.write(texto)
        print("El texto encriptado se guardo en el archivo encriptado.txt")
        print(texto)

def desencriptar(texto):
    resolver= texto
    for x in resolver:
        r= resolver.encode('utf-8')
        a= sha256(r).hexdigest()[:8]

        if a in resolver:
            with open("desencriptado.txt", "w") as file:
                file.write(resolver)
                print("El texto desencriptado se guardo en el archivo desencriptado.txt")
                print(resolver)
                break
        else:
            print("No se encontro el texto")

texto = input("Ingrese el texto a encriptar: ")



   

