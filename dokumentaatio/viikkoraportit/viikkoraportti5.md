# Viikkoraportti 5

## Työaikaraportti

|Päivämäärä|Aika|
|----------|----|
|19.4.|2 tuntia 30 min|
|20.4.|3 tuntia|
|22.4.|1 tunti|

## Mitä tehty?

- Tehty [vertaisarviointi](https://github.com/henryblu/signal-processing-project/issues/1)
- Keksitty idea (tarkemmin toteutusdokumentissa), jolla `MarkovKetju`-luokan `lisaa` ja `hae_frekvenssi` aikavaativuus saataisiin hiukan nopeammaksi.
- Refaktoroitu `MarkovKetju` käyttäen edellä mainittua ideaa.
- Refaktoroitu `YhdistelmaTekoaly`-luokka
  - Lisätty toiminnallisuus vaihtaa tekoäly kierroksittain edellisten kierroksien pisteiden perusteella. Katsoin tarkemmin [paperissa](https://doi.org/10.1038/s41598-020-70544-7) esitettyä taulukkoa tekoälyn toiminnasta ja siellä tekoälyn vaihto ei ollut useammin kuin fokus pituuden välein.
  - Pisteiden summasta pidetään erikseen kirjaa, minkä parantaa `hae_paras_tekoaly`-metodin aikavaativuutta $O(m^2)\to O(m)$.

## Mitä seuraavaksi?
