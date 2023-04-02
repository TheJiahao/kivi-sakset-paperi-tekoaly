# Viikoraportti 3

## Työaikaraportti

|Päivämäärä|Aika|
|----------|----|
|28.3.|1 tunti|
|1.4.|2 tuntia|
|2.4.|5 tuntia 30 min|

## Mitä tehty?

- Refaktoroitu `MarkovinKetju` Labtoolin palautteen perusteella: Ei tallenneta pelkkiä nollia siirtymämatriisiin.
- Lisätty alustava käyttöohje ja testausdokumentti.
- Lisätty Markovin ketjuun perustuvaa tekoälyä kuvaava `MarkovTekoaly`-luokka ja testattu yksinkertaisissa tapauksissa.
- Refaktoroitu `Peli`-luokka, poistettu turha parametri.
- Lisätty `YhditelmaTekoaly`-luokka ja testattu yksinkertaisissa tapauksissa.
- Lisätty sanakirjaa ja testausta varten `__eq__`- ja `__hash__`-metodit usealle luokalle.

## Epäselvyyksiä

- Tein hajautusarvojen laskut hyödyntäen Pythonin valmiita hajautusarvometodeja, joiden aikavaativuuksista en ole varma.
- Koska en ole varma hajautusarvojen aikavaativuuksista, niin mietin onko järkevämpää tallentaa `YhdistelmaTekoaly`-luokassa pisteet sanakirjan sijaan tauluna, missä jokaista tekoälyä vastaava pistemääräjono löytyy samalla indeksillä.
  Tällöin ei tarvita hajautusarvoja ja parhaimman tekoälyn määrittäminen tapahtuisi varmasti $O(km)$-ajassa, missä $k$ on tekoälyjen määrä ja $m$ yhdistelmätekoälyn "fokus" pituus.

## Mitä seuraavaksi?

Seuraavalla viikolla voisin aloittaa pelin logiikan ja käyttöliittymän toteuttamisen sekä aiheeseen liittyvän testauksen.
