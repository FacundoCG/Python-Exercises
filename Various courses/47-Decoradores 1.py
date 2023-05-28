#Un decorador es en cierta forma una función que añade funcionalidades a otras, "decoran funciones"

def funcion_decoradora(funcion_parametro):

    def funcion_interior():

        #Acciones adicionales que decoran
        print("Vamos a realizar un cálculo:")
        
        funcion_parametro()
        
        #Acciones adicionales que decoran
        print("Hemos terminado el cálculo")

    return funcion_interior

@funcion_decoradora
def suma():
    print(15+20)

@funcion_decoradora
def resta():
    print(30-10)

suma()
resta()