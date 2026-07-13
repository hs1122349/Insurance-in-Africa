# FANAF-CIMA Insurance Market Africa

A small analysis toolkit on Africa's index insurance market, built from
official sources: FANAF, CIMA, and a public World Bank report on the
Global Index Insurance Facility (GIIF).

## What this project does

The tool loads a real seven-year growth table for ACRE Africa, the
private-sector index insurance program covering Kenya, Rwanda, and
Tanzania, and computes year-over-year growth, compound annual growth
rate, premium per farmer, and margin as a share of premiums. It also
reports West Africa's PlaNet Guarantee project results, the 14-country
CIMA insurance zone, and a short set of facts about FANAF and CIMA
themselves.

## Data sources

- World Bank Global Index Insurance Facility (GIIF). "Réalisations du
  Mécanisme Mondial pour l'Assurance Indicielle (GIIF) dans les Pays de
  l'ACP, Phase 1 (2010-2015)." A public disclosure report, supplied by
  Hedi Souki. Pages 8 and 15-16 hold the ACRE Africa and PlaNet Guarantee
  figures used here.
- fanaf.org: the Fédération des Sociétés d'Assurances de Droit National
  Africaines, headquartered in Dakar, Senegal. Fetched 13 July 2026.
- cima-afrique.org: the Conférence Interafricaine des Marchés
  d'Assurance, headquartered in Libreville, Gabon. Fetched 13 July 2026.

See `data/README.md` and `report/sources.md` for exactly which number
came from which page or site, and what was left out because it could
not be confirmed.

## Repo layout

```
fanaf-cima-insurance-market-africa/
├── data/
│   ├── README.md                              data dictionary, source by file
│   ├── acre_africa_performance_2009_2015.csv   real 7-year growth table
│   ├── planet_guarantee_west_africa_summary.csv real project totals
│   ├── cima_member_states.csv                  14 CIMA member countries
│   └── fanaf_cima_org_facts.csv                org-level facts with sources
├── src/
│   ├── loaders.py                              CSV loading helpers
│   └── metrics.py                              growth and unit-economics functions
├── run_analysis.py                              CLI: run the full analysis
├── tests/
│   └── test_metrics.py
└── report/
    ├── results.md                              current numbers, explained in plain text
    └── sources.md                              full source list
```

## Setup

```bash
pip install -r requirements.txt
```

## Usage

```bash
python run_analysis.py
```

Run the tests:

```bash
pytest tests/
```

## What is real and what is not

Every number in `data/` comes from the World Bank GIIF report or from
fanaf.org and cima-afrique.org, with a page or fetch date noted in
`data/README.md`. FANAF's own site shows a category breakdown (life,
non-life, reinsurance, and other company counts) as animated counters
that load through JavaScript. Our fetch tool could not read those
values, so this repo reports only the one confirmed total, 203 member
companies, and does not guess at the breakdown.

## AI use disclosure

AI helped build the structure of this repo, including the module
layout, test scaffolding, and README. The market data, project figures,
and organization facts come directly from the World Bank GIIF report
and the two cited websites. Review the source report and sites yourself
before citing any of these figures elsewhere. This project is a coding
and reporting exercise, not a market research deliverable, and nothing
here should stand in for the original report or a professional
actuarial review.

## License

MIT. See `LICENSE`.
