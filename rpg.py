import random
user_name= input("what is your name?")
ally=75
user_age=int(input("how old are you?"))
rusty_knife=-25
knife= -20
bandage=20
gun=-100
user_inventory= ["knife", "bandage"]
user_health=100
weak_thug=50
thug=100
brute_thug=150

print(f"hello! welcome to hell's kitchen, {user_name}, watch your step.")
while True:
     walk_input = input("do you wish to venture forth, w, or view stats,p")

     if walk_input == 'p':
          print("you have a knife and a bandage")

     if walk_input == "w":
          i = random.randint(1,10)
          if i < 4:
               print("welcome to 1985 new york, you get from where you want to go peacefully")
          if i < 6 and i >= 4 :
               fight_input = input(f"you hear some poor orphan, she has {weak_thug} hp who's desprate, do you want to fight or run")
               if fight_input == "fight":
                    print("you use your knife and slash the orphan, she runs away and drops a rusty knife")
                    user_inventory.append("rusty knife")
               elif fight_input == "run":
                    ally=print(f"the orphan looks at you confused and apoligizes, she then askes if she can be your ally, do you want to aprove or disaprove")
                    if ally == "y":
                         print("you agree and the orphan looks at you with utmost respect and loyalty.")