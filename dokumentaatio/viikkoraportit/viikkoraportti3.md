# Viikoraportti 3

## Työaikaraportti

|Päivämäärä|Aika|
|----------|----|
|28.3.|1 tunti|
|1.4.|2 tuntia|
|2.4.|3 tuntia 30 min|

## Mitä tehty?

- Refaktoroitu `MarkovinKetju` Labtoolin palautteen perusteella: Ei tallenneta pelkkiä nollia siirtymämatriisiin.
- Lisätty alustava käyttöohje ja testausdokumentti.
- Lisätty Markovin ketjuun perustuvaa tekoälyä kuvaava `MarkovTekoaly`-luokka ja testattu yksinkertaisissa tapauksissa.
- Refaktoroitu `Peli`-luokka, poistettu turha parametri.
- Lisätty alustava `YhditelmaTekoaly`-luokka.
- Lisätty `__eq__`-metodi `MarkovinKetju`- ja `MarkovTekoaly`-luokille.
- Lisätty hajautusarvot lähes jokaiselle luokalle, (sanakirjaan tarvitaan).

## Epäselvyyksiä

- Tein hajautusarvojen laskut hyödyntäen Pythonin omia hajautusarvoja, mutta en ole varma mitä niiden aikavaativuudet ovat.

## Mitä seuraavaksi?

Seuraavalla viikolla voisin aloittaa pelin logiikan ja käyttöliittymän toteuttamisen.
