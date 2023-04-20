# Viikkoraportti 5

## Työaikaraportti

|Päivämäärä|Aika|
|----------|----|
|19.4.|2 tuntia 30 min|

## Mitä tehty?

- Tehty [vertaisarviointi](https://github.com/henryblu/signal-processing-project/issues/1)
- Keksitty idea, jolla `MarkovKetju`-luokan `lisaa` ja `hae_frekvenssi` aikavaativuus saataisiin hiukan nopeammaksi.

## Idea, jolla `MarkovKetju` toimisi $O(1)$-ajassa

Merkitään $n$-kokoisen muistin jonoa $m=m_0,m_1,\dots,m_{n-1}$.
Muodostetaan sanakirjana bijektio $f\colon A\to\\{0,1,\dots,l-1\\}$, missä $A$ on kaikkien vaihtoehtojen joukko.
Merkitään joukon $A$ kokoa $l$.

Muodostetaan toinen funktio $g\colon B\to\mathbb{N}$, missä
$$g(m)=\sum_{k=0}^{n-1}f(m_i)\cdot l^k$$
ja $B$ on kaikkien erilaisten jonojen joukko.
Esimerkiksi jono, jonka jäsenet kuvautuu jonoksi $0,1,2$, vastaa 3-lukujärjestelmän luku $012$.
Nähdään myös, että $g$ on injektio.

Kun muutetaan jonoa $m$, niin muutetaan luvun reunimmaisia numeroita yhteenlaskulla ja kertolaskulla $O(1)$-ajassa, jos tallenetaan luvun $n$ potenssit $l^1,\dots,l^n$ erikseen.
Tähän tarvitaan vain $O(n)$-tilaa.

Käyttämällä tätä jonolle laskettua arvoa voidaan välttää jonon tupleksi muuttaminen/tuplen hajautusarvon laskeminen, joka vie aikaa $O(n)$.

## Mitä seuraavaksi?
