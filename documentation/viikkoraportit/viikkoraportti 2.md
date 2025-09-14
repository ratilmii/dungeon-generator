# Viikkoraportti 1

**Käytetty aika:** n. 10 tuntia

## Mitä tehty
Halusin tällä kertaa tehdä luolaston ruudukkomallisena, joten suurin osa ajasta meni sen rakentamiseen ja siihen, että huoneet generoidaan nyt viemään tasan tietyn verran ruutuja aikasempien pikselimittojen sijaan. Luolastoon generoidaan tällä hetkellä 20 satunnaisesti sijoitettua huonetta jotka eivät mene päällekkäin ja napista painamalla satunnaisgeneraatio voidaan tehdä uudestaan. 

Huoneiden keskipisteet saadaan points-listasta, johon ne tallennetaan, kun huoneet generoidaan. Näitä pisteitä tullaan jatkossa käyttämään triangulaatiossa.

## Mitä opittu
Koodia on uskomattoman paljon mukavampi työstää kun muuttujat ym. joiden arvot vaihtelevat kehityksen aikana on määritelty alussa eikä niitä tarvitse metsästää koodin seasta enää jälkeenpäin.

## Epäselvää / vaikeuksia
Palautus jäi ohi deadlinesta, mutta sain sentään valvotun yön jälkeen palautettua sen aamulla. Stressasin paljon toimeen tarttumista ja viivyttelin taas viime hetkeen asti sen takia, joka kostautui nyt tällä tavalla. Tämä kurssi on todella tärkeää saada suoritettua tässä jaksossa, joten paineet ovat kovat ja jokin tässä yhdistelmässä vain pisti stressaamaan ja välttelemään projektin aloittamista.

## Seuraavaksi
Olen alustavasti tyytyväinen siihen, miten huoneiden generointi tapahtuu ja minulla on selvä suunnitelma jatkolle. Seuraava viikko menee triangulaation ja minimum spanning treen tekoon. Ideana oli myös, että syklien määrää voisi halutessaan myös lisätä jos luolastosta haluaa kompleksisemman, mutta taidan keskittyä siihen MST:hen nyt aluksi. 

Lisäksi mikäli aikaa jää, tutkin onko huoneiden määrää mahdollista säädellä dynaamisesti niin, että ne keskittyvät aluksi ruudun keskelle ja uudet huoneet levittäytyvät sitten reunoja kohti.

## Kysymyksiä
Minkälaiset testit olisivat järkeviä tällaisen projektin kanssa?