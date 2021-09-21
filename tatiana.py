class persona():
    def __init__(self,name):
            self.nombre = name
            
    def cantando(self):
        print ("estoy cantando")
        
    def bailar(self):
        print ("estoy bailando")
        
    def jugar (self):
        print("estoy jugando")
        
doctora = persona("monica")
arquitecto = persona ("kevin")
cantante = persona ("tiago")
 
doctora.bailar()
arquitecto.jugar()
cantante.cantando()
      