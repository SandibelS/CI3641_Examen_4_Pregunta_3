import pytest
from classes import Simulador

class TestClass:
    
    def test_describir_una_clase_no_existente(self):
        simulador = Simulador()
        with pytest.raises(ValueError):
            simulador.describir("A")

    def test_mismo_nombre_clase_simple1(self):
        simulador = Simulador()
        simulador.crear_clase_simple("A", ["f", "g"])
        with pytest.raises(ValueError):
            simulador.crear_clase_simple("A", ["f", "g"])
    
    def test_mismo_nombre_clase_simple2(self):
        simulador = Simulador()
        simulador.crear_clase_simple("A", ["f", "g"])
        simulador.crear_clase_simple("B", ["h", "i"])
        with pytest.raises(ValueError):
            simulador.crear_clase_con_herencia("A", ["f", "g"], "B")
    
    def test_mismo_nombre_clase_con_herencia1(self):
        simulador = Simulador()
        simulador.crear_clase_simple("B", [])
        simulador.crear_clase_con_herencia("A", ["f", "g"], "B")
        with pytest.raises(ValueError):
            simulador.crear_clase_con_herencia("A", ["f", "g"], "B")
    
    def test_mismo_nombre_clase_con_herencia2(self):
        simulador = Simulador()
        simulador.crear_clase_simple("B", [])
        simulador.crear_clase_con_herencia("A", ["f", "g"], "B")
        with pytest.raises(ValueError):
            simulador.crear_clase_simple("A", ["f", "g"])

    def test_no_existe_superclase(self):
        simulador = Simulador()
        with pytest.raises(ValueError):
            simulador.crear_clase_con_herencia("A", ["f", "g"], "B")

    def test_metodos_duplicados1(self):
        simulador = Simulador()
        with pytest.raises(ValueError):
            simulador.crear_clase_simple("A", ["f", "f"])
    
    def test_metodos_duplicados2(self):
        simulador = Simulador()
        simulador.crear_clase_simple("B", [])
        with pytest.raises(ValueError):
            simulador.crear_clase_con_herencia("A", ["f", "f"], "B")

    
    def test_descripcion_clase_simple(self):
        simulador = Simulador()
        simulador.crear_clase_simple("B", ["f", "g"])
        dicc_esperado = {"f" : "B", "g" : "B"}
        dicc_obtenido = simulador.describir('B')
        assert dicc_esperado == dicc_obtenido
    
    def test_descripcion_clase_con_herencia1(self):
        simulador = Simulador()
        simulador.crear_clase_simple("A", ["f", "g"])
        simulador.crear_clase_con_herencia("B", ["h", "i"], "A")
        dicc_esperado = {"f" : "A", "g" : "A", "h" : "B", "i" : "B"}
        dicc_obtenido = simulador.describir('B')
        assert dicc_esperado == dicc_obtenido
    
    def test_descripcion_clase_con_herencia2(self):
        simulador = Simulador()
        simulador.crear_clase_simple("A", ["f", "g"])
        # Con sobrecarga de metodos
        simulador.crear_clase_con_herencia("B", ["f", "i"], "A")
        dicc_esperado = {"g" : "A", "f" : "B", "i" : "B"}
        dicc_obtenido = simulador.describir('B')
        assert dicc_esperado == dicc_obtenido
    
    def test_descripcion_clase_con_herencia3(self):
        simulador = Simulador()
        simulador.crear_clase_simple("A", ["f", "g"])
        # Se sobrecargan todos los metodos
        simulador.crear_clase_con_herencia("B", ["f", "g"], "A")
        dicc_esperado = {"f" : "B", "g" : "B"}
        dicc_obtenido = simulador.describir('B')
        assert dicc_esperado == dicc_obtenido
    
    def test_descripcion_clase_con_herencia4(self):
        simulador = Simulador()
        simulador.crear_clase_simple("A", ["f", "g"])
        simulador.crear_clase_con_herencia("B", ["f", "h", "i"], "A")
        simulador.crear_clase_con_herencia("C", ["f", "i", "j"], "B")
        dicc_esperado = {"f" : "C", "g" : "A", "h": "B", "i" : "C", "j" : "C"}
        dicc_obtenido = simulador.describir('C')
        assert dicc_esperado == dicc_obtenido

