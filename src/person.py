class Person:  
  countries = ["FRANCE", "ITALY", "DEUTSCHLAND"]
  id = 0
  
  def __init__(self, lastname, firstname, country = None) -> None:
    self.lastname = lastname
    self.firstname = firstname
    self.country = country
    self._id = self.__class__.id
    self.__class__.id += 1
  
  @property
  def firstname(self) -> str: 
    return self.__firstname.capitalize()
  
  @property
  def lastname(self) -> str: 
    return self.__lastname.capitalize()
  
  @property
  def country(self) -> str:
    if self.__country.upper() in self.countries:
      return self.__country.capitalize()
    else:
      return None
  
  @firstname.setter
  def firstname(self, firstname) -> None:
    self.__firstname = firstname
  
  @lastname.setter
  def lastname(self, lastname) -> None:
    self.__lastname = lastname
    
  @country.setter
  def country(self, country) -> None:
    self.__country = country
    
  def fullname(self) -> str:
    return f"{self.lastname} {self.firstname}"
    
  def __str__(self) -> str:
    msg = "===========================\n"
    msg += f"{self.__class__.__name__}#{self._id} : {self.fullname()}"
    msg += f" et son pays est : {self.country}." if self.country else "."
    return msg

