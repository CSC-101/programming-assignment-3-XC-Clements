from data import CountyDemographics
import data_imports



#Part 1
#This function takes a county list, and for each item in it adds the 2014 population and outputs the total
def population_total(county_list:list[CountyDemographics]) -> int:
    output_population = 0
    for n in county_list:
        output_population += n.population["2014 Population"]
    return output_population

#Part 2
def filter_by_state(county_list:list[CountyDemographics], state:str) -> list[CountyDemographics]:
    output_list = []
    for n in county_list:
        if state == n.state:
            output_list.append(n)
    return output_list

print(filter_by_state(data_imports.reduced_data_set, "CA"))

#Part 3
def population_by_education(county_list:list[CountyDemographics], education_level:str) -> float:
    output = 0
    for n in county_list:
        if education_level in n.education:
            output += (n.education[education_level] / 100) * n.population['2014 Population']
        else:
            return 0.0
    return output

print(population_by_education(data_imports.reduced_data_set, 'High School or Higher'))

def population_by_ethnicity(county_list:list[CountyDemographics], ethnicity:str) -> float:
    output = 0
    for n in county_list:
        if ethnicity in n.ethnicities:
            output += (n.ethnicities[ethnicity] / 100) * n.population['2014 Population']
        else:
            return 0.0
    return output

print(population_by_ethnicity(data_imports.reduced_data_set, 'Asian Alone'))

def population_below_poverty_level(county_list:list[CountyDemographics]) -> float:
    output = 0
    for n in county_list:
        output += (n.income['Persons Below Poverty Level'] / 100) * n.population['2014 Population']
    return output

print(population_below_poverty_level(data_imports.reduced_data_set))

#Part 4
def percent_by_education(county_list:list[CountyDemographics], education_level:str) -> float:
    total_pop = 0
    for n in county_list:
        total_pop += n.population['2014 Population']
    return (population_by_education(county_list, education_level) / total_pop) * 100

print(percent_by_education(data_imports.reduced_data_set, 'High School or Higher'))

def percent_by_ethnicity(county_list:list[CountyDemographics], ethnicity:str) -> float:
    total_pop = 0
    for n in county_list:
        total_pop += n.population['2014 Population']
    total_percent = (population_by_ethnicity(county_list, ethnicity)/ total_pop) * 100
    return total_percent

print(percent_by_ethnicity(data_imports.reduced_data_set, 'Asian Alone'))

def percent_below_poverty_level(county_list:list[CountyDemographics], education_level:str) -> float:
    total_pop = 0
    for n in county_list:
        total_pop += n.population['2014 Population']
    return (population_below_poverty_level(county_list) / total_pop) * 100

print(percent_below_poverty_level(data_imports.reduced_data_set, 'High School or Higher'))

#Part 5
