from tkinter import*
root=Tk()
root.geometry("500x500")
root.title('madlib generator')
Label(root,text="Mad Lib Generator", font='arial 20 bold').place(x=40,y=80)
Label(root,text="Click Any One:", font= 'arial 15 bold').place(x=80,y=140)


def story():
    adjective = input('enter adjective : ')
    color = input('enter a color name : ')
    thing = input('enter a thing name :')
    place = input('enter a place name : ')
    person= input('enter a person name : ')
    adjective1 = input('enter an adjective : ')
    insect= input('enter a insect name : ')
    food = input('enter a food name : ')
    verb = input('enter a verb name : ')

    print('Last night I dreamed I was a ' +adjective+ ' butterfly with ' + color+ ' splotches that looked like '+thing)
    print('I flew to ' + place+' with my best friend and '+person+ ' who was a '+adjective1+ ' ' +insect+'.' )
    print('We ate some ' +food+ ' when we got there and then decided to '+verb+' and the dream ended when I said-- lets ' +verb+ '.')
def poem():
    color = input("Enter a color: ")
    pluralNoun = input("Enter a plural noun: ")
    noun = input("Enter a noun: ")

    print("Roses are", color)
    print(pluralNoun + " are blue")
    print("I can't start my day without my ", noun)
    
def greeting():
    Pluralnoun=input("Enter the name of the person whom you would like to greet:")
    adjective=input("Enter an adjective:")
    occ=input("Enter the occasion (birthday/anniversary):")
    n=input("Enter the sender's name:")
    
    print("To",Pluralnoun )
    print("Wishing you a very ",adjective)
    print(occ)
    print("with love",n)
    
def invitation():
    name=input("Reciever's name:")
    Adjective=input("Describe in with an adjective:")
    occ=input("occasion:")
    s=input("name of the host:")
    print("To", name)
    print("You are invited to the " ,Adjective,occ)
    print("of ",s)
    print("Join in the Celebration!")

Button(root,text="Story",font='arial 15',command=story,bg='ghost white').place(x=100,y=180)
Button(root,text="Invitation",font='arial 15',command=invitation,bg='ghost white').place(x=100,y=250)
Button(root,text="Poem",font='arial 15',command=poem,bg='ghost white').place(x=250,y=180)
Button(root,text="Greeting",font='arial 15',command=greeting,bg='ghost white').place(x=250,y=250)
root.mainloop()
