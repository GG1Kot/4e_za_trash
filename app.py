from scrapers.hh_scraper import HHScraper
from services.analyzer import Analyzer

def main():
    query = input("Введите запрос (например, 'python разработчик'): ")

    scraper = HHScraper()
    vacancies = scraper.fetch_vacancies(query)

    print(f"Всего вакансий получено: {len(vacancies)}")

    if not vacancies:
        print("Вакансий не найдено, завершаю.")
        return

    analyzer = Analyzer(vacancies)

    avg_salary = analyzer.average_salary()
    top_cities = analyzer.top_cities()
    top_skills = analyzer.top_skills()

    print("\n=== РЕЗУЛЬТАТЫ ===")
    if avg_salary is not None:
        print(f"Средняя зарплата: {avg_salary:.2f}")
    else:
        print("Средняя зарплата: нет данных")

    print("\nТоп городов:")
    for city, count in top_cities:
        print(f"- {city}: {count}")

    print("\nТоп навыков:")
    for skill, count in top_skills:
        print(f"- {skill}: {count}")

if __name__ == "__main__":
    main()