#1.1
number_grade = input()
def grade_calculator(number_grade):
    if number_grade >= 0 and number_grade < 60:
        msg = "F"
    elif number_grade >= 60 and number_grade < 70:
        msg = "D"
    elif number_grade >= 70 and number_grade < 80:
        msg = "C"
    elif number_grade >= 80 and number_grade < 90:
        msg = "B"
    elif number_grade >= 90 and number_grade <= 100:
        msg = "A"
    else:
        msg = "not a grade"
    return msg


#1.2
def fix_list(data1, data2, data3):
    if data1 > data2 > data3:
        return [data3 , data2, data1]
    elif data3 > data2 > data1:
        return [data1, data2, data3]
    elif data2 > data3 > data1:
        return [data1, data3, data2]
    elif data1 > data3 > data2:
        return [data2, data3, data1]
    elif data2 > data1 > data3:
        return [data3, data1, data2]
    elif data3 > data1 > data2:
        return [data2, data1, data3]
    elif data1 > data2 and data2 == data3:
        return [data3, data2, data1]
    elif data1 == data3 and data2 > data1:
        return [data1, data3, data2]
    elif data1 == data2 and data2 > data3:
        return [data3, data2, data1]
    else:
        return [data1, data2, data3]
    
#1.3
def days_in_month(month):
    if (month == 'February'):
        return 28
    elif (month == 'April' or 'June' or 'September' or 'November'):
        return 30
    elif (month == 'January' or 'March' or 'May' or 'July' or 'August' or 'October' or 'December'
        return 31


    
    
        
