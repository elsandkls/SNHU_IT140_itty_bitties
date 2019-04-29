import re

#Sentence with phrase to replace
sentence='In my string, I have my val, my-val, my_val, my&val and my=val.  But what I really want is my--val.'

#Pattern with the expression to replace
pattern = "my[ -_&=]val"

#String to use for substitution
substitution="my--val"

#Print out the original sentence
print(sentence + "\n")

#Replace the regular expression with the substitution string
match = re.findall(pattern, sentence)

#Print out the results of the match
print("Match = %s\n" % str(match))

#Replace the results
replace_results = re.sub(pattern, substitution, sentence)

#Print out the string containing the substitutions
print(replace_results)

