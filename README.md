Luckman21

# FINAL FANTASY VII AI Battles 

> [!NOTE]
> This project is still a W.I.P., not all features are implemented.

***

### Purpose

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

***

### Setup

In order to set up this system, you will need the following:[^1]
- [ ] A computer with Windows OS installed powerful enough to run FFVII and Python simlutaneously
- [ ] A copy of FINAL FANTASY VII (Steam version) installed
- [ ] Python 3.9.10 or newer (older versions may work but are not tested)
    - [ ] The following libraries installed:
        - [ ] pymem
        - [ ] PIL
        - [ ] pyautogui
        - [ ] pytesseract
        - [ ] pyscreenshot
        - [ ] keyboard

[^1]: More setup instructions will be provided when the project is closer to completion.

***

### Resources

Some helpful resources I found along the way!

- [Extract Text From Images in Python (OCR)](https://youtu.be/PY_N1XdFp4w?si=VLq-9ABWQJEfXxbV "YouTube Tutorial Link")
- [Basic Writing and Formatting Syntax for GitHub README](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax, "Link to GitHub Guide")
- [Writing GitHub README](https://medium.com/analytics-vidhya/writing-github-readme-e593f278a796 "Web Tutorial Link")

***

![GitHub all releases](https://img.shields.io/github/downloads/{luckman21}/{FINAL-FANTASY-VII-Battle-Party-AI}/total)
![GitHub language count](https://img.shields.io/github/languages/count/{luckman21}/{FINAL-FANTASY-VII-Battle-Party-AI})
![GitHub top language](https://img.shields.io/github/languages/top/{luckman21}/{FINAL-FANTASY-VII-Battle-Party-AI}?color=yellow)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/{luckman21}/{FINAL-FANTASY-VII-Battle-Party-AI})
![GitHub forks](https://img.shields.io/github/forks/{luckman21}/{FINAL-FANTASY-VII-Battle-Party-AI}?style=social)
![GitHub Repo stars](https://img.shields.io/github/stars/{luckman21}/{FINAL-FANTASY-VII-Battle-Party-AI}?style=social)