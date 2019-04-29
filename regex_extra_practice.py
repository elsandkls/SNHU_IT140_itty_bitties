#Meta-character     Description     Example
#.     Matches any character except a newline     
#^     Matches start of a string     
#$     Matches the end of a string
#*     Matches 0 or more repititions of the character immediately preceding     xy* will match xy, xyyyyy and will match x.
#Note: This is a greedy metacharacter -- it will match as many characters as possible. Maybe more than you want.
#+     Match 1 or more repititions of the character immediately preceding     xy+ will match: xy, xyyyyy, but will not match: x
#Note: This is a greedy metacharacter -- it will match as many characters as possible. Maybe more than you want.
#?     Match 1 or more repititions of the regular expression     xy? will match x and xy.
#Note: This is a greedy metacharacter -- it will match as many characters as possible. Maybe more than you want.
#*?, +?, ??     The non-greedy versions of *, +, and ?     Match as few characters as possible.
#{m}     Match exactly m copies of the regular expression     a{3} will match aaa but not aa, a, or aaaa.
#{m,n}     Match exactly m through n copies of the regular expression     a{2,4}b will match aab, aaab, aaaab but not ab, a, or aaaaab.
#\     Escapes metacharacters so you can use them in a regular expression     \* will match *.
#[]     Matches a set of characters     [ab] will match: a, b, ab

import re

pattern="[abc]"

a_str="a"
b_str="b"
c_str="c"

ab_str="ab"
bc_str="bc"
abc_str="abc"
xabc_str="xabc"

match1 = re.match(pattern, a_str)
if match1 != None:
    print(pattern + " matched " + a_str)
else:
    print(pattern + " did not match " + a_str)

match2 = re.match(pattern, b_str)
if match2 != None:
    print(pattern + " matched " + b_str)
else:
    print(pattern + " did not match " + b_str)

match3 = re.match(pattern, c_str)
if match3 != None:
    print(pattern + " matched " + c_str)
else:
    print(pattern + " did not match " + c_str)

match4 = re.match(pattern, ab_str)
if match4 != None:
    print(pattern + " matched " + ab_str)
else:
    print(pattern + " did not match " + ab_str)

match5 = re.match(pattern, bc_str)
if match5 != None:
    print(pattern + " matched " + bc_str)
else:
    print(pattern + " did not match " + bc_str)

match6 = re.match(pattern, abc_str)
if match6 != None:
    print(pattern + " matched " + abc_str)
else:
    print(pattern + " did not match " + abc_str)

match7 = re.match(pattern, xabc_str)
if match7 != None:
    print(pattern + " matched " + xabc_str)
else:
    print(pattern + " did not match " + xabc_str)
    
    
    import re

pattern='xy*'
str_x='x'
str_xy='xy'
str_xyyyyy='xyyyyy'

m1 = re.match(pattern, str_x)
if m1 != None:
    print(pattern + " matched " + str_x)
else:
    print(pattern + " did not match " + str_x)

m2 = re.match(pattern, str_xy)
if m2 != None:
    print(pattern + " matched " + str_xy)
else:
    print(pattern + " did not match " + str_xy)


m3 = re.match(pattern, str_xyyyyy)
if m3 != None:
    print(pattern + " matched " + str_xyyyyy)
else:
    print(pattern + " did not match " + str_xyyyyy)
    
    
    import re

pattern='a{3}'
str_a_quad='aaaa'
str_a_tripple='aaa'
str_a_tripple_b='aaab'
str_a_double='aa'
str_a_single='a'

m7 = re.match(pattern, str_a_quad)
if m7 != None:
    print("matched %s" % str_a_quad)
else:
    print(pattern + " did not match " + str_a_quad)

m8 = re.match(pattern, str_a_tripple)
if m8 != None:
    print("matched %s" % str_a_tripple)
else:
    print(pattern + " did not match " + str_a_tripple)

m9 = re.match(pattern, str_a_tripple_b)
if m9 != None:
    print("matched %s" % str_a_tripple_b)
else:
    print(pattern + " did not match " + str_a_tripple_b)

m10 = re.match(pattern, str_a_double)
if m10 != None:
    print("matched %s" % str_a_double)
else:
    print(pattern + " did not match " + str_a_double)

m11 = re.match(pattern, str_a_single)
if m11 != None:
    print(m11.group(0))
else:
    print(pattern + " did not match " + str_a_single)

    