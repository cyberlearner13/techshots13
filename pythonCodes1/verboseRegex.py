import re

phoneNumRegex = re.compile(r'''
\d\d\d # area code
-      # first dash
\d\d\d # first 3 digits
-      # second dash
\d\d\d\d # last 4 digits
''', re.VERBOSE )

print(phoneNumRegex.findall('Call me at 415-959-2365 or at my office number 414-665-6868'))
