# Viikoraportti 4

## Työaikaraportti

|Päivämäärä|Aika|
|----------|----|
|3.4.|40 min|

## Mitä tehty?

- Refaktoroitu `YhdistelmaTekoaly`-luokka
  - Pistetilanteet ovat nyt omassa taulukossa ja samalla indeksillä kuin vastaava tekoäly tekoälyjen taulukossa.
- Poistettu `__hash__`-metodit `MarkovinKetju`-, `MarkovTekoaly` ja `Peli`-luokista, koska sitä ei enää tarvita.

## Mitä seuraavaksi?