classmates = ["Juliette Blake", "Jillian Kane", "Joe Fitzpatrick", "Rodolfo Salinas", "Alexa Cook",
              "Alfredo Stuart", "Audrey Eaton", "Noel Finley", "Salvatore Benjamin", "Kaitlynn Mason"]

for x in classmates:  # x: full name of each student
    # print(f'{x[0]}.{x[x.index(" ")+1]}')
    print(x[0] + "." + x[x.index(' ') + 1])

"""
A list named classmates is given
Write a program that can display the initials of each student on the console in separate lines

    Ex:
        classmates = ['Cydeo School', 'Python Programming', 'Java Programming']

        output:
            C.S
            P.P
            J.P
"""
