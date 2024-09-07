# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define sun = Character("Sun")
define player = Character("player")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    call OpeningNarrative from _call_OpeningNarrative

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    sun "So… there's something I should probably tell you. It’s… a bit strange."

    "She hesitates for a second, glancing away as if gathering courage, then looks back at you."

    sun "I'm… um, I’m actually a neko. A cat girl."

    """She lowers her gaze, clearly anxious about your reaction.
 
    Her hands grip the menu a little tighter, her ears twitching nervously.

    You can see the faintest hint of her tail curling slightly around her chair,

    a reflex she’s trying to suppress."""

    sun "I know it's… unusual. And I understand if you want to end the date here. But… I hope you won't."

    menu:
        "accept":
            call acceptance from _call_acceptance
        "reject":
            call rejection from _call_rejection

    sun "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return

label OpeningNarrative:
    """It’s a late Saturday afternoon, and the sun hangs low in the sky, casting a golden glow over the small, bustling city. 
    
    You’re seated at an outdoor table of a charming, quaint café nestled on a quiet corner street.
    
    The air is cool but comfortable, with a gentle breeze that rustles the leaves of the nearby trees, 
    
    carrying with it the mingled scents of freshly brewed coffee, warm pastries, 
    
    and the subtle hint of lavender from the potted plants surrounding the tables."""

    """It's early evening, and the sun is beginning to dip below the horizon,
 
    painting the sky in shades of orange, pink, and purple.

    The warmth of the day is slowly giving way to a cooler,

    crisper air that brushes against your skin, a reminder that nightfall is near.

    The café’s overhead lights turn on, casting a soft, amber glow that mixes with the fading daylight,

    creating an almost magical atmosphere."""

    """
    Across from you sits the girl you met on OkCupid.

    She seems nervous, her eyes darting around before finally settling back on you.

    Her hands fidget with the menu, her fingers brushing against the edges in a distracted manner.

    She’s dressed simply, yet there’s a quiet elegance to her—a white blouse,

    a light blue skirt, and a small, silver necklace that catches the light when she moves.

    Her ears, slightly pointed with soft, delicate fur, twitch every now and then,

    as if sensing the world around her. You notice her tail is tucked slightly to the side,

    hidden but still, it sways ever so slightly with her mood.
    """

    """
    She looks down for a moment, taking a deep breath, then meets your eyes with a shy smile.

    Her cheeks are faintly flushed, whether from the cool air or her nerves, you can't quite tell.

    When she speaks, her voice is soft, almost hesitant.
    """
    return

label rejection:
    """You take a deep breath and shake your head slowly.

    Her face falls, her ears droop, and her tail curls around her legs like a protective shield.

    She bites her lip, nodding to herself, as if accepting your decision even though it stings.

    """

    sun "I… I understand. Thank you for being honest."

    """
    She stands up, her movements slow and deliberate,
 
    and she gives you one last, lingering look before turning away.
 
    You watch as she walks down the street, her figure growing smaller
 
    and smaller until she’s gone from sight.
    """

    """
        The café feels quieter now, the warmth from earlier replaced with a chill that seems to seep into your bones.
     
        You’re left sitting alone at the table,

        the soft sounds of the city continuing around you.
    """
    return

label acceptance:
    "You smile reassuringly, leaning forward slightly to meet her gaze."

    player "I don’t mind at all. In fact, I’m glad you told me."

    """
    Her eyes widen, and for a moment, she looks like she can’t quite believe what you said.

    Then, slowly, her expression brightens. Her ears perk up, and her tail, which had been tucked away,

    begins to sway with a newfound energy.
    """

    sun "Surprised and exhilarated. \"Really? You mean it?\""
    return


