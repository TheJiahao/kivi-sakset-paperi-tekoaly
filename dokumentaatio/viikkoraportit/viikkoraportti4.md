# Viikoraportti 4

## Työaikaraportti

|Päivämäärä|Aika|
|----------|----|
|3.4.|3 tuntia 10 min|
|10.4.|2 tunti 40 min|
|16.4.|5 tuntia 40 min|

## Mitä tehty?

- Refaktoroitu `YhdistelmaTekoaly`-luokka
  - Pistetilanteet ovat nyt omassa taulukossa ja samalla indeksillä kuin vastaava tekoäly tekoälyjen taulukossa.
- Poistettu `__hash__`-metodit `MarkovinKetju`-, `MarkovTekoaly` ja `Peli`-luokista, koska sitä ei enää tarvita.
- Lisätty testejä `YhdistelmaTekoaly`-luokalle
- Lisätty `PeliLogiikka`-luokka, joka vastaa nimenomaan pelin logiikasta
- Lisätty alustava käyttöliittymä
- Lisätty alustava toteutusdokumentti
- Päivitetty testausdokumenttia

## Mitä seuraavaksi?

- Käyttöliittymän hienosäätöä
- `YhdistelmaTekoaly`-luokalle ominaisuus, että jokaisen pelin jälkeen vaihdetaan muutaman edellisen kierroksen tuloksien perusteella
- Dokumentaation kirjoittamista
- Muiden koodien vertaisarviointi
