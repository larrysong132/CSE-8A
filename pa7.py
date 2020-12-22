#1.1
def distribution_majors(list_majors):
    dis_majors = {}
    check = 0
    counter = 0
    for key in list_majors:
        if key in dis_majors == True:
            check += 1
        if check == 0:
            for majors2 in list_majors:
                if key == majors2:
                    counter += 1
            dis_majors.update({key:counter})
        counter = 0
    return dis_majors


#1.2
def select_states(cases,threshold):
    new_cases = {}
    for key in cases:
        value = cases.get(key)
        if value < threshold:
            new_cases[key] = value
    return new_cases

#1.3
def update_standing(win_record, new_winners):
    new_win_record = {}
    for key in win_record:
        result = win_record.get(key)
        new_win_record[key] = result
        if key in new_winners:
            result = win_record.get(key) + 1
            new_win_record[key] = result
    return new_win_record
    
