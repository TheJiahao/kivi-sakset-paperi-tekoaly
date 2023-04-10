# Viikoraportti 4

## Työaikaraportti

|Päivämäärä|Aika|
|----------|----|
|3.4.|3 tuntia 10 min|
|10.4.|1 tunti 40 min|

## Mitä tehty?

- Refaktoroitu `YhdistelmaTekoaly`-luokka
  - Pistetilanteet ovat nyt omassa taulukossa ja samalla indeksillä kuin vastaava tekoäly tekoälyjen taulukossa.
- Poistettu `__hash__`-metodit `MarkovinKetju`-, `MarkovTekoaly` ja `Peli`-luokista, koska sitä ei enää tarvita.
- Lisätty testejä `YhdistelmaTekoaly`-luokalle
- Lisätty `PeliLogiikka`-luokka, joka vastaa nimenomaan pelin logiikasta
- Lisätty alustava käyttöliittymä

## Mitä seuraavaksi?
