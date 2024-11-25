import datetime
from clases.medicamentos import Medicamentos

#clase paciente principal
class Paciente():
    
    def __init__(self,nombre,apellido,identificacion,peso,fecha_nacimiento):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__identificacion = identificacion
        self.__fecha_nacimiento = fecha_nacimiento
        self.__peso = peso
    
    #get
    def getNombrePacienteCompleto(self):
        return f"{self.__nombre} {self.__apellido}"
    
    def getIdentificacion(self):
        return self.__identificacion
    
    def getPeso(self):
        return self.__peso
    
    def getFechaNacimiento(self):
        return self.__fecha_nacimiento
    
    def getEdad(self):
        print(self.__fecha_nacimiento)
        anio_actual = datetime.datetime.now().year
        edad_paciente = anio_actual - self.__fecha_nacimiento.year
        return edad_paciente


#clase hija diagnostico
class TratamientoPaciente(Paciente):
    tiempo = None
    dosis = None
    administracion = None
    
    def __init__(self,nombre,apellido,identificacion,peso,fecha_nacimiento,tm,dosis,bool_peso,nom_med):
        super().__init__(nombre,apellido,identificacion,peso,fecha_nacimiento)
        self.tiempo = tm
        self.dosis = dosis
        self.bool_peso = bool_peso,
        self.nombre_medicamento = nom_med
        
        
    def calculo_dosis(self,medicamento):
        peso = self.getPeso()
        paso1 = None
        if self.bool_peso:
            paso1 = self.getPeso() * self.dosis
        else:
            paso1 = self.dosis
        paso2 = (paso1*medicamento.concentracion_ml)/medicamento.concentracion_mg
        self.administracion = paso2