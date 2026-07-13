# Data dictionary

Every file in this folder traces back to one of three sources: the World
Bank's Global Index Insurance Facility (GIIF) report on ACP countries
(2010-2015), fanaf.org, or cima-afrique.org. Read this file before you
trust any number here.

## acre_africa_performance_2009_2015.csv (official)

A real seven-year table copied from page 8 of the World Bank GIIF ACP
report. It tracks ACRE Africa, the private-sector index insurance program
covering Kenya, Rwanda, and Tanzania. Columns: year, dollar value of
farmer investments covered by insurance, premiums collected in dollars,
number of insured farmers, and margin in dollars. The 2009 margin cell is
blank because the source table marks it with a dash, meaning no figure
was reported that year, not zero.

## planet_guarantee_west_africa_summary.csv (official)

Single-point statistics on PlaNet Guarantee's "Assurance Récolte Sahel"
project, covering Benin, Burkina Faso, Cote d'Ivoire, Mali, and Senegal
between 2011 and 2014, cited on page 15 of the same report. These are
end-of-project totals, not a time series.

## cima_member_states.csv (official)

The 14 member states of the CIMA insurance code zone, cited on page 15
of the GIIF report and confirmed by the country's own listing on
cima-afrique.org.

## fanaf_cima_org_facts.csv (official)

A short list of facts about FANAF, CIMA, and the GIIF program itself,
each with its own source page or site. FANAF's 203-member figure comes
directly from the live counter on fanaf.org's home page. FANAF's site
also shows category counters for life, non-life, reinsurance, and other
company types, but those load through JavaScript and returned as zero
in our fetch, so we left them out rather than guess.

## What is not here

BMCE-style paywalled or JavaScript-only figures are not the concern for
this repo. The concern here is that FANAF's category breakdown (life vs
non-life vs reinsurance company counts) could not be read through our
fetch tool, so this repo only reports the one confirmed total (203
members) and does not include a fabricated breakdown.
