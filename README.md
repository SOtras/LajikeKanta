***************
Ongelman kuvaus


Lajike on jonkin kasvilajin kaupallinen sovellutus, eli kasvilajia on tarkoituksella jalostettu jotta sen ominaisuuksia saadaan muokattua kohti haluttua. Esimerkiksi halutaan saada aikaan tomaattilajike joka kest�� kylm�� ilmaa ja kasvattaa silti mehevi� tomaatteja ilman kasvihuonetta. Lajin ja lajikkeen ero on siin�, ett� lajit eiv�t lis��nny kesken��n eli ristiin, mutta lajikkeet kuuluvat samaan lajiin, ovat siis saman lajin tarkoituksella jalostettuja alaversioita, joten lajikkeet ovat lis��ntymiskykyisi� kesken��n. Hy�tykasveille ei ole olemassa kunnollista kasviota, johon voisi tallentaa lajikkeita. L�hes kaikki kasviot keskittyv�t vain lajeihin ja niille mainitaan joitakin lajikkeita, yleens� vain nimelt�. 

****************
Ratkaisun kuvaus


Olisi hy�dyllist� jos olisi olemassa kasvio, johon voi tallentaa nimenomaan lajikkeita (vaikkapa kaikki tomaatit), josta niiden ominaisuuksia voi selata ja t�ten kuka tahansa voi valita itselleen sopivan lajikkeen kasvatettavaksi. Tietokanta t�ytyy rakentaa nimenomaan lajikkeita silm�ll� pit�en ja siten ett� eri lajikkeita on helppo verrata toisiinsa tai ainakin saada niiden v�liset erot selv�sti n�kyville. T�m� sovellus pyrkii ratkaisemaan useiden kaupallisten lajikkeiden tuoman ongelman.

********************************
Sovelluksen suunnittelufilosofia

Sovelluksesta tehd��n kaksi erillist� suunnitteludokumentointia.

Ensimm�isess� dokumentoinnissa noudatetaan versionumerointia alkaen versiosta 0.01 ja sit� kasvatetaan 0.01 v�lein. K�yt�n t�st� versiosta nime� "harjoitusty�". T�m� dokumentointi seuraa Helsingin yliopiston tietojenk�sittelytieteen kurssilla "Aineopintojen harjoitusty�: Tietokantasovellus" varsinaista sovellusta, joka l�ytyy my�s t�st� kyseisest� Github-repositoriosta. Menettelen n�in siksi, ett� kurssin vaatimuksissa ei esimerkiksi ole vaatimusm��rittely�. Toiseksi kurssin laajuus on 4 opintopistett�, joten harjoitusty�ss� ei kannata toteuttaa t�ytt� tietokantaa kaikilla ominaisuuksilla.

Toinen dokumentointi vied��n paljon pidemm�lle ja sen versionumerointi alkaa versiosta v1.0 ja sit� kasvatetaan my�s 0.01 v�lein. K�yt�n t�st� versiosta nime� "t�ysi sovellus". Halusin kehitt�� sovelluksen p��ss�ni loppuun asti ja siksi tein my�s dokumentin vaatimusm��rittelylle, jotta voin tuoda koko visioni sovelluksesta muidenkin n�ht�ville. T�ss� toisessa dokumentoinnissa on my�s tietokanta kehitetty loppuun saakka ajatellen ohjelman mahdollista oikeaa k�ytt��. T�t� toista, "t�ytt�", versiota sovelluksesta ei kuinkaan toteuteta t�m�n kurssin puitteissa.


*************
Dokumentaatio

Linkki vaatimusm��rittelyyn (t�ysi sovellus):
Documentation\01_Vaatimusm��rittely.pdf

Linkki tietokantam��rittelyyn (t�ysi sovellus):
Documentation\02_Tietokantam��rittely.pdf


**************
Versiohistoria

v0.05
- Lis�tty tietokantatiedosto gitignoreen.
- Otettu Postgres-tietokanta k�ytt��n Herokussa.

v0.04
- Otettu k�ytt��n kirjautusmistoiminto

v0.03
- Otettu k�ytt��n Herokun automaattinen Github-integraatio.
- Luotu perustoimintoja lajin (Species) tallentamiselle tietokantaan.
- Luotu README.md -tiedostoon kappale "Sovelluksen suunnittelufilosofia".

v0.02
- Luotu Sovellukselle n�kym� Herokuun.


v0.01
- Ensimm�inen versio

