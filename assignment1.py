import requests
from prettytable import PrettyTable

class CountryInfo:
    def __init__(self):
        self.api_url = 'https://restcountries.com/v3.1/all'
        self.data = None

    def fetch_data(self):
        response = requests.get(self.api_url)
        response.raise_for_status() 
        return response.json()
    
    def display_countries(self):
        self.data = self.fetch_data()
        
        table = PrettyTable()
        table.field_names = ['Name', 'Capital', 'Flag']
        
        for country in self.data:
            name = country.get('name', {}).get('common', 'N/A')
            capital = country.get('capital', ['N/A'])[0]
            flag_url = country.get('flags', {}).get('png', 'N/A')
            
            table.add_row([name, capital, flag_url])
        
        print(table)

if __name__ == '__main__':
    country_info = CountryInfo()
    country_info.display_countries()
