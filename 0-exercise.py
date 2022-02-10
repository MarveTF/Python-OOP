"""
Cree una clase de Persona con atributos: nombre y edad.
Cree un método display() que muestre el nombre y la edad de un objeto creado a través de la clase Person.
Cree una clase secundaria Estudiante que herede de la clase Persona y que también tenga un atributo de sección.
Cree un método displayStudent() que muestre el nombre, la edad y la sección de un objeto creado a través de la clase Student.
Cree un objeto de estudiante a través de una instanciación en la clase Student y luego pruebe el método displayStudent.
"""
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def display(self):
        print(f'nombre:{self.nombre}, edad: {self.edad}')

class Estudiante(Persona):
    def __init__(self,nombre, edad, seccion):
        Persona.__init__(self,nombre,edad)
        self.seccion = seccion
    def displayStudent(self):
        print(f'nombre:{self.nombre}, edad: {self.edad}, seccion: {self.seccion}')


persona=Persona('Marvelys',20)
persona.display()
estudiante=Estudiante('Sandro', 18, 'A')
estudiante.display()
estudiante.displayStudent()