# Bloomberg Field Mapping

## Access mode

**APPROVED_SAMPLE**

- Source inspectée : `data/sample/bloomberg_reference_sample.json`.
- Résultat canonique attendu : `data/sample/bloomberg_reference_expected.json`.
- Connexion Bloomberg LIVE : **non démontrée**.

Les valeurs sont des exemples pédagogiques issus de `data/sample/prices.csv`, pas des observations historiques certifiées Bloomberg. Le fichier source indique `is_live_bloomberg_output: false`.

La référence `docs/10_BLOOMBERG_INSTRUCTOR_REFERENCE.md` est citée dans l’énoncé, mais absente du dépôt consulté. Les correspondances ci-dessous proviennent des deux JSON présents.

## Market instruments

| Rôle | Ticker canonique | Identifiant Bloomberg |
|---|---|---|
| Instrument | AAPL | AAPL US Equity |
| Benchmark | SP500 | SPX Index |

Le projet conserve les tickers `AAPL` et `SP500`. Les identifiants Bloomberg restent à la frontière du fournisseur.

## Inspected input

Le JSON contient une liste `series`. Chaque série indique `role`, `canonical_ticker`, `provider_identifier` et une liste `observations`.

Les deux séries contiennent chacune 21 observations, du `2026-09-01` au `2026-09-30`. Tous les champs attendus sont présents, sans valeur nulle. Le volume du benchmark vaut zéro dans cet échantillon ; il doit être conservé tel quel.

## Field mapping

Les noms `observation_date`, `open_value`, `high_value`, `low_value`, `close_value` et `volume_value` sont des **clés pédagogiques**, pas des noms de champs Bloomberg LIVE.

| Champ MarketPulse | Source dans l’échantillon | Conversion pour le TD10 |
|---|---|---|
| `date` | `series[].observations[].observation_date` | Conserver la chaîne `YYYY-MM-DD` |
| `ticker` | `series[].canonical_ticker` | Recopier `AAPL` ou `SP500` dans chaque ligne |
| `open` | `series[].observations[].open_value` | Convertir en `float` |
| `high` | `series[].observations[].high_value` | Convertir en `float` |
| `low` | `series[].observations[].low_value` | Convertir en `float` |
| `close` | `series[].observations[].close_value` | Convertir en `float` |
| `volume` | `series[].observations[].volume_value` | Convertir en `int` |

## TD10 handoff

- Mode : `APPROVED_SAMPLE`.
- Identifiants : `AAPL US Equity` et `SPX Index`.
- Dates : chaînes au format `YYYY-MM-DD`.
- Entrée : liste `series`, puis liste `observations` pour chaque série.
- Champs manquants : aucun dans l’échantillon inspecté.
- Normalisation : appliquer le tableau, conserver les tickers canoniques et le volume zéro du benchmark.
- Validation : comparer les 42 lignes produites à `data/sample/bloomberg_reference_expected.json` ; la correspondance a été vérifiée sur les fichiers présents.
- Intégration : transmettre les lignes canoniques à l’alignement et aux calculs existants de `analytics.py`.

Ce document prépare l’implémentation du fournisseur au TD10. La revue du document avant fusion reste à effectuer.
