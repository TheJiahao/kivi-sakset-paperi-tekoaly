# Testausdokumentti

[![codecov](https://codecov.io/gh/TheJiahao/kivi-sakset-paperi-tekoaly/branch/main/graph/badge.svg?token=RBLETVT7VW)](https://codecov.io/gh/TheJiahao/kivi-sakset-paperi-tekoaly)

## Yksikkö- ja integraatiotestaus

Yksikkötestauksen kattavuusraportti on nähtävissä Codecovissa klikkaamalla yllä olevaa kuvaketta.

## Tietorakenteet

Markovin ketjua kuvaava `MarkovinKetju`-luokka on testattu yksikkötesteillä.

## Sovelluslogiikka

Pelin toimintaa kuvaava `Peli`-luokka on testattu yksikkötesteillä oletus- eli kivi-sakset-paperi-peliä vastaavilla parametreilla.

## Testien toistaminen

Asenna projekti [käyttöohjeen](kayttoohje.md) mukaan.
Yksikkötestien suorittaminen onnistuu komennolla:
```poetry run invoke test```
