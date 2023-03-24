# Viikkoraportti 2

## Työaikaraportti

|Päivämäärä|Aika|
|----------|----|
|22.3.|5 tuntia|
|23.3.|1 tunti 40 min|
|24.3.|3 tuntia|

## Mitä tehty?

- Lisätty ja konfiguroitu kehitystä varten pylint, black, invoke
- Konfiguroitu codecov
- Toteutettu kivi-sakset-paperi-pelialusta ja lisätty testit
- Aloitettu Markovin ketjun toteuttaminen
  - Tehty metodi luomaan kaikki n-pituiset jonot, joissa jokainen jäsen voidaan valita m-tavalla.
  - Muutettu todennäköisyyksien tallennustavaksi siirtymämatriisi [^stochasticMatrix]
  - Lisätty testit MarkovinKetjuluokalle

## Mitä seuraavaksi?

Markovin ketjun ennustustoiminto on vielä buginen eikä toimi oikein, joten se pitäisi korjata.
Lisäksi pitäisi lisätä enemmän testejä rajatapauksia varten.
Voisin myös refaktoroida Markovin ketjusta __havainnot-muuttujan pois, sillä sen voi laskea suoraan vastaavan jonon eri tapauksien frekvenssien summana.

Näiden jälkeen voisi aloittaa Markovin ketjuun perustuvan tekoälyn sekä yhdistelmätekoälyn toteuttamisen ja testaamisen, mikä vie todennäköisesti koko seuraavan viikon.

## Lähteet

[^stochasticMatrix]: Wikipedia, Stochastic matrix, 2022, <https://en.wikipedia.org/wiki/Stochastic_matrix>, luettu 23.3.2023
