from person import Person
from curriculum_mixin import CurriculumMixin

class Student(Person, CurriculumMixin):
  id = 0
  
  def __init__(self, name, firstname, country, school = None, previous_schools = None) -> None:
    super().__init__(name, firstname, country)
    self.__school = school
    self.__previous_schools = previous_schools
    
  @property
  def school(self) -> str:
    return self.__school

  @property
  def previous_schools(self):
    return self.__previous_schools or []
  
  @school.setter
  def school(self, school) -> None:
    self.__school = school
    
  def __str__(self) -> str:
    msg = super().__str__()
    msg += f" Sa classe est {self.school}." if self.school else ""
    msg += f"\n{self.pro()}"
    return msg