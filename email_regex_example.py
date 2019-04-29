# email validation
emailList = ['cersei.lannister@got.eu', 'j.a.m.i.eLan@goteu', 'nedstark_got.eu']
emailValidation = re.compile(r'''([a-zA-Z0-9._&=-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z] (2,4)))''', re.VERBOSE)
for email in emailList:
  if re.match(emailValidation, email):
    print(email, "is valid")
  else:
    print(email, "is invalid")