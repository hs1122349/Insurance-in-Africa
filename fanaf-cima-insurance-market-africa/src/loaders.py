"""Load the CSV files in data/ into pandas DataFrames. Thin wrappers, kept
separate from metrics.py so tests can mock file access if needed.
"""
from __future__ import annotations

import pandas as pd


def load_acre_performance(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def load_planet_guarantee_summary(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def load_cima_member_states(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def load_org_facts(path: str) -> pd.DataFrame:
    return pd.read_csv(path)
