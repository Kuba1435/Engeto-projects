# ENGETO 3. projekt
Třetí projekt na Engeto python Akademii 

## Popis projektu
Pomocí tohoto projektu si můžete zpřehlednit výsledky voleb do Poslanecké sněmovny z roku 2017.

### Instalace knihoven
Pro spuštění kódu budete potřebovat knihovny uložené v ``` requirements.txt ```. **Pro instalaci postupujte následovně:**

1. zkontrolujte zda máte aktivní virtuální prostřední, do kterého chcete nainstalovat požadované knihovny
2. do konzole zadejte:
    -  ```pip install -r requirements.txt```
    -  popřípadě že nemáte doposud nainstalovaný manažer *pip* proveďte do konzole následující příkaz: ```pip install package_name```    
<sub>Pokud jste byli úspěšní pokračujte na následující krok. Pokud ne, doporučuji zjistit si potřebné informace na internetu např. [zde](https://stackoverflow.com/)</sub>

### Spuštění projektu
Spuštění souboru ***project_3.py*** vyžaduje dva vstupy, a to:
- odkaz na požadovanou stránku
- název souboru, do kterého se mají data uložit končící **.csv**

>python project_3.py <odkaz na stránku> <název souboru.csv>

Následně se vám stáhnou data ze svoleného webu a uloží do .csv souboru

## Ukázka projektu
Projekt bude předveden na okresu Olomouc:
1. argument: ```https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7102```
2. argument: ```vysledky_olomouc.csv```
#### Spuštění programu:
>python project_3.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7102" "vysledky_olomouc.csv"
#### Průběh stahování

```#50C878```URL address check    ✓
```#50C878```Checking name and data type of the file    ✓
```#50C878```Getting data    ✓
```#50C878```Writing data to the data file    ✓
