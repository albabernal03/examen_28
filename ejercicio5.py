import hashlib
from sre_parse import WHITESPACE
#La alianza rebelde necesita comunicarse de manera segura pero el imperio galáctico interviene todas las comunicaciones, por lo que la princesa Leia nos encarga el desarrollo de un algoritmo de encriptación para las comunicaciones rebeldes, que contemple los siguientes requerimientos:
#cada carácter deberá ser encriptado a ocho caracteres;
#se deberá generar dos tablas hash para encriptar y desencriptar, para los caracteres desde el “ ” hasta el “}” –es decir desde el 32 al 125 de la tabla ASCII.




def main():
    mensaje= str(input("Ingrese el mensaje a encriptar: ")).encode('ASCII')
    sha256= hashlib.sha256(mensaje).hexdigest()
    with open('mesaje_encriptados.txt', 'w') as file:
        file.write(sha256)

if __name__ == '__main__':
    main()
    
