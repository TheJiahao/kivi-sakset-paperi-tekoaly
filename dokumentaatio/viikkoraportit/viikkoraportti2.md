# Viikkoraportti 2

## Työaikaraportti

|Päivämäärä|Aika|
|----------|----|
|22.3.|5 tuntia|
|23.3.|1 tunti 40 min|
|24.3.|3 tuntia|
|25.3.|2 tuntia|

## Mitä tehty?

- Lisätty ja konfiguroitu pylint, black, invoke
- Konfiguroitu codecov
- Toteutettu kivi-sakset-paperi-pelialusta ja lisätty testit
- Toteutettu Markovin ketju
  - Tehty metodi luomaan kaikki n-pituiset jonot, joissa jokainen jäsen voidaan valita m-tavalla.
  - ~~Muutettu todennäköisyyksien tallennustavaksi siirtymämatriisi [^stochasticMatrix]~~.
    Tallennetaan ainoastaan erilaisia jonoja seuraavien syotteiden frekvenssit.
    Todennäköisyydet voidaan laskea tästä suoraan.
  - Lisätty testit MarkovinKetju-luokalle

## Mitä seuraavaksi?

Seuraavaksi voisin aloittaa Markovin ketjuun perustuvan tekoälyn sekä yhdistelmätekoälyn toteuttamisen ja testaamisen, mikä vie todennäköisesti koko seuraavan viikon.

## Lähteet

[^stochasticMatrix]: Wikipedia, Stochastic matrix, 2022, <https://en.wikipedia.org/wiki/Stochastic_matrix>, luettu 23.3.2023
