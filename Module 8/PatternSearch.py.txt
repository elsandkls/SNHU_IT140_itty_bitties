import re

#Paragraph provided for search and replace

lorem_ipsum = '''Lorem ipsum dolor sit-amet, consectetur adipiscing elit. Phasellus iaculis velit ac nunc interdum tempor. 
Ut volutpat elit metus, vel auctor enim commodo at. Nunc quis quam non ligula ultricies luctus porta id justo. 
Quisque dapibus est ut sagittis bibendum. Mauris ullamcorper pellentesque porttitor. Ut sit:amet ex nec dolor gravida 
porttitor. Proin at justo finibus justo vestibulum congue. Suspendisse et ipsum et ipsum eleifend dapibus a fermentum 
lacus. Vivamus porta nunc eu nisl sagittis, quis vulputate metus dignissim. Integer non fermentum nisl, id vestibulum 
elit. Sed euismod vestibulum purus ut porttitor. Integer sit-amet mollis neque. Donec sed lacinia diam, ac finibus 
lectus. Mauris tempor ipsum nisl, vitae posuere est lacinia nec. Nam eget euismod odio.'''

#Place all the code from the previous steps here
#regular expression pattern to search for alphanumeric values
#pattern = "[a-zA-Z]"
#results = re.findall(pattern, lorem_ipsum)
#final = len(lorem_ipsum) - len(results)
#print (final)

#regular expression pattern to search for non-alphanumeric values
#a search for sequences and ranges
pattern = "[^a-zA-Z]"
results = re.findall(pattern, lorem_ipsum) 
final = len(results)
print (final)

#regular expression pattern to search for a two-word sequence separated by dashes and colons
#a search using literal characters
pattern = "sit[:-]amet"  #search for special characters (: and - ) 
occurrance_sit_amet = re.findall(pattern, lorem_ipsum)
final = len(occurrance_sit_amet)
print (final)

#regular expression pattern to replace the dashes and colons
#a search using literal characters  
pattern = "sit[:-]amet"  #search for special characters (: and - )
pattern_sub = "sit amet"
pattern2 = "sit[ ]amet" #search for special characters ( space )
replace_results = re.sub(pattern, pattern_sub,lorem_ipsum)
occurrance_sit_amet = re.findall(pattern2, replace_results)
final = len(occurrance_sit_amet)
print (final) 

