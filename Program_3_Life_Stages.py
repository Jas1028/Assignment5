# Create a program that ask for an age of a person
# Display the life stage of the person.
# Rules:
# 0 - 12 : Kid
# 13 - 17 : Teen
# 18 : Debut
# 19 above : Adult

print("\n        Life Stages:\n\nKid          0 - 12 years old\n\nTeen         13 - 17 years old\n\nDebut        18 years old\n\nAdult        19 and above years old ")
# Steps
# Ask age of a person
GetAge = int(input("\nEnter your age: "))
# Test 0 - 12 : Kid

if GetAge >= -1 and GetAge <= 12:
    print("\nYou are in Kid stage. ")
# Test 13 - 17 : Teen
else:
    if GetAge >= 13 and GetAge <= 17:
        print ("\nYour are in Teen stage. ")
# Test 18 = Debut
    else:
        if GetAge == 18:
            print("\nYou are in Debut stage. ")
# Test 19 above : Adult
        else:
            print("\nYou are in Adult stage. ")     

print("Enjoy your",GetAge,"years of existing here in our world. Goodluck to your journey!. ")



 