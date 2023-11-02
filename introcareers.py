name=input('what is your name?')
comp_prog_team={
    "team_leader":{
    "name":"jim",
    "task": ["supervise","assist","advocate"]
    },
    "analyst": {
    "name":"oscar",
    "task":["analize","examin","collect"]
    },
    "sen_dev":{
        "name":"dwight",
        "task":["train","assist","develop"]
    },
    "jr_dev":{
        "name":"ryan",
        "task": ["learn","develop",""]
    },
    "client":{
        "name":"jan",
        "task": ["propose","critique","request"]
    },
    "product_manager":{
    "name":"michael",
    "task":["managing","mediator",""]
    },
}
print(f"thanks {name} for attending, can i recap what we whent over")
print("we have five job openings, which field do you want, analyst, senior developer, junior developer, product manager, or team leader")
if input== "analyst":
    print(f"how many years of experiance do you have")
    for i in range (0,8):
        if i >= 2:
            print("your starting salary is 36000 but you can make up to 64000")
    if i >=5:
        print (" haha, nice try.")
    if input== "senior developer":
        print(f"how many years of experiance do you have")
    if i >= 3 and i <= 7 :
        print("your starting salary is 26000 but you can make up to 1,450,000")
    if i >=8 :
        print ("haha, nice try.")
    if input== "junior developer":
        print(f"how many years of experiance do you have")
    if i >= 2 and i <=5:
        print("your starting salary is 56000 but you can make up to 99,000")
    if i >=5:
        print (" haha, nice try.")
    if input== "product manager":
        print(f"how many years of experiance do you have")
    if i >= 2 and i <=4:
        print("your starting salary is 111000 but you can make up to 242000")
    if i >=5:
        print (" haha, nice try.")
    if input== "team leader":
        print(f"how many years of experiance do you have")
    if i >= 4 and i <=6:
        print("your starting salary is 37000 but you can make up to 130000")
    if i >=7:
        print (" haha, nice try.")
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