# index.py

from thehackernews import scrape_thehackernews
from secintelligence import scrape_secintelligence
from itsecguru import scrape_itsecguru

def print_results(results, site_name):
    print(f"\nScraping {site_name}...")
    for result in results:
        print(f"title: {result['Title']}, link: {result['Url']}")

def main():
    results_a = scrape_thehackernews()
    results_b = scrape_secintelligence()
    results_c = scrape_itsecguru()

    print_results(results_a, "TheHackerNews")
    print_results(results_b, "SecurityIntelligence")
    print_results(results_c, "ITSecurityGuru")

if __name__ == "__main__":
    main()
