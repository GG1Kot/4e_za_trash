class Vacancy:
    def __init__(self, title, company, city, from_salary=None, to_salary=None, 
                 currency="RUB", skills=None, link=None):
        self.title = title
        self.company = company
        self.city = city
        self.from_salary = from_salary
        self.to_salary = to_salary
        self.currency = currency
        self.skills = skills or []
        self.link = link
        
    def average_salary(self):
        if self.from_salary is None and self.to_salary is None:
           return None
        elif self.from_salary is None:
           return self.to_salary
        elif self.to_salary is None:
           return self.from_salary
      
        else:
           return (self.from_salary + self.to_salary) / 2
    
    def to_dict(self):
        return self.__dict__.copy()
    
    @classmethod
    def from_dict(cls, data: dict):
        title = data["title"]
        company = data["company"]
        city = data["city"]
        from_salary = data["from_salary"]
        to_salary = data["to_salary"]
        currency = data["currency"]
        skills = data["skills"]
        link = data["link"]
        return cls(title, company, city, from_salary, to_salary, currency, skills, link)