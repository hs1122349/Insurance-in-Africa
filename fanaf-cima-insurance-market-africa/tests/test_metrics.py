"""Unit tests for the metrics functions. Small synthetic series only.

Run with: pytest tests/
"""
import pandas as pd
import pytest

from src.metrics import cagr, coverage_ratio, margin_ratio, premium_per_farmer, yoy_growth


def test_yoy_growth_basic():
    series = pd.Series([100, 150, 120])
    result = yoy_growth(series)
    assert pd.isna(result.iloc[0])
    assert result.iloc[1] == pytest.approx(50.0)
    assert result.iloc[2] == pytest.approx(-20.0)


def test_cagr_doubling_over_one_year():
    assert cagr(100, 200, 1) == pytest.approx(100.0)


def test_cagr_flat_series_is_zero():
    assert cagr(100, 100, 5) == pytest.approx(0.0)


def test_cagr_rejects_non_positive_start():
    with pytest.raises(ValueError):
        cagr(0, 100, 5)


def test_cagr_rejects_non_positive_years():
    with pytest.raises(ValueError):
        cagr(100, 200, 0)


def test_premium_per_farmer():
    premiums = pd.Series([1000.0, 2000.0])
    farmers = pd.Series([100, 200])
    result = premium_per_farmer(premiums, farmers)
    assert result.iloc[0] == pytest.approx(10.0)
    assert result.iloc[1] == pytest.approx(10.0)


def test_margin_ratio():
    margin = pd.Series([50.0, 100.0])
    premiums = pd.Series([500.0, 1000.0])
    result = margin_ratio(margin, premiums)
    assert result.iloc[0] == pytest.approx(10.0)
    assert result.iloc[1] == pytest.approx(10.0)


def test_coverage_ratio():
    investments = pd.Series([10000.0])
    premiums = pd.Series([1000.0])
    result = coverage_ratio(investments, premiums)
    assert result.iloc[0] == pytest.approx(10.0)
