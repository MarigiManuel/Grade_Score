# Suppose you just attended a university examination. 
# The marks you obtained in various subjects are stored in a list like this:

    # Marks = [55, 64, 75, 80, 65]

# You want to find the average marks you obtained in the exam. 
# And, based on the average marks you want to find your grade. The grading rule is like this:
    # You will get Grade A if the average marks is >= 80
    # You will get Grade B if the average marks is >= 60 and < 80
    # You will get Grade C if the average marks is >= 50 and < 60
    # You will get Grade F if the average marks is < 50

# Getting the average
def average_marks(marks):
    total_marks = sum(marks)
    num_subjects = len(marks)
    average_marks = total_marks / num_subjects
    return average_marks

# Getting the Grade
def get_grade(average_marks):
    if average_marks >= 80:
       # grade = 'A'   # Can still work
        return 'A'
    elif average_marks >= 60:
        #grade = 'B'
        return 'B'
    elif average_marks >= 50:
        #grade = 'C'
        return 'C'
    else:
        return 'F'
    #     grade = 'F'
    # return grade
    

marks = [55, 64, 75, 80, 65]
print(f'Your average marks is: {average_marks(marks)}')

grade = get_grade(average_marks(marks))
print(f'Your grade is: {grade}')