import re
cerseiSpeech = "The Mad King's daughter has ferried an arm of savages to " \
               "our shores, mindless unsullied soldiers who would destroy " \
               "your castles and your holdfasts, Dothraki heathens who " \
               "will burn your villages to the ground, rape and enslave " \
               "your women, and butcher your children without a second " \
               "thought... You remember the mad king, you remember the " \
               "horrors he inflicted on his people. His daughter is no " \
               "different. In Essos her brutality is already legendary. " \
               "She crucified hundreds of noblemen in Slavers Bay. And " \
               "when she got bored of that, she them to her dragons. " \
               "It is my solemn duty to protect the people and I will, but " \
               "I need your help my lords. We must stand together, all of " \
               "us, if we hope to stop her."

# match()
if re.match('Mad', cerseiSpeech):
    print("Pattern matched!")
else:
    print("No pattern match.")
  
    pattern = "The"
if re.match(pattern, cerseiSpeech):
    print("Pattern matched!")
else:
    print("No pattern match.")
  
# search()
pattern = "your"
if re.search(pattern, cerseiSpeech):
    print("Pattern matched!")
else:
    print("No pattern match.")