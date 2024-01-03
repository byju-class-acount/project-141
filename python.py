import requests
from bs4 import BeautifulSoup
import csv
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


START_URL = "https://en.wikipedia.org/wiki/Lists_of_stars"  


CSV_HEADERS = ["Name", "Distance (light years)", "Mass (Solar mass)", "Radius (Solar radius)"]


star_data = []


def scrape_stars():
    
    response = requests.get(START_URL, verify=False)
    
    if response.status_code == 200:
        
        soup = BeautifulSoup(response.content, 'html.parser')

        
        star_table = soup.find('table')

        
        rows = star_table.find_all('tr')

       
        for row in rows:
          
            cells = row.find_all(['td', 'th'])
            star_row = [cell.text.strip() for cell in cells]
            
           
            if star_row:
                star_data.append(star_row)

       
        with open('star_data.csv', 'w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(CSV_HEADERS)
            csv_writer.writerows(star_data)

if __name__ == "__main__":
    scrape_stars()
