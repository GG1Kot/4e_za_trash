from scrapers.base import BaseScraper
from models.vacancy import Vacancy 
import requests
class HHScraper(BaseScraper):
    def __init__(self):
        self.base_url = "https://api.hh.ru/vacancies"
        self.user_agent = "your-app-name"
        self.per_page = 20
        self.max_vacancies = 50
        self.area = None
        
    def fetch_vacancies(self, query: str):
        vacancies = []
        page = 0
        max_page = 60
        while page < max_page:
            params = {
                "text": query,
                "per_page": self.per_page,
                "page": page
            }
            response = requests.get(self.base_url, params=params, headers={"User-Agent": self.user_agent})
            data = response.json()
            items = data["items"]
            if len(items) == 0:
                break
            for item in items:

                vacancy = self._item_to_vacancy(item)
                vacancies.append(vacancy)
                if len(vacancies) == self.max_vacancies: break
            if page >= data["pages"] - 1: break
            page += 1
        return vacancies
    
    def _item_to_vacancy(self, item: dict) -> Vacancy:
        title = item.get("name")

        employer = item.get("employer") or {}
        company = employer.get("name")

        area = item.get("area") or {}
        city = area.get("name")

        salary = item.get("salary") or {}
        from_salary = salary.get("from") if salary else None
        to_salary = salary.get("to") if salary else None
        currency = salary.get("currency") if salary else "RUB"

        raw_skills = item.get("key_skills") or []
        skills = [s.get("name") for s in raw_skills if isinstance(s, dict)]
        
        link = item.get("alternate_url")

        return Vacancy(
            title=title,
            company=company,
            city=city,
            from_salary=from_salary,
            to_salary=to_salary,
            currency=currency,
            skills=skills,
            link=link,
        )