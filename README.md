Luckman21

FINAL FANTASY VII AI Battles

The purpose of this project is for fun and learning.  My goal is to make a functional AI that can make the right decisions during
battles and (hopefully) complete a full run of the game.  This project implements the following skills I'll need to pull this off:

- Keyboard input generation
- Keyboard key monitoring
- Text from image processing
- Interface for the AI to interact with the game
- AI model to learn and make decisions

Keyboard input generation will allow me to send commands to the game (as I'm playing on PC) like Attack, Magic, Summon, etc.

By monitoring keyboard inputs, I can pause / start the battle algorithm and typing functions.  This way keys and battle functions 
won't be spammed during battle.  

Text from image processing will allow me to take battle UI elements and read values like health, MP and more.  This information
will be critical to helping the AI model learn.

Creting an interface for the AI model to use will allow me to train the AI while letting it interact with the game. 
The interface creates "hotkey" functions I've defined to automate certain inputs (like moving around the menu to select a command).
This way, the AI model can focus on battle strategy rather than figuring out how to input commands.

The AI model will be the biggest and most complex part of the project.  Choosing which model and implementing it will be challenging.
I will update the README with more information when I have more information on the AI model I'm using and my implementation.