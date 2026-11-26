# Checkpoint B — Mayeul Bonnaud

Compte GitHub : `OxR0n` · Groupe G01 · Équipe T3M

| Preuve | Travail présenté |
|---|---|
| [Pull Request](01_pull_request.png) | La [PR n°8](https://github.com/matthcab/esilv-marketpulse-g01-t3M/pull/8) ajoute la comparaison d’AAPL et du S&P 500 sur les dates communes du CSV. Elle a été fusionnée dans `main`. |
| Revue de code | À compléter avec la capture `02_code_review.png` d’une revue technique personnelle sur la contribution d’un coéquipier. |
| [Données Yahoo](03_yahoo_market_data.png) | Le fournisseur interroge Yahoo Finance pour AAPL et l’indice `^GSPC`. Il renvoie les identifiants MarketPulse `AAPL` et `SP500` avec la date, les prix et le volume. |
| [Comparaison](04_instrument_benchmark.png) | Sur 23 séances communes du 26 octobre au 25 novembre 2026, le rendement est de +3,39 % pour AAPL et de −6,43 % pour le S&P 500. L’écart calculé avant arrondi est de +9,83 points de pourcentage. |

Les captures Yahoo proviennent de deux exécutions depuis la racine du dépôt sur la branche `feature/yahoo-provider` :

```bash
.venv/bin/python src/providers/yahoo_provider.py
.venv/bin/python src/main.py
```
