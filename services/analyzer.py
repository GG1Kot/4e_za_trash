from models.vacancy import Vacancy
class Analyzer:
    def __init__(self, vacancies):
        self.vacancies = vacancies
        
    def average_salary(self):
        vac = []
        for el in self.vacancies:
            elem = el.average_salary()
            if elem != None:
                vac.append(elem)
        return None if len(vac) == 0 else sum(vac) / len(vac)
    
    def top_cities(self, n: int = 5):
        cities = {}
        for el in self.vacancies:
            city = el.city
            cities[city] = cities.get(city, 0) + 1
        pairs = sorted(cities.items(), key=lambda x: x[1], reverse=True)
        return pairs[:n]
    
    def top_skills(self, n: int = 10):
        skills = {}
        for el in self.vacancies:
            for skill in el.skills:
                skills[skill] = skills.get(skill, 0) + 1
        pairs = sorted(skills.items(), key=lambda x: x[1], reverse=True)
        return pairs[:n]
    