# Create a program that will ask for grade percentage. Display the equivalent Grade/Mark and Description
# Example:
# Input grade: 87.6
# Grade/Mark: 1.75
# # Description: Very Good
print("\n                      PUP Grading System\n\nGrade/Mark          Percentage/Equivalent           Description")
print("\n   1.0                    97-100                  Excellent")
print("\n   1.25                   94-96                   Excellent")
print("\n   1.5                    91-93                   Very Good")
print("\n   1.75                   88-90                   Very Good")
print("\n   2.0                    85-87                   Good")
print("\n   2.25                   82-84                   Good")
print("\n   2.5                    79-81                   Satisfactory")
print("\n   2.75                   76-78                   Satisfactory")
print("\n   3.0                     75                     Passing")
print("\n   5.0                    66-74                   Failure")
print("\n   Inc.                                           Incomplete")
print("\n   W                                              Withdrawn")
print("\n   D                                              Dropped")
print("\nType 0 if the grade is incomplete.\nType 1 if it's withdrawn.\nType 2 if it's dropped. ")
# Steps
# 1. Ask for grade percentage. 
def GetGrade():
    GetGradePercentage = float(input("\nEnter Grade Percentage: "))
    return GetGradePercentage

    
# 2 Display the equivalent Grade/Mark and Description
def GradeMark():
        if Grade >= 97 and Grade <= 100:
            print("Your Grade/Mark is 1.0.\n       Excellent. ")
        else:
            if Grade >= 94 and Grade <= 96:
                print("Your Grade/Mark is 1.25.\n       Excellent. ")
            else:
                if Grade >= 91 and Grade <= 93:
                        print("Your Grade/Mark is 1.5.\n       Very Good.  ")
                else: 
                     if Grade >= 88 and Grade <= 90:
                            print("Your Grade/Mark is 1.75.\n       Very Good. ")
                     else: 
                        if Grade >= 85 and Grade <= 87:
                                print("Your Grade/Mark is 2.0.\n       Good. ")
                        else:
                            if Grade >= 82 and Grade <= 84:
                                    print("Your Grade/Mark is 2.25.\n       Good. ")
                            else: 
                                if Grade >= 79 and Grade <= 81:
                                        print("Your Grade/Mark is 2.5.\n       Satisfactory. ")
                                else:
                                     if Grade >= 76 and Grade <= 78:
                                             print("Your Grade/Mark is 2.75.\n       Satisfactory. ")
                                     else:    
                                        if Grade == 75:
                                                 print("Your Grade/Mark is 3.0.\n       Passing. ")
                                        else:
                                             if Grade >= 65 and Grade <= 74:
                                                       print("Your Grade/Mark is 5.0.\n       Failure. ")
                                             else:
                                                if Grade == 0:
                                                          print("Your Grade/Mark is Inc.\n       Incomplete. ")
                                                else: 
                                                     if Grade == 1:
                                                              print("Your Grade/Mark is W.\n       Withdrawn. ")
                                                     else:
                                                          if Grade == 2:
                                                                 print("Your Grade/Mark is D.\n       Dropped. ")                                   

Grade = GetGrade()      
Grade = round(Grade)   
GradeMark()                       
                                


                                

