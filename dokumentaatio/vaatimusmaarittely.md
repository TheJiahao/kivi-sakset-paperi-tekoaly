# Vaatimusmäärittely

## Opinto-ohjelma

Tietojenkäsittelytieteiden kandiohjelma

## Kieli

Ohjelma toteutetaan Pythonilla, mutta osaan myös Javaa.
Dokumentaatio ja muuttujan nimeäminen tehdään suomeksi.

## Käytettävät algoritmit ja tietorakenteet

Sovelluksessa käytetään eri pituisia Markovin ketjuja pelaajan syötteen ennustamiseen [^multiAi].

Sovelluksessa käytetään ainakin seuraavia tietorakenteita:

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

Ideana on toteuttaa komentoriviohjelma, jolla voidaan pelata kivi-sakset-paperia tietokonetta vastaan tai antaa tekoälyn pelata itseään vastaan ja tutkia mitä tapahtuu.

## Syötteet

Ohjelma ottaa syötteeksi merkin `k` (kivi), `s` (sakset) tai `p` (paperi).

## Aika- ja tilavaativuus

### Markovin ketjuun perustuva tekoäly

Eri vaiheet:

- $n$-aikaisemman vaiheen muistaminen eli jonon 1. alkion poistaminen ja alkion lisääminen perään, $O(1)$.
- $n$-aikaisemman askeletta vastaavan tapauksen laskureiden ja todennäköisyyksien päivittäminen sanakirjassa, noin $O(1)$

Näin ollen aikavaativuus on $O(1)$.

Lisäksi muistetaan todennäköisyyksiä eri $n$-pituisille tapauksille, joita on enintään $3^n$ kpl (lisätään sanakirjaan sitä mukaan, kun tapauksia esiintyy).
Pelkkä $n$-vaiheen muistamiseen tarvittava jono vie tilaa $O(n)$ ja on selvästi pienempi kuin $O(3^n)$.
Täten tilavaativuus on $O(3^n)$.

### Yhdistelmätekoäly

Käydään joka kierroksen alussa läpi kaikki tekoälyt ja valitaan se, jolla on parhaat pisteet.
Tämä onnistuu ajassa $O(k)$, missä $k$ on yksittäisten tekoälyjen määrä.

Lisäksi voidaan arvioida jokaisen tekoälyn tilavaativuutta ylöspäin tilavaativuuteen $O(3^n)$.
Koska tekoälyjä on $k$ kpl, niin yhteensä tarvitaan tilaa $O(k\cdot 3^n)$.

## Jatkokehitysideoita

- Aiheideoissa mainitut Lisko ja Spock mukaan kivi-sakset-paperi-peliin.
  Jos tekoälyt ja varsinainen peli toteutetaan toisistaan riippumattomasti (eli tekoäly ottaa vain pelaajan syöte sekä pelin tulos ja peliluokka laskee kumpi voittaa), niin tämän pitäisi onnistua helposti.
- Muita tapoja ennustamiseen, esimerkiksi voidaan kokeilla sovittaa tulokset diskreetteihin jakaumiin tai muistetaan eri syötteiden suhteelliset frekvenssit aiemmilla $n$-askeleella.

## Lähteet

[^multiAi]:<https://doi.org/10.1038/s41598-020-70544-7> "Wang, L., Huang, W., Li, Y. et al. Multi-AI competing and winning against humans in iterated Rock-Paper-Scissors game. Sci Rep 10, 13873 (2020)"
