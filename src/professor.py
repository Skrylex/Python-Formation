from person import Person
from curriculum_mixin import CurriculumMixin

class Professor(Person, CurriculumMixin):
  id = 0
  
  def __init__(self, name, firstname, country, company = None, previous_companies = None) -> None:
    super().__init__(name, firstname, country)
    self.__company = company
    self.__previous_companies = previous_companies

  @property
  def company(self) -> str:
    return self.__company

  @property
  def previous_companies(self):
    return self.__previous_companies or []
  
  @company.setter
  def domain(self, company) -> None:
    self.__company = company
    
  def __str__(self) -> str:
    msg = super().__str__()
    msg += f" Son entreprise est {self.company}." if self.company else ""
    msg += f"\n{self.pro()}"
    return msg