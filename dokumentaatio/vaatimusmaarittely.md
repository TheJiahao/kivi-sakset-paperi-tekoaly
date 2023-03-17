# Vaatimusmäärittely

## Opinto-ohjelma

Tietojenkäsittelytieteiden kandiohjelma

## Kieli

Ohjelma toteutetaan Pythonilla. Osaan myös Javaa.
Dokumentaatio ja muuttujat ovat suomeksi.

## Käytettävät algoritmit ja tietorakenteet

Sovelluksessa käytetään useaa algoritmia pelaajan syötteen ennustamiseen [(Wang, Huang, et al. 2020)](https://doi.org/10.1038/s41598-020-70544-7).
Ideana käyttää Markovin ketjuun, frekvenssiin sekä mahdollisesti jotain muihin tapoihin perustuvia ennustusta.
Lisäksi käytetään tietorakenteina ainakin:

- taulukkoa/listaa
  - tekoälyjen muistaminen
- jonoa
  - tehokkaasti aiemman $n$-askeleen muistaminen
- sanakirjaa
  - tekoälyjen suoritukseen perustuvien pisteiden säilyttäminen
  - eri syötteiden frekvenssien muistaminen
  - Markovin ketjussa eri tapauksien todennäköisyyksien muistaminen
  - laskurit eri syötteiden määrälle

## Sovelluksen tarkoitus

Ideana on toteuttaa komentoriviohjelma, jolla voidaan pelata kivi-sakset-paperia tietokonetta vastaan tai antaa tekoälyn pelata itseään vastaan.

## Syötteet

Ohjelma ottaa syötteeksi merkin `k` (kivi), `s` (sakset) tai `p` (paperi).

## Aikavaativuus

### Markovin ketjuun perustuva tekoäly, $O(1)$

Eri vaiheet:

- $n$-aikaisemman vaiheen muistaminen eli jonon 1. alkion poistaminen ja alkion lisääminen perään, $O(1)$.
- $n$-aikaisemman askeletta vastaavan tapauksen laskureiden ja todennäköisyyksien päivittäminen sanakirjassa, noin $O(1)$

### Frekvenssiin perustuva tekoäly, O(1)

Eri syötteiden laskurien päivittäminen ja frekvenssien laskeminen, O(1). Eri syötteitä on vakio määrä (3 kpl).

### Yhdistelmätekoäly, $O(k)$

Käydään joka kierroksen alussa läpi kaikki tekoälyt ja valitaan se, jolla on parhaat pisteet.
Tämä onnistuu ajassa $O(k)$, missä $k$ on yksittäisten tekoälyjen määrä.

### Tilavaativuus

### Markovin ketjuun perustuva tekoäly, $O(3^n)$

Ylläpidetään eri $n$-pituisten tapauksien, joita on $3^n$ kpl, todennäköisyyksiä.
Lisätään sanakirjaan sitä mukaan, kun tapauksia esiintyy.
Pelkkä $n$-vaiheen jono vie tilaa $O(n)$ ja on selvästi pienempi kuin $O(3^n)$.

### Frekvenssiin perustuva tekoäly, O(1)

Eniten tilaa vie kolmen parin (syöte, todennäköisyys) sanakirja eli vakiomäärä tilaa tarvitaan.

### Yhdistelmätekoäly, $O(k\cdot 3^n)$

Voidaan arvioida jokaisen tekoälyn tilavaativuutta ylöspäin tilavaativuuteen $O(3^n)$.
Koska tekoälyjä on $k$ kpl, niin yhteensä tarvitaan tilaa $O(k\cdot 3^n)$.

## Lähteet

- Wang, L., Huang, W., Li, Y. et al. Multi-AI competing and winning against humans in iterated Rock-Paper-Scissors game. Sci Rep 10, 13873 (2020). <https://doi.org/10.1038/s41598-020-70544-7>
