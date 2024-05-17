# CS110 Project 
  
CS110 Final Project Spring, 2024

## Team Members

Sam Lin

## Project Description

A three stage 2D pixel base street fighter game that you would see in a aracade back in the day. The game has a somewhat well design starter menu that allows the player to either begin the game or exit the application, the start menu also a volume slider that has a sword which can be slide to the left to decrease the volume of the music or to the right to increase it. After the entering the game there is a two second countdown before player drop to the ground and began the battle.


## GUI Design

### Initial Design
![initial gui]("assets/Inital_GUI.jpg")

### Final Design
![final gui]("assets/Final_GUI.png")

## Program Design
### Features
     1. Change maps every round (up to three rounds)
     2. Moveable character, which runs turn there body based on the direct they run.
     3. Health Bar that track damage taken
     4. Internal systems to track scores and a winner's screen that appears after the match
     5. Ingame sound-track, that can be lower or raised in the starter menu

### Classes 

 Evil Wizard: magic type character that is operated with the arrow keys and have it's basic attack as "numpad keys 1" and "numpad key 2"

 Warrior: physical type character that has it's movement set as "wasd" and attacks as "r" and "t"

## ATP

### Test Case 1: Character Movement
Test Description: Verify that the character's movement is as expected.
    Test Steps:
    1. Press the Spacebar to test the jump feature
    2. Watch the character fall for any animation issue
    3. Verify that the character moves left.
    4. Verify that the character moves right.
Expected Outcome: The players should move left and right in response to the arrow key inputs for player two and “wasd” for player one.


### Test Case 2: Collision Detection
Test Description: Ensure collisions between the player's attacks are detected correctly.
     Test Steps:
     1. Start the game.
     2. Fire primary attack 
     3. Verify that the opposite player received damage
     4. Fire secondary attack 
     5. Verify that the opposite player received damage
     6. Fire an attack away from the enemy
     7. Verify that no collision is detected.
Expected Outcome: The attack should connect and reduce the health of the target.

### Test Case 3: Game Over Condition
Test Description: Confirm that the game ends after one of the two players wins three rounds.
     Test Steps:
     1. Start the game.
     2. Play until the player loses all lives.
     3. Verify that the game displays a "Winner Winner" message.
Expected Outcome: The game should display a "Winner Winner" message after the opposite player loses all three turns

#### Test Case 4: Music and In-Game Audio
Test Description: Test the soundtrack and In-Game Audio to ensure they are functional.
     Test Steps:
     1. Start the game.
     2. Listen to the in-game music.
     3. Verify the soundtrack can be heard.
     4. Perform basic attacks for both characters.
     5. Verify that each character's basic attack leads to an audio output.
     6. Perform secondary attacks for both characters.
     7. Verify that each character's secondary attack leads to an audio output.
Expected Outcome: The game should have three major audio tracks, one of which is the main soundtrack, which can be heard throughout the game. The second is the melee swing for player one’s basic and secondary attack, and lastly, the magic sound effect for player 2.

### Test Case 5: Error Handling
Test Description: Verify that the program handles unexpected inputs gracefully.
     Test Steps:
     1. Start the game.
     2. Enter inputs during gameplay.
     3. Verify that the program does not crash and displays appropriate error messages.
     4. Press either “a” or “d” key and move the character to in-game boundaries.
     5. Verify that the character stays with in the boundaries and does not move off the visible screen.
Expected Outcome: The program should handle unexpected inputs without crashing.
