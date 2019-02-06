#! /usr/bin/python3
# pw.py - 
import sys, pyperclip, re
patterns = {
  'numbers':r'\d+',
  'non-numbers': r'\D+',
  'special-char': r'\W+', #Not a Letter and not a number. Includes space and newline
  'pure-text': r'w+',
  'white-space': r'\s+',
  'non-white-space': r'\S+',
  'email': r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4}))',
  'phone': r'((\+\d{2,3}-?)?(( ?\d{2}( \d\d){3})|\d{8}))' # generated from https://pythex.org/?regex=(%5C%2B%5Cd%7B2%2C3%7D-%3F)%3F((%20%3F%5Cd%7B2%7D(%20%5Cd%5Cd)%7B3%7D)%7C%5Cd%7B8%7D)&test_string=%2B45%2040%2098%2094%2080%20lkj%20%2B44-34%2034%2034%2034%20lkjlkj%20%0A34%2033%2022%2033%20eller%20denne%3A%205656566565665%20erer%2043%2035%2036%2036%2036%2036%20denne%20%2B45-44332211&ignorecase=0&multiline=0&dotall=0&verbose=0
}

if len(sys.argv) < 2: # 
  print('Usage: python pw.py [account] - copy account password')
  sys.exit()
input = sys.argv[1] # first command line arg is the file name second should be the account: email, blog, etc..
pattern = patterns.get(input, input) # second arg to .get is a default value.
match_obj = re.compile(pattern, re.IGNORECASE) 
content = pyperclip.paste() # paste from the clipboard
results = match_obj.findall(content)
print(results)
if(input == 'email' or input == 'danish-phone'): # the email pattern has an extra group (the last part: (\.[a-zA-Z]{2,4})) this means that the findall method returns list of tuples of results in group(0) and group(1) instead of list of strings
  results = [res[0] for res in results] # this comprehension transforms the list of tuples: [('tha@cphbusiness.dk', '.dk'), ('whoever@whereever.com', '.com'), ('ada@lovelace.co.uk', '.uk')] with the list of strings: ['tha@cphbusiness.dk', 'whoever@whereever.com', 'ada@lovelace.co.uk']
print(results)
pyperclip.copy("\n".join(results))

# content_array = ['* '+str.strip() for str in content.splitlines() if len(str)>0]

