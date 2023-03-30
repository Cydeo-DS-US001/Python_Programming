email = 'joshua_baker@yahoo.com'

first_name = email[:email.index('_')].capitalize()
last_name = email[email.index('_') + 1: email.index('@')].capitalize()
domain = email[email.index('@') + 1: email.rindex('.')].capitalize()

print(first_name)
print(last_name)
print(domain)

is_gmail = email.endswith('gmail.com')
is_hotmail = email.endswith('hotmail.com')
is_yahoo = email.endswith('yahoo.com')

print(is_gmail)
print(is_hotmail)
print(is_yahoo)