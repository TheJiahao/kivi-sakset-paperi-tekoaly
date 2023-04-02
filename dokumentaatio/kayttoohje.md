# Käyttöohje

## Asennus

1. Asenna Python `3.11.x` ja [Poetry](https://python-poetry.org/).
2. Klonaa repositorio.
3. Asenna riippuvuudet:

    ```shell
    poetry install
    ```

## Invoke-tehtävät

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
