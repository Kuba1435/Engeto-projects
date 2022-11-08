"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie
author: Jakub Macura
email: kubamacura@email.cz
discord: Kuba1435#9487
"""


from bs4 import BeautifulSoup as soup
from rich.console import Console
from time import sleep
from pprint import pprint
import requests
import sys      
import csv      
import unicodedata           

class WebScraper:
    result = []
    registered = []
    envelopes = []
    valid = []
    fronde = []
    voters = []
    
    a = []
    
    console = Console()
    actions = {"URL address check": True,
                "Checking name and data type of the file": True, 
                "Getting data": True,
                "Data processing": True,
                "Writing data to the data file": True,}
    done = False
    processing = True
    
    link = []
    
    def fetch(self, url):
        return requests.get(url)
        
        
    def parse(self, html):
        """
            Funkce slouží k zpracování dat z webu
        """
        
        #zpracování jmena a cisla obce
        content = soup(html, "html.parser")
        table = content.find_all(class_="overflow_name")
        numbers = content.find_all(class_="cislo")
        
        # Uložení dat
        for name, number in zip(table, numbers):
            self.result.append([name.getText() for name in table])
            self.result.append([number.getText() for number in numbers]) 
    
    
        #data obálek
        links = []
        
        for href in numbers:
            for link in href.find_all("a", href=True):
                link = "http://volby.cz/pls/ps2017nss/" + link["href"]
                election_data = requests.get(link) 
                content_data = soup(election_data.text, "html.parser")
                table2 = content_data.find_all("td", class_="cislo" )
                links.append(link)
   
            # Uložení dat
            for registered, envelopes, valid in zip(table2[3], table2[6], table2[7]):
                registered = unicodedata.normalize("NFKD", registered)
                envelopes = unicodedata.normalize("NFKD", envelopes)
                valid = unicodedata.normalize("NFKD", valid)
                self.registered.append(registered)
                self.envelopes.append(envelopes)
                self.valid.append(valid)  
                    
        #zpracování hlasů
        for link in links:
            election_data = requests.get(link) 
            content_data = soup(election_data.text, "html.parser")
            table2 = content_data.find_all(class_="table", headers="t1sa2 t1sb3")
            pprint(table2)
                

               
                    
    def to_csv(self):
        with open(file_name, "w") as file:
            csv_header = ["code", "location", "registered", "envelopes", "valid"]
            writer = csv.writer(file)
            for header in self.fronde:
                csv_header.append(header)
            writer.writerow(csv_header)
            
            for name, number, registered, envelopes, valid in zip(self.result[0], self.result[1], self.registered, self.envelopes, self.valid):
                writer.writerow([number, name, registered, envelopes, valid])
    
    def input_check(self):
        """simple function which check data and returning if the are correct or not
        """
        global responce
        global file_name
        
        #kontrola správnosti URL
        try:
            responce = self.fetch(sys.argv[1])
        except:
            self.actions["URL address check"] = False
            self.console_output() 
        # else:
        #     if "https://www.volby.cz/pls/ps2021/ps32?xjazyk=CZ&xkraj=" not in responce:
        #         self.actions["URL address check"] = False
        #         self.console_output() 
        
        #kontrola správnosti názvu souboru, do kterého se mají data uložit
        try:
            file_name = sys.argv[2]
            if ".csv" not in file_name:
                self.actions["Checking name and data type of the file"] = False
        except:
            self.actions["Checking name and data type of the file"] = False 
      
        

    def console_output(self):
        with self.console.status("[bold purple]Working on tasks...") as status:
            for check_name, check_values in zip(self.actions.keys(), self.actions.values()):
                sleep(2)
                if check_values == False:
                    self.console.log(f"[bold red]{check_name}    ✕")
                    quit()
                else:
                    self.console.log(f"[bold green]{check_name}    ✓")
                    
            print("Returning output...")
       
                
    def run(self):
        self.input_check()
        self.parse(responce.text)
        # self.console_output()
        self.to_csv()
        
        
if __name__ == "__main__":
    scraper = WebScraper()
    scraper.run()
    