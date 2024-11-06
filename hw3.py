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