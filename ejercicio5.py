import hashlib
from sre_parse import WHITESPACE
#La alianza rebelde necesita comunicarse de manera segura pero el imperio galáctico interviene todas las comunicaciones, por lo que la princesa Leia nos encarga el desarrollo de un algoritmo de encriptación para las comunicaciones rebeldes, que contemple los siguientes requerimientos:
#cada carácter deberá ser encriptado a ocho caracteres;



#se deberá generar dos tablas hash para encriptar y desencriptar, para los caracteres desde el “ ” hasta el “}” –es decir desde el 32 al 125 de la tabla ASCII.



def encriptar():
    texto = input("Ingrese el texto a encriptar: ")
    texto_encriptado = ""
    for i in texto:
        texto_encriptado += hashlib.sha256(i.encode()).hexdigest()[:8]#[:8] es para que tome los primeros 8 caracteres

    with open("encriptado.txt", "w") as file:
        file.write(texto_encriptado)
        print("El texto encriptado se guardo en el archivo encriptado.txt")

    
if __name__ == "__main__":
    encriptar()
   

