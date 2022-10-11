# W04-Hilo
This is a simple game of hilo, where you guess what the next card will be! Here is how the game is played:
The dealer draws and displays a card. Then, you guess if the next card drawn will be higher or lower than the current one.
The dealer draws and displays another card. If your guess is correct, you earn 100 points. Otherwise, you lose 75 points.
If you reach 0 points, the game is over.

## Getting Started
---
Make sure you have Python 3.8.0 or newer installed and running on your machine. Open a terminal and 
browse to the project's root folder. Start the program by running the following command.
```
py hilo
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the hilo folder and click the "run" button.

## Game Design
---
Object: Director                      

Responsibility:                         
- to control the sequence of play       
                                        
Behaviors:                    
- play game         
- track score       
- draw card                                        
- end game                        

---
Object: Player                        

Responsibility:                         
- to keep track of guess and points     
                                        
                                        
Behaviors:          
- guess higher or lower                            
- increase points if correct            
- decrease points if correct            
- keep track of score 

---
Object: Card                      

Responsibility:                         
- to keep track of which card is drawn       
                                        
Behaviors:                    
- draw card from deck          

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder) ("W04-HILO")
+-- hilo                (source code for game) ("hilo")
  +-- game              (specific classes) ("game")
  +-- director          (class)
  +-- player            (class)
  +-- card              (class)
  +-- __main__.py       (program entry point) ("__main__.py")
+-- README.md           (general info)
```

## Required Technologies
---
* Python 3.8.0

## Authors
---
* Kim Watson (wat22013@byui.edu)