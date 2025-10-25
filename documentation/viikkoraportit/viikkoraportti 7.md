# Viikkoraportti 7 (lopullinen palautus)

**Käytetty aika:** n. 25-30 tuntia.

## Mitä tehty
Pathfinding on saatu toteutettua valmiiksi. Ohjelma löytää nyt A*-algoritmilla polut kaikille triangulaation sivuille ja oletuksena piirtää niistä pienimmän virittävän puun polut. Käyttäjä voi myös halutessaan piirtää lisää polkuja näytöllä olevalla liukusäätimella. 

Ohjelman lopullinen UI on toteutetty pygame_guilla.

Pathfindingin testit on tehty.

Ohjelma on nyt kaiken kaikkiaan sellaisessa kunnossa, että voin olla tyytyväinen siihen, vaikka en lisäisi siihen enää tämän jälkeen mitään.

## Mitä opittu
A* pathfinding oli kaikista työläin urakka, mutta se on nyt mielestäni hyvin hallussa. Tämän lisäksi tuli opiskeltua pygame_gui:ta ensimmäistä kertaa ja sain ohjelman ulkoasun mielestäni ihan mukavalle mallille.

## Epäselvää / vaikeuksia
Vaikka kuinka yritin säätää polkujen painotuksia ja suosia jo luotuja polkuja, silloin tällöin tulee edelleen tapauksia, joissa kaksi polkua ovat vieri vieressä, vaikka niiden pitäisi yhdistyä. En tiedä mistä tämä johtuu, mutta se ei loppujen lopuksi ole niin suuri ongelma, että se olisi jäänyt vaivaamaan. Kyseessä lähinnä kosmeettinen haitta ja enimmäkseen vain silloin, kun polkuja piirretään enemmäin kuin MST.

## Seuraavaksi
Korkeintaan pientä hienosäätöä, mikäli inspiraatio iskee. Kurssi on kuitenkin nyt loppu.

## Kysymyksiä
Ainoastaan se olisi kiva kuulla, jos koodista sattuu silmään syy sille, että polut eivät yhdisty, mutta muuten ei mitään.