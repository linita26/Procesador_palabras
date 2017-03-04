# INICIO DEL PROGRAMA

import socket

cliente = socket.socket()

"""direccion ip del servidor, puerto del servidor"""

cliente.connect(("localhost", 35000))

while True:


    #lista = ['1.Listar', '2.Crear', '3.Modificar', '4.Eliminar', '5.salir']

    #for i in lista:
     #       print i


    import opciones

    opciones.crear()
    opciones.modificar()
    opciones.eliminar()




    if mensaje_cliente == "salir":

        break



print "vuelva cuando quiera"
cliente.close()

