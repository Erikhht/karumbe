/*
 *  Ejemplo Cuadrado
 *   
 *  Este ejemplo muestra como usar la extension dibujos (creado
 *  por czayas), que utiliza turtle para python.
 *   
 *  Este modulo fue lo que impulzo la creación the karumbe.
 *   
 *  (c) ninguna
 */

# Importar el modulo "dibujos"
# 
# En karumbe cuando se importa un modulo, este define
# una serie de funciones o metodos escritos en el lenguaje
# "compilado" (o lenguaje host, en este caso python).
# Para simplificar las cosas no es necesario ejecutar "dibujos.foo",
# solo es necesario "foo". Para evitar problemas será necesario
# algún tipo de estandarización al escribir los modulos ya que 
# karumbe se enfoca en la simpleza y el fácil aprendizaje.
usar dibujos

un cuadrado tiene lado y es
    repetir 4 veces
         izquierda 90
         adelante lado
    fin  
fin

un rectangulo tiene largo,ancho y es
    izquierda 90
    adelante largo
    #
    izquierda 90
    adelante ancho
    #
    izquierda 90
    adelante largo
    #
    izquierda 90
    adelante ancho
    
fin
