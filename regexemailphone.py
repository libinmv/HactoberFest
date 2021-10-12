#!
# TODO: Create a program that scrapes phone number and from a document using regular expression
import pyperclip, re
#create regex for phone

phoneregx = re.compile(r'''(
(\d\d\d\d(\s|-)?)?#area code
(\d\d\d\d)
(- | \s)?
(\d\d\d(\d)?)
((\s)?\((\w)+\))?
)
''', re.VERBOSE)

#create regex for email
emailregx = re.compile(r'''
#something@something.com, .nic.in, .in, etc.
[a-zA-Z0-9-.+_]+   #name part
@                   #@ part
[a-zA-Z0-9-.+_]+   #text part
''',re.VERBOSE)
#copy text off clipboard
paste = pyperclip.paste()
#extract email and phone number
phone = phoneregx.findall(paste) #scrape telephone numbers
email = emailregx.findall(paste) #scrape email ID

allphone = []
for i in phone:
    allphone.append(i[0])
#copy extracted 
last = '\n'.join(allphone) + '\n' + '\n'.join(email)
print(last)
pyperclip.copy(last)
