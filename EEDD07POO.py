class Circulo:

   def __init__(self, cx, cy, radio):
      self.cx = cx
      self.cy = cy
      self.radio = radio

   def getCx(self):
      return self.cx
   
   def getCy(self):
      return self.cy
   
   def getRadio(self):
      return self.radio

   def setCx(self, cx):
      if cx is None or not isinstance(cx, (int, float)):
         self.cx = 0
      else:
         self.cx = cx
   
   def setCy(self, cy):
      if cy is None or not isinstance(cy, (int, float)):
         self.cy = 0
      else:
         self.cy = cy
   
   def setRadio(self, radio):
      if radio is None or not isinstance(radio, (int, float)):
         self.radio = 0
      else:
         self.radio = radio
         
   def calcularArea(self):
      import math
      return math.pi * self.radio ** 2
      
   def calcularPerimetro(self):
      import math
      return 2 * math.pi * self.radio
      
   def contienePunto(self, x, y):
      distancia = ((x - self.cx) ** 2 + (y - self.cy) ** 2) ** 0.5
      return distancia <= self.radio
      
   def __str__(self):
      return f"Circulo(cx={self.cx}, cy={self.cy}, radio={self.radio})"


if __name__ == "__main__":
    # Crear un círculo
    c1 = Circulo(5, 10, 7)
    print("Círculo creado:", c1)
    
    print(f"Centro: ({c1.getCx()}, {c1.getCy()})")
    print(f"Radio: {c1.getRadio()}")
    
    print(f"Área: {c1.calcularArea():.2f}")
    print(f"Perímetro: {c1.calcularPerimetro():.2f}")
    
    punto1 = (6, 11)
    punto2 = (20, 20)
    print(f"¿Contiene el punto {punto1}? {c1.contienePunto(*punto1)}")
    print(f"¿Contiene el punto {punto2}? {c1.contienePunto(*punto2)}")
    
    c1.setCx(8)
    c1.setRadio(10)
    print("Círculo modificado:", c1)
    
    c1.setCx(None)
    print("Después de setCx(None):", c1)
    
    c2 = Circulo(0, 0, 5)
    print("Nuevo círculo:", c2)