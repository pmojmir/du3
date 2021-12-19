import json
from pyproj import CRS, Transformer
from math import sqrt

adresy =  "adresy.geojson"
kontejnery = "kontejnery.geojson"
wgs2jtsk = Transformer.from_crs(CRS.from_epsg(4326), CRS.from_epsg(5514))

def nacteni_geojson(souborJSON):
    """
    Funkce načte soubor, případně ukáže chybu 
    """
    try:
        with open(souborJSON, encoding="utf-8") as openJSON:
            return json.load(openJSON) ["features"]
    except ValueError: 
        print(f"Soubour {souborJSON} nebyl nalezen")
        exit()
    except FileNotFoundError:
        print(f"Soubour {souborJSON} neexistuje")
        exit()
    except PermissionError:
        print(f"Program nemá přístup k  {souborJSON}")
        exit()

def adresa1(vstup):
    """
    Funkce vrací z geojsonu ulici a číslo adresního a souřadnici 
    """
    ulice = vstup["properties"]["addr:street"] + " " + vstup["properties"]["addr:housenumber"]
    fi = vstup["geometry"]["coordinates"][1]
    la = vstup["geometry"]["coordinates"][0]
    return ulice, wgs2jtsk.transform(fi, la)

def kontejner1(vstup):
    """
    Funkce vrací z geojsonu ulici a souřadnice kontejneru.
    Dále je zde podmínka, aby byl konternej volně příspný
    """
    ulice = vstup["properties"]["STATIONNAME"]
    souradnice = vstup["geometry"]["coordinates"]
    pristup = vstup["properties"]["PRISTUP"]
    if pristup=="volně":
        return ulice, souradnice
    
def data1(data, kontejner=True):
    """
    Funkce vrací z geojsonu ulici a souřadnice kontejneru.
    Dále je zde podmínka, aby byl konternej volně příspný
    """
    nacteni = {}
    for vstup in data:
            if kontejner:
                ulice, souradnice = kontejner1(vstup)
            else:
                ulice, souradnice = adresa1(vstup)
            nacteni[ulice] = souradnice
    return (nacteni)
    
def vzdalenost(kontejnery, adresy):
    """
    Fuknce slouží k vypočtení vzdálenosti od adresy k nebližšími veřejnému kontejneru 
    """
    vzdalenosti = {}
    for (adresa_U, adresaS) in adresy.items():
        min_vzd = float('inf')
        for kontejnery_U, kontejnery_S in kontejnery.items():
            if kontejnery_S==None and kontejnery_U==adresa_U:
                min_vzd = 0
                break
            if kontejnery_S==None:
                continue  
            vzdalenost = sqrt(((adresaS[0] - kontejnery_S[0])**2) + ((adresaS[1] - kontejnery_S[1])**2)) #Pythagovova věta 
            if vzdalenost < min_vzd:
                min_vzd = vzdalenost

        if min_vzd > 10000: #Podmínka, že kontejner by měl být méně než 10 km 
            print("Vzdálenost ke kontejneru je delší než 10 km ")
            exit()
        vzdalenosti[adresa_U] = min_vzd
    return vzdalenosti

#Aplikace funkcí 
nacteni_kontejnery = data1(nacteni_geojson(kontejnery))
nacteni_adresy = data1(nacteni_geojson(adresy), False)
vzdalenosti = vzdalenost(nacteni_kontejnery, nacteni_adresy)
prumer = sum(vzdalenosti.values()) / len(vzdalenosti)

#Výpočet maximální vzdálenosti 
MAXIMUM = max(vzdalenosti.values())
for (adresa, vzdalenost) in vzdalenosti.items():
    if vzdalenost == MAXIMUM:
        nej = adresa

# Výpis výsledků, zaokrouhlení 
print(f"Celkem bylo načteno: {len(nacteni_adresy)}")
print(f"Celkem bylo načteno kontejnerů na tříděný odpad: {len(nacteni_kontejnery)}")
print(f"Průměrná vzdálenost adresního bodu ke kontejneru: "f"{prumer:.0f}"" metrů")
print(f"Nejdále ke kontejneru je z adresního bodu '{nej}', konkrétně {MAXIMUM:.0f} metrů")
