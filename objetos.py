print ("hola mundo OOP PPO")
def transportar (per):
    print ("estoy transportando",per,"personas") 
class carro ():
    
    def __init__(self, name):
        self.nombre = name
        
    def acelerar (self):
        print ("estoy acelerando")
    
    def transportar (self,per):
        print ("estoy transportando",per,"personas",self.nombre)

brw01 = carro("brw01") #crea el objeto
brw01.acelerar()
brw01.transportar(6)

mazda01 = carro("mazda01") #crea el objeto
mazda01.transportar(2)

brw01.transportar (11)
transportar(10)