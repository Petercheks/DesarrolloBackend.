
class Persona:

    def __init__ (self, nombre):
        self.nombre = nombre
#        self.edad = edad
    
    def saluda(self, otra_persona):
        
        return f'Hola {otra_persona}, me llamo {self.nombre}.'

 
    
if __name__ == '__main__':
    david = Persona('David')
    erika = Persona('Erika')
    
    print(david.saluda(erika))
    
        
  

