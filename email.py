# get user email addresss

email = input('What is your email address?: ').strip()
# slice out user name

user = email[:email.index('@')]
print(user)

#slice domain name
domain = email[email.index('@')+1:email.index('.')]
print(domain)

output = 'Your username {} and your domain name is {}'.format(user,domain)

print(output)
