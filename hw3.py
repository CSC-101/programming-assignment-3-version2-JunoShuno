from data import *
def population_total(counties: list[CountyDemographics]) -> int:
    return sum(county.population['2014 Population'] for county in counties)

def filter_by_state(counties: list[CountyDemographics], state_abbr: str) -> list[CountyDemographics]:

    return [county for county in counties if county.state == state_abbr]
def population_by_education(counties: list[CountyDemographics], education_key: str) -> float:

    total = 0.0
    for county in counties:
        if education_key in county.education:
            total += (county.education[education_key] / 100) * county.population['2014 Population']
    return total
def population_by_ethnicity(counties: list[CountyDemographics], ethnicity_key: str) -> float:

    total = 0.0
    for county in counties:
        if ethnicity_key in county.ethnicities:
            total += (county.ethnicities[ethnicity_key] / 100) * county.population['2014 Population']
    return total
def population_below_poverty_level(counties: list[CountyDemographics]) -> float:
    total = 0.0
    for county in counties:
        if 'Persons Below Poverty Level' in county.income:
            total += (county.income['Persons Below Poverty Level'] / 100) * county.population['2014 Population']
    return total

def percent_by_education(counties: list[CountyDemographics], education_key: str) -> float:
    total_population = population_total(counties)
    if total_population == 0:
        return 0.0
    return (population_by_education(counties, education_key) / total_population) * 100
def percent_by_ethnicity(counties: list[CountyDemographics], ethnicity_key: str) -> float:
    total_population = population_total(counties)
    if total_population == 0:
        return 0.0
    return (population_by_ethnicity(counties, ethnicity_key) / total_population) * 100
def percent_below_poverty_level(counties: list[CountyDemographics]) -> float:
    total_population = population_total(counties)
    if total_population == 0:
        return 0.0
    return (population_below_poverty_level(counties) / total_population) * 100
def education_greater_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    return [county for county in counties if county.education.get(key, 0) > threshold]

def education_less_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    return [county for county in counties if county.education.get(key, 0) < threshold]

def ethnicity_greater_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    return [county for county in counties if county.ethnicities.get(key, 0) > threshold]

def ethnicity_less_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    return [county for county in counties if county.ethnicities.get(key, 0) < threshold]

def below_poverty_level_greater_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    return [county for county in counties if county.income.get('Persons Below Poverty Level', 0) > threshold]

def below_poverty_level_less_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    return [county for county in counties if county.income.get('Persons Below Poverty Level', 0) < threshold]
