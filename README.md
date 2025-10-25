# Dungeon Generator

Tämä ohjelma generoi näytölle satunnaisen luolaston käyttäen Delaunay-triangulaatiota. 

Huoneita sijoitetaan annettu määrä satunnaisiin paikkoihin ja niiden keskipisteet on yhdistetty triangulaatiolla, joka on toteutettu Bowyer-Watson-algoritmilla. Triangulaatiolle luodaan pienin virittävä puu Primin algoritmilla, joka varmistaa, että kaikkiin huoneisiin pääsee vähintään yhtä reittiä. Lopuksi huoneiden välille piirretään käytävät käyttäen A* polunetsintäalgoritmia. 

Luolastojen generointi tapahtuu reaaliajassa, ilman minkäänlaista havaittavaa viivettä. 

## Asennus

- Kloonaa repositorio
- Mene projektin juurihakemistoon ja aja komento `poetry install`
- Käynnistä poetry-virtuaaliympäristö esimerkiksi komennolla `poetry shell`
- Aja ohjelma komennolla `python src\main.py`

## Käyttö

Ohjelma luo käynnistyessään luolaston oletusparametreilla. Huoneita on vähintään 4 ja enintään 20, mikäli kaikki huoneet mahtuivat ruudulle. Luolastolle on generoitu triangulaatio, pienin virittävä puu, sekä polut kaikille triangulaation sivuille. Oletuksena näytöllä näkyvät ensin vain huoneet ja niiden välillä olevat, pienimmän virittävän puun sivuja vastaavat käytävät.

Käyttäjä voi näyttää/piilottaa triangulaation, pienimmän virittävän puun ja huoneiden keskipisteet vasemmassa laidassa olevien säätimien avulla. Tämän lisäksi käyttäjä voi halutessaa näyttää käytävät kokonaan, myös niiltä osin, jotka menevät huoneiden päälle, valitsemalla pudotusvalikosta vaihtoehdon "näytä käytävät" -> "kaikki".

Käyttäjä voi muuttaa huoneiden määrää dynaamisesti liukusäätimellä. Kun säätimen paikkaa muutetaan, generoidaan luolasto uudelleen vastaamaan huoneiden uutta lukumäärää. 

Käyttäjä voi halutessaan piirtää ylimääräisiä käytäviä pienimmän virittävän puun käytävien lisäksi liukusäätimellä. Oletuksena ylimääräisiä käytäviä ei piirretä.

Painamalla "generoi"-nappia, käyttäjä voi generoida uuden luolaston nykyisillä parametreilla.
