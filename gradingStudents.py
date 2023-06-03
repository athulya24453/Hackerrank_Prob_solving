def grading(grades):
    ans_arr = []
    
    for grade in grades:
        ans_arr = []
    
    for grade in grades:
        if grade<38 or grade%5<3:
            ans_arr.append(grade)
            
        else:
            ans_arr.append(grade-(grade%5)+5)
            
    return ans_arr

results = grading([77,89,13,42])

for result in results:
    print(result)