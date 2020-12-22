from CSE8ACSV import *

blm_protest_data = get_blm_data("blm_state.csv")
tech_diversity_data = get_diversity_data("tech_diversity.csv")
state_populations = get_state_pops()

def total_blm_protests(states):
    #TODO: Fill in the function body
    total = 0
    for item in states:
        for row in blm_protest_data:
            if row['State'] == item:
                s = row['TotalProtests']
                total += s
    return int(total)


def protest_attendance(threshold):
    #TODO: Fill in the function body
    lst = []
    for row in blm_protest_data:
        for state in state_populations:
            if row['TotalAttendance']/state_populations.get(state) > threshold/100 and state == row['State']:
                lst.append(row['State'])
    return lst

def diversity_in_tech(threshold, field):
    #TODO: Fill in the function body
    dic = {}
    for company in tech_diversity_data:
        if tech_diversity_data[company][field] < threshold:
            dic.update({company:tech_diversity_data[company][field]})
    return dic 


