import re
#The string to search for the regular expression occurrence (This is provided to the student)

search_string='''This is a string to search for a regular expression like regular expression or regular-expression or regular:expression or regular&expression'''

print(search_string)
#1.  Write a regular expression that will find all occurrences of:
a_pattern = "regular expression"
a_match = re.match(a_pattern, search_string)
b_pattern = "regular-expression"
b_match = re.match(b_pattern, search_string)
c_pattern = "regular:expression"
c_match = re.match(c_pattern, search_string)
d_pattern = "regular&expression" 
d_match = re.match(d_pattern, search_string)    
    
#2.  Assign the regular expression to a variable named pattern
a_pattern = "regular expression"
a_match = re.findall(a_pattern, search_string)
 
pattern_list = ["regular expression","regular-expression","regular:expression","regular&expression"]
##1.  Using the findall() method from the re package determine if there are occurrences in search_string
for i in range(0,len(pattern_list),1):
    #.   Assign the outcome of the findall() method to a variable called match1
    match1 = re.findall(pattern_list[i], search_string)
    #2.  If match1 is not None:
    if match1 != "":
        #    a.  Print to the console the pattern used to perform the match, 
        #    followed by the word 'matched'
        print(pattern_list[i]," matched")
        #3.  Otherwise:
    else:
        #   a.  Print to the console the pattern used to perform the match, 
        #   followed by the words 'did not match'
        print(pattern_list[i]," did not match")
