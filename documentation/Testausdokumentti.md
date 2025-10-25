# Dungeon Generator - Testit

## Kattavuusraportti

```
Name                 Stmts   Miss Branch BrPart  Cover   Missing
----------------------------------------------------------------
src\delaunay.py         56      0     24      0   100%
src\dungeon.py          52     12     10      0    71%   71-73, 80-90
src\pathfinding.py     105     15     46      2    75%   150, 170->162, 187-193, 200-208
src\prim.py             34      0     12      0   100%
----------------------------------------------------------------
TOTAL                  247     27     92      2    84%
```

Html-raportin voi luoda ajamalla komennon `coverage html`. Tämä luo kansioon htmlcov tiedoston index.html, jonka voi avata selaimessa.

## Mitä testattu

Testit on tehty pytest yksikkötesteillä. Testeillä testataan ohjelman päätoiminnallisuutta ja oleellisia osa-alueita, käyttöliittymän piirtämistä ei testata. Testit löytyvät kansiosta src/tests.

Testeissä on käytetty testiolioita, joille on annettu tarvittavat parametrit. Testit voidaan ajaa komennolla `pytest`.


### dungeon_test.py

Luodaan testi-dungeon samoilla parametreilla, joita ohjelma käyttää oletuksena. 

Generoidaan huoneet ja testataan, että 1. huoneita generoidaan vähintään yksi, mutta ei enempää kuin room_count ja 2. generoidut huoneet eivät ole päällekkäin tai aivan vierekkäin (BUFFER minimiväli)

### delaunay_test.py

Luodaan testi-dungeon samoilla parametreilla, joita ohjelma käyttää oletuksena. Tallennetaan huoneiden keskipisteet, triangulaatio ja kolmioiden sivut muuttujiin.

Testataan, että ohjelma osaa tarkistaa onko piste ympärysympyrän sisällä, ovatko kolme pistettä samalla suoralla ja että triangulaatio luo vähintään yhden kolmion.

Tarkistetaan, että 1. jokainen piste kuuluu ainakin yhteen triangulaatiosta saatuun kolmioon, 2. yksikään piste ei ole sellaisen kolmion, johon se ei kuulu, ympärysympyrän sisällä ja 3. kaikki kolmioiden indeksit ovat valideja.

Testataan, että kaikki sivut, jotka saadaan triangulaatiosta, ovat jossakin kolmiossa.

### prim_test.py

Luodaan testi-dungeon samoilla parametreilla, joita ohjelma käyttää oletuksena. Tallennetaan huoneiden keskipisteet ja pisteiden väliset sivut muuttujiin.

Generoidaan minimum spanning tree ja testataan, että 1. kaikki points-listan pisteet sisältyvät MST:hen, 2. MST:ssä on oikea määrä sivuja ja 3. kaikki MST:n sivut kuuluvat triangulaatioon.

Testataan, että weight laskee euklidisen etäisyyden oikein.

### pathfinding_test.py

Luodaan testi-path ja testataan, että path luo oikean määrän soluja ja että jokainen solu on oikean kokoinen pygame.rect-olio oikeassa sijainnissa

Luodaan testi-dungeon samoilla parametreilla, joita ohjelma käyttää oletuksena.

Testataan, että pikselikoordinaatit muutetaan onnistuneesti grid_table solukoordinaateiksi.

Testataan, että generoitujen huoneiden solujen arvo muutetaan 1:ksi grid_tablessa, ts. huone on "walkable".

Testataan, että naapureiden solukoordinaatit saadaan oikein sekä keskellä että reunasijainneissa.

Testataan, että Manhattan-etäisyys lasketaan oikein.

Testataan, että polku on luotu oikein ja sisältää sen alku- ja loppupisteen.

Testataan, että A*-algoritmi löytää polun alku- ja loppupisteen välille.

Testataan, että polkuja on löydetty ja niillä kaikilla on jokin pituus. Testataan lisäksi, että MST:n polut + ylimääräiset polut kattavat kaikki triangulaation sivut.