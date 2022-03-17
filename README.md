# Othello-board game

Othello is a strategy board game for two players, played on an 8×8 uncheckered board.

Basics:
There are sixty-four identical game pieces called disks (often spelled "discs"), which are light on one side and dark on the other. 
Players take turns placing disks on the board with their assigned color facing up. 
During a play, any disks of the opponent's color that are in a straight line and bounded by the disk just placed and another disk of the current player's color are turned over to the current player's color. The objective of the game is to have the majority of disks turned to display one's color when the last playable empty square is filled.

Strategies applied: 
First, it checks if any disk could be placed in one of the corners. A second option would be to check the exterior frame of the board, but to avoid the frame of the corners in case the diagonal isn't conquered by the computer (to not risk losing the corner). The third option applied is to remain in the central 4x4 board and not extend more. If there still isn't a possible move until now, it checks if there is any valid move to make except the inner-exterior frame (because of that move, the computer could lose the exterior frame which turns most of the disks). If there is a valid move which is not in the innner-exterior frame it positions a disk there, otherwise it chooses any move even if it is on the inner-exterior frame. If no move is possible at all, the computer has to skip its turn and the user's turn is next. 

