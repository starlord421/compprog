import random
user_name= input("what is your name?")
ally=75
user_age=int(input("how old are you?"))
rusty_knife=-25
knife= -20
bandage=20
gun=-100
shotgun=-250
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
               if fight_input == "run":
                    ally=input(f"the orphan looks at you confused and apoligizes, she then askes if she can be your ally, do you want to aprove or disaprove")
                    if ally == "y":
                         print("you agree and the orphan looks at you with utmost respect and loyalty.")
                         user_inventory.append("rusty knife")
                    if i < 9 and i >= 6 :
                     fight_input = input(f"you hear some one yell after you, he has {thug} hp and wants to rob you, do you want to fight or run")
                    if fight_input == "fight":
                      print(thug+knife+rusty_knife)
                    ally=input(f"the thug looks at you standing over him, he begs you to spare him, do you want to aprove or disaprove")
                    if ally == "y":
                         print("you agree and the thug looks at you with a grudging admeration, for he now owes you his life.")
                    user_inventory.append("gun")
                    if fight_input == "run":
                         print("the thug decides not to chase you")
                         user_inventory.append("gun")
                         if i < 9 and i >= 6 :
                              fight_input = input(f"you hear a sound like a foghorn bellow after you, he has {brute_thug} hp and wants to beat you tf up, do you want to fight or run")
                    if fight_input == "fight":
                      print(brute_thug+knife+rusty_knife+gun)
                    print ("you use your knife and slash the thug, your orphaned friend followes up with a quick stab, your thug ally then shots him. the brute falls over dead")
                    user_inventory.append("shotgun")
                    print("you and your allies realize that you work really well together and your conquest of hells kitchen begins")
                    if fight_input == "run":
                         print("the thug decides not to chase you")