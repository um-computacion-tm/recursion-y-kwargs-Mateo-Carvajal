def buscar_datos(*args, **kwargs):
        argumentos = list(args)
        for key, value in kwargs.items():
            id = [key]
        #print(id)
            for k, v in value.items():
                valores = list(value.values())
            id.extend(valores)
        #print(id)
            if any(arg in id for arg in argumentos):
                print("Resultado de busqueda: ", id)
                break
        else:
            print("No se encuentra en la base de datos")

database = {
    "persona1": {
        "primer_nombre": "Pablo",
        "segundo_nombre": "Diego",
        "primer_apellido": "Ruiz",
        "segundo_apellido": "Picasso"
    },
    "persona2": {
        "primer_nombre": "Mateo",
        "segundo_nombre": "Ezequiel",
        "primer_apellido": "Carvajal",
        "segundo_apellido": "Ojeda"
    },
    "persona3": {
        "primer_nombre": "Ignacio",
        "segundo_nombre": "",
        "primer_apellido": "Aguilera",
        "segundo_apellido": "Baigorria"
    }
}
input_usuario = input("Ingrese los datos a buscar separados por espacios: ")
datos_busqueda = input_usuario.split()

buscar_datos(*datos_busqueda, **database)