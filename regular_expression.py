import re

text = ''' 
abcdefghijklmnopqrstuvwxyz.
ABCDEFGHIJKLMNOPQRSTUVWXYZ.

Matched escaped..,

facebook.com

Mr. Puneeth
Mr Smith
Ms Riana
Mrs. Robinson
Mr. T

puneethpgowda0825@gmail.com
PPG2596@gmail.com
puneeth.techie.tm@gmail.net
puneeth-techie@outlook-gmail.org


'''
urls = '''https://www.facebook.com
http://localhost:5000
https://india.gov
http://bbc.co.uk
'''
# Match names
#pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')

# pattern = re.compile(r'[A-Za-z0-9.-]+@[a-z-]+\.(com|net|org)')
# matches = pattern.finditer(text)

# Match URL's
pattern = re.compile(r'https?://(www\.)?(\w+)[:]?[0-9]*(\.\w+\.\w+|)(\.\w+|)')
subbed_urls = pattern.sub(r'\2\3\4', urls)
print(subbed_urls)
# matches = pattern.finditer(text)
# for match in matches:
#     print(match)
