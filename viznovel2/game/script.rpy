'''
Summary:

You are a murdered student who was part of a student adventuring party when you were alive. 
You have no past memories of who you were and what happened but you do know that the world
will end soon if nothing happens.

Learn more about the characters & figure out if they are bad/good (figure out who murdered you)
and guide correct characters to possibly change the future.

Genre:
Fantasy

Setting:
Historical, rural, magic academy
'''

#defining characters
default mana = 0
define you = Character('You', color="#ffffff")

define faerin = Character('Faerin')
#emo, introverted, deadpan, textbook magic, good at studies, goes insane later maybe, rival of mc(?) <-- makes people sus her

define zaelf = Character('Zaelf')
#also introverted, mute, dark magic <-- makes people sus him(?)

define io = Character('Io')
#extrovert, outgoing girl, sus magic 
#possibly ur murderer (?) try to make her least expected :0 <-- could change but idk a better character that could fit rn


define uxie = Character('Uxie')
#you, DEAD, possibly had powerful magic when you were still alive <-- why they killed you(?)
#maybe you are hexarias daughter/vessel though not sure what that would mean

define azer = Character('Azer')
#stereotypical aloof guy, can get scared for his life which makes him more selfish <-- makes people sus him 

#lowkey want to make both sides of the story morally gray so the player has a harder time to choose which side to help
define faerin_unknown = Character('???', color="#000000")
define io_unknown = Character('???', color="#914b4b")
define azer_unknown = Character('???', color="#0b3b2e")
define zaelf_unknown = Character('???', color="#0b3b2e")
define helio = Character('Helio', color="#60288b") #helioptile
define helio_unknown = Character ('???',color="#5da0c4" )
define unknown_girl3 = Character('???')

#vision/introduction
label start:
    #cutscene of vision
    "Hazy images of supernatural creatures grabbing students by the throat fill your vision."

    "Large flames roar in the background, unable to muffle the screaming voices of the students."

    "One of the creatures stare directly at you"

    #waking up

    "You wake up with a sharp pang in your head."

    you "Ugh."

    "You find yourself laying on a grassy field. Plants and flowers rustle in the wind."

    "You can feel their magic pulsating through the air, as they breathe."
#choice to recall memories
menu: 
        "Try to remember what happened.":
            jump memories
#trying to recall memories but can't
label memories:
    "You tried to recall what happened, you search your mind for something, anything, to explain who you are, and what you are doing but to no avail."
        jump introduction
#introduction to the student's names & personalities
label introduction:
    "You begin hear voices nearby, getting louder and louder as they approach you."

    show io surprise  

    io_unknown "Hey! Look over here!"

    "The unknown girl runs over to where you are laying, three other figures running to catch up to her."
    
    show io happy

    io_girl "Ah! Found it! Hexaria's Flower!" #hexaria is the goddess who gifted the world magic, so the flower is extremely rare to find for some reason (idk) also important bc maybe it leads to the worlds downfall

    "The girl peers over, staring directly at you, face almost touching yours and pointing almost past you."

    you "!"

    you "Can she not see me?"

    show faerin neutral

    faerin_unknown "We can't use those Io."

    "The other unknown girl bends forward, her hand reaches past you."

    you "!" 

    show faerin holding_flower

    "When she pulls her hand out, she is holding a small, wilted flower." #cutscene instead of words maybe
    
    faerin_unknown "This flower's magic is almost out." #aka its dying

    faerin_unkown "Weird. It's almost as if someone sat on this whole patch of grass."

    "The girl traces in the air, circling the perimeter around where you are laying."

    faerin_unknown "Look, all the plants here are crushed."

    show azer angry

    azer_unknown "Ugh! It must've been those first years again!"

    azer_unknown "Professor Fiddlesticks is going to scold us again for sure and it's not even my fault this time!"

    faerin_unknown "..."

    show io casting

    io "Faerin wait! let me try something."

    faerin "Don't. You shouldn't use your magic on this sort of thing." #foreshadowing that io has sus magic(?)

    faerin "Plus, the Professor always knows when magic is used to tamper things. This flower is already dead." #hints that magic shouldn't be used to revive things (not sure why yet tho)

    "The flower distintegrates in faerin's hand. Black ashes float up and scatter across the field."

    io "Awww alright. But where are we supposed to find more?"
    
    azer_unknown "Yeah !it already took us half the time to find this one patch!"

    azer_unknown "Ugh! I'm going to file a report against those first years."

    faerin "Azer."

    faerin "Calm down, we still have time."

    faerin "Zaelf, do you have enough magic to cast another spell?"

    "Zaelf nods."

    "Zaelf concentrates, you can feel magic flowing in the air intensely."
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

#going to someplace to look at more flowers
label part_2:
    "You watch as the boy gathers magical energy... it feels familliar, but you can't put your finger on it yet." 

    zaelf "..."

    "Zaelf nods again, towards the direction of a forest."

    io "PLACEHOLDER?" #come up with a good name for some spooky location 

    "You get this cold feeling, as fragmented memories flash through your head."

    "CHARLIE STOP IT, YOU'LL DIE!" # put this in quotes mysteryyyy

    you "Who the hell is Charlie?" 
    
    "You are brought back to the present, but there are still many missing pieces." 

    show azer nervous

    azer "Are you sure? Even the professors don't go up there..." 

    io "Don't tell me you're chickening out now? We said we would get 100 on this project, so we are guaranteeing that 100."

    "Faerin sighs"

    faerin "Professor Fiddlesticks said that Hexaria's flower is extremely important to the academy's operation..."

    faerin "If we fail we may have to retake the magic exam" #something or other

    azer "fine...."

    zaelf "..."

    menu:
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


#character background info, could probably split these into multiple parts that you find out later
#(don't have to discover all of their full backstories, player should want to choose who they think the imposter is)
label io_story:

label faerin_story:

label zaelf_story:

label azer_story:

label uxie_story:

label helio_story:










    

