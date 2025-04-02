string = "a c sedjnhe dnft INFR SENRIFWE  wdnr fj cf vrr frg r vnfbbv"
valid = True
i = 0  
while i < len(string):
    if not ('A' <= string[i] <= 'Z' or 'a' <= string[i] <= 'z' or string[i] == ' '):
        valid = False
        break
    i += 1
if valid:
    print("Valid")
else:
    print("Invalid")
