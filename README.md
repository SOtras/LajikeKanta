***************
Ongelman kuvaus


Lajike on jonkin kasvilajin kaupallinen sovellutus, eli kasvilajia on tarkoituksella jalostettu jotta sen ominaisuuksia saadaan muokattua kohti haluttua. Esimerkiksi halutaan saada aikaan tomaattilajike joka kestää kylmää ilmaa ja kasvattaa silti meheviä tomaatteja ilman kasvihuonetta. Lajin ja lajikkeen ero on siinä, että lajit eivät lisäänny keskenään eli ristiin, mutta lajikkeet kuuluvat samaan lajiin, ovat siis saman lajin tarkoituksella jalostettuja alaversioita, joten lajikkeet ovat lisääntymiskykyisiä keskenään. Hyötykasveille ei ole olemassa kunnollista kasviota, johon voisi tallentaa lajikkeita. Lähes kaikki kasviot keskittyvät vain lajeihin ja niille mainitaan joitakin lajikkeita, yleensä vain nimeltä. 

****************
Ratkaisun kuvaus


Olisi hyödyllistä jos olisi olemassa kasvio, johon voi tallentaa nimenomaan lajikkeita (vaikkapa kaikki tomaatit), josta niiden ominaisuuksia voi selata ja täten kuka tahansa voi valita itselleen sopivan lajikkeen kasvatettavaksi. Tietokanta täytyy rakentaa nimenomaan lajikkeita silmällä pitäen ja siten että eri lajikkeita on helppo verrata toisiinsa tai ainakin saada niiden väliset erot selvästi näkyville. Tämä sovellus pyrkii ratkaisemaan useiden kaupallisten lajikkeiden tuoman ongelman.

********************************
Sovelluksen suunnittelufilosofia

Sovelluksesta tehdään kaksi erillistä suunnitteludokumentointia.

Ensimmäisessä dokumentoinnissa noudatetaan versionumerointia alkaen versiosta 0.01 ja sitä kasvatetaan 0.01 välein. Käytän tästä versiosta nimeä "harjoitustyö". Tämä dokumentointi seuraa Helsingin yliopiston tietojenkäsittelytieteen kurssilla "Aineopintojen harjoitustyö: Tietokantasovellus" varsinaista sovellusta, joka löytyy myös tästä kyseisestä Github-repositoriosta. Menettelen näin siksi, että kurssin vaatimuksissa ei esimerkiksi ole vaatimusmäärittelyä. Toiseksi kurssin laajuus on 4 opintopistettä, joten harjoitustyössä ei kannata toteuttaa täyttä tietokantaa kaikilla ominaisuuksilla.

Toinen dokumentointi viedään paljon pidemmälle ja sen versionumerointi alkaa versiosta v1.0 ja sitä kasvatetaan myös 0.01 välein. Käytän tästä versiosta nimeä "täysi sovellus". Halusin kehittää sovelluksen päässäni loppuun asti ja siksi tein myös dokumentin vaatimusmäärittelylle, jotta voin tuoda koko visioni sovelluksesta muidenkin nähtäville. Tässä toisessa dokumentoinnissa on myös tietokanta kehitetty loppuun saakka ajatellen ohjelman mahdollista oikeaa käyttöä. Tätä toista, "täyttä", versiota sovelluksesta ei kuinkaan toteuteta tämän kurssin puitteissa.


*************
Dokumentaatio

Linkki vaatimusmäärittelyyn (täysi sovellus):
Documentation\01_Vaatimusmäärittely.pdf

Linkki tietokantamäärittelyyn (täysi sovellus):
Documentation\02_Tietokantamäärittely.pdf


**************
Versiohistoria

v0.05
- Lisätty tietokantatiedosto gitignoreen.
- Otettu Postgres-tietokanta käyttöön Herokussa.

v0.04
- Otettu käyttöön kirjautusmistoiminto

v0.03
- Otettu käyttöön Herokun automaattinen Github-integraatio.
- Luotu perustoimintoja lajin (Species) tallentamiselle tietokantaan.
- Luotu README.md -tiedostoon kappale "Sovelluksen suunnittelufilosofia".

v0.02
- Luotu Sovellukselle näkymä Herokuun.


v0.01
- Ensimmäinen versio

