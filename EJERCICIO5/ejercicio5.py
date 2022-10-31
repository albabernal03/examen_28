import hashlib
from hashlib import sha256
#La alianza rebelde necesita comunicarse de manera segura pero el imperio galáctico interviene todas las comunicaciones, por lo que la princesa Leia nos encarga el desarrollo de un algoritmo de encriptación para las comunicaciones rebeldes, que contemple los siguientes requerimientos:
#cada carácter deberá ser encriptado a ocho caracteres;



#se deberá generar dos tablas hash para encriptar y desencriptar, para los caracteres desde el “ ” hasta el “}” –es decir desde el 32 al 125 de la tabla ASCII.



def encriptar(texto, texto_encriptado):
    texto = input("Ingrese el texto a encriptar: ")

    texto_encriptado=  sha256(texto.encode('utf-8')).hexdigest()[:8]
    with open("encriptado.txt", "w") as file:
        file.write(texto_encriptado)
        print("El texto encriptado se guardo en el archivo encriptado.txt")
        print(texto_encriptado)

def desencriptar(texto_encriptado):
    resolver= texto_encriptado
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




   

