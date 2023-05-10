# Käyttöohje

## Asennus

Lataama uusimmasta [releasesta](https://github.com/TheJiahao/kivi-sakset-paperi-tekoaly/releases/tag/loppupalautus) `ksp_peli_linux`-tiedosto.

## Käynnistys

Suorita `ksp_peli_linux`-tiedosto (Linux-käyttöjärjestelmässä).
Käynnistettyään ohjelma tulostaa ohjeet.
Syöttämällä `1` ohjelma kysyy pelin asetuksia, minkä jälkeen peli alkaa.

Pelin alettua pelaaja voi syöttää merkkejä `k` (kivi), `s` (sakset) ja `p` (paperi) tai näiden yhdistelmiä.
Ohjelma käsittelee ne järjestyksessä ja tulostaa pelitulokset.
Syöttämällä `x` peli päättyy.

Pelin päätyttyä ohjelma kysyy asetuksia tilaston graafista esitystä varten ja tulostaa tilaston.

## Asennus ja käynnistäminen Poetryn avulla

1. Asenna Python `3.11.x` ja [Poetry](https://python-poetry.org/).
2. Klonaa repositorio.
3. Asenna riippuvuudet:

    ```shell
    poetry install
    ```

4. Käynnistä ohjelma:

    ```shell
    poetry run invoke start
    ```

### Invoke-tehtävät

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

Suoritettavan ohjelman tuottaminen:

```shell
poetry run invoke build
```

Suoritettava ohjelma ilmestyy juurihakemiston polkuun `dist/ksp_peli`.
Jos ohjelmaa ei pysty suorittaa, niin tarkista, että tiedostolla on suoritusoikeudet.
Jos `build` ei onnistu, niin todennäköisesti käyttöjärjestelmästä puuttuu jokin riippuvuus.
[Pyinstallerin](https://pyinstaller.org/en/stable/index.html) sivulta löytyy lisätietoa.
