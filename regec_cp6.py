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

# findall()
pattern = "your"
results = re.findall(pattern, cerseiSpeech)
print(results)

# output ['your', 'your', 'your', 'your', 'your', 'your']

pattern1 = "I "
pattern2 = "your"
pattern3 = "we"
results1 = re.findall(pattern1, cerseiSpeech)
results2 = re.findall(pattern2, cerseiSpeech)
results3 = re.findall(pattern3, cerseiSpeech)


print('Cersei used ', pattern1, len(results1), ' times and ', pattern2, '& ', pattern3, (len(results2)+len(results3)), 'times.')
if (len(results2)+len(results3)) >= (len(results1)):
  print("That is hardly a sign of a selfish ruler.")