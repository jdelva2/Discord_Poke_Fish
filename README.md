## INTRODUCTION:

Discord Pokemon is a text to play game which is based on the Pokemon games. Players may be able to use certain commands to 
explore and catch pokemon. This small project was created to help a friend up their fishing game!

This small NLP project specifically allows a user to automate their experience in the game by catching pokemon automatically
for you while fishing. Using API request calls we can send certain text commands to play for us! This saves the player time and prevents them
them from losing an opportunity on an important pokemon catch!


## Minor bugs:

Possible bugs may display multiple casting if the bot is playing by itself or with multiple people.
The message list may need to be adjusted to be more or less depending on active players sending messages.
Changing parameters will depend on number of players active.

i.e if the bot is playing solo, the number of messages that it checks will be lower ~6 
if there are around 5-6 people actively playing the number might need to be increase to around 120.


Another feature that was in the process of being added was the BIG_FISH event which would have the bot wait until another new message appears. This was added within the conditional check but allowed the program to "pass".
It is a rare event which does not happen often however part of the fix will be to include this. For now the bot is able to catch common event items, pokemon and recasts reel if the line broke.

