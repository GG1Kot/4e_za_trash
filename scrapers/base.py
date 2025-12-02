from abc import ABC, abstractmethod

class BaseScraper(ABC):
    @abstractmethod
    def fetch_vacancies(self, query: str):
        pass
        