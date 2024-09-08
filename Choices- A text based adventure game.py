import time #Imports a module to add a pause

#Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

#Grabbing objects
sword = 0
flower = 0

required = ("\nUse only A, B, or C\n") #Cutting down on duplication

#The story is broken into sections, starting with "intro"
def intro():
  print ("After a SLUMBER PARTY with friends, you wake up the "
  "next day in a place called the OTHERWORLD. Your head spins , "  
  "trying to recollect your thoughts, you stand and marvel at your new, "
  "Magical but mysterious forest setting. You snap from your dazed state when you hear a "
  "grotesque sound emitting behind you. A Dragons flying "
  "straight for you. You will:")
  time.sleep(1)
  print ("""  A. Grab a nearby rock and throw it at the Dragon
  B. Lie down and wait to be Barbequed
  C. Run""")
  choice = input(">>> ") #Here is your first choice.
  if choice in answer_A:
    option_rock()
  elif choice in answer_B:
    print ("\nDamn, that was reaalllyyyy smart. "
    "\n\nYou died!!!")
  elif choice in answer_C:
    option_run()
  else:
    print (required)
    intro()


def option_rock(): 
  print ("\nThe Dragon is stunned, but regains control. It begins "
  "Flying towards you again. Will you:")
  time.sleep(1)
  print ("""  A. Run
  B. Throw another rock
  C. Run towards a nearby cave""")
  choice = input(">>> ")
  if choice in answer_A:
    option_run()
  elif choice in answer_B:
    print ("\nYou really think a rocks gonna hurt that Dragon ?! " 
    " The Dragon launches a Flaming Ball Of Fire Towards You. "
    "The rock got chared and the ball of fire hit you. Adios!!!. \n\nYou died!!!")
    
  elif choice in answer_C:
    option_cave()
  else:
    print (required)
    option_rock()

def option_cave():
  print ("\nYou were hesitant, since the cave was dark and "
  "ominous. Before you fully enter, you notice a shiny sword on "
  "the ground called the OTHREWORLD DRAGON SLAYER. Do you pick up a sword. Y/N?")
  choice = input(">>> ")
  if choice in yes:
    sword = 1 #adds a sword
  else:
    sword = 0
  print ("\nWhat do you do next?")
  time.sleep(1)
  print ("""  A. Hide in silence
  B. Fight
  C. Run""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("\nReally? You're going to hide in the dark? I think "
    "Dragons can see very well in the dark, right? And also sense Fear? Not sure, but "
    "I'm going with YES, so...Good Luck Playing Hide N Seek!!!\n\nYou died!")
  elif choice in answer_B:
   if sword > 0:
    print ("\nYou laid in wait. The shimmering sword attracted "
    "the Dragon, which thought you were no match for it. As it flew "
    "closer and closer, your heart started beating rapidly. As the Dragon "
    "flew in to grab the sword, you pierced the blade into "
    "its chest tearing the Dragon Apart. \n\nYou survived!")
   else: #If the user didn't grab the sword
     print ("\nYou should have picked up that sword. WHAT DID YOU THINK WAS GONNA HAPPEN,HUH???!!! You're "
     "defenseless. \n\nYou died!")
  elif choice in answer_C:
    print ("As the Dragon enters the dark cave, you sliently "
    "sneak out. You're several feet away, but the Dragon sniffs "
    "you out and sees you running.")
    option_run()
  else:
    print (required)
    option_cave()

def option_run():
  print ("\nYou run as quickly as possible, but the Dragon's "
  "speed is too great. You will:")
  time.sleep(1)
  print ("""  A. Hide behind boulder
  B. Trapped, so you fight
  C. Run towards an abandoned town""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("You're easily spotted. Fire Ball on the way. Boom!!! "
    "\n\nYou died!")
  elif choice in answer_B:
    print ("\nYou're no match for a Dragon. You'd have to be insane to think that...!!! "
    "\n\nYou died!")
  elif choice in answer_C:
    option_town()
  else:
    print (required)
    option_run()
    
def option_town():
  print ("\nWhile frantically running, you notice another rusted "
  "sword lying in the mud. You quickly reach down and grab it, "
  "but miss. You try to calm your heavy breathing as you hide "
  "behind a delapitated building, waiting for the Dragon to come "
  "charging around the corner. You notice a purple flower "
  "near your foot. Do you pick it up? Y/N")
  choice = input(">>> ")
  if choice in yes:
    flower = 1 #adds a flower
  else:
    flower = 0
  print ("You hear its heavy wingbeats and ready yourself for "
  "the teriffying Dragon.")
  time.sleep(1)
  if flower > 0:
    print ("\nYou quickly hold out the purple flower, somehow "
    "hoping it will stop the Dragon. It does!!! The Dragon was looking "
    "for love. Apparently, That Flower was an Ingridient for a Love Powder. "
    "\n\nThis got weird, but CONGRATULATIONS!!! You survived!!!")
  else: #If the user didn't grab the sword
     print ("\nWhy do you want so much violence ?! Try Love sometimes!! You made the Dragon mad!! "
     "\n\nYou died!")

intro()

