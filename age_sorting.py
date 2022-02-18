from pip import main


age = [3,10,25,20,8,10,26,27,28,29,
    30,50,33,45,20,8,26,67,92,45,5,12,90
    ,83,37,47,58,34,5,55,67,38,46,39,76,45,
    33,28,84,2,65,38,47,38,76,6,72,23,74,38,75,
    37,65,38,53,72,33,48,65,36,17,19,43,15
    ,8,63,91,99,7,3,5,23,13,27,1,29,24,72,78,
    83,27,52,94,62,71,82,94,24,11,6,39,48,46,28,37]
def first_option():
    
    print(len(age))
    first_age_bracket =[] #for age 1-33
    second_age_bracket =[] #for age 34-66
    third_age_bracket = [] #for age 67-99
    for each_age in age:
        if (1<= each_age) and (each_age<=33):
            first_age_bracket.append(each_age)
        elif each_age<=66:
            second_age_bracket.append(each_age)
        elif each_age <=99:
            third_age_bracket.append(each_age)
    print("age range of 1-33: ",first_age_bracket)
    print("age range of 34-66: ",second_age_bracket)
    print("age range of 67-99: ",third_age_bracket)


#filter expression
def second_option():
    first_age_bracket =[each_age for each_age in age if each_age>=1 and each_age<=33]
    second_age_bracket = [each_age for each_age in age if each_age>=34 and each_age<=66]
    third_age_bracket = [each_age for each_age in age if each_age>=66 and each_age<=99]
    print("age range of 1-33: ",first_age_bracket)
    print("age range of 34-66: ",second_age_bracket) 
    print("age range of 67-99: ",third_age_bracket)

second_option()
