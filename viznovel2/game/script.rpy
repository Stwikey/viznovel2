'''
Summary:

You are a higher power (angel? someone from the future? ghost?) that knows that the world is going 
to end (but lost your memories?). You do not have a direct effect on the world but you watch as the characters play out 
their lives.

You can choose to give the characters visions/prophecies/different items but make sure to choose the
correct one otherwise the world will end.

Genre:
Fantasy
'''

#defining characters
default mana = 0
define you = Character('You', color="#ffffff")
define sora = Character('Sora', color="#2a0f26")
define unknown_girl = Character('???', color="#000000")
define unknown_girl2 = Character('???', color="#914b4b")
define unknown_boy = Character('???', color="#0b3b2e")
define unknown_boy2 = Character('???', color="#0b3b2e")


label start:
    #waking up to prophecy of the world ending
    '''vision of the apocaplyse/future'''

    "You wake up with a sharp pang in your head."

    you "Ugh."

    "You look around. A INSERT SETTING HERE" #insert setting here

    #meeting the characters (maybe not all of them(?))

menu: 
        "Try to remember what happened.":
            jump introduction

label introduction:
    "You can hear voices nearby, getting louder and louder as they approach you."

    show sora surprise  

    unknown_girl "Hey! Look over here!"

    "She runs over to you, three other figures running to catch up to her."
    show sora happy

    unknown_girl "It's the INSERT IMPORTANT FLOWER OR INGREDIENT OR SOMETHING!"

    "The girl peers over, staring directly at you and pointing almost past you."

    show unknown_girl2 neutral

    unknown_girl2 "We can't use those Sora."

    "The *other* (IDK) girl bends forward, face almost touching yours and her hand reaches past you."

    you "What?" #this is when you notice they don't see u or wtv

    show unknown_girl2 holding_flower

    "When she pulls her hand out, she is holding a small, wilted flower." #cutscene instead of words maybe
    
    unknown_girl2 "This flower's magic is almost out." #aka its dying

    unknown_girl2 "Weird. It's almost as if someone sat on this whole patch of grass."

    "The girl traces in the air, circling the perimeter around where you are laying."

    show unknown_boy angry

    unknown_boy "Ugh! It must've been those first years again!"

    unknown_boy "Professor's gonna scold us again for sure and it's not even my fault this time!"

    show sora casting

    sora "Wait! let me try something."

    unknown_girl2 "Don't. You shouldn't use your magic on this sort of thing."

    unknown_girl2 "Plus, the Professor always knows when magic is used to tamper things. This flower is already dead."

    "The flower distintegrates in the girl's hand. Black ashes float up and scatter across the field."

    sora "Awww alright. But where are we supposed to find more?"
    
    unknown_boy "Yeah !it already took us half the time to find this one patch!"

    unknown_boy "Ugh! I'm going to file a report against those first years."

    unknown_girl2 "Calm down, we still have time."

    unknown_girl2 "NAME do you have enough magic to cast another spell?"

    "unknown_boy2 nods."

    "Unkown_boy2 concentrates, you can feel magic flowing in the air intensely."

#taking magic mechanic introduction
menu: 
    "Absorb some of the magic":
        jump absorb_magic
    "Do nothing":
        jump part_2

label absorb_magic: #will make this an actual mechanic later but I don't want the player to make game changing decisions that early
    "You reach out, drawing the magic in the air towards yourself."
    "It feels natural, and you realize how deprived your body is of magic." #em fix
    "You grasp hungrily at the magic in the air."

    unknown_boy2 "!"

    "The boy stares directly at you and you feel the magic in the air snap back."

    unknown_girl "What happened?"

    "The unknown boy shakes his head, confused."

    jump part_2:

label part_2:
    "e"









    

