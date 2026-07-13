"""Compute growth and unit-economics metrics on the ACRE Africa index
insurance time series, and print the West Africa and org-level facts
alongside them.

Usage:
    python run_analysis.py
"""
import pandas as pd

from src.loaders import (
    load_acre_performance,
    load_cima_member_states,
    load_org_facts,
    load_planet_guarantee_summary,
)
from src.metrics import cagr, coverage_ratio, margin_ratio, premium_per_farmer, yoy_growth


def main():
    acre = load_acre_performance("data/acre_africa_performance_2009_2015.csv")

    acre["premium_yoy_pct"] = yoy_growth(acre["premiums_usd"])
    acre["farmers_yoy_pct"] = yoy_growth(acre["farmers_insured"])
    acre["premium_per_farmer_usd"] = premium_per_farmer(acre["premiums_usd"], acre["farmers_insured"])
    acre["coverage_ratio"] = coverage_ratio(acre["investments_insured_usd"], acre["premiums_usd"])
    acre["margin_pct_of_premiums"] = margin_ratio(acre["margin_usd"], acre["premiums_usd"])

    print("=== ACRE Africa performance, 2009-2015 (official, World Bank GIIF ACP report) ===")
    print(acre.round(2).to_string(index=False))

    premium_cagr = cagr(acre["premiums_usd"].iloc[0], acre["premiums_usd"].iloc[-1], 6)
    farmer_cagr = cagr(acre["farmers_insured"].iloc[0], acre["farmers_insured"].iloc[-1], 6)
    print(f"\nPremium CAGR, 2009-2015: {premium_cagr:.1f}%")
    print(f"Farmers insured CAGR, 2009-2015: {farmer_cagr:.1f}%")

    print("\n=== PlaNet Guarantee, West Africa (official, World Bank GIIF ACP report) ===")
    print(load_planet_guarantee_summary("data/planet_guarantee_west_africa_summary.csv").to_string(index=False))

    print("\n=== CIMA member states (official, GIIF ACP report and cima-afrique.org) ===")
    print(load_cima_member_states("data/cima_member_states.csv").to_string(index=False))

    print("\n=== FANAF, CIMA, and GIIF org facts (official, fanaf.org, cima-afrique.org, GIIF ACP report) ===")
    print(load_org_facts("data/fanaf_cima_org_facts.csv").to_string(index=False))


if __name__ == "__main__":
    main()
