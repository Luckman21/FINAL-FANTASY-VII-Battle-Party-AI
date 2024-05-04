Luckman21

FINAL FANTASY VII AI Battles

The purpose of this project is for fun and learning.  My goal is to make a functional AI that can make the right decisions during
battles and (hopefully) complete a full run of the game.  This project implements the following skills I'll need to pull this off:

- Multithreading
- Reading from other processes' memory addresses
- Text from image processing
- Keyboard input generation and key monitoring
- Interface for the AI to interact with the game
- AI model to learn and make decisions

Multithreading will be crucial for a few things.  1.) Creating general application features like a kill-switch, battle toggle and more.
2.) Managing the actions of each party member seperately (one thread for each party member).  3.) Creating another thread to manage the
party, which will tie into the AI and future decision making, similar to an orchestrator.

By reading from other processes' memory, I can grab exact values of HP, MP and other status effects of both the party and enemies,
allowing the AI to extract information that is both visible and hidden from the player.  This will go a long way in helping the AI create
more complex and meaningful decisions.

Keyboard input generation will allow me to send commands to the game (as I'm playing on PC) like Attack, Magic, Summon, etc.  
By monitoring keyboard inputs, I can pause / start the battle algorithm and typing functions.  This way keys and battle functions 
won't be spammed during battle.  

Text from image processing will allow me to take battle UI elements like names and other features that are difficult to read from memory.

Creting an interface for the AI model to use will allow me to train the AI while letting it interact with the game. 
The interface creates "hotkey" functions I've defined to automate certain inputs (like moving around the menu to select a command).
This way, the AI model can focus on battle strategy rather than figuring out how to input commands.

The AI model will be the biggest and most complex part of the project.  Choosing which model and implementing it will be challenging.
I will update the README with more information when I have more information on the AI model I'm using and my implementation.