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

Následně se vám stáhnou data ze zvoleného webu a uloží do .csv souboru

## Ukázka projektu
Projekt bude předveden na okresu Olomouc:
1. argument: ```https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7102```
2. argument: ```vysledky_olomouc.csv```
#### Spuštění programu:
>python project_3.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7102" "vysledky_olomouc.csv"
### Průběh stahování
Při správném zadání vstupu:
```
URL address check    ✓
Checking name and data type of the file    ✓
Getting data    ✓
Writing data to the data file    ✓
Returning output...
```
Při špatném zadání URL:
```
URL address check ✕
```
Při špatném zadání typu souboru:
```
URL address check    ✓
Checking name and data type of the file    ✕
```
***Částečný výstup:***
```
code, location, registered, envelopes, valid, Občanská demokratická strana,...
552356, Babice, 370, 256, 254, 13, 0, 0, 10, 0	18, 25, 1, 5
500526,Bělkovice-Lašťany, 1801, 1078, 1069, 97, 0, 0, 83, 1, 44, 81, 18, 6
...
```




