name = input("what is your name")
recap = input(f"thanks {name} for attending, can i recap what we went over")
forward = input("we only have one job opening, analyst, do you want to continue?")
schooling=int(input("how many years of schooling do you have"))
if forward == "y":  
    print: input(f"how many years of experiance do you have")
    if schooling >= 2 and schooling <=5:
        salary=int(input("what salary do you want to start with"))
        print: salary
        if salary <= 64000 and salary >=40000:
            print: input ("you drive a hard bargin, to prove you are the real deal we're going to do a little quiz do you want to continue?")
    else:
        print("you're hired!")
    if input=="y":
        print: input ("how many years of schooling do you need to get here")
    else:
        print("no job for you, you come back one year")
    if schooling == 4:
        print: input("one down, two to go, what kind of degree do you need")
    if input== "bachelors" or "Bachelors":
        print: input ("alright last question, what does the analyst do?")
    if input == "analyse":
        print("well done for getting here, you're hired")
    if input== "analyse duh":
        print("one question, can you change your aditude for the future, you're hired")
# 2-4 years of schooling 
# beginning salary is 59941
# max salary is 170000
# senior developer takes 3-7 years of in job experiance
# junior developer takes 3-5 years of in job experiance
# analyst takes 4 years of schooling
# team leader takes 4-6 years of related experiance
# junior devs can make 56-99k yearly
# analysts make 36-64k yearly
# senior devs make from 26k-1.45m yearly   
# product managers make 111-242k yearly