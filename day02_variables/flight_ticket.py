from_ = 'New York'
to = 'Los Angles'
ticket_price = 425.5

print('From ' + from_ + ' to ' + to + ' is $' + str(ticket_price) )

print('From {} to {} is ${}'.format(from_, to, ticket_price ) )

print(f"From {from_} to {to} is ${ticket_price}")

"""
create a python file named flight_ticket, and declare the following variables:
                1. from
                2. to
                3. ticketPrice
    use concatenation to display the full info of the ticket
    ex:
            Given Data:
                from = "Las Vegas"
                to = "McLean"
                ticketPrice = 425.5
            Output:
                From Las Vegas to McLean is $425.5
"""