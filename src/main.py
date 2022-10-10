from professor import Professor
from student import Student

## EXO 1
persons = []
persons.append(Professor("deschamps", "ghislain", "france", "MVMS", ["AMVS"]))
persons.append(Professor("bejenne", "nicolas", "deutschland", "MVMS", ["CDiscount", "CPEMG"]))
persons.append(Student("grossard", "romain", "italy", "UPHF"))
persons.append(Student("bernard", "junior", "chinese", None, ["Branleur"]))
persons.append(Student("euillot", "aurélien", "france"))

for person in persons: print(person)
