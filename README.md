# Ultimate_File_Duplicator

This program can be used to duplicate a file or folder so that it applies to all characters in Smash Ultimate. The main function 
is to copy animation files such as taunts, but includes some functionality for other things as well. It was made to work on 
windows, so some syntax may need to be changed to allow it to work in a Linux environment, since it uses command line prompts.


## HOW TO USE:

### DUPLICATING ANIMATION FILE(s):

Place the file(s) you would like to duplicate directly into the "input" folder. Then run "Ultimate_File_Duplicator.exe". 
When it is done, look inside your "output" folder. There should be another folder called "My_Mod", which you can then 
place in your "mods" folder on your SD card and rename it to whatever you like!

This will work with multiple input files, but be aware that they will all be placed in the same My_Mod folder.
    
### DUPLICATING OTHER FILE(s):

(Before trying this method please note that unlike animation files, most other files such as Voices and UI have names 
that are character specific. This won't work on other characters without also being renamed, which this program cannot do 
as of right now, so you will need to rename them manually after being copied.) 
        
Place the file(s) you would like to duplicate into a tree branching from the <character name> folder, and put that in the
"input" folder. For example, if you for wanted to duplicate the "model.nuhlpb" file to the 0th slot of all 
characters, your input would have to contain a folder that looks like this: model\body\c00\model.nuhlpb. Then run 	
"Ultimate_File_duplicator.exe:. When it is done, look inside your "output" folder. There should be another folder called 
"My_Mod", which you can then place in your "mods" folder on your SD card if done correctly, and rename it to whatever 
you like!

This will work with multiple input files, but be aware that they will all be placed in the same My_Mod folder.

### CHANGING WHICH SLOTS/CHARACTERS FILES ARE DUPLICATED TO:

If you would like to exclude certain characters and/or slots from having your files duplicated onto, you can go into the
lib\default_empty_taunt_folders directory and remove/change any folders that you don't want the files to be duplicated to.

## FINAL NOTES:

I hope at least some people find this tool useful! It started out as a personal tool to automate the process of duplicating 
taunts onto all characters, but I figured I might as well get some experience in releasing programs to the public. I plan to 
expand on this program sometime in the future, including learning how to make a GUI and implementing additional features.
And if you're wondering about the .placeholder files, they're only here because GitHub doesn't keep track of empty folders,
so you can delete once they're on your computer if needed. The program will also delete them itself, except for the empty
character folders since I'm lazy lol.

I would also appreciate any feedback on issues or things I should change. This program is not perfect and could definitely be 
optimized further, and may have issues that I missed. If you find anything let me know at either my Gamebanana (https://
gamebanana.com/members/2085889) or GitHub Project Page (https://github.com/Tever725/Ultimate_File_Duplicator). Thanks!

Feel free to create modify your own version of this program if there is anything you would like to change about it. Credit would 
be appreciated if you upload anything that uses it as well!
