# Dungeon Generator - Toteutus

## Yleisrakenne

Ohjelma generoi luolaston, jossa on annettu määrä huoneita. Huoneiden keskipisteet on yhdistetty Delaunay-triangulaatiolla, jolle on löydetty pienin virittävä puu Primin algoritmilla. Tämän jälkeen triangulaation sivuille on tehty pathfinding A*-algoritmilla. Löydetyt polut on jaettu pienimmän virittävän puun polkuihin ja muihin, "ylimääräisiin" polkuihin.

Ohjelma piirtää oletuksena näytölle luolaston huoneet ja pienimmän virittävän puun polut niin, että polut eivät näy huoneiden kanssa päällekkäin. Käyttäjä voi halutessaan muuttaa huoneiden ja ylimääräisten polkujen määrää dynaamisesti, sekä näyttää tai piilottaa triangulaation, pienimmän virittävän puun ja polkujen osat, jotka menevät huoneiden päälle. 

## Aika- ja tilavaativuudet (pseudokoodien perusteella)

### Bowyer-Watson
Aika: O(n²) pahimmillaan, O(n log n) keskimäärin.

Tila: O(n).

missä n on triangulaation pisteiden määrä.

### Prim

Aika: O(V²) naiivi.

Tila: O(V + E).

missä V on pisteiden määrä, E on sivujen määrä.

### A*

Aika: O(b^d) pahimmillaan, O((V + E) log V) käytännössä.

Tila: O(b^d).

missä b on solun keskimääräinen naapurien määrä, d on lyhyimmän polun pituus.

## Puutteet ja parannusehdotukset

Tällä hetkellä on edelleen mahdollista, että jotkin polut kulkevat vierekkäin yhdistymisen sijaan. En tiedä mistä tämä johtuu, enkä saanut sitä ratkaistua ajoissa.

Piirtoalue voisi olla äärettömän kokoinen ja vieritettävissä.

Valmiin luolaston tulostaminen kuvana.

## Laajojen kielimallien käyttö

ChatGPT:tä käytetty enimmäkseen "palautteen" antamiseen, eli ts. teen toteutuksen ja kysyn, vaikuttaako se hyvältä, vai olenko mahdollisesti jättänyt jotain huomiotta. Lisäksi jos jäin jumiin, enkä löytänyt virhettä, kysyin apua tällaisessa tapauksessa. Esimerkiksi yhdessä kohtaa polut generoitiin vääriin paikkoihin, koska olin vahingossa käyttänyt taulukon rivejä ja sarakkeita väärässä järjestyksessä.

## Lähteet

https://en.wikipedia.org/wiki/Bowyer%E2%80%93Watson_algorithm

https://en.wikipedia.org/wiki/Prim's_algorithm

https://en.wikipedia.org/wiki/A*_search_algorithm