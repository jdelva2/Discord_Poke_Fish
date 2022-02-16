# INTRODUCTION:

Discord Pokemon is a text to play game which is based on the Pokemon games. Players may be able to use certain commands to 
explore and catch pokemon. This small project was created to help a friend up their fishing game!

This small project specifically allows a user to automate their experience in the game by catching pokemon automatically
for you while fishing. Using API request calls we can send certain text commands to play for us! This saves the player time and prevents them
them from losing an opportunity on an important pokemon catch!


# CODE BUGS:

Possible bugs may display multiple casting if the bot is playing by itself or with too many people.
The message list may need to be adjusted to be more or less depending on active players sending messages.
Changing parameters will depend on number of players active.

           CHART  
   Players  |  Messages(~Line 55) |  
   1 (bot)  |         6           |  
     2      |         26          |  
     3      |         51          |  
     4      |         76          |     


Another feature that was in the process of being added was the BIG_FISH event which would have the bot wait until another new message appears.
This was added within the conditional check but allowed the program to "pass".
