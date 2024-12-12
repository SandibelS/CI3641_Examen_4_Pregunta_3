import classes

def main():

    simulador : classes.Simulador = classes.Simulador()

    seguir_ejecutandose : bool = True

    while (seguir_ejecutandose):
        
        input_usuario_str : str = input()

        if input_usuario_str == "":
            print("Se necesita una accion")
            continue
        
        input_usuario_list : list[str] = input_usuario_str.split(" ")

        if input_usuario_list[0] == "CLASS":

            if len(input_usuario_list) < 2:
                print("Insuficientes argumentos")
             
            if input_usuario_list[2] == ":":
                nombre = input_usuario_list[1]
                super_clase = input_usuario_list[3]
                metodos =  input_usuario_list[4:]

                try:
                    simulador.crear_clase_con_herencia(nombre, metodos, super_clase)
                except Exception as e:
                    print(f"ERROR. {e}")
            
            else:
                nombre = input_usuario_list[1]
                metodos = input_usuario_list[2:]

                try:
                    simulador.crear_clase_simple(nombre, metodos)
                except Exception as e:
                    print(f"ERROR. {e}")


        elif input_usuario_list[0] == "DESCRIBIR":

            nombre = input_usuario_list[1]

            try:
                metodos = simulador.describir(nombre)

                s = ""
                for nombre_metodo in metodos:
                    # metodos[nombre_metodo] nos da el nombre 
                    # de la clase de la cual usaremos el metodo
                    s += f"{nombre_metodo} -> {metodos[nombre_metodo]} :: {nombre_metodo}\n"
                
                print(s)

            except Exception as e:
                    print(f"ERROR. {e}")


        elif input_usuario_list[0] == "SALIR":

            seguir_ejecutandose = False

        else:
            print("Accion no reconocida")


            