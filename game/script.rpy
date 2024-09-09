# The script of the game goes in this file.

define neko_girl = Character("Sun", color="#ff0000")
define player = Character("[player_name]", color="#0000ff")

# The game starts here.

label start:

    scene bg room

    "It's a late Saturday afternoon, and the sun hangs low in the sky, casting a golden glow over the small, bustling city."
    "You're seated at an outdoor table of a charming, quaint café nestled on a quiet corner street."
    "The air is cool but comfortable, with a gentle breeze that rustles the leaves of the nearby trees, carrying with it the mingled scents of freshly brewed coffee, warm pastries, and the subtle hint of lavender from the potted plants surrounding the tables."
    
    $ player_name = renpy.input("what is your name?", length=10).strip()

    if not player_name:
        $ player_name = "Player"

    "The café is alive with the sound of soft chatter and the clinking of cups and cutlery, a cozy ambiance that feels welcoming yet private."
    "A few other patrons are scattered around, engrossed in their own worlds, creating a perfect balance between lively and intimate."
    "The table before you is small and round, made of wrought iron with a delicate floral pattern that matches the vintage style of the chairs."
    "A single candle flickers softly in the center, its flame dancing with every small gust of wind."
    "It's early evening, and the sun is beginning to dip below the horizon, painting the sky in shades of orange, pink, and purple."
    "The warmth of the day is slowly giving way to a cooler, crisper air that brushes against your skin, a reminder that nightfall is near."
    "The café's overhead lights turn on, casting a soft, amber glow that mixes with the fading daylight, creating an almost magical atmosphere."
    "Across from you sits the girl you met on OkCupid. She seems nervous, her eyes darting around before finally settling back on you."
    "Her hands fidget with the menu, her fingers brushing against the edges in a distracted manner."
    "She's dressed simply, yet there's a quiet elegance to her—a white blouse, a light blue skirt, and a small, silver necklace that catches the light when she moves."
    "Her ears, slightly pointed with soft, delicate fur, twitch every now and then, as if sensing the world around her."
    "You notice her tail is tucked slightly to the side, hidden but still, it sways ever so slightly with her mood."
    "She looks down for a moment, taking a deep breath, then meets your eyes with a shy smile."
    "Her cheeks are faintly flushed, whether from the cool air or her nerves, you can't quite tell."
    "When she speaks, her voice is soft, almost hesitant."
    neko_girl "Quietly, with a touch of nervousness. \"So… there's something I should probably tell you. It's… a bit strange.\""
    "She hesitates for a second, glancing away as if gathering courage, then looks back at you."
    neko_girl "I'm… um, I'm actually a neko. A cat girl."
    "She lowers her gaze, clearly anxious about your reaction. Her hands grip the menu a little tighter, her ears twitching nervously."
    "You can see the faintest hint of her tail curling slightly around her chair, a reflex she's trying to suppress."
    neko_girl "I know it's… unusual. And I understand if you want to end the date here. But… I hope you won't."
    "Her eyes meet yours again, and you can see a mix of hope and fear in them. She's waiting for your response, holding her breath, unsure of what you'll say."

    menu:
        "accept":
            jump acceptance
        "reject":
            jump rejection

label rejection:
    "You take a deep breath and shake your head slowly."
    "Her face falls, her ears droop, and her tail curls around her legs like a protective shield. She bites her lip, nodding to herself, as if accepting your decision even though it stings."
    neko_girl "With a sad smile. \"I… I understand. Thank you for being honest.\""
    "She stands up, her movements slow and deliberate, and she gives you one last, lingering look before turning away. You watch as she walks down the street, her figure growing smaller and smaller until she's gone from sight."
    "The café feels quieter now, the warmth from earlier replaced with a chill that seems to seep into your bones. You're left sitting alone at the table, the soft sounds of the city continuing around you."
    return

label acceptance:
    "You smile reassuringly, leaning forward slightly to meet her gaze."
    player "I don’t mind at all. In fact, I’m glad you told me."
    neko_girl "Surprised and exhilarated. \"Really? You mean it?\""
    player "Of course! I'm here to get to know you, and that includes everything about you."
    neko_girl "Her eyes light up, and she beams at you, her tail swishing excitedly behind her. \"Wow… I didn't expect that! This makes me so happy!\""
    "She leans in closer, her shyness melting away as the two of you continue your conversation, the date taking a turn for the better."

    neko_girl "But… I should explain something before I get too excited. You see, in this world, beast people like me… we're seen as beneath others in society. Most of us aren't free and are often owned by someone as servants or even pets."
    "She glances around to make sure no one is eavesdropping before continuing, her voice softer."
    neko_girl "I don't have a master right now, and it's rare for someone like me to be a student in an education field. It's been difficult, but I've worked hard to be here."
    "She pauses, her earlier enthusiasm dimming slightly as she looks at you, searching your face for any sign of discomfort."
    neko_girl "I found your profile really interesting, and I was hoping we'd get along. But… before I let myself get too excited, I need to ask… what do you do for a living?"
    "Her tone is cautious, as if she's bracing herself for your answer."

    menu:
        "Unemployed":
            jump unemployed_choice
        "Warehouse Worker":
            jump warehouse_worker_choice
        "Teacher":
            jump teacher_choice
        "Engineer":
            jump engineer_choice


label unemployed_choice:
    player "With a small, somewhat sheepish smile. \"I'm currently between jobs, so… unemployed.\""
    neko_girl "Her expression softens with understanding, and she offers a sympathetic smile. \"I know how that feels. I've been on and off work myself while trying to stay in school. It's not easy, especially since I have to pay just to remain free and be a full-time student.\""
    "She pauses, her gaze drifting to the table for a moment before she looks back up at you."
    neko_girl "I'm studying graphic art design."
    neko_girl "It's what I really love, and I hope to get into a field where I can put my skills to use."
    neko_girl "But… if I can't find steady income soon, I might have to find a master who would protect and finance me."
    neko_girl "It's not what I want, but… sometimes you have to make tough choices."
    "She sighs softly, her eyes reflecting both determination and a hint of worry."
    neko_girl "It's hard, trying to balance everything."
    neko_girl "But I'm doing my best. I'm glad you're being honest with me."
    neko_girl "It makes me feel like… maybe we're in the same boat,\n just trying to make things work."
    "She gives you a small, hopeful smile, clearly still interested in continuing the conversation."
    jump job_question_done

label warehouse_worker_choice:
    player "With a straightforward tone. \"I work in a warehouse, handling shipments and inventory.\""
    neko_girl "She nods, considering your words. \"That sounds like hard work. It's honest and steady… I respect that. I'm glad you're making a living.\""
    jump job_question_done

label teacher_choice:
    player "With a hint of pride. \"I'm a teacher. I work with kids, helping them learn and grow.\""
    neko_girl "Her eyes widen, and her ears perk up with genuine interest. \"Really? That's amazing! I always admired teachers… You must have a lot of patience and care for others. That's… really wonderful.\""
    jump job_question_done

label engineer_choice:
    player "With a confident smile. \"I'm an engineer. I work on designing and building things.\""
    neko_girl "Her eyes light up again, clearly impressed. \"Wow, that's incredible! You must be really smart and creative. It's not often I meet someone who works in such a technical field… I think that's really cool!\""
    jump job_question_done

label job_question_done:
    "Waiter" "Good evening! Are you both ready to order?"
    "You glance at the menu, considering your options."

    menu:
        "Stir-Fried Pork Rice":
            $ persistent.fav_food_option = False
            jump stir_fried_pork_rice_choice
        "Sushi Bento Box":
            $ persistent.fav_food_option = True
            jump sushi_bento_box_choice
        "Chicken Katsu":
            $ persistent.fav_food_option = False
            jump chicken_katsu_choice

label stir_fried_pork_rice_choice:
    player "Pointing to the menu. \"I'll have the stir-fried pork rice, please.\""
    neko_girl "She smiles politely, though you notice a subtle flicker of disappointment in her eyes. She quickly hides it, maintaining her ladylike composure. \"That sounds nice. I'll have the sushi bento box.\""
    "As the waiter leaves, she looks at you with a soft smile. \"I'm not the biggest fan of pork rice, but honestly, just being here with you makes it taste better.\""
    jump food_question_done

label sushi_bento_box_choice:
    player "With a smile. \"I'll go with the sushi bento box.\""
    neko_girl "Her eyes widen slightly, and she seems to brighten up. \"Really? That's my favorite! I'll have the same.\""
    "The waiter nods and leaves with the order. You catch a glimpse of her as she watches the waiter leave"
    "her lips part slightly, a hint of drool forming at the corner of her mouth before she quickly regains her composure, dabbing at her lips with a napkin."
    neko_girl "Sorry about that! I just really love sushi, but… it's important to maintain appearances, right?"
    "She laughs softly, her eyes shining with excitement."
    jump food_question_done

label chicken_katsu_choice:
    player "With a confident tone. \"I'll have the chicken katsu.\""
    neko_girl "She nods approvingly. \"Good choice! I'll have the sushi bento box.\""
    "As the waiter leaves, she smiles at you, her gaze warm."
    "Chicken katsu is delicious, but there's something about sushi that I just can't resist. I hope you'll enjoy your meal as much as I will."
    jump food_question_done

label food_question_done:
    "After the waiter leaves with your order, she looks at you curiously, tilting her head slightly. "
    neko_girl "So, we've talked a bit about work, but… what are your aspirations? What do you really want out of life?"

    menu:
        "I want to further my career.":
            $ persistent.knock_out_option = False
            $ persistent.i_want_to_rule_the_world_option = False
            jump i_want_to_further_my_career
        "I want to abolish beast men apartheid.":
            $ persistent.knock_out_option = True
            $ persistent.i_want_to_rule_the_world_option = False
            jump i_want_to_abolish_beast_men_apartheid
        "I want to rule the world.":
            if persistent.fav_food_option == True:
                $ persistent.isekai_scene = True
            elif persistent.fav_food_option == False:
                $ persistent.knock_out_option = True
            jump i_want_to_rule_the_world

label i_want_to_further_my_career:
    player "With a determined tone. \"I want to further my career, make a name for myself, and really succeed in my field.\""
    neko_girl "She nods thoughtfully, her eyes reflecting admiration. \"I respect that a lot. It's not easy to stay focused and driven, especially in a world like ours. I can see you're someone who's serious about their goals… that's really attractive.\""
    jump want_out_of_life_question_done

label i_want_to_abolish_beast_men_apartheid:
    player "With passion in your voice. \"I want to abolish beast men apartheid. I can't stand the way people are treated differently just because of who they are.\""
    neko_girl "Her eyes widen, and she leans in closer, clearly moved by your words. \"You… really mean that? I've never met anyone who cared so much about our struggles. That's… incredible. I didn't expect to find someone like you tonight.\""
    "Her admiration for you deepens, and she looks at you with newfound respect and hope."
    jump want_out_of_life_question_done

label i_want_to_rule_the_world:
    player "With a playful smirk. \"I want to rule the world. Why settle for less, right?\""
    neko_girl "She laughs, her eyes sparkling with amusement. \"You're ambitious, I'll give you that! The idea of someone with big dreams is always intriguing… but make sure you don't forget about the little people like me when you're in charge.\""
    "There's a teasing tone to her voice, but she's clearly intrigued by your boldness."
    "I just want to fuck."
    player "With a casual shrug. \"Honestly? I just want to fuck. Life's too short to complicate things.\""
    neko_girl "She raises an eyebrow, a mischievous smile playing on her lips. \"Straight to the point, huh? I appreciate the honesty, though I'd say there's more to life than just that. Still… a bold answer like that takes guts.\""
    jump want_out_of_life_question_done

label want_out_of_life_question_done:
    "The waiter returns after some time, clearing away the empty plates and thanking you both for dining at the café. The evening air has grown cooler, and the streetlights have come on, casting a soft glow over the scene."
    neko_girl "She looks at you, her expression slightly shy but with a hint of anticipation. \"I've really enjoyed our time together tonight… Would you like to go back to your place? I'd love to spend more time with you.\""

    menu:
        "Yes.":
            jump go_back_to_your_place_yes
        "No.":
            jump go_back_to_your_place_no

label go_back_to_your_place_yes:
    player "With a warm smile. \"Yes, I'd like that.\""
    neko_girl "Her face brightens, and she stands up, ready to leave with you. \"Great! Let's go. I'm excited to see where this night takes us.\""
    "You both leave the café, walking together into the night, the connection between you growing stronger with every step."
    jump arrival_at_your_place

label go_back_to_your_place_no:
    player "With a gentle tone. \"No, I think it's best we end the night here.\""
    neko_girl "She looks a bit disappointed but quickly recovers, offering you a soft smile. \"I understand. Thank you for being honest with me. I had a great time tonight.\""
    "She stands up, smoothing out her clothes as she prepares to leave."
    neko_girl "I hope we can see each other again. Take care, okay?"
    "With a final wave, she walks away into the night, leaving you to reflect on the evening as the café buzzes with the low hum of conversation around you."
    jump end_of_story

label arrival_at_your_place:
    "The two of you walk back to your place, the night air crisp and quiet."
    "However, as soon as the door closes behind you, something unexpected happens."
    
    if persistent.knock_out_option == True:
        #"The Knockout"
        "You turn to say something, but before the words leave your mouth, she moves with lightning speed, delivering a sharp blow to the back of your head. Darkness floods your vision as you collapse to the floor, unconscious."
        
        # shake effect
        show neko_girl happy at center:
            linear 0.1 xalign 0.5 yalign 0.5
            linear 0.1 xalign 0.48 yalign 0.5
            linear 0.1 xalign 0.52 yalign 0.5
            linear 0.1 xalign 0.5 yalign 0.5


        # fade to black
        scene black with dissolve
        with Pause(1)
        
        "When you regain consciousness, you're lying on a cold, hard surface."
        "The room around you is dimly lit, and you can hear faint whispers and shuffling nearby. As your vision clears, you realize you're not alone."

        # fade to red
        show scene_red with dissolve
        with Pause(1)

        "Several figures are standing around you, all with the same feline features—ears, tails, sharp eyes. They're all neko women, watching you intently."
        "You try to move, but your limbs are restrained. Panic surges through you, but before you can react further, she steps into view, her expression serious but no longer hostile."
        neko_girl "You're awake. Good."
        "She kneels beside you, her tone calm but with an undercurrent of urgency."
        neko_girl "I'm sorry for the rough treatment, but I had to make sure you were serious about what you said. I needed to bring you somewhere safe—somewhere where you could truly understand what's at stake."
        "She gestures to the others around you, who are now looking at you with a mix of hope and desperation."
        neko_girl "Welcome to the resistance. We're a group of beast girls—mostly nekos—who are fighting against the system that oppresses us. We've been working in the shadows, trying to gather allies, resources, anything we can to change our fate."
        "One of the other neko women steps forward, her eyes wide and pleading."
        "Neko Woman" "We've heard what you want—to either abolish the apartheid or even rule the world. We need someone like you on our side. Please, help us. We've been suffering for so long, and we're running out of time."
        "Another neko woman nods, her voice trembling with emotion."
        "Neko Woman 2" "We don't have much, but we're willing to do whatever it takes to end this. We need someone strong, someone who believes in a better future… someone like you."
        "They all look at you, their eyes filled with hope and desperation, waiting for your response."
        "The path ahead is uncertain, but one thing is clear: your decisions will shape the future of not just these neko women, but perhaps the entire world."

        menu:
            "join the resistance and help them fight for their freedom":
                jump unknown_1
            "walk away, leaving them to continue their struggle alone":
                jump unknown_1
    
    elif persistent.isekai_scene == True:
        #"isekai (alternate world)"
        "The two of you step out from the cozy warmth of your apartment into the crisp night air. It's a Saturday evening, and the city hums softly around you."
        "The streets are less crowded now, the earlier buzz of activity settling into a more relaxed, almost serene atmosphere."
        "A light breeze brushes against your face, carrying with it the faint scent of jasmine from a nearby flower shop that has long since closed for the night."
        "The streetlights flicker intermittently, their yellowish glow casting long shadows that dance on the pavement."
        "You notice how the light reflects off her eyes, giving them a mysterious, almost ethereal shimmer."
        "She seems lighter now, her steps graceful as if a weight has been lifted. Her tail sways gently behind her, and her ears, twitching with every small sound, peek out from her hair, more prominent now in the dim light."
        "Overhead, the sky is a deep navy blue, dotted with stars that blink in and out behind passing clouds. The moon, nearly full, hangs low, casting a soft silver light that seems to follow your steps."
        "The air is cool but not biting—just enough to remind you of the warmth of the café you left behind and the closeness you felt there."
        "You walk side by side, your footsteps in sync, your breaths forming faint puffs in the cool air."
        "You come to a crossroad, a quiet intersection where the street narrows and the buildings seem to lean in, as if listening to your conversation. A streetlight above buzzes faintly, struggling to stay on."

        # truck sound effect
        play sound "audio/truck_sound.wav"

        # start vpunch effect
        scene bg room at start_vpunch_effect(0.2)
        
        "The road is empty save for the distant rumble of a truck far off in the distance, its headlights barely visible through the haze of the city's ambient light."

        # stop vpunch effect
        scene bg room at stop_vpunch_effect

        # fade to black
        scene black with dissolve
        with Pause(0.5)

        "She laughs softly at something you said, her voice bright against the muted sounds of the city night."
        "Her laugh is warm, and it makes you feel, just for a moment, like you're the only two people in the world."
        "She turns to you, her face framed by the moonlight, looking as if she's about to say something more, something important…"

        #"The Isekai Twist: Sudden Impact"
        "And then—there's a blinding flash of headlights, a roar of an engine, and the screeching of tires against asphalt."
        "The truck seems to come out of nowhere, barreling down the narrow street with terrifying speed."
        "You barely have time to register what's happening before it's too late."
        "There's a moment of weightlessness, a sense of everything moving in slow motion."
        "You feel the impact, the force sending you flying back, and then—darkness."
        "The world around you fades away, replaced by an all-encompassing black void."
        #"Waking Up: The Otherworldly Realm"
        "When you open your eyes again, you're no longer on the cold, hard street. Instead, you're floating in a vast, boundless space that seems to stretch infinitely in all directions."
        "The air is warm here, filled with a soft, comforting light that wraps around you like a blanket."
        "You feel weightless, as if suspended in a gentle current."
        "The space around you shimmers, the light shifting and swirling like liquid gold."
        "Faint, ethereal sounds fill the air—like a distant chorus singing a melody you can't quite make out."
        "The sensation is calming, almost soothing, but also deeply surreal."
        "You feel a strange mix of peace and anticipation, as if something is about to happen."
        "Suddenly, a figure materializes before you, slowly taking shape from the glowing mist."
        "At first, you see only the outline—large, graceful wings that stretch out behind her, glistening with a thousand tiny, sparkling lights."
        "As she steps forward, the details come into focus: feline ears perched atop her head, a fluffy tail swaying gently behind her, and eyes that are deep and knowing, with an otherworldly glow."
        "It's an angel, but not any ordinary one—a neko angel, her presence both powerful and serene."
        "She radiates an aura of gentle authority, her voice soft but commanding, as if each word is woven from the threads of a dream."
        "Angel Neko" "With a gentle smile, her voice carrying a soothing echo. \"Welcome to the new world, chosen one. You may have left your previous life behind, but here, your desires can be fulfilled.\""
        "Her smile is kind, yet mysterious, as if she knows more about you than you do yourself."
        "Angel Neko" "\"You said you wanted to rule the world, didn't you? In this world, I will grant you the power to shape your destiny, to become what you've always dreamed of.\""
        "She lifts her hand, and you feel a rush of warmth flood through your body, like fire and light intermingling, awakening a power deep within you that you never knew existed. The energy is electrifying, filling you with a sense of purpose, of infinite possibility."
        "Angel Neko" "\"Go forth, and may you find what you seek in this new life. Good luck on your journey, and remember—this world is yours to conquer.\""
        jump isekai_beginning


label isekai_beginning:
    "The radiant space around you begins to shift and warp, solidifying into a new landscape—a world unknown yet brimming with potential."
    "You feel the ground beneath your feet, the air rich with the scent of unfamiliar flowers, the sky above vast and unending."
    "Your adventure has just begun, and the choices you make will shape everything to come."
    "..."







label unknown_1:
    ". . ."

label end_of_story:
    ". . ."