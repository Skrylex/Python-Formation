class Classe1:
  def m(self):
    print("Dans classe 1")
    
class Classe2(Classe1):
  def m(self):
    print("Dans classe 2")
    super().m()
    
class Classe3(Classe1):
  def m(self):
    print("Dans classe 3")
    super().m()
    
class Classe4(Classe2, Classe3):
  def m(self):
    print("Dans classe 4")
    super().m()
    
obj = Classe4()
obj.m()