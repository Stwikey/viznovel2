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
define charlie = Character('Charlie', color="#60288b")
define unknown_girl3 = Character ('???',color="#5da0c4" )


label start:
    #waking up to prophecy of the world ending
    '''vision of the apocaplyse/future'''

    "You wake up with a sharp pang in your head."

    you "Ugh."

    "You look around. It seems as though you are in the middle of a densely populated city. 
    The cars speed past and you wonder what rush they must be in." #insert setting here

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

    jump part_2

label part_2:
    "You watch as the boy gathers magical energy... it feels familliar, but you can't put your finger on it yet." 

    unknown_boy2 "Haha! Told you I could do it!"

    # not sure how we want to show this? also not sure where you were going with this ngl lol

    unknown_girl2 "Okay I think if we go to the PLACEHOLDER" #come up with a good name for some spooky location 

    "You get this cold feeling, as fragmented memories flash through your head."

    "CHARLIE STOP IT, YOU'LL DIE!" # put this in quotes mysteryyyy

    you "Who the hell is Charlie?" 
    
    "You are brought back to the present, but there are still many missing pieces." 

    unknown_boy "Are you sure? Even the professors don't go up there..." 

    unknown_girl "Don't tell me you're chickening out now? We said we would get 100 on this project, so we are guaranteeing that 100."

    menu:
        #both end in the characters dying
        "Try to warn them":
            jump danger
        
        "Do nothing":
            jump oblivious
label danger: 
    "You concentrate hard as you try your best to warn them, shouting at the top of your lungs."

    show sora silly

    you "STOP DON'T GO!" 

    "You jump right in the middle of the group, waving your arms around to get someones attention."

    "The group continues to chatter, blissfully unaware of your attempts to contact them."
    
    you "I don't know why I try, they can't see or hear me. I can't save them if I continue like this."

    jump part_3

label oblivious:
    "You watch as they leave. Chattering away about their plans, maybe it was just a one off feeling." 

    "But as you continue to wander around the city, the sinking feeling in your stomach continues to eat away at you."

    jump part_3

label part_3: 
    # basically learn a bit about who charlie is in this universe 
    "You continue to wander around, walking through the street."
    you "Who is Charlie? And what was he doing..."
    
    you "Something is going to destroy this world, I know I'm not a mortal like those kids from earlier." 

    "Suddenly as you pass by a cafe, you catch a fragment of a conversation."

    show unknown_girl3 angry
    unknown_girl3 "Charlie I told you, you need to give it up. I'm tired of hearing about your stupid conspiricy theories."

    show charlie angry
    charlie "And I'm telling you, it's not a conspiracy! The world is ending and I don't know how to stop it!"

    unknown_girl3 "Can you just drop it. Mom and Dad are worried, you stopped returning your calls, you stopped going out with me for drinks, it's like I don't even know you anymore."

    show charlie aloof 
    charlie "I'll be fine."

    unknown_girl3 "No you aren't! You've been like this ever since-"

    charlie "Don't drag her into this."

    unknown_girl3 "You have to let go eventually."

    charlie "No. I don't. It was nice meeting with you sis, I'm going to leave now." 

    you "Charlie... I have to follow him."

    "You follow Charlie out of the cafe as he makes his way through the city."

    "You can't help but instinctively walk beside him, a part of you finds it familliar."

    charlie "What am I even doing..."

    "Charlie continues to mumble to himself as he continues to walk down the street." 

    charlie "I mean, you heard what she said, and I know maybe I am too deep into this."

    charlie "But how couldn't I be, especially when..."

    show charlie turned towards you

    "You feel chills run down your body as he turned to look in your direction. You stop walking as he stares right into your eyes."

    "He can see you?!"

    show charlie laughing

    charlie "Who am I kidding, it's not like you're listening. But I like to imagine you are."

    "He laughs to himself, there's something in you that can't help but chuckle at the sight."

    "Charlie makes his way to a small cemetary on the outter parts of the city." #my spelling bad help

    charlie "I'm sorry I haven't been visiting as often as I used to."

    charlie "But I hope you understand, I'm trying to continue where we left off."












    

