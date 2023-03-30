
grade_level = int(input('Enter your grade level:\n'))

school_type = None

if 1 <= grade_level <= 18:

    if 17 <= grade_level:
        school_type = 'Grad School'
    elif 13 <= grade_level:
        school_type = 'College'
    elif 9 <= grade_level:
        school_type = 'High School'
    elif 6 <= grade_level:
        school_type = 'Middle School'
    else:
        school_type = 'Elementary School'

else:
    school_type = 'Invalid grade level given'


print(school_type)



"""
Create a python file named grade_level.py
    Given a number grade level determine and print which school type someone is in.
            grade level and types are:
                    1-5: Elementary school
                    6-8: Middle school
                    9-12: High school
                    13-16: College
                    17-18: Grad School

                    For Any Other grade: Invalid grade level given

            NOTE: MUST USE NESTED IF. DO NOT USE MORE THAN ONE PRINT STATEMENT
"""
