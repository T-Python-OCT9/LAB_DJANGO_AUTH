
class Doctors:
    
    def __init__(self, name : str, description : str, specialization: str, experience_years: str, rating: float) -> None:
        
        self.__name = name
        self.__description = description
        self.__specialization = specialization
        self.__experience_years = experience_years
        self.__rating = rating

    
    def describe(self):
        return f" {self.getName()} ,  {self.getDescription()}, {self.getSpecialization()},  {self.getExperienceYears()},  {self.getRating()}  "


    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name
    
    def getDescription(self):
        return self.__description

    def getSpecialization(self):
        return self.__specialization

    def getExperienceYears(self):
        return self.__experience_years

    def getRating(self):
        return self.__rating    