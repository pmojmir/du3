Dokumentace k domácímu úkolu číslo 3.

*****
Zadání
*****
Pro zvolenou množínu adresních bodů a množinu kontejnerů na tříděný odpad zjistěte průměrnou a maximální vzdálenost k nejbližšímu veřejnému kontejneru na tříděný odpad. Pro každý adresní bod tedy určete nejbližší veřejný kontejner na tříděný odpad a následně z těchto vzdáleností spočtěte průměr a maximum. Průměr a maximum vypište, pro maximum vypište i adresu, která má nejbližší veřejný kontejner nejdále.

*****
Vstup
*****

Vstupními daty budou 2 soubory GeoJSON. První obsahuje adresní body zvolené čtvrti ve WGS-84, lze jej stáhnout z Overpass Turbo pomocí Exportovat -> Stáhnout jako GeoJSON. V atributu addr:street naleznete jméno ulice, v atributu addr:housenumber naleznete číslo orientační / číslo popisné. Soubor po stažení pojmenujte adresy.geojson a pod tímto jménem ho program také bude načítat.

Druhý soubor obsahuje souřadnice kontejnerů na tříděný odpad, lze jej stáhnout z pražského Geoportálu v S-JTSK. Každý kontejner obsahuje v atributu STATIONNAME adresu, kde se nachází a v atributu PRISTUP, zda je veřejně přístupný, nebo je přístupný pouze obyvatelům domu. Soubor po stažení pojmenujte kontejnery.geojson a pod tímto jménem ho také program bude načítat.

*****
Výstup
*****

Program vypíše, jaká je pro zvolenou množinu adres průměrná nejmenší vzdálenost k veřejnému kontejneru na tříděný odpad a ze které adresy je to k nejbližšímu veřejnému kontejneru nejdále a jak daleko (v metrech, zaokrouhleno na cele metry). Kontejnery, které jsou přístupné pouze obyvatelům domu nebudeme v základní verzi uvažovat. Dále program může, ale nemusí, vypsat statistické údaje o vstupních souborech, jako je počet adres a počet kontejnerů, tyto údaje by měly být stručné a jasné a nic dalšího by program neměl vypisovat (pokud to nepožaduje nějaký bonus).

Testovací data jsou pro oblast Praha 16 Radotín. 