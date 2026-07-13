"""Growth and unit-economics metrics for the ACRE Africa index insurance
time series (2009-2015), pulled from the World Bank GIIF ACP report.

Every function takes a plain pandas Series or two scalars, so it runs on
the committed CSV and on any updated version with the same columns.
"""
from __future__ import annotations

import pandas as pd


def yoy_growth(series: pd.Series) -> pd.Series:
    """Year-over-year percent change. First value is always NaN."""
    return series.pct_change() * 100


def cagr(start_value: float, end_value: float, years: float) -> float:
    """Compound annual growth rate, as a percent."""
    if start_value <= 0 or years <= 0:
        raise ValueError("start_value and years must be positive")
    return ((end_value / start_value) ** (1 / years) - 1) * 100


def premium_per_farmer(premiums_usd: pd.Series, farmers_insured: pd.Series) -> pd.Series:
    """Average premium paid per insured farmer, in USD."""
    return premiums_usd / farmers_insured


def margin_ratio(margin_usd: pd.Series, premiums_usd: pd.Series) -> pd.Series:
    """Margin as a share of premiums collected, as a percent."""
    return (margin_usd / premiums_usd) * 100


def coverage_ratio(investments_insured_usd: pd.Series, premiums_usd: pd.Series) -> pd.Series:
    """How many dollars of farmer investment one premium dollar covers."""
    return investments_insured_usd / premiums_usd
