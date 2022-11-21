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
import random
class WebScraper:
    result = []
    registered = []
    envelopes = []
    valid = []
    voters = []
    party1 = []
    party2 = []
    table1_data = []
    table2_data =[]
    header = ["code", "location", "registered", "envelopes", "valid"]
    
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
        
        #zpracování jmen a čísel obcí
        content = soup(html, "html.parser")
        table = content.find_all(class_="overflow_name")
        numbers = content.find_all(class_="cislo")
        
        # Uložení dat jmen a cisel obcí
        for name, number in zip(table, numbers):
            self.result.append([name.getText() for name in table])
            self.result.append([number.getText() for number in numbers]) 
    
        #politické strany
        content_data = soup(requests.get("https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=12&xobec=552356&xvyber=7102").text, "html.parser")
        table1_data = content_data.select("table")
        for data in table1_data:
            parties1 = data.find_all(class_="overflow_name", headers="t1sa1 t1sb2")
            parties2 = data.find_all(class_="overflow_name", headers="t2sa1 t2sb2")
            
            for party1 in parties1:
                self.header.append(party1.getText())
                self.party1.append(party1.getText())
                
            for party2 in parties2:
                self.header.append(party2.getText())
                self.party2.append(party2.getText())
            
            # if party1 != []:
            #     self.header.append(party1)        
            # if party2 != []:
            #     self.header.append(party2)  
            # pprint(self.header)
                
        #data obálek
        for href in numbers:
            for link in href.find_all("a", href=True):
                link = "http://volby.cz/pls/ps2017nss/" + link["href"]
                election_data = requests.get(link) 
                content_data = soup(election_data.text, "html.parser")
                envelopes_data = content_data.find_all("td", class_="cislo" )
                
                # data tabulek
                table1_data = content_data.select("table")
                for data in table1_data:
                    # PRVNÍ TABULKA - zpracování hlasů
                    table1_data =data.find_all(headers="t1sa2 t1sb3")
                    table1 = [unicodedata.normalize("NFKD", table1.getText()) for table1 in table1_data]
                    if table1 != []:
                        self.table1_data.append(table1)
                    # DRUHÁ TABULKA - zpracování hlasů
                    table2_data =data.find_all(headers="t2sa2 t2sb3")
                    table2 = [unicodedata.normalize("NFKD", table2.getText()) for table2 in table2_data]
                    if table2 != []:
                        self.table2_data.append(table2)
         
            # Uložení dat obálek
            for registered, envelopes, valid in zip(envelopes_data[3], envelopes_data[6], envelopes_data[7]):
                registered = unicodedata.normalize("NFKD", registered)
                envelopes = unicodedata.normalize("NFKD", envelopes)
                valid = unicodedata.normalize("NFKD", valid)
                self.registered.append(registered)
                self.envelopes.append(envelopes)
                self.valid.append(valid)    
        
        
            
                
    def to_csv(self):
        with open(file_name, "w", newline="") as file:
            # identifying header
            writer = csv.DictWriter(file, fieldnames = self.header)
            writer.writeheader()
            
            # # writing data row-wise into the csv file
            for name, number, registered, envelopes, valid, table1_data, table2_data in zip(self.result[0], self.result[1], self.registered, 
                                                                                            self.envelopes, self.valid, self.table1_data, self.table2_data):
                writer.writerow({
                    "code": number,
                    "location": name,
                    "registered": registered,
                    "envelopes": envelopes,
                    "valid": valid,
                    'Občanská demokratická strana': table1_data[0],
                    'Řád národa - Vlastenecká unie': table1_data[1],
                    'CESTA ODPOVĚDNÉ SPOLEČNOSTI': table1_data[2],
                    'Česká str.sociálně demokrat.': table1_data[3],
                    'Radostné Česko': table1_data[4],
                    'STAROSTOVÉ A NEZÁVISLÍ': table1_data[5],
                    'Komunistická str.Čech a Moravy': table1_data[6],
                    'Strana zelených': table1_data[7],
                    'ROZUMNÍ-stop migraci,diktát.EU': table1_data[8],
                    'Strana svobodných občanů': table1_data[9],
                    'Blok proti islam.-Obran.domova': table1_data[10],
                    'Občanská demokratická aliance': table1_data[11],
                    'Česká pirátská strana': table1_data[12],       
                    'Referendum o Evropské unii': table2_data[0],
                    'TOP 09': table2_data[1],
                    'ANO 2011': table2_data[2],
                    'Dobrá volba 2016': table2_data[3],
                    'SPR-Republ.str.Čsl. M.Sládka': table2_data[4],
                    'Křesť.demokr.unie-Čs.str.lid.': table2_data[5],
                    'Česká strana národně sociální': table2_data[6],
                    'REALISTÉ': table2_data[7],
                    'SPORTOVCI': table2_data[8],
                    'Dělnic.str.sociální spravedl.': table2_data[9],
                    'Svob.a př.dem.-T.Okamura (SPD)': table2_data[10],
                    'Strana Práv Občanů': table2_data[11],             
                })
                
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
        else: 
            if "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=" not in sys.argv[1]:
                self.actions["URL address check"] = False
                self.console_output() 
  
        #kontrola správnosti názvu souboru, do kterého se mají data uložit
        try:
            file_name = sys.argv[2]
        except:
            self.actions["Checking name and data type of the file"] = False 
            self.console_output() 
        else:
            if ".csv" not in file_name:
                self.actions["Checking name and data type of the file"] = False
                self.console_output

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
        self.console_output()
        self.to_csv()
        
        
if __name__ == "__main__":
    scraper = WebScraper()
    scraper.run()
