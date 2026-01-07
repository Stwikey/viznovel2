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

define higeki = Character('Higeki') #CHARLIE REPLACEMENT NAME (???)
#replacement for charlie name to fit theme more lol lmk if this is ok replacement name cus idrk? 
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
define huntsman = Character('Huntsman')

define io_mom = Character('Io\'s Mom')
define io_dad = Character('Io\'s Dad')



#vision of apocalypse/introduction
label start:
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

    "\"CHARLIE STOP IT, YOU'LL DIE!\"" # put this in quotes mysteryyyy

    you "Who the hell is Charlie?" 
    
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
    # basically learn a bit about who charlie is in this universe 
    "You continue to wander around, walking through the street."

    you "Who is Charlie? And what was he doing..." #change his name 
    
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

    show charlie angry
    charlie "Don't drag her into this."

    unknown_girl3 "You have to let go eventually."

    show charlie calmer
    charlie "No. I don't. It was nice meeting with you sis, I'm going to leave now." 

    you "Charlie..." 

    you "I have to follow him."

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

    "Charlie makes his way to a small cemetary on the outter parts of the city." 

    charlie "I'm sorry I haven't been visiting as often as I used to."

    charlie "But I hope you understand, I'm trying to continue where we left off."

    charlie "I hate them."

    charlie "I know you said not to, but I hate them."

    charlie "I hate the way they get to continue walking around, even after all they did." #this is first implication that the group was the cause of your death

    charlie "And I hate you."

    charlie "I hate that you left me alone, to deal with all of this."

    you "Charlie... I'm sorry, I don't remember what happened"

    you "but I promise I'll figure it out."

    charlie "I heard they are going to Willowsburrow. Idiots." #the spooky location from intro scene 

    charlie "They are going to get themselves killed. As if one wasn't enough might as well make it the rest of the party." #more implication 

    you "The group from earlier... they were going to Willowsburrow."

    menu: 
        "Stay by Charlie's side.":
            jump stay
        
        "Try to track down the adventuring group from earlier.":
            jump track

# when staying we learn about how the flower contributes to their goal and the mission they are on but we will be late or possibly miss the opening to try to intervene 
label stay:
    you "I can't leave him now."

    you "He might know more information about the world ending. And if what he's saying is true I need to prevent it from happening."

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

# when you catch up with the party different depending on if you stayed behind to learn more or rushed to stop them 
label part_4: 
    unknown_girl3 "Did you hear about the party going to Willowsburrow?" #unknown is just placeholder, too lazy to make ?? characters rn

    unknown "It was probably Faerin's idea, you know her repuation at the school."

    unknown "I'm surpirsed Azer didn't fight it harder, we all know he's a scardy cat when it comes to danger."

    unknown "As if one tradgey wasn't enough for them."

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

    hide librarian

    "You manage to quickly take the book and slip out of the library."

    #continue 

#character background info, could probably split these into multiple parts that you find out later
#(don't have to discover all of their full backstories, player should want to choose who they think the imposter is)
label io_story_1:
    "..."

    io "Uxie I promise it'll be fun!"

    uxie "I'm not sure..."

    uxie "I don't really do outings."


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

    azer "Okay let's just get going, (not charlie but idk new name yet) is waiting for us at the front of the school."

    uxie "Oh yeah! I hope his test went well." #oh for charlie or whatever his name is, lets not give him a backstory so its spooky hahaha also i lazy 

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

    fade with black 
    show classroom 

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

    #jump to wherever 


label azer_story_1:
    "..."

label uxie_story_1:
    "..."

label helio_story_1:
    "..."

#the group comes back,, too lazy to write the stuff that happens before lol
label arrival:



#io disappears 
label io_story_2:
    "You rush after Io as she disppears into the forest, leaving the others behind."

    you "I'm worried about them but... I need to know what is happening with Io."

    "Sparks of magic burst unexpectedly from Io's fingers and she winces in pain"

    io "UGH why is it malfunctioning now?!"


#possible ending 1 iea: u are hexaria and u get resurrected but you are blinded by rage so the vision comes true & you destroy everything

#hexaria's backstory, fell in love with a mortal who died eventually and did not want to spend immortality with her, hexaria's tears created magical plants known as hexaria's flowers that were abundant in magical energy. 
#hexaria ended up cursing his bloodline (? maybe?) 
label hexaria_story: #NOT FINISHED

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

    huntsman "haha... did it really take you this long to notice?"

    huntsman "as for you, you haven't changed one bit"

    #hexaria tries to use her magic to keep him as alive as possible but he starts decomposing lollll
    #he tells hexaria he wants to be free and hexaria gets angry cus she thinks he doesnt love her anymore
    #hexaria CRASHES OUT cus HE DIES

    "hexaria fell into a deep sadness and her tears rained down the skies for 32 days"

    "from the rain a new species of flower was discovered, named as hexaria's flower"

    "from that day on hexaria disappeared and no longer visited the mortal realm"

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

    

#give player limited mana so they can only save certain amount of people
label battle:

















    

