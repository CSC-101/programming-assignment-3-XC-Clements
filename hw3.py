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
#This func takes a list of counties and iterates to find counties in a specified state
def filter_by_state(county_list:list[CountyDemographics], state:str) -> list[CountyDemographics]:
    output_list = []
    for n in county_list:
        if state == n.state:
            output_list.append(n)
    return output_list

print(filter_by_state(data_imports.reduced_data_set, "CA"))

#Part 3
#This function takes a list of counties and an education level, and returns the total population in those counties with that education level
def population_by_education(county_list:list[CountyDemographics], education_level:str) -> float:
    output = 0
    for n in county_list:
        if education_level in n.education:
            output += (n.education[education_level] / 100) * n.population['2014 Population']
        else:
            return 0.0
    return output

print("pop_by_ed", population_by_education(data_imports.reduced_data_set, 'High School or Higher'))

##This function takes a list of counties and an ethnicity, and returns the total population in those counties with that ethnicity
def population_by_ethnicity(county_list:list[CountyDemographics], ethnicity:str) -> float:
    output = 0
    for n in county_list:
        if ethnicity in n.ethnicities:
            output += (n.ethnicities[ethnicity] / 100) * n.population['2014 Population']
        else:
            return 0.0
    return output

print("pop_by_eth", population_by_ethnicity(data_imports.reduced_data_set, 'Asian Alone'))
#This function takes a list of counties and returns the total population under the poverty level
def population_below_poverty_level(county_list:list[CountyDemographics]) -> float:
    try:
        output = 0
        for n in county_list:
            output += (n.income['Persons Below Poverty Level'] / 100) * n.population['2014 Population']
        return output
    except ZeroDivisionError:
        return 0.0

print(population_below_poverty_level(data_imports.reduced_data_set))

#Part 4
#This function takes a list of counties and an education level, and returns the percent of people in the counties matching that criteria
def percent_by_education(county_list:list[CountyDemographics], education_level:str) -> float:
    total_pop = 0
    for n in county_list:
        total_pop += n.population['2014 Population']
    return (population_by_education(county_list, education_level) / total_pop) * 100

print(percent_by_education(data_imports.reduced_data_set, 'High School or Higher'))

#This function takes a list of counties and an ethnicity, and returns the percent of people in the counties matching that criteria
def percent_by_ethnicity(county_list:list[CountyDemographics], ethnicity:str) -> float:
    total_pop = 0
    for n in county_list:
        total_pop += n.population['2014 Population']
    total_percent = (population_by_ethnicity(county_list, ethnicity)/ total_pop) * 100
    return total_percent

print(percent_by_ethnicity(data_imports.reduced_data_set, 'Asian Alone'))
#This function takes a list of counties, and returns the percent of people in the counties matching that criteria
def percent_below_poverty_level(county_list:list[CountyDemographics]) -> float:
    total_pop = 0
    for n in county_list:
        total_pop += n.population['2014 Population']
    return (population_below_poverty_level(county_list) / total_pop) * 100

print(percent_below_poverty_level(data_imports.reduced_data_set))

#Part 5
#This function takes a list of counties, an education level, and a threshold, and returns the counties that have an education level above the threshold
def education_greater_than(county_list:list[CountyDemographics], education_level:str, threshold:float) -> list[CountyDemographics]:
    output_list = []
    for county in county_list:
        if county.education[education_level] > threshold:
            output_list.append(county)
    return output_list

print(education_greater_than(data_imports.reduced_data_set, 'High School or Higher', 90))

#This function takes a list of counties, an education level, and a threshold, and returns the counties that have an education level below the threshold
def education_less_than(county_list:list[CountyDemographics], education_level:str, threshold:float) -> list[CountyDemographics]:
    output_list = []
    for county in county_list:
        if county.education[education_level] < threshold:
            output_list.append(county)
    return output_list

print(education_less_than(data_imports.reduced_data_set, 'High School or Higher', 90))

#This function takes a list of counties, an ethnicity, and a threshold, and returns the counties that have an ethnicity above the threshold
def ethnicity_greater_than(county_list:list[CountyDemographics], ethnicity:str, threshold:float) -> list[CountyDemographics]:
    output_list = []
    for county in county_list:
        if county.ethnicities[ethnicity] > threshold:
            output_list.append(county)
    return output_list

print(ethnicity_greater_than(data_imports.reduced_data_set, 'Asian Alone', 10))

#This function takes a list of counties, an ethnicity, and a threshold, and returns the counties that have an ethnicity below the threshold
def ethnicity_less_than(county_list:list[CountyDemographics], ethnicity:str, threshold:float) -> list[CountyDemographics]:
    output_list = []
    for county in county_list:
        if county.ethnicities[ethnicity] < threshold:
            output_list.append(county)
    return output_list

print(ethnicity_less_than(data_imports.reduced_data_set, 'Asian Alone', 10))

#This function takes a list of counties and a threshold, and returns the counties that have a poverty rate above the threshold
def below_poverty_level_greater_than(county_list:list[CountyDemographics], threshold:float) -> list[CountyDemographics]:
    output_list = []
    for county in county_list:
        if county.income['Persons Below Poverty Level'] > threshold:
            output_list.append(county)
    return output_list

print(below_poverty_level_greater_than(data_imports.reduced_data_set, 10))

#This function takes a list of counties and a threshold, and returns the counties that have a poverty rate below the threshold
def below_poverty_level_less_than(county_list:list[CountyDemographics], threshold:float) -> list[CountyDemographics]:
    output_list = []
    for county in county_list:
        if county.income['Persons Below Poverty Level'] < threshold:
            output_list.append(county)
    return output_list

print(below_poverty_level_less_than(data_imports.reduced_data_set, 10))