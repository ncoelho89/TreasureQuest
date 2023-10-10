print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome young adventurer.")
print("Your mission is to find the treasure in Minerva Dungeon.") 
print("You will be given a series of choices to make.")
print("Please type in your choice.")
print("Good luck!")
start = input("Type the word 'start' to begin your jounrney into the dungeon\n").lower()
if start == "start":
  print("You begin your descent and walk for what seems like hours.")
  print("You arrive at a rectangular well lit room with a terrifyingly ominous door")
  print("You can feel your skin crawl at the thought of going any further")
else: 
  print("You decide to leave")

choice1 = input("Do you choose to 'continue' or 'turn back'?\n").lower()
if choice1 == "continue":
  print("You decide to push forward despite the ominous presence...")
  print("You arrive at a circular room with 2 doors. You see rats scurrying around.")
  print("A loud scream echoes through your mind, unsure if you imagined it or not.")
else: 
  print("You decide to leave and return to the safety of your home")

choice2 = input("Do you choose the door on the 'right' or the 'left'?\n").lower()
if choice2 == "right":
  print("You decide to go through the door on the right")
  print("You hear a loud roar and see a flash of fire erupt from the darkness.")
  print("You dodge the fireball and avoid taking any damage.")
  print("The room begins to glow from ancient glyphs on the wall.")
  print("That's when you notice a DRAGON!!!")
  print("A red scaled dragon floats before you with a dark knight riding on it's back.")
  print('''                        /\
                        ||
                        ||
                        ||
                        ||                                               ~-----~
                        ||                                            /===--  ---~~~
                        ||                   ;'                 /==~- --   -    ---~~~
                        ||                (/ ('              /=----         ~~_  --(  '
                        ||             ' / ;'             /=----               \__~
     '                ~==_=~          '('             ~-~~      ~~~~        ~~~--\~'
     \\                (c_\_        .i.             /~--    ~~~--   -~     (     '
      `\               (}| /       / : \           / ~~------~     ~~\   (
      \ '               ||/ \      |===|          /~/             ~~~ \ \(
      ``~\              ~~\  )~.~_ >._.< _~-~     |`_          ~~-~     )\
       '-~                 {  /  ) \___/ (   \   |` ` _       ~~         '
       \ -~\                -<__/  -   -  L~ -;   \\    \ _ _/
       `` ~~=\                  {    :    }\ ,\    ||   _ :(
        \  ~~=\__                \ _/ \_ /  )  } _//   ( `|'
        ``    , ~\--~=\           \     /  / _/ / '    (   '
         \`    } ~ ~~ -~=\   _~_  / \ / \ )^ ( // :_  / '
         |    ,          _~-'   '~~__-_  / - |/     \ (
          \  ,_--_     _/              \_'---', -~ .   \
           )/      /\ / /\   ,~,         \__ _}     \_  "~_
           ,      { ( _ )'} ~ - \_    ~\  (-:-)       "\   ~ 
                  /'' ''  )~ \~_ ~\   )->  \ :|    _,       " 
                 (\  _/)''} | \~_ ~  /~(   | :)   /          }
                <``  >;,,/  )= \~__ {{{ '  \ =(  ,   ,       ;
               {o_o }_/     |v  '~__  _    )-v|  "  :       ,"
               {/"\_)       {_/'  \~__ ~\_ \\_} '  {        /~\
               ,/!          '_/    '~__ _-~ \_' :  '      ,"  ~ 
              (''`                  /,'~___~    | /     ,"  \ ~' 
             '/, )                 (-)  '~____~";     ,"     , }
           /,')                    / \         /  ,~-"       '~'
       (  ''/                     / ( '       /  /          '~'
    ~ ~  ,, /) ,                 (/( \)      ( -)          /~'
  (  ~~ )`  ~}                   '  \)'     _/ /           ~'
 { |) /`,--.(  }'                    '     (  /          /~'
(` ~ ( c|~~| `}   )                        '/:\         ,'
 ~ )/``) )) '|),                          (/ | \)                 -sjm
  (` (-~(( `~`'  )                        ' (/ '
   `~'    )'`')                              ''')

else:
  print("You choose the door on the left and walk through cautiously...")
  print("All seems well until you hear the turning of gears in the distance")
  print("By the time you realize, it is too late to react.")
  print("A trap door opens and you plummet to your death")
  print("GAME OVER")

choice3 = input("Do you 'Attack', 'Run', or 'Do nothing'?\n").lower()
if choice3 == "run":
  print("The knight commands the dragon to blast you with fire as you turn around")
  print("You try to dodge, but the blast is too large... and you burn to death")
  print("Game Over")
elif choice3 == "attack":
  print("The Dark Knight laughs at your measly attacks")
  print("The Knight dismounts and thrusts his lances through your chest")
  print("Unable to speak as you gasp for air, the Knight takes your head in one swing")
  print("You are puzzled that you can see your body from...without a head")
  print("You try to scream but your vision fade to darkness")
  print("Game Over")
elif choice3 == "do nothing":
  print("You decide to do nothing")
  print("The knight looks at you and senses you are pure of heart")
  print("The knight lets you pass into the single door behind him")
  print("Cautious as you pass, but true to his word, you make it to the next room")
  print("You safely enter the room and see two large treasure chests")

choice4 = input("Open chest on the 'right' or 'left'\n").lower()
if choice4 == "left":
  print("You receive an enchanted sword and shield")
  print("As you turn to leave a portal opens underneath you")
  print("You fall in and are teleported to another dimension")
  print("To be continued")
elif choice4== "right":
  print("You recieve millions worth of jewels and gold")
  print("You blink in disbelief and find yourself at the entrance of the dungeon")
  print("With your treasure in hand you hold your head high and head to the town")
  print("You get back and pay off your loans and hit the strip club with the boys!")
  

