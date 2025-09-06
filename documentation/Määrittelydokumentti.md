# Dungeon Generator

## Projektin tarkoitus  
Tarkoituksena on kehittää Pythonilla työkalu luolastojen generointia varten. Luolastot koostuvat satunnaisen kokoisista huoneista, joita yhdistää joukko käytäviä niin, että jokaisesta huoneesta on vähintään yksi reitti kaikkiin muihin huoneisiin.
Työkalua voi käyttää esimerkiksi videopelikehityksessä tai pöytäroolipelaamisessa tarvittavien karttojen luomiseen. 

Käyttäjä määrittelee eri parametreja, esimerkiksi:  
- Huoneiden määrä  
- Huoneiden minimi- ja maksimikoko
- Huoneiden välillä olevien käytävien määrä 
- Huoneiden sijainti muihin huoneisiin verrattuna (kuinka tiheään pakattuja huoneet saavat olla) 

Generoitu luolasto päivittyy reaaliajassa, tai riittävän lähellä sitä, jotta käyttö olisi dynaamista ja erilaisten vaihtoehtojen generointi tapahtuisi nopeasti. Kun käyttäjä on tyytyväinen lopputulokseen, voi luolaston tallentaa tiedostoon (tallennustyyppi tarkentuu projektin aikana).  

## Algoritmit ja toteutus  
Tarkoituksena on hyödyntää **Delaunay-triangulaatiota**, joka toteutetaan **Bowyer-Watson -algoritmilla**. Mahdolliset bonustoiminnallisuudet ja niihin käytetyt algoritmit tarkentuvat projektin aikana.  

## Projektin tiedot  
- **Opinto-ohjelma:** tietojenkäsittelytieteen kandidaatti  
- **Projektin ohjelmointikieli:** Python
- **Dokumentaation kieli:** suomi  
- **Ohjelmointikielet, joilla tehtyjä töitä voin vertaisarvioida:** Python, Java, C++  

## Lisätietoja  
- [Delaunay-triangulation (Wikipedia)](https://en.wikipedia.org/wiki/Delaunay_triangulation)  
- [Bowyer-Watson algorithm (Wikipedia)](https://en.wikipedia.org/wiki/Bowyer%E2%80%93Watson_algorithm)  
