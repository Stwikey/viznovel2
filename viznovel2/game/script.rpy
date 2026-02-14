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
define name = Character('[name]')

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

define orryx = Character('Orryx') #charlie REPLACEMENT NAME
#knows what happened and refuses to let go of the past while all the others did, depressed guy 

#lowkey want to make both sides of the story morally gray so the player has a harder time to choose which side to help
define faerin_unknown = Character('???', color="#000000")
define io_unknown = Character('???', color="#914b4b")
define azer_unknown = Character('???', color="#0b3b2e")
define zaelf_unknown = Character('???', color="#0b3b2e")
define helio = Character('Helio', color="#60288b") #helioptile 
# helio is also the corn god from d20 :D <-  everything goes back to dropout :sob:
define helio_unknown = Character ('???',color="#5da0c4" )
define unknown_girl3 = Character('???')
define unknown = Character('???')

define hexaria = Character('Hexaria')
define huntsman = Character('Renrir')

define io_mom = Character('Io\'s Mom')
define io_dad = Character('Io\'s Dad')

#story paths 
default stay_at_cemetary = False 

define npc = Character('npc')
default figgly = Character('Professor Figgly')

#constants
define fade = Fade(0.5, 0.0, 0.5)


#vision of apocalypse/introsduction
label start:
    $name = renpy.input("what will you name yourself?", length=20)
    #cutscene of vision

    show vision_1

    "Hazy images of supernatural creatures grabbing students by the throat fill your vision."

    show vision_2

    "Large flames roar in the background, unable to muffle the screaming voices of the students."
    
    show vision_3

    "One of the creatures stares directly at you"

    play sound "hiss"

    #waking up

    "You wake up with a sharp pang in your head."

    you "Ugh."

    "You find yourself laying on a grassy field. Plants and flowers rustle in the wind."

    "You can feel their magic pulsating through the air, as they breathe."

#you wake up to your pigeon (or other) carrier squawking in your face, it seems like you got mail
label intro: 
    "You wake up with a hard smack to your face."

    "A bird lets out a loud SQUACK and flaps it's wings urgently, hitting your face."

    you "Ugh, what the heck Helio?!"

    Helio "CAWWWW!"

    "Helio drops a pile of scrolls that it was carrying in it's claws on your face and lands gently on your stomach."

    menu: 
        "Look at the mail":
            jump look_at_the_mail
        "Go back to sleep":
            jump go_back_to_sleep

# You wake up and start reading the mail
label look_at_the_mail:
    you "Ugh okay okay."

    "You sit up tiredly, rubbing your eyes, knowing that Helio will start pecking you again if you don't wake up."

    "Helio tilts his head, looking at you expectantly."

    menu: 
        "Read the letter":
            jump read

# You try to go back to sleep but Helio prevents you from doing so, so you get up anyways
label go_back_to_sleep:
    "You cover your head with your blanket, blocking your eyes from the bright sunlight being cast in your room."

    Helio "SQUWAKKKKKKKKKKKK"

    "Helio starts pecking you aggressively, and you feel his beak through the blanket."

    jump look_at_the_mail

# You read the letter, surprised to find out the magic academy you applied to accepted you after a few months of rejecting you
label read:
    "You sign, slowly opening up the scroll, reading,"

    "\"Dear [name], Congratulations! Fortunately a spot has recently opened up for you to attend the magic academy! Hope to see you there!\"" #fix 

    "\" Sincerely, Headmaster Dean."

    menu:
        "What?":
            jump what

# You are shocked because of the letter
label what:
    you "huh?"

    "You vividly recall memories of being rejected months ago."

    "After hopefully applying to the academy you waited excitedly for days to see if you got in."

    "However, when you finally received the mail you got rejected."

    menu:
        "It's a prank":
            jump prank
        
        "Jump for joy":
            jump joy

# You think the letter is definetly a prank but Helio says otherwise
label prank:
    you "This has got to be a prank"

    "You lay back down ready to go back to sleep."

    Helio "SQUWAKKKK SQUWAKKKKKKKK"

    you "what? the Headmaster personally gave you the letter?"

    you "I don't believe you"

    Helio "SQUWAKKK"

    you "okay fine fine, I'll go I'll go"

    Helio "chirp"

    menu:
        "Set off for the academy":
            jump set_off

# You jump for joy, excited to finally attend your dream academy
label joy:
    you "yay yay! I knew they made a mistake when they didn't choose me!"

    "You hug Helio excitedly"

    Helio "squwakkkkkk...."

    menu:
        "Set off for the academy":
            jump set_off

# You walk to the academy
label set_off:
    "You quickly get dressed and pack your bags, eagerly setting off to the academy."

    "After a long walk and many rides, you finally arrive at the grand entrance of the academy."

    menu:
        "Open the doors":
            jump open

label open: 
    "You take a deep breath, and push open the large doors that reveal a grand interior"

    npc "?"

    npc "Oh! You must be [name]! The new student, correct?"

    menu:
        "Yep thats me!":
            label yep

label yep:
    npc "Perfect! Here's your schedule, a map of the school, and let me take you to meet your dorm mates!"

    "The professor hands you two large scrolls and you take them carefully."

    "In a quick glance you see the large layout of the school, as well as classses on your schedule such as potion making and spell casting"

    npc "Let me know when you're ready to leave!"

    menu:
        "I'm ready!":
            jump ready
        "Give me a moment":
            jump moment

label moment:
    "You take in the interior of the school, large, tall pillars reach towards the sky and with large emblems and intricate designs flowing through the ceiling."
    
    "It's your dream school, and you are finally attending it."

    menu:
        "I'm ready now":
            jump ready

label ready:
    npc "Alright! follow me!"

    "The guide leads you through long hallways and delicate staircases"

    "After what feels like forever, the guide finally stops at a large, wooden door"

    npc "Here it is! They might be on edge since you're new here after months but I'm sure you'll all be friendly in no time!"

    npc "I'll leave you be now, you can come to me if you have anymore questions!"

    "The guide walks away, their footsteps getting quieter as they walk away."

    menu: 
        "Knock on the door":
            jump knock

label knock:
    "You knock gently on the door, hearing subtle whispers from behind it"

    "The door slowly creaks open, revealing three faces"

    faerin_unknown "..."

    you "yikes, they sure are on edge"

    "A blonde haired girl pops up from behind the girl, patting her on the back"

    io_unknown "ahaha faerin don't be like that!"

    "She smiles at you sheepishly"

    io_unknown "you must be our new dormmate right? My name's Io! and this is Faerin"

    faerin_unknown "..."

    io_unknown "aaaand that's Zaelf over there!"

    zaelf_unknown "..."

    "Zaelf gives you a small nod."

    io_unknown "Yeah Zaelf is actually mute, but Faerin's being mean today apparently."

    menu:
        "Introduce yourself":
            jump introduce_yourself

label introduce_yourself:
    you "My name's [name], nice to meet you all..."

    "an awkward silence passes."

    io "aaaaaanyways! It's almost lunch time so let's go to the cafeteria?"

    "Zaelf moves forward and looks back at you, and you follow nervously, things were not going as smoothly as you had hoped"

    "As you walk further away from Io and Faerin who stayed back, you hear fragments of their under the breath conversation"

    io "I told you to be nice to her! she didn't do anything wrong!"

    faerin "...I know..."

    jump cafeteria

label cafeteria:
    "You and Zaelf arrive to the cafeteria first and Faerin and Io arrive shortly after, the delicious smell of freshly made food makes you hungry"

    "Zaelf points in the direction of a long line and you and the group quickly grab food, sitting down at one of the empty tables."

    "Still feeling the tension in the air, you quickly gobble down the food, without making eye contact"

    io "after lunch, well have class"

    io "since you joined late you're probably behind but we'll help you catch up!"

    "she smiles at you brightly"

    io "what class do you have now?"

    you "umm let me check."

    "You quickly open up your now crumpled time table"

    you "spell casting"

    "Io's smile quickly drops"

    io "oh you share the same class as Faerin!"

    "She shoots Faerin a glare"

    io "she'll help you through the class, right?"

    "Faerin nods slowly, without looking up"

    "You sit tightly at your seat, watching the time slowly tick by"
    
    jump first_class

label first_class:
    "The bell rings, signaling the end of the lunch period."

    "Students all start rushing out the cafeteria."

    io "[name], me and Zaelf have potion making class now so we'll see you guys back at the dorm!"

    menu:
        "See you!":
            jump see_you

label see_you:
    "You follow Faerin nervously as she takes off without a word."

    menu:
        "Try to make small talk":
            jump small_talk
        "Stay silent":
            jump silent

label small_talk:
    you "I'm going to be in the same dorm as these people for the rest of this school year, might as well try to make friends"

    you "Faerin-"

    faerin "We're here."

    "Faerin gestures towards a door with a plaque that reads \"Spell Casting 101\""

    "Guess she isn't a big fan of talking."
    
    jump spell_casting

label silent:
    "You stay silent, ignoring the awkward silence."

    jump spell_casting

# You learn a new spell in this class!, as well as possibly making progress with your friendship with faerin
label spell_casting:
    "You and Faerin find an empty bench to sit on."

    "Suddenly, a booming voice echos across the room."

    figgly "HELLO HELLO!"

    figgly "Once again, I am your Spell Casting professor, Professor Figgly!"

    menu:
        "What type of name is Figgly?":
            faerin "..."

            "She doesn't say another but you can see her trying stiffle a laugh."

    figgly "Today, we'll be learning..."

    figgly "...a new spell!"

    figgly "I've decided on four basic level spells that you can choose from, after that split up into the groups that want to learn the same spell as you."

    menu:
        "I want to learn the light spell":
            jump learning

label learning:
    "You get put into groups."

    "Surpisingly Faerin is also there."

    faerin "Stop following me."

    menu:
        "I'm not following anyone.":
            you "Why would I ever want to follow you?"

        "Sorry.":
            you "Sorry."

    faerin "Whatever."

    figgly "Wonderful! Now that you are put into teams, you will venture out and find the elusive exclusive amazing..."

    figgly "Drum roll please~"

    "Random person" "Just tell us already you old man."

    figgly "That's not very nice."

    "The professor looks down, a bit saddened."

    menu: 
        "Try to cheer him up.":
            "You start pitter pattering on the table to create a drum roll."

            "His expression cheers up."

            "Faerin looks at you a bit nicer now."

            "You take that as a win."

        "Point and laugh.":
            "You start laughing at him."

            "He hears the laughter but ignores it."

            faerin "..."

            "You have lost favour with faerin."

    figgly "Continuing, each of you in your pairs will be sent to complete various tasks associated with the spell you have chosen."

    "You watch as he begins to walk around, handing out various assignment sheets."

    figgly "Ahh Faerin! I trust you will be able to do this well."

    "He looks at you."

    figgly "[name]? Was it? I hope you can follow in her footsteps."

    faerin "I will ensure we accomplish this to the best of our abilities."

    figgly "Mm."

    "He nods before walking away."

    "You look down to read the assignemnt."

    show assignment paper 

    faerin "This should be simple enough."

    jump assignment_mission 

label assignment_mission: 
    faerin "We need to find Hexaria's flower."

    faerin "They are abundant at this time so there shouldn't be any issues."

    you "Oh, that's nice."

    faerin "Yeah."

    faerin "Whatever, just try not to mess things up."

    "She walks ahead of you."

    "As you continue walking you reach a village."
    
    "It's located near the outskirts of town near, nearby the location of Hexaria's flower."

    faerin "Willowsburrow is nice towards newcomers, especially students so we shouldn't have any trouble."

    faerin "Just try to stay away from-"

    "You can't hear what she says as you get distracted from the village enterance in front of you."

    "Flowers line the walls, with children laughing and running around."

    "Faerin gestures you to follow her."

    faerin "I'll go grab the flower, you can just... stay here I guess."

    menu:
        "No I want to go with you.":
            jump go_with_faerin

        "Fine, I'll stay here.":
            jump get_mugged 

label go_with_faerin:
    faerin "Fine."

    faerin "Don't get in my way."

    "You walk towards the back of the village a tiny gate blocks enterance."

    "Guard" "Hello how can I help you two?"

    faerin "We were wondering if we could get a flower for our assignment."

    "Guard" "Certainly, although for security reasons we will need to see proof of the assignment."

    "Guard" "I assume your professor has given a written permission slip?"

    menu:
        "Permission slip?!":
            you "Um- I-"

            faerin "Here it is."

            "Gaurd" "Ah perfect!"

        "Yeah it's right here!":
            "You pull out a blank paper."

            "you could've sworn you placed it in your pocket."

            "Gaurd" "Sorry ma'am, but that is a blank sheet of paper."

            faerin "Excuse her, here it is."

            "Gaurd" "Ah perfect!"

    "The gaurd opens the the gate."

    "Gaurd" "Please limit yourself to only one."

    faerin "Yes."

    "Faerin goes to pick the flower."

    "You walk back out of the flowered section, not wanting to cause her more trouble."

    jump get_mugged

label get_mugged: 
    "As you wait outside, two muscular men approach behind you."

    "???" "Hey there..."

    "You turn around and see them."

    "They have masks over their faces and their hands held up, a mysterious magic surging from them."

    "Something... dark."

    "???" "Heard you were students getting your hands on Hexaria's flower."

    "???" "Me and my buddy here, would really apperciate that flower."

    menu:
        "Sorry, I need it for an assignment!":
            you "Sorry, I need it for an assignment."

        "Get your own flower you nasty, ugly, fat, not even that buff, super weak prolly, scrawny little rats.":
            you "I'd advise you get your own. Sorry."

    "???" "We aren't really taking no for an answer."

    "They start heading over to a spot where they can attack Faerin when she exits."

    menu: 
        "Allow them to take the flower from Faerin.":
            jump allow_take

        "Defend Faerin.":
            jump dont_take 

label allow_take: 
    "You stand there frozen."

    faerin "[name] I am done with-"

    "Before she can finish one of the men tackle her to the ground."

    "You watch as she struggles before behind hit by some type of dark magic spell."

    "She goes limp under them as they prepare to take the flower."

    menu:
        "Attempt to stop them.":
            you "Stop it!"

            "You run at the man currently trying to grab the flower out of Faerin's hand."

        "Your feet start moving, you raise your hands up."

    menu: 
        "Cast the light spell.":
            "You decide to cast the light spell."
        
        "Push them over.":
            "The push does little to no effect except turn their attention onto you."

            "You decide to cast the light spell."

    "Raising your hands up, you see the flower that fell to the floor begin to glow."

    "Since this is the first time casting this spell, you feel yourself begin to shake."

    "The flower glows brighter, leading you to release an unseen of amount of power."

    "???" "What the?"

    "???" "I thought she was dead?"

    "They get blasted away."

    "What is left, is simply dust in where they once stood."

    faerin "...!?"

    "You see Faerin begin to stir."

    faerin "Uxie?"

    you "Um... no just me."

    faerin "..."

    "There's something... off about Faerin now."

    "Her eyes have changed from the light blue they once were to a dark red."

    faerin "Thank you for saving me."

    "She picks up the now wilted flower, before looking back over at the field."

    faerin "Seems this one is useless now."

    faerin "We will have to obtain another permssion slip from the professor."

    faerin "Correction, you will."

    faerin "I no longer have interest in learning this spell."

    you "???"

    "You drop the discussion. Not wanting to press further."

    jump return_to_school

label return_to_school:
    figgly "Ah what a shame, I will certainly write you another."

    "He turns to you."

    figgly "I am impressed by your display of magic you haven't practiced yet."

    figgly "Where did you learn it?"

    menu:
        "I'm not too sure, sorry.":
            figgly "Aw a shame. Reminds me of a past student we had."
    
    "There's a sad look on his face."

    "You glance at Faerin and she seemed to have flinched at him mentioning a past student."

    faerin "Professor, if I could interupt."

    figgly "Please go ahead."

    faerin "I would like to switch to learning the dark casting spell instead of the light one."

    figgly "Oh?"

    figgly "How unusual. Well, since you are a star student gladly."

    figgly "[name], I trust you will be able to complete this on your own?"

    you "Yeah, no problem."

    "Faerin looks at you, not saying anything."

    faerin "Where did you say you were from?"

    you "Oh..."

    menu: 
        "Try to recall your memories.":
            "You try hard to think."

    faerin "You look constipated are you okay?"

    you "Oh uh, yeah sorry just trying to remember."

    figgly "I will leave you to your own devices, [name], please find another partner to continue the assignment or find an already existing pair to join."

    figgly "Faerin, I will put in your transfer. I wish you the best of luck."

    "You part ways with Faerin."

    "Congrats you have successfully learned the light spell!"

    jump continue_school 

label continue_school:
    "You head back to your door to be greeted by Io and Zaelf."

    io "How was class?"

    menu: 
        "Tell her what happened.":
            "You summarize what happened today."

            io "Yikes, you must've just been unlucky. Thankfully no one got hurt right Z?"

            zaelf "..."

            "He does a light nod."

            you "Keke, yeah."

        "Tell her everything including the weirdness of Faerin.":

            "You summarize everthing that happened."

            you "Also..."

            io "Mm?"
            
            you "Faerin started acting... strange."

            you "She got hit with some dark spell and mentioned someone named Uxie?"

            io "Oh."

            io "i wouldn't worry about it."

            io "Faerin's been having a hard time ever since... yeah."

            io "It's nothing personal, just how things ended up."

            zaelf "..."

            "Zaelf nods, as if to reassure you."

    
    io "Well we said we would meet everyone tomorrow for lunch, so get a good nights rest."

    io "Don't let the bed bugs bite!"

    "Io makes a silly face at you before heading off to her room."

    "Zaelf waves goodnight before heading off to his room."

    jump lunch_meeting

label lunch_meeting:
    "You wake up and head out with Io and Zaelf."

    io "Ah... a nice day to be out."

    "You see two people running to apprach."

    "???" "IO! ZAELF!"

    io "Orryx! Azer!"

    orryx "Oh who's this?"

    you "Hi my name is [name]!"

    azer "My name's Azer and this is Orryx!"

    azer "Hey where's Faerin?"

    io "She should be here soon, maybe she's just running late."

    "You hear hurried footsteps."

    faerin "Sorry, I got distracted with something."

    "Faerin shoots you a glare. She seems to be hiding something."

    you "???"

    faerin "We should go."

    io "Gotcha! Let's goooooo~"

    "The group continues to walk to the lunch spot."

    "As you walk you find yourself talking to Azer and Orryx, getting to know them better."

    orryx "And this one, Uxi- I mean, our friend gave me this charm."

    "He points towards the various charms on his bag."

    azer "Yeah, those were the days."

    "They both seem to have this look of sadness on their face."

    menu: 
        "Ask about who Uxie is.":
            you "Um, if you don't mind, who is Uxie?"

            azer "..."

            orryx "..."

            "Faerin turns her head to look at you."

            faerin "She's our friend that moved."

            "Faerin turns back around and continues walking next to Zaelf and Io."

    azer "... yeah, she moved."

    orryx "We should visit her soon though, I bet she's getting pretty lonely."

    azer "Yeah we could after lunch? Maybe [name] can meet her!"

    menu:
        "I'd love to meet her.":
            io "Look the resturant's there!"
            jump lunch_eating 

label lunch_eating: 
    "\"It's supernatural\" was the name of the resturant you were at."

    "It sure did live up to it's name as various species were seen eating at the tables."

    you "Is that a dragon?"

    "You point towards the dragon species eating steaks."

    io "Yep! Everyone is welcome here."

    you "Ooo and are those elves?"

    azer "A bunch of different species like to gather here, it's kind of a safe space."

    orryx "Plus if you even try starting a fight, the body guards will kick you out."

    "He points towards two cloaked figures, you can't tell what species they are but you can tell by their sheer size that they aren't afraid of conflict."

    faerin "Please stop pointing at the other customers and sit down already."

    "You all sit down at the table."

    faerin "Hello could I get the toasted eels?"

    io "!?"

    "Server" "Haven't heard of that order in a while."

    io "Haha, yeah. We are planning on visting her today."

    "Server" "Is that so? Send her my regards, I'll cover your meal as well. On the house."

    azer "No no we couldn't possibly."

    "Server" "I insist."

    orryx "Thank you."

    "Everyone else says their order and it is now your turn."

    menu:
        "Order a sandwich with mysterious ingredients":
            you "I'd like the dragonborne sandwhich."

            "Server" "Interesting choice."

        "Order noodles made with Hexaria petals.":
            you "I'd like the noodles with Hexaria petals."

            "Server" "Good choice."

        "Order a mystery item.":
            you "Could I just have something random?"

            io "???"

            io "She's so similar to-"

            "Server" "Oh? Haha if I hadn't known any better I'd think you were Ux-"

            faerin "That will be all."
    
    orryx "Well now that foods settled, [name] you should tell us about yourself!"

    menu: 
        "Tell them what you remember":
            you "Well, I woke up in a field of grass."

            you "And now I'm here."

    
    io "???"

    io "Parents? Past friends? Anything else?"

    you "Nope."

    orryx "Haha, she's as secretative as Faerin."

    faerin "..."

    "After conversing more you learn that they have all been attending the school for a while and met during orientation."

    you "Yeah I vividly remember being rejected?"

    io "Why on earth would they reject you?"

    you "Uh... look at me I'm..."

    menu:
        "Underqualified.":
            you "I think I was just underqualified."

            io "But you did so good casting the light spell for the first time!"

            you "Yeah I guess."

        "Overqualified.":
            you "I think I was just overqualified."

        "A useless rat who doesn't do much so I'm not sure why they let me in to begin with.":
            you "I'm just a useless rat who doesn't do much so I'm not sure why they let me in to begin with."




#big boss battle that almost kills ur friends --> if u choose to use the new (artifical) spell (big damage) u get affected, 
#if not ur friends just get very ingjured or one of them can die idc --> if u get affected io helps u and u get brought to the dark side and u dont then u dont uh
# also the reason why faerin dont like u in the beginning is cus uxie went missing and they replaced her with u so quick so faerin dont like u + 
# the school but io is ok with u cus she knows uxie is alive just in the evil faction and lowkey zaelf is just chillin cus hes nonchalant idk bro
'''
BREAK BREAK BREAK BREAK inc 
'''

#choice to recall memories
menu: 
    "Try to remember what happened.":
        jump memories
#trying to recall memories but can't remember anything about yourself
label memories:
    "You tried to recall what happened, you search your mind for something, anything, to explain who you are, and what you are doing but to no avail."

    you "Who am I? I can't remember my name..."

    you "Where am I...?"

    you "Ugh my head hurts."

    jump introduction
#introduction to the student's names & personalities
label introduction:
    
    "You begin to hear voices nearby and footsteps that get louder and louder as they approach you."

    show io surprise  

    io_unknown "Hey! Look over here!"

    "The unknown girl runs over to where you are laying, three other figures running to catch up to her."
    
    show io happy

    io_unknown "Ah! Found it! Hexaria's Flower!" #hexaria is the goddess who gifted the world magic, so the flower is extremely rare to find for some reason (idk) also important bc maybe it leads to the worlds downfall

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

    faerin_unknown "Weird. It's almost as if someone sat on this whole patch of grass."

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
    
    azer_unknown "Yeah! It already took us half the time to find this one patch!"

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

    azer "!"

    "The boy stares directly at you and you feel the magic in the air snap back."

    io "What happened?"

    "Azer shakes his head, confused."

    jump part_2

#going to someplace to look at more flowers
label part_2:
    "You watch as the boy gathers magical energy... it feels familliar, but you can't put your finger on it yet." 

    zaelf "..."

    "Zaelf nods again, towards the direction of a forest."

    io "Willowsburrow?"

    "A familiar feeling rushes through your mind."

    "You get this cold feeling, as fragmented memories flash through your head."

    "\"LAZAR STOP IT, YOU'LL DIE!\"" # put this in quotes mysteryyyy

    you "Who the hell is Lazar?" 
    
    "You are brought back to the present, but there are still many missing memories." 

    show azer nervous

    io "Don't tell me you're chickening out now? We said we would get 100 on this project, so we are guaranteeing that 100."

    "Faerin sighs"

    faerin "Professor Fiddlesticks said that Hexaria's flower is extremely important to the academy's operation..."

    faerin "If we fail we may have to retake the magic exam. Or worse, we face expulsion." #something or other

    azer "fine...."

    zaelf "..."

    menu:
        "Try to warn them":
            jump danger
        
        "Do nothing":
            jump oblivious


label danger: 
    "You concentrate hard as you try your best to warn them, shouting at the top of your lungs."

    show io silly

    you "STOP DON'T GO!" 

    "You jump right in the middle of the group, waving your arms around to get someones attention."

    "The group continues to chatter, blissfully unaware of your attempts to contact them."

    io "Well we better go! Let's not worry too much and try to enjoy the assignment. Professor said we should be more focused on learning anyways."
    
    you "I don't know why I try, they can't see or hear me. I can't save them if I continue like this."

    jump part_3

label oblivious:
    "You watch as they leave. Chattering away about their plans, maybe it was just a one off feeling." 

    "But as you continue to wander around the city, the sinking feeling in your stomach continues to eat away at you."

    jump part_3

label part_3: 
    # basically learn a bit about who Lazar is in this universe 
    "You continue to wander around, walking through the street."

    you "Who is Lazar? And what was he doing..." 
    
    you "Something is going to destroy this world, I know I'm not a mortal like those kids from earlier." 

    "Suddenly as you pass by a cafe, you catch a fragment of a conversation."

    show unknown_girl3 angry
    unknown_girl3 "Orryx I told you, you need to give it up. I'm tired of hearing about your stupid conspiricy theories."

    show Orryx angry
    orryx "And I'm telling you, it's not a conspiracy! The world is ending and I don't know how to stop it!"

    unknown_girl3 "Can you just drop it. Mom and Dad are worried, you stopped returning your calls, you stopped going out with me for drinks, it's like I don't even know you anymore."

    show Orryx aloof 
    orryx "I'll be fine."

    unknown_girl3 "No you aren't! You've been like this ever since-"

    show Orryx angry
    orryx "Don't drag her into this."

    unknown_girl3 "You have to let go eventually."

    show Orryx calmer
    orryx "No. I don't. It was nice meeting with you sis, I'm going to leave now." 

    you "Orryx..." 

    you "I have to follow him."

    "You follow Orryx out of the cafe as he makes his way through the city."

    "You can't help but instinctively walk beside him, a part of you finds it familliar."

    orryx "What am I even doing..."

    "Orryx continues to mumble to himself as he continues to walk down the street." 

    orryx "I mean, you heard what she said, and I know maybe I am too deep into this."

    orryx "But how couldn't I be, especially when..."

    show Orryx turned towards you

    "You feel chills run down your body as he turned to look in your direction. You stop walking as he stares right into your eyes."

    "He can see you?!"

    show Orryx laughing

    orryx "Who am I kidding, it's not like you're listening. But I like to imagine you are."

    "He laughs to himself, there's something in you that can't help but chuckle at the sight."

    "Orryx makes his way to a small cemetary on the outter parts of the city." 

    orryx "I'm sorry I haven't been visiting as often as I used to."

    orryx "But I hope you understand, I'm trying to continue where we left off."

    orryx "I hate them."

    orryx "I know you said not to, but I hate them."

    orryx "I hate the way they get to continue walking around, even after all they did." #this is first implication that the group was the cause of your death

    orryx "And I hate you."

    orryx "I hate that you left me alone, to deal with all of this."

    you "Orryx... I'm sorry, I don't remember what happened"

    you "but I promise I'll figure it out."

    orryx "I heard they are going to Willowsburrow. Idiots." #the spooky location from intro scene 

    orryx "They are going to get themselves killed. As if one wasn't enough might as well make it the rest of the party." #more implication 

    you "The group from earlier... they were going to Willowsburrow."

    menu: 
        "Stay by Orryx's side.":
            jump stay
        
        "Try to track down the adventuring group from earlier.":
            jump track

# when staying we learn about how the flower contributes to their goal and the mission they are on but we will be late or possibly miss the opening to try to intervene 
label stay:
    $ stay_at_cemetary = True
    you "I can't leave him now."

    you "He might know more information about the world ending. And if what he's saying is true I need to prevent it from happening."

    orryx "You always could talk some sense into them."

    orryx "I remember when you used to talk Zaelf's ear off."

    orryx "I know he never said anything about it but we both know he liked it."

    jump zaelf_story_1

label stay_2: 
    you "..."

    you "Uxie..."

    show Orryx looking down to his watch

    orryx "Shoot, I'm not gonna get there in time to stop them!"

    show Orryx running away 

    you "I should search for them too."

    jump track

#when leaving we will find the group but have no idea what their goals or plans are 
label track: 
    you "I can't be wasting time, I have to find them."

    "You leave the cemetary in search of the group from earlier."

    #we could add a flash back here to earlier opening scene where the people phased through 

    you "They mentioned finding a flower."

    you "If I could figure out what it was used for, I could find help!"

    you "I have magical ablities, and my interactions with this world are uncertain."

    #recall the scene from earlier where when you sat down the grass and stuff flattened 

    you "But it seems like I can interact with things... just not people?"

    "You look down to see a bug crawling inbetween the cracks of the sidewalk."

    menu: #both result in same findings just fun interactive part 
        "Try to squish it with your foot.":
            jump murderer

        "Try to pick it up.":
            jump pacifist

label murderer: 
    "You raise your foot, stomping down hard on the spot where the bug was."

    "To your surprise the bug crawls through, not being affected by your pressance."

    jump part_4

label pacifist: 
    "You lower your hand, extending a finger in the direction the bug is crawling in."

    "To your surprise, it walks through, not being affected by your pressance."

    jump part_4

# when you catch up with the party different depending on if you stayed behind to learn more or rushed to stop them 
label part_4: 
    unknown_girl3 "Did you hear about the party going to Willowsburrow?" #unknown is just placeholder, too lazy to make ?? characters rn

    unknown "It was probably Faerin's idea, you know her repuation at the school."

    unknown "I'm surpirsed Azer didn't fight it harder, we all know he's a scardy cat when it comes to danger."

    unknown "As if one tragdey wasn't enough for them."

    "The student scoffs, he seemed younger than the party from earlier."

    unknown "Maybe you shouldn't be so quick to judge, I mean, we haven't even gone on an adventure yet."

    unknown "No one has, the school practically banned it for lower years ever since-"

    unknown "Ugh stop talking! Just thinking about it give me the heebie jeebies."

    show unknown person taunting other person
    unknown "Who knows maybe she's haunting you right now~"

    unknown "Shut up! I can't stand being around you."

    "The girl storms away, as the boy chases after her."

    menu: 
        #two pathways, first one just more explicit in giving information to the player, second is basically a time saver
        "Try to piece together clues.":
            jump detective

        "Wander around the city in search for a map.":
            jump explore

label detective: 
    "There was an incident that occured at the school." #can flash images of the boy at the cemetary

    "Ever since then, younger years have been forbidden from doing adventures." #show image of the unknown people talking from earlier

    "But the party from earlier were still conducting adventures." #show flashes of faerin, azer, etc. 

    "The best conclusion I can come up with is that..."

    "The adventuring party from earlier orginally had one more member."

    you "The best place to find information would be a library of some sort."

    you "From what I've gathered, it seems like I can interact with inanimate objects and plants." #conclusion i drew, feel free to change

    if stay_at_cemetary == True:
        you "Uxie must have been the student that died."

        you "And whoever Orryx is must have been in the party with her."

        you "As well as the others from earlier."

        jump explore

    else:
        jump explore

label explore: 
    "The signs posted all over the city prove useful as they eventually lead you into the direction of a library."

    "The library was empty, as the sun set in the city."

    "Looking around, there was a librarian cataloging books while grumbling under her breath." #MY SPELLIGN HELP

    menu: 
        "Approach the librarian":
            jump part_5


label part_5:
    #idea that i have feel free to use or throw away
    #mc goes to library and finds book on the hexaria flower 
    #maybe the reason why the adventuring party is so like set on this mission is that they are under the belief that it can ressurect people 
    #or can make them all like bad people and they all it in for the grade and sacrificed you on purpose
    #hexaria's flower similar to the one in tangled where in a sense it has incrediable healing ablities and is rumoured to be able to ressurect when combined with dark magic???
    #extremely risky as when you go onto the path of ressurection you trap the dead person in a limbo. (which could be what the mc is experincing rn)
    #mc finds only about the healing ablities or can find out about the whole thing depending on how long gameplay wants to be
    
    librarian "Those kids... they sign out the books and have the nerve to return it 2 weeks past the due date. If it wasn't Professor Fiddlesticks that sent them on the mission I would've given them detention."
    #i imagine to an old lady with reading glasses with the beads that connect so that when they fall it just dangles like a necklace 
    #wears probably a really burgandy cardigan, with a cup of steeped tea, and a pamphlet for mental health reasources that no one takes on the table
    
    you "Professor Fiddlesticks..."

    you "The group from earlier... that had to be it."

    "You glance at the table, seeings the front cover of a bright yellow flower, its petals opened all the way exposing an unique white center."

    you "I can't sign the book out... so I have to steal it."

    "You walk over to a shelf, sticking your arm out and knocking all the books off."

    "BANG"

    librarian "!"

    show librarian angry

    librarian "How many times have I told those first years to be careful!"

    hide librarian angry 

    "You manage to quickly take the book and slip out of the library with the book in hand."
    
    show book 
    menu: 
        "Open the book.":
            jump hexaria_story

label part_6: 
    you "Hexaria's flower..."

    you "The magic it holds has the possiblity of healing anything."

    you "Could it... somehow heal my memory loss?"

    "You can't afford to get distracted now."

    you "The group from earlier, if I follow them..."

    you "I'll be able to find one."

    "Thinking about it for longer, you remember when you could absorb magic."

    "This could be your key to remembering and maybe escaping this... limbo?"

    "\"Hexaria's flower is abundant on the mountain she is said to have lived. The famed Willowsburrow, known for it's extremely wet and slippery terrain."

    "The terrain is said to be due to the amount of tears Hexaria cried those faithful days.\"" 

    you "Willowsburrow! I have to go there."

    "You hear someone running from behind you."

    orryx "Those idiots! When will they learn their actions have consequences."

    "It was Orryx from earlier... except this time he was holding a staff of some sort along with a bag on his back."

    orryx "Willowsburrow? Seriously?"

    "As of by habit, you started jogging beside him."

    orryx "One person wasn't enough, so they're gonna kill everyone else huh?"

    "You continue to follow him through various terrain, even continuing through the night."

    "By the end of the journey, Orryx looked tired. Unlike you, the lack of sleep was not as kind."

    "His poor posture and growing eye bags only further supported this."

    orryx "This is stupid."

    orryx "Uxie... why did you have to leave..."

    if stay_at_cemetary == False: 
        you "Uxie?"

        you "It must be the person who died."

    show orryx tearing up 

    "You notice his steps begin to falter as he begins to slow down."

    orryx "I don't want to continue anymore. No matter what I do I can't change anything."

    orryx "Who am I kidding... they'll probably be done the mission and get themselves killed as a part of it."

    orryx "If you were here you'd probably be scolding me for not believing in our friends." 

    you "You feel a vision come to you."

    scene fade with black 
    jump uxie_story_1

label part_7: 
    "Suddenly you were back."

    "Except Orryx laid on the ground, unmoving."

    "His chest was still rising and falling, but he looked ill."

    menu:
        "Try to heal him.":
            "You hold out both your hands as a yellow glow emitts from them."

    "You see as the bags under his eyes seem to fade and his breathing returns to normal." 
    
    orryx "..."

    orryx "*groans*, what the heck?"

    "He springs up immediately and begins looking around frantically."

    menu: 
        "Get up Orryx, please.":
            orryx "UXIE? WHERE? WHAT?"

    orryx "I must've been dreaming."

    "He holds his head with his hands before picking up his backpack."

    orryx "Man I guess I really needed that rest."

    orryx "I hope I'm not too late."

    "He continues to venture towards where you assume the direction of Willowsborrow is."

    jump part_7

label part_7: 
    

#character background info, could probably split these into multiple parts that you find out later
#(don't have to discover all of their full backstories, player should want to choose who they think the imposter is)
label io_story_1:
    "..."

    io "Uxie I promise it'll be fun!"

    uxie "I'm not sure..."

    uxie "It's supposed to be raining kinda bad that day."

    io "Fine fine party pooper."

    #idk where im going with this rn 


label faerin_story_1:
    # i feel like in this story we can jsut see a glimpse of how faerin interacted before her... issues??? 
    "..."

    unknown_helio "Faerin, excellent work as always!" #using helio for now feel free to change later just using this as prof varible 

    "The professor hands back the marked assignment to Faerin, a big \"100\" scrawled on the front page in bright red ink."

    unknown_helio "Good on paper Uxie... but no practical application."

    "Uxie stared down at the paper, a 74 inked with red pen stared back at her."

    faerin "..."

    "Faerin stares at you, sliding over her paper in exchange for yours." # gonna assume mc knows they are Uxie at this point in time but works either way just lmk and i fix

    uxie "Oh, yeah you can take mine." 

    "Faerin doesn't reply as she begins flipping through your work, scrawling corrections with her own pencil."

    show faerin emotionless
    faerin "It makes sense in theory, they just want you to do it this way. Textbook says so."

    "She seems to be indifferent about this whole situation as a whole. Seemingly only curious at the fact that you had something written not from the textbook."

    uxie "We should go. They are probably waiting for us."

    "You don't bother to put any effort into making yourself more amiable towards her, not like she would care regardless."

    show the rest of the group

    io "We should hang out! I mean, class is over and we don't have homework-"

    faerin "I'm going home."

    "Io stares at Faerin."

    io "Please Faerin you never come! I know Zaelf would want you there~"

    zaelf "..."

    "He never spoke much, or in general from what you could remember."

    uxie "It's okay, I know Faerin isn't much of an outside person."

    "Faerin looks at you with a slight thankfulness in her eyes."

    "Io huffs angrily."

    io "Oh fine, but next time you are so coming with you hear me?"

    "Faerin nods before waving goodbye and leaving before anyone could reply."

    io "One day I'll get that girl out of her shell, just like I did with Zaelf!"

    "Io pats Zaelf on the shoulder while he stands still and stares."

    azer "Okay let's just get going, Orryx is waiting for us at the front of the school."

    uxie "Oh yeah! I hope his test went well." #oh for Orryx or whatever his name is, lets not give him a backstory so its spooky hahaha also i lazy 

    #jump to wherever 

label zaelf_story_1:
    "..."

    uxie "... and then he said that he wouldn't let me! Can you believe it?"

    zaelf "..."

    uxie "I KNOW RIGHT? Ugh and I know he's also kinda right but he doesn't get what this means to me."

    zaelf "..."

    uxie "Yeah that's a good point. I should talk to him."

    "Zaelf nods, as you both walk down the hallway."

    "You stop at a classroom, the plaque outside titled \"Herbology 235\"."

    uxie "I hope professor doesn't make us work with torch ginger again!"

    "Zaelf was always a good listener."

    scene black with fade 
    scene classroom 

    uxie "Sweet! We get to work with turkey tangle frogfruit!"

    "A small smile appears on Zaelf's face, he wasn't as nerdy as Faerin but he enjoyed herbology."

    "It was one of the rare times where he wasn't seen as..."

    "different."

    professor "Class, I want to continue where we left off..."

    "The professor's voice fades into the background as you continue to talk to Zaelf."

    uxie "Oooo I think Io wants to hang out today? Something about practicing our abilites. Sometimes I think she's more academically motivated than Faerin."
    #puts like foreshadowing of Io

    "Zaelf nods, you can't tell if he actually wanted to attend, or did so to not have to answer more questions."

    "A part of you always liked to think he just liked listening to everyone talk."

    zaelf "*points towards the flower*"

    uxie "Oh yeah! What did the professor say again?"

    "A smile breaks out on Zaelf's face as he began to do something with his hands."

    "A dark coloured aura surrounded his hands." #yo his stink

    "Before he could apply it onto the plant, a voice from somewhere in the class shouted."

    unknown "I DON'T UNDERSTAND? You teach too fast!"

    professor "Okay okay, calm down. I'll be over in a moment to assist you."

    "You hide a snicker as you start conjuring magic in your hands instead."

    uxie "I got this!"

    "..."
    show plant being magiced on 

    "BOOM!"

    show you and zaelf cover in soot 

    uxie "Whoops?"

    professor "What in the name of helio is going on here?" #idk using helio for now

    zaelf "..."

    uxie "..."

    professor "*sighs*"

    if stay_at_cemetary == True:
        jump stay_2
    else:
        #j

label azer_story_1:
    "..."

    uxie "Do it! Do it! Do it!"

    azer "I can't!"

    io "Come on~, don't be a scardey cat!"

    azer "I am a scaredy cat now get me down!" 

    show everyone watching azer_at the top of a tree

    "Azer was afraid of heights."

    "Very afraid."

    "Which leads us to wonder how he ended up in this situation."

    scene black with fade 

    "A few moments ago..."

    #he was pretending to be like super cool and non chalant but got scared so badly he ran up a tree 

label uxie_story_1:
    "..."

    "You see an open feild, a group of children are playing in the grass chasing each other and shouting."

    io "Just you wait! I'm gonna be the greatest mage in the world!"

    azer "Io, you haven't even got your magic yet, meanwhile the great and powerful Azer is already one step ahead!"

    show child_io puffing her cheeks out angry 

    uxie "Stop trying to pick a fight Azer, why can't you be more like Zaelf."

    show uxie pointing towards zaelf 

    zaelf "..."

    faerin "Words of wisdom that guy."

    uxie "Exactly!"

    show orryx trying to jumpscare uxie 

    orryx "BOO!"

    uxie "!"

    orryx "Ehe, just me!"

    uxie "Not funny!"

    show everyone laughing cus it so funny

    "Looking away from the children, a familliar flower comes into view."

    show flower 

    "Tucked away in the grass, there it was."

    "Hexaria's flower..."

    you "This is what they are looking for..."

    "You feel a pull towards the flower."

# then like something and you can absorb magic to give orryx more energy or like so he feels ur aura (stink) idk 
    menu:
        "Try to absorb magic.":
            jump part_7

#the group comes back,, too lazy to write the stuff that happens before lol
label arrival:
#io disappears 

label io_story_2:
    "You rush after Io as she disppears into the forest, leaving the others behind."

    you "I'm worried about them but... I need to know what is happening with Io."

    "Sparks of magic burst unexpectedly from Io's fingers and she winces in pain"

    io "UGH why is it malfunctioning now?!" 

    io "After all I did..."

    show io turning to your direction so like staring_at the screen

    "Io turns to look at you."

    you "!"

#possible ending 1 iea: u are hexaria and u get resurrected but you are blinded by rage so the vision comes true & you destroy everything

#hexaria's backstory, fell in love with a mortal who died eventually and did not want to spend immortality with her, hexaria's tears created magical plants known as hexaria's flowers that were abundant in magical energy. 
#hexaria ended up cursing his bloodline (? maybe?) 
label hexaria_story: #finished for you feel free to change

    "Hexaria was a loving Goddess who loved to travel to the mortal realm and the mortals loved her."

    "They tossed baskets of flower petals in which she danced in, and granted wishes to the people."

    "One day, when she was wandering through the woods, she met a huntsman who mistakened for a lost girl."

    "He helped her into his home in the woods and fed her."

    "Hexaria found this silly, she was a Goddess after all. However, for once in her life time she was the one who was being taken care of, and she felt warmer than ever."

    "Hexaria fell in love with the huntsman and soon after, they promised each other with the rest of their lives."

    "However as time went on, it was clear that they were of different worlds."

    show hexaria holding basket of apples

    hexaria "I'm backkkkkk, we can make apple pie for dessert today!"

    hexaria "?"

    hexaria "Hey why is your hair turning gray? You look... different"

    huntsman "Haha... did it really take you this long to notice?"

    huntsman "As for you, you haven't changed one bit."

    "Some could say that Hexaria was blissfully unaware. Or maybe some would call her a fool."

    "But her grasp on mortal lives..."

    "was limited."

    huntsman "I'm aging... it's what mortals do."

    hexaria "Is that an illness? I can heal you!"

    huntsman "No, no. None of that."

    huntsman "This is simply the way of life."

    hexaria "The way of life?"

    "Maybe at the time she didn't fully understand that the way of life always involves death."

    "Or maybe she just couldn't accept it."

    show hexaria watching hunstman laying in bed 

    hexaria "I don't understand, I tried healing you but it's not working!"

    huntsman "You cannot heal this, for it is not an illness silly. *coughs*"

    huntsman "It's my time... please don't cry."

    show hexaria crying

    huntsman "You are far too beautiful to be crying."

    hexaria "You said you would stay with me... for the rest of our lives."

    huntsman "I didn't mean to be made a liar. I'm sorry, I truly am my dearest, Hexaria." #HAMILTON????

    "\"The rest of their lives...\""

    "Hexaria's understanding was askew. For the huntsman did spend the rest of his life with her."

    "But she still had infinity to go. An infinity without... him."

    "When he passed... she flew into a great depression."

    show hexaria crying sobbing wailing 

    "She tried to bring him back."

    "Really she did."

    "But you can't heal the dead."

    show hexaria looking_at her hands

    "As time passed she couldn't bear to seperate from the Huntsman."

    "Even if that meant, seeing his remains."

    "Time heals all wounds..."

    "But time only rubbed more salt into them."

    show hexaria w the rotting corpse 

    hexaria "You lied."

    hexaria "You said we would live the rest of our lives together, and now you've left me."

    "Of course she knew what really happened."

    "But believing that he hated her hurt less than accepting the truth."

    #hexaria tries to use her magic to keep him as alive as possible but he starts decomposing lollll
    #he tells hexaria he wants to be free and hexaria gets angry cus she thinks he doesnt love her anymore
    #hexaria CRASHES OUT cus HE DIES

    "Hexaria fell into a deep sadness and her tears rained down the skies for 32 days"

    "from the rain a new species of flower was discovered, named as Hexaria's flower"

    "from that day on Hexaria disappeared and no longer visited the mortal realm."
    jump part_6

#cut backstories up into parts later
label io_backstory:
    "Io grew up in a small neighbourhood and lived a normal childhood, at least she thought it was normal to her."

    show io dad smile

    io_dad "Io! come here! want to see something cool?"

    io "yeah!"

    "io's dad flicks his wrist, and with a concluding snap, bubbles begin rising from the dew on the grass"

    io "Wow! Dad this is so cool!"

    io "How did you do that? I wanna know I wanna know!"

    io_dad "This, Io, is called magic."

    io_dad "It makes what seems impossible possible and it was a gift that came from the great Goddesss Hexaria."

    "Io's mom smiles nervously"

    "Io grins widely"

    io "WOW! Can you teach me how?"

    "Io's dad smiles weakly and ruffles his daughter's hair"

    io_dad "haha not now honey, maybe when you're older." 

    "Io jumps with excitement and runs away, going to play with her dinosaur toys."

    "Her mom pulls her dad to the side."

    io_mom "Why would you tell her about magic?"

    io_dad "She's going to find out eventually."

    io_dad "Magic is simply used too mnuch everywhere."

    "Io's mom sighs and looks down."

    io_mom "What will happen when she finds out that she can't use magic? Her greatest dream is to become a mage."

    io_dad "It'll be fine. I promise."

    #io gets magic artificially from a underground faction without her parents knowing (unstable)
    #her magic is based on bubbles --> she uses foam & air bubbles to fight
    #she shows her parents her magic and they think its a miracle and she enrolls into the academy

    "As time passed, there never came the day where Io got powers."

    "Never the day that she would run to her parents bragging about her newly found magic."

    "But you can't just dangle candy in front of a child and expect them not to chase it?"

    io "It isn't fair."
    
    "It was at that time..."

    "Io realized she would never be blessed with magic."

    "So she blessed herself."

    show io gaining artifical powers

    "Artifical magic."

    unknown "There are drawbacks."

    show io like pawbert where he had like that mad look in his eyes 

    io "I know."

    hide io 

    "When she told her parents..."

    "They were so, so, so proud."

    io_mom "Honey it's a miracle! Our little girl is a mage!"

    show io_mom super happy and hugging io 

    # more details here of scene 

    #... 

    "Overtime, the cracks began showing."

    show io attempting magic alone it crackles and fizzes out

    show io frustrated 

    io "You... you can't give up on me now. Not after I worked so hard to make this happen."

    io "What I had to give up in return..."

    "Of course, all magic has a price."

    "So when Io started experiencing issues..."

    "She saught ways of fixing it."

    show io looking flipping through books seeing the book about hexarias flower 

    "You would never expect such a lovely girl, to go to extreme lengths to make sure no one found out."

    io "I really am sorry, but I can't really be the greatest mage that ever lived... if I'm not a mage."

    show io hovering over someone 

    #jump to netx
    


#give player limited mana so they can only save certain amount of people
label battle:


return
#good ending
#label win:

#bad ending
#label lose:









    

