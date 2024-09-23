student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for grade in student_scores:
    score= student_scores[grade]
    if(score>=91):
        student_grades[grade]='Outstanding'
    elif(score>=81 and score<=90):
        student_grades[grade]='Exceeds Expectations'
    elif(score>=71 and score<=90):
        student_grades[grade]='Acceptable'
    else:
        student_grades[grade]='Fail'

print(student_grades)