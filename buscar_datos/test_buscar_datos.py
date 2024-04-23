import unittest

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
                return id
        return "No se encuentra en la base de datos"
class TestBuscarDatos(unittest.TestCase):
    def setUp(self):
         
        self.database = {
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

    def test_persona_encontrada(self):
        id = buscar_datos("Pablo", "Diego", "Ruiz", "Picasso", **self.database)
        self.assertEqual(id, ["persona1", "Pablo", "Diego", "Ruiz", "Picasso"])

    def test_persona_no_encontrada(self):
        id = buscar_datos("Juan", "Agustin", "Lopez", "Gonzalez", **self.database)
        self.assertEqual(id, "No se encuentra en la base de datos")

unittest.main()