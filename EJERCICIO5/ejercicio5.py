class TablaHash():
    def __init__(self, tam):
        '''Constructor de la clase TablaHash'''
        self.tam= tam
        self.tabla= [None]*self.tam

    def mostrar_tabla(self):
        '''Muestra la tabla'''
        for i in range(self.tam):
            print(i, self.tabla[i])
            
