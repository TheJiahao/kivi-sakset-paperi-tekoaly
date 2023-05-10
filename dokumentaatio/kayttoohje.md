# Käyttöohje

## Asennus

1. Asenna Python `3.11.x` ja [Poetry](https://python-poetry.org/).
2. Klonaa repositorio.
3. Asenna riippuvuudet:

    ```shell
    poetry install
    ```

## Käynnistys

Sovellus käynnistyy komennolla:

```shell
poetry run invoke start
```

Käynnistettyään ohjelma tulostaa ohjeet.
Syöttämällä `1` ohjelma kysyy pelin asetuksia, minkä jälkeen peli alkaa.

Pelin alettua pelaaja voi syöttää merkkejä `k` (kivi), `s` (sakset) ja `p` (paperi) tai näiden yhdistelmiä.
Ohjelma käsittelee ne järjestyksessä ja tulostaa pelitulokset.
Syöttämällä `x` peli päättyy.

Pelin päätyttyä ohjelma kysyy asetuksia tilaston graafista esitystä varten ja tulostaa tilaston.

## Invoke-tehtävät

Ilmeisesti Windows-koneilla invoke-tehtävät ei toimi.
Saattaa korjaantua asettamalla `tasks.py` tiedostosta `ctx.run`-metodin parametriksi `pty=False`.
Jos ei onnistu, niin alkuperäiset komennot löytyvät `tasks.py`-tiedostosta.

Seuraavat Invoke-tehtävät toimivat projektin juurihakemistossa.

Kattavuusraportin luominen:

```shell
poetry run invoke coverage-report
```

Koodin formatointi:

```shell
poetry run invoke format
```

Pylint:

```shell
poetry run invoke lint
```

Testaus:

```shell
poetry run invoke test
```
