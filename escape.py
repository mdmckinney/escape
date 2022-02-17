#######################################################################
#                              ESCAPE                                 #
#######################################################################
# Michael D. McKinney
# January 14, 2021
# (Updated February 16, 2022 - bug/grammar fixes and improving code.)
# A simple text adventure game to showcase elements of a text adventure
# game such as movement, inventory, game states, clearing of screen,  
# debugging/debug mode, etc.
# There are five rooms in this text adventure.
#
# I have tried to anticipate everything a player could type in the game 
# and developed a response for each inputs.
#

#######################################################################
#            IMPORTING STUFF FOR CLEAR SCREEN FUNCTION                #
#######################################################################
from os import system, name 

#######################################################################
#                            INVENTORY                                #
#######################################################################
inventory = []

#######################################################################
#                            GAME STATES                              #
#######################################################################
# roomid - 1-5 (1 = Center Room, 2 = East Room, 3 = West Room, 
# 4 = South Room, and 5 = North Room.)
# northdoor, southdoor, eastdoor, westdoor - 0 (locked) or 1 (unlocked).
# silverbox, goldenbox and irongate - 0 (locked) or 1 (unlocked/open)
# northaccesspanel - 0 (closed) or 1 (open)
# southaccesspanel - 0 (closed/locked), 1 (closed/unlocked) or 2 (open)
# deadplant and planter - 0 (still intact) or 1 (crumbled)
# flashlight - 0 (off) or 1 (on)
# flashlight batteries - 0 (not inserted) or 1 (inserted)
# escaped - 0 (not escaped) or 1 (escaped)
game_states = {"roomid": 1, "northdoor": 0, "southdoor": 0, "eastdoor": 1, 
"westdoor": 0, "blackbox": 0, "northaccesspanel": 0, "silverbox": 0, 
"southaccesspanel": 1, "deadplant": 0, "planter": 0, "flashlight": 0, 
"flashlightbatteries": 0, "goldenbox": 0, "irongate": 0, "escaped": 0}

#######################################################################
#                        CLEAR SCEEN FUNCTION                         #
#######################################################################
def clear(): 
  
    # Windows
    if name == 'nt': 
        _ = system('cls') 
  
    # Mac and Linux 
    else: 
        _ = system('clear') 


#######################################################################
#                            CENTER ROOM                              #
#######################################################################
def centerroom():
	clear()
	print("\t\t-----------------------------------------------")
	print("\n\t\t\t\t CENTER ROOM\n")
	print("\t\t-----------------------------------------------")
	print("\n\n\nYou're in the center room.")
	game_states["roomid"] = 1

	### SET THE COLOR OF DOOR LIGHTS      ### 
	### (RED = LOCKED, GREEN = UNLOCKED.) ###
	if game_states["northdoor"] == 0:
		print("The light above the door in the north is red.")
	if game_states["northdoor"] == 1:
		print("The light above the door in the north is green.")		
	if game_states["southdoor"] == 0:
		print("The light above the door in the south is red.")
	if game_states["southdoor"] == 1:
		print("The light above the door in the south is green.")	
	if game_states["eastdoor"] == 0:
		print("The light above the door in the east is red.")
	if game_states["eastdoor"] == 1:
		print("The light above the door in the east is green.")	
	if game_states["westdoor"] == 0:
		print("The light above the door in the west is red.")
	if game_states["westdoor"] == 1:
		print("The light above the door in the west is green.")

	### MAIN SECTION OF THE CENTER ROOM FUNCTION ###															
	while True:

		### WAITING ON PLAYER'S INPUT ###
		player_input = input("\n> ")
		player_input = player_input.strip()
		player_input = player_input.lower()

		### NORTH / SOUTH / EAST / WEST ###
		if player_input == 'n' or player_input == 'north':
			if game_states["northdoor"] == 0:
				print("The north door is locked.")
				continue
			if game_states["northdoor"] == 1:
				northroom()	
		if player_input == 's' or player_input == 'south':
			if game_states["southdoor"] == 0:
				print("The south door is locked.")
				continue
			if game_states["southdoor"] == 1:
				southroom()	
		if player_input == 'e' or player_input == 'east':
			if game_states["eastdoor"] == 0:
				print("The east door is locked.")
				continue
			if game_states["eastdoor"] == 1:
				eastroom()	
		if player_input == 'w' or player_input == 'west':
			if game_states["westdoor"] == 0:
				print("The west door is locked.")
				continue
			if game_states["westdoor"] == 1:
				westroom()			

		### LOOK / LOOK ROOM ###
		if (player_input == 'look' or 
		    player_input == 'look room'):
			print("The walls, doors, ceiling, and floor are metal.")
			print("There is a light source on the ceiling.")
			print("It looks like a very bright LED embedded in the ceiling.")
			print("There are four doors here, with a light above it.")
			if game_states["northdoor"] == 0:
					print("The light above the door in the north is red.")
			if game_states["northdoor"] == 1:
					print("The light above the door in the north is green.")		
			if game_states["southdoor"] == 0:
					print("The light above the door in the south is red.")
			if game_states["southdoor"] == 1:
					print("The light above the door in the south is green.")	
			if game_states["eastdoor"] == 0:
					print("The light above the door in the east is red.")
			if game_states["eastdoor"] == 1:
					print("The light above the door in the east is green.")	
			if game_states["westdoor"] == 0:
					print("The light above the door in the west is red.")
			if game_states["westdoor"] == 1:
					print("The light above the door in the west is green.")	
			if game_states["flashlight"] == 1:
				print("Light is shining from the flashlight.")							
			continue				

		## LOOK DOOR LIGHT / LOOK LIGHT ABOVE DOOR ###
		if (player_input == 'look door light' or 
			player_input == 'look light above door'):
			print("The light is an indicator of the status of the door.")
			print("Red is locked and green is unlocked.")
			if game_states["northdoor"] == 0:
					print("The light above the door in the north is red.")
			if game_states["northdoor"] == 1:
					print("The light above the door in the north is green.")		
			if game_states["southdoor"] == 0:
					print("The light above the door in the south is red.")
			if game_states["southdoor"] == 1:
					print("The light above the door in the south is green.")	
			if game_states["eastdoor"] == 0:
					print("The light above the door in the east is red.")
			if game_states["eastdoor"] == 1:
					print("The light above the door in the east is green.")	
			if game_states["westdoor"] == 0:
					print("The light above the door in the west is red.")
			if game_states["westdoor"] == 1:
					print("The light above the door in the west is green.")			
			continue		

		### LOOK LIGHT ###
		if player_input == 'look light':
			print("There is a light source on the ceiling.")
			print("It looks like a very bright LED embedded in the ceiling.")				
			print("The light above the door is an indicator of the status of "
				  "the door.")
			print("Red is locked and green is unlocked.")
			if game_states["northdoor"] == 0:
					print("The light above the door in the north is red.")
			if game_states["northdoor"] == 1:
					print("The light above the door in the north is green.")		
			if game_states["southdoor"] == 0:
					print("The light above the door in the south is red.")
			if game_states["southdoor"] == 1:
					print("The light above the door in the south is green.")	
			if game_states["eastdoor"] == 0:
					print("The light above the door in the east is red.")
			if game_states["eastdoor"] == 1:
					print("The light above the door in the east is green.")	
			if game_states["westdoor"] == 0:
					print("The light above the door in the west is red.")
			if game_states["westdoor"] == 1:
					print("The light above the door in the west is green.")						
			if game_states["flashlight"] == 1:
				print("Light is shining from the flashlight.")
			continue

		### INPUT HANLDER ### 
		### (FOR ANY INPUT THAT IS DESIGNED TO WORK IN MULTIPLE ROOMS) ###
		else:
			inputhandler(player_input)
			continue

#######################################################################
#                             EAST ROOM                               #
#######################################################################
def eastroom():
	clear()
	print("\t\t-----------------------------------------------")
	print("\n\t\t\t\t EAST ROOM\n")
	print("\t\t-----------------------------------------------")
	print("\n\n\nYou're in the east room.")
	game_states["roomid"] = 2

    ### LOCKS THE DOOR AS SOON AS THE PLAYER ENTERS THE ROOM ###
	game_states["eastdoor"] = 0
	print("As soon as the door behind you closes, the light above the door "
		  "turns red.")

	### LIGHT ABOVE THE DOOR.  (RED IS LOCKED, GREEN IS UNLOCKED.) ###
	if game_states["eastdoor"] == 0:
			print("The light above the door in the west is red.")				
	if game_states["eastdoor"] == 1:
			print("The light above the door in the west is green.")	

	### BLACK BOX - SILVER KEY INSIDE THE BOX ###
	if game_states["blackbox"] == 0:
			print("There is a black box on the floor in center of the "
				  "room.")
			print("The lid on the black box is closed.")		
	if game_states["blackbox"] == 1:
			print("There is a black box on the floor in center of the "
				  "room.")
			print("The lid on the black box is closed.")
	if game_states["blackbox"] == 2 and "silver key" not in inventory:
			print("There is a black box on the floor in center of the "
				  "room.")
			print("The lid on the black box is open.")	
			print("There is a silver key inside the black box.")
	if game_states["blackbox"] == 2 and "silver key" in inventory:
			print("There is a black box on the floor in center of the "
				  "room.")
			print("The lid on the black box is open.")	
			print("The black box is empty.")

	### PAPER - COVERING THE YELLOW SWITCH - UNLOCKS DOOR EAST DOOR. ###
	if "paper" not in inventory:
			print("There is a paper on the floor in the southeast corner.")		
	if "paper" in inventory:
			print("There is a yellow switch on floor in the southeast corner.")			

	### GREEN SWITCH - UNLOCKS NORTH DOOR ###
	print("There is a green switch on the north wall.")		


	### MAIN SECTION OF THE EAST ROOM FUNCTION ###																
	while True:

		### WAITING ON PLAYER'S INPUT ###
		player_input = input("\n> ")
		player_input = player_input.strip()
		player_input = player_input.lower()

		### NORTH / SOUTH / EAST / WEST ###
		if player_input == 'n' or player_input == 'north':
			print("There's no route north from here.")
		if player_input == 's' or player_input == 'south':
			print("There's no route south from here.")
		if player_input == 'e' or player_input == 'east':
			print("There's no route east from here.")
		if player_input == 'w' or player_input == 'west':
			if game_states["eastdoor"] == 0:
				print("The door is locked.")
				continue
			if game_states["eastdoor"] == 1:
				centerroom()			

		### LOOK / LOOK ROOM ###
		if (player_input == 'look' or 
			player_input == 'look room'):
			print("The walls, door, ceiling, and floor are metal.")
			print("There is a light source on the ceiling.")
			print("It looks like a very bright LED embedded in the ceiling.")
			print("There is a door in the west.")	
			if game_states["eastdoor"] == 0:
				print("The light above the door is red.")
			if game_states["eastdoor"] == 1:
				print("The light above the door is green.")	
			print("There is a green switch on the north wall.")
			if "paper" not in inventory:
				print("There is a paper on the floor in southeast corner.")
			if "paper" in inventory:
				print("There is a yellow switch on the floor in southeast "
					  "corner.")				
			print("There is a black box in the center of the room.")
			print("The black box looks like it's made out of obsidian.")
			if game_states["blackbox"] == 0 or game_states["blackbox"] == 1:
				print("The black box is currently closed.")	
			if game_states["blackbox"] == 2:
				print("The black box is currently open.")	
				if "silver key" not in inventory:
					print("There is a silver key inside the black box.")
				if "silver key" in inventory:
					print("The black box is empty.")
			if game_states["flashlight"] == 1:
				print("Light is shining from the flashlight.")					
			continue		

		### LOOK DOOR LIGHT / LOOK LIGHT ABOVE DOOR ###
		if (player_input == 'look door light' or 
			player_input == 'look light above door'):
			print("The light is an indicator of the status of the door.")
			print("Red is locked and green is unlocked.")
			if game_states["eastdoor"] == 0:
					print("The light above the door in the west is red.")
			if game_states["eastdoor"] == 1:
					print("The light above the door in the west is green.")			
			continue				

		### LOOK LIGHT ###
		if player_input == 'look light':
			print("There is a light source on the ceiling.")
			print("It looks like a very bright LED embedded in the ceiling.")			
			print("The light above the door is an indicator of the status of "
			      "the door.")
			print("Red is locked and green is unlocked.")	
			if game_states["eastdoor"] == 0:
					print("The light above the door in the west is red.")
			if game_states["eastdoor"] == 1:
					print("The light above the door in the west is green.")				
			if game_states["flashlight"] == 1:
				print("Light is shining from the flashlight.")
			continue				

		### SWITCHES ###
		if (player_input == 'look switch' or 
			player_input == 'look switches'):
			print("Green switch on the wall is a push button switch the size "
				  "of a quarter.")
			if "paper" in inventory:
					print("Yellow switch on the floor is a pressure plate "
						  "switch the size of a dollar bill.")		
			continue		

		# Green switch - Unlocks North Door.
		if (player_input == 'look green' or 
			player_input == 'look green switch'):
			print("Green switch on the wall is a push button switch the size "
				  "of a quarter.")		
			continue							

		if ((player_input == 'press green switch' or 
			player_input == 'push green switch' or
			player_input == 'press green' or
			player_input == 'push green') and 
			(game_states["northdoor"] == 0 and game_states["blackbox"] != 2)):
			print("You press the green switch.")
			game_states["northdoor"] = 1
			continue

		if ((player_input == 'press green switch' or 
			player_input == 'push green switch' or
			player_input == 'press green' or
			player_input == 'push green') and 
			(game_states["northdoor"] == 1 and game_states["blackbox"] != 2)):
			print("You press the green switch.")
			game_states["northdoor"] = 0
			continue	

		if ((player_input == 'press green switch' or 
			player_input == 'push green switch' or
			player_input == 'press green' or
			player_input == 'push green') and 
			(game_states["northdoor"] == 1 and game_states["blackbox"] == 2)):
			print("You press the green switch.")
			game_states["northdoor"] = 0
			continue		

		if ((player_input == 'press green switch' or 
			player_input == 'push green switch' or
			player_input == 'press green' or
			player_input == 'push green') and 
			(game_states["northdoor"] == 0 and game_states["blackbox"] == 2)):
			print("You press the green switch.")
			game_states["northdoor"] = 0
			continue					

		if ((player_input == 'take green switch' or 
			player_input == 'take green switch' or
			player_input == 'take green' or
			player_input == 'take green')):
			print("Green switch is securely affixed to the wall.  You "
			  "can't take it.")
			continue						

		# Yellow Switch - Unlocks East door.  Initially covered by paper.
		if (player_input == 'look yellow' or 
			player_input == 'look yellow switch'):
			if "paper" not in inventory:
					print("You don't see any yellow switch here.")
			if "paper" in inventory:
					print("Yellow switch on the floor is a pressure plate "
						  "switch the size of a dollar bill.")		
			continue		

		if ((player_input == 'press yellow switch' or 
			player_input == 'push yellow switch' or
			player_input == 'press yellow' or
			player_input == 'push yellow') and 
		    "paper" not in inventory):
			print("You don't see any yellow switch here.")
			continue			

		if (((player_input == 'press yellow switch' or 
			player_input == 'push yellow switch' or
			player_input == 'press yellow' or
			player_input == 'push yellow') and 
			game_states["eastdoor"] == 0) and "paper" in inventory):
			print("You press the yellow switch.")
			print("\nThe light above the door in the west is now green.")
			game_states["eastdoor"] = 1
			continue			

		if (((player_input == 'press yellow switch' or 
			player_input == 'push yellow switch' or
			player_input == 'press yellow' or
			player_input == 'push yellow') and 
			game_states["eastdoor"] == 1) and "paper" in inventory):
			print("You press the yellow switch.")
			print("\nThe light above the door in the west is now red.")
			game_states["eastdoor"] = 0		
			continue

		if ((player_input == 'take yellow switch' or 
			player_input == 'take yellow switch' or
			player_input == 'take yellow') and 
		    "paper" not in inventory):
			print("You don't see any yellow switch here.")
			continue					

		if ((player_input == 'take yellow switch' or 
			player_input == 'take yellow switch' or
			player_input == 'take yellow' or
			player_input == 'take yellow') and 
		    "paper" in inventory):
			print("Yellow switch is securely affixed to the floor.  You "
			      "can't take it.")
			continue													

		### BLACK BOX ###
		if ((player_input == 'look box' or 
			   player_input == 'look black box') and
			(game_states["blackbox"] == 0 or 
			 game_states["blackbox"] == 1)):
			print("The black box looks like it's made out of obsidian.")
			print("The black box is currently closed.")
			print("You can't see any keyhole on it.")
			continue

		if ((player_input == 'look box' or 
			   player_input == 'look black box') and
			  (game_states["blackbox"] == 2)):
			print("The black box looks like it's made out of obsidian.")
			print("The black box is currently open.")
			print("You can't see any keyhole on it.")
			if "silver key" not in inventory:
				print("There is a silver key inside the black box.")
			if "silver key" in inventory:
				print("The black box is empty.")
			continue					

		if ((player_input == 'open box' or 
			player_input == 'open black box') and
			game_states["blackbox"] == 0):
			print("The black box is securely locked.  You can't open it.")
			continue	

		if ((player_input == 'open box' or 
			player_input == 'open black box') and
			game_states["blackbox"] == 1):
			print("You open the black box.")
			game_states["blackbox"] = 2
			game_states["northdoor"] = 0
			game_states["southdoor"] = 0
			game_states["westdoor"] = 1
			if "silver key" not in inventory:
				print("There is a silver key inside the black box.")	
			if "silver key" in inventory:
				print("The black box is empty.")		
			continue		

		if ((player_input == 'open box' or 
			player_input == 'open black box') and
			game_states["blackbox"] == 2):
			print("The black box is already open.")
			continue		

		if ((player_input == 'close box' or 
			player_input == 'close black box') and
			game_states["blackbox"] == 2):
			print("You close the black box.")
			game_states["blackbox"] = 1
			game_states["northdoor"] = 0
			game_states["southdoor"] = 1
			game_states["westdoor"] = 0			
			continue		

		if ((player_input == 'close box' or 
			player_input == 'close black box') and
			(game_states["blackbox"] == 1 or game_states["blackbox" == 0])):
			print("The black box is already closed.")		
			continue	

		if (player_input == 'take box' or player_input == 'take black box'):
			print("The black box seems be part of the floor.")  
			print("It is impossible to lift it off the floor.")	
			continue				

		### PAPER ###
		if player_input == 'take paper' and "paper" not in inventory:
			print("Taken.")
			print("\nThe paper was covering a yellow switch.")
			inventory.append("paper")
			continue			

		if ((player_input == 'look paper') and
			"paper" not in inventory):
			print("You'll need to take the paper before looking at it.")
			continue			

		### SILVER KEY ###
		if ((player_input == 'take silver key' or 
			 player_input == 'take key') and 
			"silver key" not in inventory and 
			game_states["blackbox"] == 2):
			print("Taken.")
			inventory.append("silver key")
			continue			

		if (((player_input == 'take silver key' or 
			  player_input == 'look silver key') and 
			"silver key" not in inventory) and 
			(game_states["blackbox"] == 0 or game_states["blackbox"] == 1)):
			print("You don't see any silver key here.")
			continue				

		if ((player_input == 'take silver key' or 
			 player_input == 'take key') and
			("silver key" in inventory)):
			print("You already took the silver key.")
			continue						

		if (((player_input == 'take key' or 
			  player_input == 'look key') and 
			"silver key" not in inventory) and 
			(game_states["blackbox"] == 0 or game_states["blackbox"] == 1)):
			print("You don't see any key here.")
			continue					

		if ((player_input == 'look silver key' or 
			 player_input == 'look key') and
			("silver key" not in inventory and game_states["blackbox"] == 2)):
			print("You'll need to take the silver key before looking at it.")
			continue									

		### INPUT HANLDER ### 
		### (FOR ANY INPUT THAT IS DESIGNED TO WORK IN MULTIPLE ROOMS)
		else:
			inputhandler(player_input)
			continue							

#######################################################################
#                             WEST ROOM                               #
#######################################################################
def westroom():
	clear()
	print("\t\t-----------------------------------------------")
	print("\n\t\t\t\t WEST ROOM\n")
	print("\t\t-----------------------------------------------")
	print("\n\n\nYou're in the west room.")
	game_states["roomid"] = 3

	### FLASHLIGHT OFF - ROOM PITCH BLACK ###
	### IF GOLDEN BOX IS CLOSED AND FLASHLIGHT IS OFF THEN DOOR IS UNLOCKED ### 
	if game_states["flashlight"] == 0 and game_states["goldenbox"] == 1: 
		print("It's pitch black in here.")
		print("The only source of light is a dim red light above the door in "
			  "the east.")

	### FLASHLIGHT OFF - ROOM PITCH BLACK ###
	### IF GOLDEN BOX IS OPEN AND FLASHLIGHT IS OFF THEN DOOR IS LOCKED ###
	if game_states["flashlight"] == 0 and game_states["goldenbox"] == 0: 
		print("It's pitch black in here.")
		print("The only source of light is a dim green light above the door in "
			  "the east.")		

	### FLASHLIGHT ON - ROOM NOT PITCH BLACK ###
	### IF FLASHLIGHT IS ON THEN DOOR IS LOCKED REGARDLESS OF STATUS OF BOX ###
	if game_states["flashlight"] == 1: 
		print("Your flashlight is illuminating the room.")
		print("The light above the door in the east is red.")
		print("There is a sensor on the ceiling.")
		print("There is a golden box on the floor in center of the room.")
		if game_states["goldenbox"] == 0:
			print("The golden box is closed.")
		if game_states["goldenbox"] == 1:
			print("The golden box is open.")
		print("On the golden box is a keyhole.")	

	### MAIN SECTION OF THE WEST ROOM FUNCTION ###	
	while True:

		### IF OPEN IS BOX AND FLASHLIGHT IS ON - DOOR IS LOCKED ###
		if game_states["goldenbox"] == 1 or game_states["flashlight"] == 1:
		   game_states["westdoor"] = 0

		### IF OPEN IS CLOSED AND FLASHLIGHT IS OFF - DOOR IS UNLOCKED ###
		if game_states["goldenbox"] == 0 and game_states["flashlight"] == 0:
		   game_states["westdoor"] = 1				

		### WAITING ON PLAYER'S INPUT ###
		player_input = input("\n> ")
		player_input = player_input.strip()
		player_input = player_input.lower()

		### FLASHLIGHT IS OFF - ROOM IS PITCH BLACK ###
		if game_states["flashlight"] == 0: 

			### NORTH / SOUTH / EAST / WEST ###
			if player_input == 'n' or player_input == 'north':
				print("It's too dark to see if there's any route north.")
				continue
			if player_input == 's' or player_input == 'south':
				print("It's too dark to see if there's any route south.")
				continue
			if player_input == 'e' or player_input == 'east':
				if game_states["westdoor"] == 0:
					print("The door is locked.")
					continue
				if game_states["westdoor"] == 1:
					centerroom()	
			if player_input == 'w' or player_input == 'west':
				print("It's too dark to see if there's any route west.")
				continue

			### LOOK / LOOK ROOM ###
			if player_input == 'look' or player_input == 'look room':
				print("It's too dark to see anything in the room.")
				print("It's pitch black in here.")
				if (game_states["flashlight"] == 0 and 
					game_states["goldenbox"] == 1): 
					print("The only source of light is a dim red light "
						  "above the door in the east.")
				if (game_states["flashlight"] == 0 and 
					game_states["goldenbox"] == 0): 
					print("The only source of light is a dim green light "
						  "above the door in the east.")				

			### FLASHLIGHT ###
			if ((player_input == "turn on flashlight" or 
				player_input == "turn flashlight on") and
				("flashlight" in inventory and
				game_states["flashlightbatteries"] == 0)):
				print("The flashlight is not turning on. There are no batteries"
					  " in it.")
				continue

			if ((player_input == "turn on flashlight" or 
				player_input == "turn flashlight on") and
				("flashlight" not in inventory)):
				print("What flashlight?")
				continue									

			if ((player_input == "turn on flashlight" or 
				player_input == "turn flashlight on") and
				("flashlight" in inventory and
				game_states["flashlightbatteries"] == 1)):
				print("You turn on the flashlight. The light is illuminating "
					  "the room.")
				print("The light above the door in the east is red.")			
				print("There is a golden box on the floor in center of "
					  "the room.")
				if game_states["goldenbox"] == 0:
					print("The golden box is closed.")
				if game_states["goldenbox"] == 1:
					print("The golden box is open.")	
				print("On the golden box is a keyhole.")
				print("You notice a sensor in the ceiling.")
				game_states["flashlight"] = 1
				continue	

			### QUIT THE GAME ###
			if player_input == 'q' or player_input == 'quit':
				end()		

			### DEBUG ###
			if player_input == 'debug':
				debug()					

			### DISABLE THE INPUT HANDLER WHEN ROOM IS PITCH BLACK ###
			else:
				print("It's too dark to do anything.")
				continue		


		### FLASHLIGHT IS ON ###
		if game_states["flashlight"] == 1:

			### NORTH / SOUTH / EAST / WEST ###
			if player_input == 'n' or player_input == 'north':
				print("There is no route north from here.")
				continue
			if player_input == 's' or player_input == 'south':
				print("There is no route south from here.")
				continue
			if player_input == 'e' or player_input == 'east':
				if game_states["westdoor"] == 0:
					print("The door is locked.")
					continue
				if game_states["westdoor"] == 1:
					centerroom()
			if player_input == 'w' or player_input == 'west':
				print("There is no route west from here.")
				continue

			### LOOK / LOOK ROOM ###
			if (player_input == 'look' or 
				player_input == 'look room'):
				print("The walls, door, ceiling, and floor are metal.")
				print("There is no light anywhere in the room except for the "
					  "light \nabove the door in the east and the flashlight.")
				print("There is a door to the east.")	
				if game_states["westdoor"] == 0:
					print("The light above the door in the east is red.")
				if game_states["westdoor"] == 1:
					print("The light above the door in the east is green.")				
				print("There is a golden box here in center of the room.")
				print("The golden box looks like it's made out of gold.")
				if game_states["blackbox"] == 0:
					print("The golden box is currently closed.")	
				if game_states["blackbox"] == 1:
					print("The golden box is currently open.")	
					if "iron key" not in inventory:
						print("There is an iron key inside the golden box.")
					if "iron key" in inventory:
						print("The golden box is empty.")	
				continue		

			### LOOK DOOR LIGHT ###
			if (player_input == 'look door light' or 
				player_input == 'look light above door'):
				print("The light is an indicator of the status of the door.")
				print("Red is locked and green is unlocked.")
				if game_states["westdoor"] == 0:
					print("The light above the door in the east is red.")
				if game_states["westdoor"] == 1:
					print("The light above the door in the east is green.")			
				continue					

			### LOOK LIGHT ###
			if player_input == 'look light':
				if game_states["roomid"] == 3:
					print("There is no light in this room except for the light "
						  "above the door in the east.")
					print("Your flashlight is the source of light in this "
						  "room.")				
				print("The light above the door is an indicator of the status "
					  "of the door.")
				print("Red is locked and green is unlocked.")
				if game_states["westdoor"] == 0:
					print("The light above the door in the east is red.")
				if game_states["westdoor"] == 1:
					print("The light above the door in the east is green.")		
				continue			

			### TAKE LIGHT ###
			if (player_input == 'take light'):
				print("There is no light in the room other than the light "
					  "above the door in the west.")
				continue								

			# TURNING FLASHLIGHT OFF ###
			if ((player_input == 'turn flashlight off' or 
				player_input == 'turn off flashlight' or
				player_input == 'turn light off' or
				player_input == 'turn off light')
				and ("flashlight" in inventory and 
				game_states["flashlightbatteries"] == 1)):
				print("You turn the flashlight off.")
				game_states["flashlight"] = 0	
				print("It's pitch black in here.")

				### IF GOLDEN BOX IS CLOSED, DOOR LIGHT IS RED ###
				if game_states["goldenbox"] == 1:
					print("The only source of light is a dim red light above "
						  "the door in the east.")
					continue

				### IF GOLDEN BOX IS CLOSED, DOOR LIGHT IS GREEN ###
				if game_states["goldenbox"] == 0:
					print("The only source of light is a dim green light above "
						  "the door in the east.")	
					continue				
				continue		

			### LOOK SENSOR / TAKE SENSOR ###
			if (player_input == 'look sensor'):
				print("A sensor the size of a dime is on the ceiling.")
				print("It seems to be detecting something.")
				continue	

			if (player_input == 'take sensor'):
				print("Sensor is securely affixed to the ceiling. You can't "
					  "take it.")
				continue						

			### GOLDEN BOX - OPEN / CLOSE / LOOK / TAKE / USE KEYS ###
			if ((player_input == 'use gold key on box' or 
				player_input == 'use gold key' or
				player_input == 'use gold key on golden box' or
				player_input == 'use gold key to open box' or
				player_input == 'use gold key to open gold box' or 
				player_input == 'open box with gold key' or
				player_input == 'open golden box with gold key' or
				player_input == 'unlock golden box using gold key' or
				player_input == 'unlock golden box with gold key' or	
				player_input == 'unlock box with gold key' or		
				player_input == 'open golden box using gold key' or
				player_input == 'open box with gold key' or
				player_input == 'open box using gold key'or
				player_input == 'open gold box using gold key' or
				player_input == 'open gold box with gold key') and	
				"gold key" in inventory and 
				game_states["goldenbox"] == 0):
				print("You insert the gold key into the keyhole on the "
					  "golden box.")
				print("It fits, and the golden box opens.")
				print("Inside the golden box there is an iron key.")	
				print("You take the gold key out of the keyhole.")
				game_states["goldenbox"] = 1
				continue			

			if ((player_input == 'use gold key on box' or 
				player_input == 'use gold key' or
				player_input == 'use gold key on golden box' or
				player_input == 'use gold key to open box' or
				player_input == 'use gold key to open gold box' or 
				player_input == 'open box with gold key' or
				player_input == 'open golden box with gold key' or
				player_input == 'unlock golden box using gold key' or
				player_input == 'unlock golden box with gold key' or	
				player_input == 'unlock box with gold key' or		
				player_input == 'open golden box using gold key' or
				player_input == 'open box with gold key' or
				player_input == 'open box using gold key'or
				player_input == 'open gold box using gold key' or
				player_input == 'open gold box with gold key') and	
				"gold key" not in inventory):
				print("What gold key?")	
				continue	

			if ((player_input == 'use gold key on box' or 
				player_input == 'use gold key' or
				player_input == 'use gold key on golden box' or
				player_input == 'use gold key to open box' or
				player_input == 'use gold key to open gold box' or 
				player_input == 'open box with gold key' or
				player_input == 'open golden box with gold key' or
				player_input == 'unlock golden box using gold key' or
				player_input == 'unlock golden box with gold key' or	
				player_input == 'unlock box with gold key' or		
				player_input == 'open golden box using gold key' or
				player_input == 'open box with gold key' or
				player_input == 'open box using gold key'or
				player_input == 'open gold box using gold key' or
				player_input == 'open gold box with gold key') and	
				"gold key" in inventory and 
				game_states["goldenbox"] == 1):
				print("The golden box is already unlocked and open.")
				continue					

			if ((player_input == 'use silver key on box' or 
				player_input == 'use silver key' or
				player_input == 'use silver key on golden box' or
				player_input == 'use silver key to open box' or
				player_input == 'use silver key to open gold box' or 
				player_input == 'open box with silver key' or
				player_input == 'open golden box with silver key' or
				player_input == 'unlock golden box using silver key' or
				player_input == 'unlock golden box with silver key' or	
				player_input == 'unlock box with silver key' or		
				player_input == 'open golden box using silver key' or
				player_input == 'open box with silver key' or
				player_input == 'open box using silver key'or
				player_input == 'open gold box using silver key' or
				player_input == 'open gold box with silver key') and	
				"silver key" in inventory):
				print("Silver key doesn't fit in the keyhole on the golden "
					  "box.")
				continue		

			if ((player_input == 'use silver key on box' or 
				player_input == 'use silver key' or
				player_input == 'use silver key on golden box' or
				player_input == 'use silver key to open box' or
				player_input == 'use silver key to open gold box' or 
				player_input == 'open box with silver key' or
				player_input == 'open golden box with silver key' or
				player_input == 'unlock golden box using silver key' or
				player_input == 'unlock golden box with silver key' or	
				player_input == 'unlock box with silver key' or		
				player_input == 'open golden box using silver key' or
				player_input == 'open box with silver key' or
				player_input == 'open box using silver key'or
				player_input == 'open gold box using silver key' or
				player_input == 'open gold box with silver key') and	
				"silver key" not in inventory):
				print("What silver key?")
				continue					

			if ((player_input == 'use iron key on box' or 
				player_input == 'use iron key' or
				player_input == 'use iron key on golden box' or
				player_input == 'use iron key to open box' or
				player_input == 'use iron key to open gold box' or 
				player_input == 'open box with iron key' or
				player_input == 'open golden box with iron key' or
				player_input == 'unlock golden box using iron key' or
				player_input == 'unlock golden box with iron key' or	
				player_input == 'unlock box with iron key' or		
				player_input == 'open golden box using iron key' or
				player_input == 'open box with iron key' or
				player_input == 'open box using iron key'or
				player_input == 'open gold box using iron key' or
				player_input == 'open gold box with iron key') and	
				"iron key" in inventory):
				print("Iron key doesn't fit in the keyhole on the golden "
					  "box.")
				continue	

			if ((player_input == 'use iron key on box' or 
				player_input == 'use iron key' or
				player_input == 'use iron key on golden box' or
				player_input == 'use iron key to open box' or
				player_input == 'use iron key to open gold box' or 
				player_input == 'open box with iron key' or
				player_input == 'open golden box with iron key' or
				player_input == 'unlock golden box using iron key' or
				player_input == 'unlock golden box with iron key' or	
				player_input == 'unlock box with iron key' or		
				player_input == 'open golden box using iron key' or
				player_input == 'open box with iron key' or
				player_input == 'open box using iron key'or
				player_input == 'open gold box using iron key' or
				player_input == 'open gold box with iron key') and	
				"iron key" not in inventory):
				print("What iron key?")
				continue														

			if ((player_input == 'open golden box' or 
				player_input == 'open box') and
				"gold key" not in inventory and 
				game_states["goldbox"] == 0):
				print("You can't open the golden box.  You don't have the "
					  "correct key to open it.")
				continue			

			if ((player_input == 'open golden box' or 
				player_input == 'open box') and
				game_states["goldenbox"] == 1):
				print("The golden box is already open.")
				continue						

			if ((player_input == 'close box' or 
				player_input == 'close golden box') and
				game_states["goldenbox"] == 1):
				print("You close the golden box.  Upon closing, it "
					  "automatically locks.")
				game_states["goldenbox"] = 0
				continue			

			if ((player_input == 'open box' or 
				   player_input == 'open box with key') and
				("silver key" in inventory or 
				 "gold key" in inventory or 
				 "iron key" in inventory) and 
				game_states["goldenbox"] == 0):
				print("Please specify which key to use to unlock the golden "
					  "box.")
				continue					

			if ((player_input == 'open box' or 
				player_input == 'open gold box' or
				player_input == 'open golden box') and
				game_states["goldenbox"] == 0):
				print("The gold box is securely locked. You will need a key "
					  "to unlock it.")
				continue				

			if ((player_input == 'close box' or 
				player_input == 'close golden box' or 
				player_input == 'close gold box') and
				game_states["goldenbox"] == 1):
				print("You close the golden box. Upon closing, it automatically"
					  " locks.")
				game_states["goldenbox"] = 0		
				continue

			if ((player_input == 'close box' or 
				player_input == 'close golden box' or 
				player_input == 'close gold box') and
				game_states["goldenbox"] == 0):
				print("The golden box is already closed.")		
				continue		

			if ((player_input == 'look box' or 
				 player_input == 'look gold box') and
				(game_states["goldenbox"] == 0)):
				print("The golden box looks like it's made out of gold. "
					  "It currently is closed.")
				print("There is a keyhole on a side.")
				continue

			if ((player_input == 'look box' or 
				 player_input == 'look gold box') and
				(game_states["goldenbox"] == 1)):
				print("The golden box looks like it's made out of gold. "
					  "It currently is open.")
				print("There is a keyhole on a side.")
				if "iron key" not in inventory:
					print("There is an iron key inside the golden box.")
				if "iron key" in inventory:
					print("The golden box is empty.")
				continue							
						
			if (player_input == 'take box' or 
				player_input == 'take golden box'):
				print("The golden box seems be part of the floor.")
				print("It is impossible to lift it off the floor.")	
				continue						

			### IRON KEY ###
			if ((player_input == 'take iron key' or
				 player_input == 'take key') and
				"iron key" not in inventory and 
				game_states["goldenbox"] == 1):
				print("Taken.")
				inventory.append("iron key")
				continue

			if ((player_input == 'take iron key' or 
				 player_input == 'take key') and
				"iron key" in inventory):
				print("You already took the iron key.")	
				continue					

			if ((player_input == 'take iron key') and
				"iron key" not in inventory and 
				game_states["goldenbox"] == 0):
				print("You don't see any iron key here.")		
				continue			

			if ((player_input == 'take key') and
				"iron key" not in inventory and 
				game_states["goldenbox"] == 0):
				print("You don't see any key here.")		
				continue					
							
		### INPUT HANLDER ### 
		### (FOR ANY INPUT THAT IS DESIGNED TO WORK IN MULTIPLE ROOMS)
			else:
				inputhandler(player_input)
				continue			


#######################################################################
#                            SOUTH ROOM                               #
#######################################################################
def southroom():
	clear()
	print("\t\t-----------------------------------------------")
	print("\n\t\t\t\t SOUTH ROOM\n")
	print("\t\t-----------------------------------------------")
	print("\n\n\nYou're in the south room.")
	game_states["roomid"] = 4

	print("It's quite messy in here.")

	### DOOR LIGHT STATE ###	      	 	
	if game_states["southdoor"] == 0:
			print("The light above the door in the north is red.")
	if game_states["southdoor"] == 1:
			print("The light above the door in the north is green.")	

	### METAL ACCESS PANEL ###
	if (game_states["southaccesspanel"] == 0 or 
		game_states["southaccesspanel"] == 1):
		print("There is a metal access panel on the west wall. It is currently "
		      "closed.")	
	if game_states["southaccesspanel"] == 2:
		print("There is a metal access panel on the west wall. It is currently "
		      "open.")
		print("You can see a blue switch and a red switch.")

	### ITEMS IN THE ROOM ###
	print("Several large gears are stacked in the northeast corner.")					      	
	print("Springs of varying sizes are scattered everywhere in the room.")
	print("Rubbish are piled up in the southwest corner.")

	### DEAD PLANT INSIDE PLANTER ###
	### IF PLANTER IS CRUMBLED - DEAD PLANT IMMEDIATELY CRUMBLES ###
	if game_states["deadplant"] == 0 and game_states["planter"] == 0:
		print("A large planter with a dead and decaying plant is in "
			  "southeast corner.")

	if game_states["deadplant"] == 1 and game_states["planter"] == 0:
		print("A large planter with a pile of dust on it is in "
			  "southeast corner.")

	### STATE OF THE PLANTER AND THE GOLD KEY INSIDE PLANTER ###
	if game_states["planter"] == 1 and "gold key" not in inventory:
		print("There is a pile of dirt is in southeast corner.")
		print("A gold key is partially buried in the pile of dirt.")	

	if game_states["planter"] == 1 and "gold key" in inventory:
		print("There is a pile of dirt is in southeast corner.")		


	### MAIN SECTION OF THE SOUTH ROOM FUNCTION ###															
	while True:

		### WAITING ON PLAYER'S INPUT ###
		player_input = input("\n> ")
		player_input = player_input.strip()
		player_input = player_input.lower()

		### NORTH / SOUTH / EAST / WEST ###
		if player_input == 'n' or player_input == 'north':
			if game_states["southdoor"] == 0:
				print("The door is locked.")
				continue
			if game_states["southdoor"] == 1:
				centerroom()
		if player_input == 's' or player_input == 'south':
			print("There's no route south from here.")
			continue
		if player_input == 'e' or player_input == 'east':
			print("There's no route east from here.")
			continue
		if player_input == 'w' or player_input == 'west':
			print("There's no route west from here.")		
			continue		

		### LOOK / LOOK ROOM ###
		if (player_input == 'look' or 
			player_input == 'look room'):
			print("It's quite messy in here.")			
			print("The walls, door, ceiling, and floor are metal.")
			print("There is a light source on the ceiling.")
			print("It looks like a very bright LED embedded in the ceiling.")
			print("There is a door in the north.")	
			if game_states["southdoor"] == 0:
				print("The light above the door is red.")
			if game_states["southdoor"] == 1:
				print("The light above the door is green.")				
			if game_states["planter"] == 0 and game_states["deadplant"] == 0:
				print("There is a planter in southeast corner with a dead plant"
				      " in it.")
			if game_states["planter"] == 0 and game_states["deadplant"] == 1:
				print("There is a planter in southeast corner with a pile of "
					  "dust in it.")					
			if game_states["planter"] == 1:
				print("There is a pile of dirt in southeast corner.")					
				if "gold key" not in inventory:
					print("A gold key is partially buried in pile of dirt.")
			print("There is a pile of rubbish in southwest corner.")
			print("Gears are stacked in northeast corner.")
			print("Springs are scattered all over the room.")
			print("There is a metal access panel on the west wall.")
			if (game_states["southaccesspanel"] == 0 or 
				game_states["southaccesspanel"] == 1):
				print("The access panel is currently closed.")
			if (game_states["southaccesspanel"] == 2):
				print("The access panel is currently open.")	
				print("You can see red and blue switches in the access "
			    	  "panel.")
			if game_states["flashlight"] == 1:
				print("Light is shining from the flashlight.")				
			continue	

		### DOOR LIGHT / LOOK LIGHT ABOVE DOOR ###
		if (player_input == 'look door light' or 
			player_input == 'look light above door'):
			print("The light is an indicator of the status of the door.")
			print("Red is locked and green is unlocked.")
			if game_states["southdoor"] == 0:
					print("The light above the door in the north is red.")
			if game_states["southdoor"] == 1:
					print("The light above the door in the north is green.")			
			continue				

		### LOOK LIGHT ###
		if player_input == 'look light':
			print("There is a light source on the ceiling.")
			print("It looks like a very bright LED embedded in the ceiling.")		
			print("The light above the door is an indicator of the status of "
				  "the door.")
			print("Red is locked and green is unlocked.")
			if game_states["southdoor"] == 0:
				print("The light above the door in the north is red.")
			if game_states["southdoor"] == 1:
				print("The light above the door in the north is green.")	
			if game_states["flashlight"] == 1:
				print("Light is shining from the flashlight.")
			continue						

		### ACCESS PANEL ###	  			
		if ((player_input == 'open access panel' or 
			player_input == 'open metal access panel' or
			player_input == 'open panel' or
			player_input == 'open access') and 
			game_states["southaccesspanel"] == 1):
			game_states["southaccesspanel"] = 2
			game_states["southdoor"] = 0
			print("Opening the metal access panel reveals two switches.")
			print("You can see a red switch here.")
			print("You can see a blue switch here.")	
			print("The light above the door in the north is now red.")
			continue		

		if ((player_input == 'open access panel' or 
			player_input == 'open metal access panel' or
			player_input == 'open panel' or
			player_input == 'open access') and 
			game_states["southaccesspanel"] == 2):	
			print("It's already open.")
			continue	

		if ((player_input == 'open access panel' or 
			player_input == 'open metal access panel' or
			player_input == 'open panel' or
			player_input == 'open access') and 
			game_states["southaccesspanel"] == 0):	
			print("It's securely locked.")
			continue				

		if ((player_input == 'close access panel' or 
			player_input == 'close metal access panel' or
			player_input == 'close panel' or
			player_input == 'close access') and 
			game_states["southaccesspanel"] == 2):
			game_states["southaccesspanel"] = 1
			game_states["southdoor"] = 1
			print("You close the metal access panel.")	
			print("The light above the door in the north is now green.")
			continue			

		if ((player_input == 'close access panel' or 
			player_input == 'close metal access panel' or
			player_input == 'close panel' or
			player_input == 'close access') and 
			(game_states["southaccesspanel"] == 1 or
			game_states["southaccesspanel"] == 0)):	
			print("It's already closed.")
			continue				

		if ((player_input == 'look metal access panel' or 
			 player_input == 'look look metal panel' or
			 player_input == 'look metal access' or
		     player_input == 'look access panel' or
		     player_input == 'look panel') and
			(game_states["southaccesspanel"] == 0 or 
			 game_states["southaccesspanel"] == 1)):
			print("It's a metal access panel. It's currently closed.")
			continue

		if ((player_input == 'look metal access panel' or 
			 player_input == 'look look metal panel' or
			 player_input == 'look metal access' or
			 player_input == 'look access panel' or
			 player_input == 'look panel') and
			(game_states["southaccesspanel"] == 2)):
			print("It's a metal access panel. It's currently open.")
			print("You can see red and blue switches in the access panel.")
			continue					

		### SWITCHES ###
		if (player_input == 'look switch' or 
			player_input == 'look switches'):
			if "southaccesspanel" == 2:
				print("Inside the access panel are red and blue switches.")	
				print("Both red and blue switches are square push button "
					  "switch the size of a dime.")	
			if "southaccesspanel" == 0 or "southaccesspanel" == 1:
				print("I don't see any switch here.")
			continue		

		if (player_input == 'look red' or 
			player_input == 'look red switch'):
			if "southaccesspanel" == 2:
				print("Red switch inside the access panel is a square push "
					  "button switch the size of a dime.")	
			if "southaccesspanel" == 0 or "southaccesspanel" == 1:
				print("I don't see any red switch here.")				 	  	
			continue			

		if (player_input == 'look blue' or 
			player_input == 'look blue switch'):
			if "southaccesspanel" == 2:
				print("Blue switch inside the access panel is a square push "
					  "button switch the size of a dime.")	
			if "southaccesspanel" == 0 or "southaccesspanel" == 1:
				print("I don't see any blue switch here.")				 	  	
			continue	

		if (((player_input == 'press blue switch' or 
			player_input == 'push blue switch' or
			player_input == 'press blue' or
			player_input == 'push blue') and 
			game_states["southaccesspanel"] == 2) and 
			game_states["eastdoor"] == 0):
			print("You press the blue switch.")
			game_states["eastdoor"] = 1
			continue	

		if (((player_input == 'press blue switch' or 
			player_input == 'push blue switch' or
			player_input == 'press blue' or
			player_input == 'push blue') and 
			game_states["southaccesspanel"] == 2) and 
			game_states["eastdoor"] == 1):
			print("You press the blue switch.")
			game_states["eastdoor"] = 0
			continue	

		if ((player_input == 'press blue switch' or 
			player_input == 'push blue switch' or
			player_input == 'press blue' or
			player_input == 'push blue') and 
			(game_states["southaccesspanel"] == 0 or 
			game_states["southaccesspanel"] == 1)):
			print("What blue switch?")
			continue			

		if (((player_input == 'press red switch' or 
			player_input == 'push red switch' or
			player_input == 'press red' or
			player_input == 'push red') and 
			game_states["southaccesspanel"] == 2) and 
			game_states["blackbox"] == 0):
			print("You press the red switch.")
			game_states["blackbox"] = 1
			continue	

		if (((player_input == 'press red switch' or 
			player_input == 'push red switch' or
			player_input == 'press red' or
			player_input == 'push red') and 
			game_states["southaccesspanel"] == 2) and 
			game_states["blackbox"] == 1):
			print("You press the red switch.")
			game_states["blackbox"] = 0
			continue

		if ((player_input == 'press red switch' or 
			player_input == 'push red switch' or
			player_input == 'press red' or
			player_input == 'push red') and
			(game_states["southaccesspanel"] == 0 or 
			game_states["southaccesspanel"] == 1)):
			print("What red switch?")
			continue			

		if ((player_input == 'take red switch' or 
			player_input == 'take red') and 
			game_states["southaccesspanel"] == 2):
			print("Red switch is securely affixed to inside of the panel. You "
			      "can't take it.")
			continue			

		if ((player_input == 'take red switch' or 
			player_input == 'take red') and 
			(game_states["southaccesspanel"] == 0 or 
			game_states["southaccesspanel"] == 1)):
			print("What red switch?")
			continue					

		if ((player_input == 'take blue switch' or 
			player_input == 'take blue') and 
			game_states["southaccesspanel"] == 2):
			print("Blue switch is securely affixed to inside of the panel. "
				  "You can't take it.")
			continue					

		if ((player_input == 'take blue switch' or 
			 player_input == 'take blue') and 
			(game_states["southaccesspanel"] == 0 or 
			 game_states["southaccesspanel"] == 1)):
			print("What blue switch?")
			continue																												

		### RUBBISH / PILE OF RUBBISH ###
		if (player_input == 'look rubbish' or
			player_input == 'look pile of rubbish' or
			player_input == 'look pile rubbish'):
			print("It's a pile of rubbish.")
			continue		

		if ((player_input == 'take rubbish' or 
			 player_input == 'move rubbish' or
			 player_input == 'search rubbish' or
			 player_input == 'take pile of rubbish' or
			 player_input == 'take pile rubbish' or
			 player_input == 'take rubbish pile' or
			 player_input == 'search pile of rubbish' or
			 player_input == 'search rubbish pile') and 
			 "flashlight" not in inventory):
			print("You decide to search the pile of rubbish.")
			print("After a few minutes of searching, you find a flashlight.")
			print("You take the flashlight.")
			inventory.append("flashlight")			
			continue			

		if ((player_input == 'take rubbish' or 
			 player_input == 'move rubbish' or
			 player_input == 'search rubbish' or
			 player_input == 'take pile of rubbish' or
			 player_input == 'take pile rubbish' or
			 player_input == 'take rubbish pile' or
			 player_input == 'search pile of rubbish' or
			 player_input == 'search rubbish pile') and 
			 "flashlight" in inventory):
			print("You decide to search the pile of rubbish.")
			print("After a few minutes of searching, you haven't found anything"
			      " useful.")			
			continue				

		### PLANTER ###
		if (player_input == 'look planter' or 
			player_input == 'look large planter'):
			print("It's a large planter. It is broken and beginning to "
				  "crumble.")
			continue		

		if ((player_input == 'take planter' or 
			player_input == 'take large planter') and 
			game_states["planter"] == 0):
			print("You try to move the planter.")
			print("Since it is already crumbling, it readily collapses and "
				  "crumbles into \na pile of dirt.")
			print("There is a gold key partially buried in the pile of dirt.")
			game_states["deadplant"] = 1
			game_states["planter"] = 1
			continue			

		if ((player_input == 'take planter' or 
			player_input == 'take large planter') and 
			game_states["planter"] == 1):
			print("The planter is just a pile of dirt now.  You can't take it.")
			continue			

		### PILE OF DIRT / DIRT ###
		if ((player_input == 'take dirt' or 
			player_input == 'take pile of dirt' or
			player_input == 'take dirt pile' or
			player_input == 'take pile dirt') and 
			game_states["planter"] == 1):
			print("You can't take it.")
			continue		

		if ((player_input == 'take dirt' or 
			player_input == 'take pile of dirt' or
			player_input == 'take dirt pile' or
			player_input == 'take pile dirt') and 
			game_states["planter"] == 0):
			print("What pile of dirt?")
			continue		

		if ((player_input == 'look dirt' or 
			player_input == 'look pile of dirt' or
			player_input == 'look dirt pile' or
			player_input == 'look pile dirt') and 
			game_states["planter"] == 0):
			print("You don't see any pile of dirt.")
			continue	

		if ((player_input == 'look dirt' or 
			player_input == 'look pile of dirt' or
			player_input == 'look dirt pile' or
			player_input == 'look pile dirt') and 
			game_states["planter"] == 1):
			print("It's a pile of dried soil.")
			continue														

		### DEAD PLANT ###
		if (player_input == 'look plant'):
			print("It's a long-dead plant.")
			continue		

		if ((player_input == 'take plant' or 
			player_input == 'take dead plant' or
			player_input == 'take decaying plant' or
			player_input == 'take dead and decaying plant') and 
			game_states["deadplant"] == 0):
			print("As soon as you touch it, the plant crumbles into a pile "
				  "of dust.")
			game_states["deadplant"] = 1
			continue				

		if ((player_input == 'take plant' or 
			player_input == 'take dead plant' or
			player_input == 'take decaying plant' or
			player_input == 'take dead and decaying plant') and 
			game_states["deadplant"] == 1):
			print("It's just a pile of dust now.  You can't take it.")
			continue			

		### PILE OF DUST / DUST ###
		if ((player_input == 'take dust' or 
			player_input == 'take pile of dust' or
			player_input == 'take dust pile' or
			player_input == 'take pile dust') and 
			game_states["deadplant"] == 0):
			print("What pile of dust?")
			continue		

		if ((player_input == 'take dust' or 
			player_input == 'take pile of dust' or
			player_input == 'take dust pile' or
			player_input == 'take pile dust') and 
			game_states["deadplant"] == 1):
			print("You can't take them.  They're too fine to take ahold of.")
			continue		

		if ((player_input == 'look dust' or 
			player_input == 'look pile of dust' or
			player_input == 'look dust pile' or
			player_input == 'look pile dust') and 
			game_states["deadplant"] == 1):
			print("It's a dead plant that had crumbled into a pile of dust.")
			continue	

		if ((player_input == 'look dust' or 
			player_input == 'look pile of dust' or
			player_input == 'look dust pile' or
			player_input == 'look pile dust') and 
			game_states["deadplant"] == 0):
			print("You don't see any pile of dust.")
			continue				

		### GOLD KEY ###
		if ((player_input == 'take gold key' or 
			player_input == 'take key') and 
			("gold key" not in inventory and game_states["planter"] == 1)):
			print("Taken.")
			inventory.append("gold key")
			continue										

		if ((player_input == 'take gold key') and 
			("gold key" not in inventory and game_states["planter"] == 0)):
			print("What gold key?")
			continue		

		if ((player_input == 'take key') and 
			("gold key" not in inventory and game_states["planter"] == 0)):
			print("What key?")
			continue			

		if ((player_input == 'take gold key' or 
			player_input == 'take key') and
			("gold key" in inventory)):
			print("You already took the gold key.")
			continue											

		if ((player_input == 'look gold key' or 
			player_input == 'look key') and
			("gold key" not in inventory and game_states["planter"] == 1)):
			print("You'll need to take the gold key before looking at it.")
			continue																																

		### GEARS ###
		if (player_input == 'take gears' or 
			player_input == 'take large gears'):
			print("You try to lift one of gears, but they're too heavy. You "
			      "can't take them.")
			continue	

		if (player_input == 'look gears' or
			player_input == 'look large gears'):
			print("Large and heavy-looking rusting gears are stacked up in a "
				  "corner.")
			print("You're not sure if you'll be able to lift one.")			
			continue					

		### SPRINGS ###
		if (player_input == 'take springs'):
			print("You try to take some, but they're heavily rusted and "
				  "crumbled in your hand. \nYou can't take them.")
			continue			

		if (player_input == 'look springs'):
			print("Springs of varying sizes are scattered all over the room. "
				  "\nThey're severely rusted.")
			continue	

		### INPUT HANLDER ### 
		### (FOR ANY INPUT THAT IS DESIGNED TO WORK IN MULTIPLE ROOMS)
		else:
			inputhandler(player_input)
			continue		

#######################################################################
#                            NORTH ROOM                               #
#######################################################################
def northroom():
	clear()
	print("\t\t-----------------------------------------------")
	print("\n\t\t\t\t NORTH ROOM\n")
	print("\t\t-----------------------------------------------")
	print("\n\n\nYou're in the north room.")
	game_states["roomid"] = 5

	### LOCK THE EAST DOOR AS SOON AS PLAYER ENTERS NORTH ROOM. ###
	print("Upon entering the room, you stepped on a pressure switch on the "
		  "floor.")
	game_states["eastdoor"] = 0

	### DOOR LIGHT STATE ###	
	if game_states["northdoor"] == 0:
			print("The light above the door in the south is red.")
	if game_states["northdoor"] == 1:
			print("The light above the door in the south is green.")		

	### PASSAGE TO THE EXIT ###
	print("You can see the passage to the exit in the north.")
	print("There is an impassable thick iron gate blocking the passage.")
	print("There is a keyhole on the iron gate.")

	### ACCESS PANEL STATUS ###	
	if game_states["northaccesspanel"] == 0:
		print("There is a metal access panel on the west wall.  It is currently"
		      " closed.")	
	if game_states["northaccesspanel"] == 1:
		print("There is a metal access panel on the west wall.  It is currently"
		      " open.  You can see gray and white switches.")	

	### SILVER BOX STATUS ###	      	 
	if game_states["silverbox"] == 0:
		print("There is a silver box on the floor in center of the room.")
		print("The silver box is currently closed.")
		print("There is a keyhole on a side of the silver box.")	
	if game_states["silverbox"] == 1 and "batteries" not in inventory:
		print("There is a silver box on the floor in center of the room.")
		print("The silver box is currently open.")
		print("There are several batteries inside the silver box.")
		print("There is a keyhole on a side of the silver box.")	

	if game_states["silverbox"] == 1 and "batteries" in inventory:
		print("There is a silver box on the floor in center of the room.")
		print("The silver box is currently open.")
		print("The silver box is empty.")
		print("There is a keyhole on a side of the silver box.")			

	### MAIN SECTION OF THE NORTH ROOM FUNCTION ###	  															
	while True:

		### WAITING ON PLAYER'S INPUT ###
		player_input = input("\n> ")
		player_input = player_input.strip()
		player_input = player_input.lower()

		### NORTH / SOUTH / EAST / WEST ###
		if ((player_input == 'n' or
                     player_input == 'north' or
                     player_input == 'open gate') and 
			game_states["irongate"] == 0):
			print("The iron gate is locked.")
			continue
		if ((player_input == 'n' or
                     player_input == 'north' or
                     player_input == 'open gate') and 
			game_states["irongate"] == 1):
			game_states["escaped"] = 1
			end()			
		if player_input == 's' or player_input == 'south':
			if game_states["northdoor"] == 0:
				print("The door is locked.")
				continue
			if game_states["northdoor"] == 1:
				centerroom()
		if player_input == 'e' or player_input == 'east':
			print("There's no route east from here.")
			continue
		if player_input == 'w' or player_input == 'west':
			print("There's no route west from here.")	
			continue		

		### LOOK PASSAGE / LOOK GATE ###
		if (player_input == 'look passage' or 
			player_input == 'look gate'):
			print("Peering through the iron gate and squinting to see beyond "
				  "the passage, \nyou can see blue sky and grassy meadows.")	
			continue					

		### LOOK / LOOK ROOM ###
		if (player_input == 'look' or 
			player_input == 'look room'):		
			print("The walls, door, ceiling, and floor are metal.")
			print("There is a light source on the ceiling.")
			print("It looks like a very bright LED embedded in the ceiling.")		
			print("There is a door in the south.")	
			if game_states["northdoor"] == 0:
				print("The light above the door is red.")
			if game_states["northdoor"] == 1:
				print("The light above the door is green.")	
			print("In the north is an iron gate blocking the passage to the "
				  "exit.")			
			print("There is a silver box in center of the room.")
			if game_states["silverbox"] == 0:
				print("The silver box is currently closed.")	
			if game_states["silverbox"] == 1:
				print("The silver box is currently open.")
				if "batteries" not in inventory:
					print("There are batteries in the silver box.")
				if "batteries" in inventory:
					print("The silver box is empty.")	
			print("There is a metal access panel on the west wall.")
			if game_states["northaccesspanel"] == 0:
				print("The access panel is currently closed.")
			if (game_states["northaccesspanel"] == 1):
				print("The access panel is currently open.")	
				print("You can see gray and white switches in the access "
			    	  "panel.")
			if game_states["flashlight"] == 1:
				print("Light is shining from the flashlight.")				
			continue			

		### LOOK DOOR LIGHT ###
		if (player_input == 'look door light' or 
			player_input == 'look light above door'):
			print("The light is an indicator of the status of the door.")
			print("Red is locked and green is unlocked.")
			if game_states["northdoor"] == 0:
					print("The light above the door in the south is red.")
			if game_states["northdoor"] == 1:
					print("The light above the door in the south is green.")			
			continue				

		### LOOK LIGHT ###
		if player_input == 'look light':
			print("There is a light source on the ceiling.")
			print("It looks like a very bright LED embedded in the ceiling.")
			print("There are also light coming into the room through the "
				  "passage to the north.")	
			print("The light above the door is an indicator of the status of "
				"the door.")
			print("Red is locked and green is unlocked.")
			if game_states["northdoor"] == 0:
					print("The light above the door in the south is red.")
			if game_states["northdoor"] == 1:
					print("The light above the door in the south is green.")		
			if game_states["flashlight"] == 1:
				print("Light is shining from the flashlight.")
			continue				

		### ACCESS PANEL ###	  			
		if ((player_input == 'open access panel' or 
			player_input == 'open metal access panel' or
			player_input == 'open panel' or
			player_input == 'open access') and 
			game_states["northaccesspanel"] == 0):
			game_states["northaccesspanel"] = 1
			game_states["northdoor"] = 0
			print("Opening the metal access panel reveals two switches.")
			print("You can see a gray switch here.")
			print("You can see a white switch here.")	
			print("The light above the door in the south is now red.")
			continue		

		if ((player_input == 'open access panel' or 
			player_input == 'open metal access panel' or
			player_input == 'open panel' or
			player_input == 'open access') and 
			game_states["northaccesspanel"] == 1):	
			print("It's already open.")
			continue	

		if ((player_input == 'close access panel' or 
			player_input == 'close metal access panel' or
			player_input == 'close panel' or
			player_input == 'close access') and 
			game_states["northaccesspanel"] == 1):
			game_states["northaccesspanel"] = 0
			game_states["northdoor"] = 1
			print("You close the metal access panel.")	
			print("The light above the door in the south is now green.")
			continue			

		if ((player_input == 'close access panel' or 
			player_input == 'close metal access panel' or
			player_input == 'close panel' or
			player_input == 'close access') and 
			game_states["northaccesspanel"] == 0):	
			print("It's already closed.")
			continue	

		if ((player_input == 'look metal access panel' or 
			 player_input == 'look look metal panel' or
			 player_input == 'look metal access' or
			 player_input == 'look access panel' or
			 player_input == 'look panel') and
			(game_states["northaccesspanel"] == 0)):
			print("It's a metal access panel. It's currently closed.")
			continue

		if ((player_input == 'look metal access panel' or 
			 player_input == 'look look metal panel' or
			 player_input == 'look metal access' or
			 player_input == 'look access panel' or
			 player_input == 'look panel') and
			(game_states["northaccesspanel"] == 1)):
			print("It's a metal access panel. It's currently open.")
			print("You can see gray and white switches in the access panel.")
			continue												

		### SWITCHES ###
		if (player_input == 'look switch' or 
			player_input == 'look switches'):
			if "northaccesspanel" == 1:
				print("Inside the access panel are gray and white switches.")	
				print("Both gray and white switches are round push button "
					  "switch the size of a dime.")	
			if "northaccesspanel" == 0:
				print("I don't see any switch here.")
			continue		

		if (player_input == 'look gray' or 
			player_input == 'look gray switch'):
			if "northaccesspanel" == 1:
				print("Gray switch inside the access panel is a round push "
				 	  "button switch the size of a dime.")	
			if "northaccesspanel" == 0:
				print("I don't see any gray switch here.")				 	  	
			continue			

		if ((player_input == 'take gray switch' or 
			player_input == 'take gray') and 
			game_states["northaccesspanel"] == 1):
			print("Gray switch is securely affixed to inside of the panel. "
				  "You can't take it.")
			continue					

		if ((player_input == 'take gray switch' or 
			player_input == 'take gray') and 
			(game_states["northaccesspanel"] == 0)):
			print("What gray switch?")
			continue			

		if ((player_input == 'press gray switch' or 
			player_input == 'push gray switch' or
			player_input == 'press gray' or
			player_input == 'push gray') and
			game_states["northaccesspanel"] == 0):
			print("What gray switch?")
			continue

		if (((player_input == 'press gray switch' or 
			player_input == 'push gray switch' or
			player_input == 'press gray' or
			player_input == 'push gray') and
			game_states["northaccesspanel"] == 1) and	
			game_states["southdoor"] == 0):
			print("You press the gray switch.")
			game_states["southdoor"] = 1
			continue

		if (((player_input == 'press gray switch' or 
			player_input == 'push gray switch' or
			player_input == 'press gray' or
			player_input == 'push gray') and
			game_states["northaccesspanel"] == 1) and			
			game_states["southdoor"] == 1):
			print("You press the gray switch.")
			game_states["southdoor"] = 0
			continue					

		if (player_input == 'look white' or 
			player_input == 'look white switch'):
			if "northaccesspanel" == 1:
				print("White switch inside the access panel is a round push "
					  "button switch the size of a dime.")	
			if "northaccesspanel" == 0:
				print("I don't see any white switch here.")				 	  	
			continue		

		if ((player_input == 'take white switch' or 
			player_input == 'take white') and 
			game_states["northaccesspanel"] == 1):
			print("White switch is securely affixed to inside of the panel. "
				  "You can't take it.")
			continue					

		if ((player_input == 'take white switch' or 
			player_input == 'take white') and 
			(game_states["northaccesspanel"] == 0)):
			print("What white switch?")
			continue		

		if ((player_input == 'press white switch' or 
			player_input == 'push white switch' or
			player_input == 'press white' or
			player_input == 'push white') and
			game_states["northaccesspanel"] == 0):
			print("What white switch?")
			continue

		if (((player_input == 'press white switch' or 
			player_input == 'push white switch' or
			player_input == 'press white' or
			player_input == 'push white' ) and
			game_states["northaccesspanel"] == 1) and			
			game_states["southaccesspanel"] == 0):
			print("You press the white switch.")
			game_states["southaccesspanel"] = 1
			continue

		if (((player_input == 'press white switch' or 
			player_input == 'push white switch' or
			player_input == 'press white' or
			player_input == 'push white') and
			game_states["northaccesspanel"] == 1) and			
			game_states["southaccesspanel"] == 1):
			print("You press the white switch.")
			game_states["southaccesspanel"] = 0
			continue								

		### BATTERIES ###
		if ((player_input == 'take batteries') and
			"batteries" not in inventory and 
			game_states["silverbox"] == 1):
			print("Taken.")
			inventory.append("batteries")
			continue	

		if ((player_input == 'take batteries') and
			"batteries" not in inventory and 
			game_states["silverbox"] == 0):
			print("What batteries?")		

		if ((player_input == 'look batteries') and
			("batteries" not in inventory and game_states["silverbox"] == 1)):
			print("You'll need to take the batteries before looking at it.")
			continue								

		### SILVER BOX ###
		if ((player_input == 'open silver box' or 
			player_input == 'open box') and
			"silver key" not in inventory and 
			game_states["silverbox"] == 0):
			print("You can't open the silver box.  You don't have the correct "
				  "key to open it.")
			continue		

		if ((player_input == 'open silver box' or 
			player_input == 'open box') and
			game_states["silverbox"] == 1):
			print("The silver box is already open.")
			continue						

		if ((player_input == 'close box' or 
			player_input == 'close silver box') and
			game_states["silverbox"] == 1):
			print("You close the silver box.  Upon closing, it automatically "
				  "locks.")
			game_states["silverbox"] = 0
			continue			

		if ((player_input == 'open box' or 
                         player_input == 'open silver box' or
                         player_input == 'use key on box' or
			 player_input == 'open box with key') and
			("silver key" in inventory or 
			 "gold key" in inventory or 
			 "iron key" in inventory) and 
			game_states["silverbox"] == 0):
			print("Please specify which key to use to unlock the silver box.")
			continue			

		if ((player_input == 'look box' or 
			 player_input == 'look silver box') and
			(game_states["silverbox"] == 0)):
			print("The silver box looks like it's made out of silver. "
				  "The silver box is currently closed.")
			print("There is a keyhole on a side of the silver box.")
			continue

		if ((player_input == 'look box' or 
			 player_input == 'look silver box') and
			(game_states["silverbox"] == 1)):
			print("The silver box looks like it's made out of silver. "
				  "The silver box is currently open.")
			print("There is a keyhole on a side of the silver box.")
			if "batteries" not in inventory:
				print("There are batteries inside the silver box.")
			continue			

		if (player_input == 'take box' or player_input == 'take silver box'):
			print("The silver box seems be part of the floor.")
			print("It is impossible to lift it off the floor.")	
			continue						

		### IRON GATE ###
		if ((player_input == 'open gate' or 
			player_input == 'open iron gate') and
			"iron key" not in inventory and 
			game_states["irongate"] == 0):
			print("You can't open the iron gate.  You need a key to open it.")
			continue	

		if (player_input == 'take gate' or player_input == 'take iron gate'):
			print("The iron gate is part of the wall.")
			print("It is impossible to take it off its hinge.")	
			continue					

		### USING KEYS ON BOX OR GATE ###
		### Using Silver/Gold/Iron Key on the Silver Box ###
		if ((player_input == 'use silver key on box' or 
			player_input == 'use silver key on silver box' or
			player_input == 'use silver key to open box' or 
			player_input == 'open box with silver key' or
			player_input == 'open silver box with silver key' or
			player_input == 'unlock silver box using silver key' or
			player_input == 'unlock silver box with silver key' or	
			player_input == 'unlock box with silver key' or		
			player_input == 'open silver box using silver key' or
			player_input == 'open box with silver key' or
			player_input == 'open box using silver key') and
			"silver key" in inventory and 
			game_states["silverbox"] == 0):
			print("You insert the silver key into the keyhole on the "
				  "silver box.")
			print("The key fits, and the silver box opens.")
			if "batteries" not in inventory:
				print("Inside the silver box there are batteries.")
			if "batteries" in inventory:
				print("The silver box is empty.")
			print("You take the silver key out of the keyhole.")
			game_states["silverbox"] = 1
			continue			

		if ((player_input == 'use silver key on box' or 
			player_input == 'use silver key on silver box' or
			player_input == 'use silver key to open box' or 
			player_input == 'open box with silver key' or
			player_input == 'open silver box with silver key' or
			player_input == 'unlock silver box using silver key' or
			player_input == 'unlock silver box with silver key' or	
			player_input == 'unlock box with silver key' or		
			player_input == 'open silver box using silver key' or
			player_input == 'open box with silver key' or
			player_input == 'open box using silver key' or
		    player_input == 'use gold key on box' or 
			player_input == 'use gold key on silver box' or
			player_input == 'use gold key to open box' or 
			player_input == 'open box with gold key' or
			player_input == 'open silver box with gold key' or
			player_input == 'unlock silver box using gold key' or
			player_input == 'unlock silver box with gold key' or	
			player_input == 'unlock box with gold key' or		
			player_input == 'open silver box using gold key' or
			player_input == 'open box with gold key' or
			player_input == 'open box using gold key' or	
			player_input == 'use iron key on box' or 
			player_input == 'use iron key on silver box' or
			player_input == 'use iron key to open box' or 
			player_input == 'open box with iron key' or
			player_input == 'open silver box with iron key' or
			player_input == 'unlock silver box using iron key' or
			player_input == 'unlock silver box with iron key' or	
			player_input == 'unlock box with iron key' or		
			player_input == 'open silver box using iron key' or
			player_input == 'open box with iron key' or
			player_input == 'open box using iron key') and	
			(game_states["silverbox"] == 1)):
			print("The silver box is already unlocked and open.")
			continue			

		if ((player_input == 'use gold key on box' or 
			player_input == 'use gold key on silver box' or
			player_input == 'use gold key to open box' or 
			player_input == 'open box with gold key' or
			player_input == 'open silver box with gold key' or
			player_input == 'unlock silver box using gold key' or
			player_input == 'unlock silver box with gold key' or	
			player_input == 'unlock box with gold key' or		
			player_input == 'open silver box using gold key' or
			player_input == 'open box with gold key' or
			player_input == 'open box using gold key') and		
			"gold key" in inventory):
			print("Gold key doesn't fit in the keyhole on the silver box.")
			continue			

		if ((player_input == 'use iron key on box' or 
			player_input == 'use iron key on silver box' or
			player_input == 'use iron key to open box' or 
			player_input == 'open box with iron key' or
			player_input == 'open silver box with iron key' or
			player_input == 'unlock silver box using iron key' or
			player_input == 'unlock silver box with iron key' or	
			player_input == 'unlock box with iron key' or		
			player_input == 'open silver box using iron key' or
			player_input == 'open box with iron key' or
			player_input == 'open box using iron key') and
			"iron key" in inventory):
			print("Iron key doesn't fit in the keyhole on the silver box.")
			continue		

		if ((player_input == 'use silver key on box' or 
			player_input == 'use silver key on silver box' or
			player_input == 'use silver key to open box' or 
			player_input == 'open box with silver key' or
			player_input == 'open silver box with silver key' or
			player_input == 'unlock silver box using silver key' or
			player_input == 'unlock silver box with silver key' or	
			player_input == 'unlock box with silver key' or		
			player_input == 'open silver box using silver key' or
			player_input == 'open box with silver key' or
			player_input == 'open box using silver key') and
			"silver key" not in inventory):
			print("What silver key?")	
			continue		

		if ((player_input == 'use gold key on box' or 
			player_input == 'use gold key on silver box' or
			player_input == 'use gold key to open box' or 
			player_input == 'open box with gold key' or
			player_input == 'open silver box with gold key' or
			player_input == 'unlock silver box using gold key' or
			player_input == 'unlock silver box with gold key' or	
			player_input == 'unlock box with gold key' or		
			player_input == 'open silver box using gold key' or
			player_input == 'open box with gold key' or
			player_input == 'open box using gold key') and		
			"gold key" not in inventory):
			print("What gold key?")	
			continue			

		if ((player_input == 'use iron key on box' or 
			player_input == 'use iron key on silver box' or
			player_input == 'use iron key to open box' or 
			player_input == 'open box with iron key' or
			player_input == 'open silver box with iron key' or
			player_input == 'unlock silver box using iron key' or
			player_input == 'unlock silver box with iron key' or	
			player_input == 'unlock box with iron key' or		
			player_input == 'open silver box using iron key' or
			player_input == 'open box with iron key' or
			player_input == 'open box using iron key') and
			"iron key" not in inventory):
			print("What iron key?")	
			continue									

		### Using Silver/Gold/Iron Key on the Iron Gate ###
		if ((player_input == 'use silver key on gate' or 
			player_input == 'use silver key on iron gate' or
			player_input == 'use silver key to open gate' or
			player_input == 'use silver key to open iron gate' or
			player_input == 'open iron gate with silver key' or
			player_input == 'open gate with silver key' or
			player_input == 'open iron gate using silver key' or
			player_input == 'open gate using silver key' or
			player_input == 'unlock gate using silver key' or
			player_input == 'unlock gate with silver key' or
			player_input == 'unlock iron gate using silver key' or
			player_input == 'unlock iron gate with silver key' or	
			player_input == 'use silver key to unlock iron gate' or		
			player_input == 'use silver key to unlock gate') and
			"silver key" in inventory):
			print("Silver key doesn't fit in the keyhole on the iron gate.")
			continue			

		### Using Silver/Gold/Iron Key on the Iron Gate ###
		if ((player_input == 'use silver key on gate' or 
			player_input == 'use silver key on iron gate' or
			player_input == 'use silver key to open gate' or
			player_input == 'use silver key to open iron gate' or
			player_input == 'open iron gate with silver key' or
			player_input == 'open gate with silver key' or
			player_input == 'open iron gate using silver key' or
			player_input == 'open gate using silver key' or
			player_input == 'unlock gate using silver key' or
			player_input == 'unlock gate with silver key' or
			player_input == 'unlock iron gate using silver key' or
			player_input == 'unlock iron gate with silver key' or	
			player_input == 'use silver key to unlock iron gate' or		
			player_input == 'use silver key to unlock gate') and
			"silver key" not in inventory):
			print("What silver key?")
			continue						

		if ((player_input == 'use gold key on gate' or 
			player_input == 'use gold key on iron gate' or
			player_input == 'use gold key to open gate' or
			player_input == 'use gold key to open iron gate' or
			player_input == 'open iron gate with gold key' or
			player_input == 'open gate with gold key' or
			player_input == 'open iron gate using gold key' or
			player_input == 'open gate using gold key' or
			player_input == 'unlock gate using gold key' or
			player_input == 'unlock gate with gold key' or
			player_input == 'unlock iron gate using gold key' or
			player_input == 'unlock iron gate with gold key' or	
			player_input == 'use gold key to unlock iron gate' or		
			player_input == 'use gold key to unlock gate') and
			"gold key" in inventory):
			print("Gold key doesn't fit in the keyhole on the iron gate.")
			continue	

		if ((player_input == 'use gold key on gate' or 
			player_input == 'use gold key on iron gate' or
			player_input == 'use gold key to open gate' or
			player_input == 'use gold key to open iron gate' or
			player_input == 'open iron gate with gold key' or
			player_input == 'open gate with gold key' or
			player_input == 'open iron gate using gold key' or
			player_input == 'open gate using gold key' or
			player_input == 'unlock gate using gold key' or
			player_input == 'unlock gate with gold key' or
			player_input == 'unlock iron gate using gold key' or
			player_input == 'unlock iron gate with gold key' or	
			player_input == 'use gold key to unlock iron gate' or		
			player_input == 'use gold key to unlock gate') and
			"gold key" not in inventory):
			print("What gold key?")
			continue							

		if ((player_input == 'use iron key on gate' or 
			player_input == 'use iron key on iron gate' or
			player_input == 'use iron key to open gate' or
			player_input == 'use iron key to open iron gate' or
			player_input == 'open iron gate with iron key' or
			player_input == 'open gate with iron key' or
			player_input == 'open iron gate using iron key' or
			player_input == 'open gate using iron key' or
			player_input == 'unlock gate using iron key' or
			player_input == 'unlock gate with iron key' or
			player_input == 'unlock iron gate using iron key' or
			player_input == 'unlock iron gate with iron key' or	
			player_input == 'use iron key to unlock iron gate' or		
			player_input == 'use iron key to unlock gate') and
			"iron key" in inventory and 
			game_states["irongate"] == 0):
			print("Iron gate is now unlocked.")
			game_states["irongate"] = 1
			continue			

		if ((player_input == 'use iron key on gate' or 
			player_input == 'use iron key on iron gate' or
			player_input == 'use iron key to open gate' or
			player_input == 'use iron key to open iron gate' or
			player_input == 'open iron gate with iron key' or
			player_input == 'open gate with iron key' or
			player_input == 'open iron gate using iron key' or
			player_input == 'open gate using iron key' or
			player_input == 'unlock gate using iron key' or
			player_input == 'unlock gate with iron key' or
			player_input == 'unlock iron gate using iron key' or
			player_input == 'unlock iron gate with iron key' or	
			player_input == 'use iron key to unlock iron gate' or		
			player_input == 'use iron key to unlock gate') and
			"iron key" not in inventory):
			print("What iron key?")
			continue						

		if ((player_input == 'use iron key on gate' or 
			player_input == 'use iron key on iron gate' or
			player_input == 'use iron key to open gate' or
			player_input == 'use iron key to open iron gate' or
			player_input == 'open iron gate with iron key' or
			player_input == 'open gate with iron key' or
			player_input == 'open iron gate using iron key' or
			player_input == 'open gate using iron key' or
			player_input == 'unlock gate using iron key' or
			player_input == 'unlock gate with iron key' or
			player_input == 'unlock iron gate using iron key' or
			player_input == 'unlock iron gate with iron key' or	
			player_input == 'use iron key to unlock iron gate' or		
			player_input == 'use iron key to unlock gate') and
			game_states["irongate"] == 1):
			print("Iron gate is already unlocked.")
			continue									

		if ((player_input == 'use silver key') and
			"silver key" in inventory):
			print("Please specify which lock to open.")	
			continue	

		if ((player_input == 'use gold key') and
			"gold key" in inventory): 
			print("Please specify which lock to open.")	
			continue	

		if ((player_input == 'use iron key') and
			"iron key" in inventory): 
			print("Please specify which lock to open.")	
			continue				

		if ((player_input == 'use key') and
			("iron key" in inventory or 
			"silver key" in inventory or 
			"gold key" in inventory)): 
			print("Please specify which key to open which lock.")	
			continue

		if ((player_input == 'use key on gate') or
                        player_input == 'use key to open gate' or
                        player_input == 'use key to unlock gate' or
                        player_input == 'open gate with key' and
			("iron key" in inventory or 
			"silver key" in inventory or 
			"gold key" in inventory)): 
			print("Please specify which key to use to open the gate.")	
			continue
		    

		### PRESSURE PLATE ###
		if (player_input == 'look pressure plate' or
			player_input == 'look pressure' or
			player_input == 'look plate'): 
			print("The pressure plate is almost invisible on the floor.")
			print("The only reason you know it is there is because you felt it "
				  "as you entered the room.")
			continue	

		if (player_input == 'take pressure plate' or
			player_input == 'take pressure' or
			player_input == 'take plate'): 
			print("The pressure plate seems to be an integral part of the "
				  "floor.")
			print("As much as you try to, you can't take it.")
			continue																												

		### INPUT HANLDER ### 
		### (FOR ANY INPUT THAT IS DESIGNED TO WORK IN MULTIPLE ROOMS)
		else:
			inputhandler(player_input)
			continue						
								
#######################################################################
#                          INPUT HANDLER                              #
#######################################################################
def inputhandler(player_input):

	### MAIN SECTION FOR THE INPUT HANDLER FUNCTION ###
	while True:

		### DEBUG ###
		if player_input == 'debug':
			debug()
			return()

		### INVENTORY ###
		if player_input == 'inventory' or player_input == 'i':
			playerinventory()
			return()		

		### WALL, DOOR, CEILING, AND FLOOR IN ALL ROOMS ###
		if player_input == 'look wall':
			print("The walls are made of metal.")
			return()			

		if player_input == 'look floor':
			print("The floor is made of metal.")
			return()	

		if player_input == 'look ceiling':
			print("The ceiling is made of metal.")
			return()			

		if (player_input == 'take wall'):
			print("As much as you try to, you can't take down the wall.")
			return()		

		if (player_input == 'take ceiling'):
			print("As much as you try to, you can't take down the ceiling.")
			return()	

		if (player_input == 'take floor'):
			print("As much as you try to, you can't tear up the floor.")
			return()																					

		if player_input == 'look door':
			if game_states["roomid"] == 1:
				print("The doors are made of metal and opens automatically "
					"when you approach them.")
				print("There isn't any window on the doors.")
			else:
				print("The door is made of metal and opens automatically "
					"when you approach them.")
				print("There isn't any window on the door.")
			return()		

		if (player_input == 'take door'):
			print("As much as you try to, you can't tear the door out of "
				  "its frame.")
			return()									

		### TAKE DOOR LIGHT ###
		if (player_input == 'take door light'):
			print("As much as you try to, you can't dislodge the light "
				  "above of the door.")
			return()				

		### FLASHLIGHT ###
		if ((player_input == 'take flashlight' or 
			   player_input == 'look flashlight') and 
			"flashlight" not in inventory):
			print("What flashlight?")
			return()	

		if player_input == 'take flashlight' and "flashlight" in inventory:
			print("You already took the flashlight.")
			return()				

		if ((player_input == 'look flashlight') and
			"flashlight" in inventory and
			game_states["flashlightbatteries"] == 0):
			print("It is a flashlight.  It needs some batteries, though.")
			return()		

		if ((player_input == 'look flashlight') and
			"flashlight" in inventory and
			(game_states["flashlightbatteries"] == 1 and 
			game_states["flashlight"] == 1)):
			print("It is a flashlight.  It is currently on and illuminating "
				  "the area.")
			return()	

		if ((player_input == 'look flashlight') and
			"flashlight" in inventory and
			(game_states["flashlightbatteries"] == 1 and 
			game_states["flashlight"] == 0)):
			print("It is a flashlight. It is currently off.")
			return()			

		### PUTTING BATTERIES INTO FLASHLIGHT ###
		if ((player_input == 'put batteries in flashlight' or 
			player_input == 'insert batteries in flashlight' or 
			player_input == 'insert batteries into flashlight' or
			player_input == 'put batteries into flashlight')
			and ("flashlight" in inventory and 
				 "batteries" in inventory and 
				 game_states["flashlightbatteries"] == 0)):
			print("Batteries are now in the flashlight.")
			game_states["flashlightbatteries"] = 1
			return()		

		if ((player_input == 'put batteries in flashlight' or 
			player_input == 'insert batteries in flashlight' or 
			player_input == 'insert batteries into flashlight' or
			player_input == 'put batteries into flashlight')
			and ("flashlight" in inventory and 
				 "batteries" in inventory and 
				 game_states["flashlightbatteries"] == 1)):
			print("Flashlight already contains batteries.")
			return()				

		if ((player_input == 'put batteries in flashlight' or 
			player_input == 'insert batteries in flashlight' or 
			player_input == 'insert batteries into flashlight' or
			player_input == 'put batteries into flashlight')
			and ("flashlight" not in inventory and "batteries" in inventory)):
			print("What flashlight?")
			return()		

		if ((player_input == 'put batteries in flashlight' or 
			player_input == 'insert batteries in flashlight' or 
			player_input == 'insert batteries into flashlight' or
			player_input == 'put batteries into flashlight')
			and ("flashlight" in inventory and "batteries" not in inventory)):
			print("You don't have any batteries.")
			return()			

		if ((player_input == 'put batteries in flashlight' or 
			player_input == 'insert batteries in flashlight' or 
			player_input == 'insert batteries into flashlight' or
			player_input == 'put batteries into flashlight')
			and ("flashlight" not in inventory and 
			"batteries" not in inventory)):
			print("What flashlight?")
			print("What batteries?")			
			return()					

		### TURNING FLASHLIGHT ON AND OFF ###
		if ((player_input == 'turn flashlight on' or 
			player_input == 'turn on flashlight' or
			player_input == 'turn on light' or
			player_input == 'turn light on')
			and ("flashlight" in inventory and 
			game_states["flashlightbatteries"] == 1)):
			print("You turn the flashlight on.  Light is shining from it.")
			game_states["flashlight"] = 1			
			return()		

		if ((player_input == 'turn flashlight on' or 
			player_input == 'turn on flashlight' or
			player_input == 'turn on light' or
			player_input == 'turn light on' or
			player_input == 'turn flashlight off' or 
			player_input == 'turn off flashlight' or
			player_input == 'turn off light' or
			player_input == 'turn light off')
			and ("flashlight" not in inventory)):
			print("What flashlight?")		
			return()				

		if ((player_input == 'turn flashlight on' or 
			player_input == 'turn on flashlight' or
			player_input == 'turn on light' or
			player_input == 'turn light on')
			and ("flashlight" in inventory and 
			game_states["flashlightbatteries"] == 0)):
			print("Flashlight won't turn on.  There are no batteries in it.")		
			return()					

		if ((player_input == 'turn flashlight off' or 
			player_input == 'turn off flashlight' or
			player_input == 'turn off light' or
			player_input == 'turn light off')
			and ("flashlight" in inventory and 
			game_states["flashlightbatteries"] == 1)):
			print("You turn the flashlight off.")
			game_states["flashlight"] = 0	
			return()										

		### KEYS ###
		if ((player_input == 'look silver key') and
			"silver key" in inventory):
			print("It's a smooth silver key.")
			return()	

		if ((player_input == 'look gold key') and
			("gold key" in inventory)):
			print("It's a key made of solid gold.")
			return()			

		if ((player_input == 'look iron key') and
			("iron key" in inventory)):
			print("It's a very heavy key made of iron.")
			return()			

		if ((player_input == 'look key') and
			("iron key" in inventory or 
			 "silver key" in inventory or 
			 "gold key" in inventory)):
			print("Please specify which key to look at.")
			return()	

		if ((player_input == 'look key') and
			("iron key" not in inventory and 
			 "silver key" not in inventory and 
			 "gold key" not in inventory)):
			print("I don't see any key.")
			return()									

		if (player_input == 'take gold key' and 
			"gold key" in inventory):
			print("You already took the gold key.")
			return()	

		if (player_input == 'take silver key' and 
			"silver key" in inventory):
			print("You already took the silver key.")
			return()	

		if (player_input == 'take iron key' and 
			"iron key" in inventory):
			print("You already took the iron key.")
			return()											

		if ((player_input == 'use key') or
                        player_input == 'use key on box' or
                        player_input == 'open box with key' and 
			("gold key" not in inventory and 
			 "silver key" not in inventory and
			 "iron key" not in inventory)):	
			print("What key?")
			return()	

		if ((player_input == 'use key') and
			("gold key" in inventory or 
			 "silver key" in inventory or 
			 "iron key" in inventory)):
			print("Please specify which key.")	
			return()			

		### PAPER ###
		if (player_input == 'take paper' and "paper" in inventory):
			print("You already took the paper.")
			return()				

		if ((player_input == 'look paper') and
			"paper" in inventory):
			print("It's a blank paper.")
			return()					

		# BATTERIES
		if (player_input == 'take batteries' and 
			"batteries" in inventory):
			print("You already took the batteries.")
			return()		

		if ((player_input == 'take batteries' or
			 player_input == 'look batteries') and 
			"batteries" not in inventory):
			print("What batteries?")
			return()									

		if ((player_input == 'look batteries') and
			"batteries" in inventory):
			print("They're D cell batteries.")
			return()	

		###################################################	
		# ANY ROOM EXCEPT FOR CENTER AND WEST ROOMS       #
		###################################################	
		if game_states["roomid"] != 1 and game_states["roomid"] != 3:
			#Pressing switch without specifying the color									
			if (player_input == 'press switch' or 
				player_input == 'push switch' or
				player_input == 'take switch'):
				print("Please specify the color of the switch.")
				return()

		###################################################	
		# CENTER AND WEST ROOMS                           #
		###################################################	
		if game_states["roomid"] == 1 or game_states["roomid"] == 3:
			# There are no switches in Center and West rooms.									
			if (player_input == 'press switch' or 
				player_input == 'push switch' or 
				player_input == 'look switch' or 
				player_input == 'look switches' or
				player_input == 'take switch' or 
				player_input == 'take switches'):
				print("You don't see any switch here.")
				return()										

		###################################################	
		# NORTH AND SOUTH ROOMS                           #
		###################################################	
		if game_states["roomid"] == 4 or game_states["roomid"] == 5:
								
			if (player_input == 'take metal access panel' or 
				player_input == 'take access panel' or 
				player_input == 'take panel' or 
				player_input == 'take metal panel' or
				player_input == 'take metal access'):
				print("You try to tear the panel off the wall but it's proving "
					  "to be impossible.")
				return()

		###################################################	
		# ANY ROOM EXCEPT FOR WEST ROOM                   #
		###################################################	
		if game_states["roomid"] != 3:
			if ((player_input == 'look iron key' or 
				player_input == 'take iron key') and
				("iron key" not in inventory)):
				print("What iron key?")
				return()	

			if (player_input == 'open golden box' or 
				player_input == 'open gold box' or
				player_input == 'unlock gold box' or
				player_input == 'take golden box' or
				player_input == 'take gold box'):
				print("What golden box?")
				return()			

			if (player_input == 'look sensor' or
				player_input == 'take sensor'):
				print("What sensor?")
				return()		

			if (player_input == 'take light'):
				print("As much as you try to, you can't dislodge the light from"
					  " the ceiling.")
				return()										

		###################################################
		# ANY ROOM EXCEPT FOR EAST ROOM                   #
		###################################################	
		if game_states["roomid"] != 2:	

			### PAPER ###
			if ((player_input == 'look paper' or 
				 player_input == 'take paper') and
				"paper" not in inventory):
				print("What paper?")
				return()	

			### SILVER KEY ###
			if ((player_input == 'look silver key' or 
				player_input == 'take silver key') and
				("silver key" not in inventory)):
				print("What silver key?")
				return()			

			### BLACK BOX ###
			if (player_input == 'open black box' or 
				player_input == 'open black box' or
				player_input == 'unlock black box' or
				player_input == 'take black box'):
				print("What black box?")
				return()			

			### SWITCHES ###
			if (player_input == 'press green switch' or 
				player_input == 'push green switch' or
				player_input == 'push green' or
				player_input == 'press green' or
				player_input == 'look green' or
				player_input == 'look green switch' or
				player_input == 'take green switch'):
				print("What green switch?")
				return()		
									
			if (player_input == 'press yellow switch' or 
				player_input == 'push yellow switch' or
				player_input == 'press yellow' or
				player_input == 'push yellow' or
				player_input == 'look yellow' or
				player_input == 'look yellow switch' or
				player_input == 'take yellow switch'):
				print("What yellow switch?")
				return()																

		###################################################
		# ANY ROOM EXCEPT FOR SOUTH ROOM                  #
		###################################################	
		if game_states["roomid"] != 4:

			### GOLD KEY ###
			if ((player_input == 'look gold key' or 
				player_input == 'take gold key') and
				("gold key" not in inventory)):
				print("What gold key?")
				return()													

			### PLANTER ###
			if (player_input == 'look planter' or 
				player_input == 'take planter'):
				print("What planter?")
				return()	

			### PLANT ###
			if (player_input == 'look plant' or 
				player_input == 'take plant'):
				print("What plant?")
				return()					

			### GEARS ###
			if (player_input == 'look gears' or 
				player_input == 'take gears' or
				player_input == 'look large gears' or
				player_input == 'take large gears'):
				print("What gears?")
				return()		

			### SPRINGS	###
			if (player_input == 'look springs' or 
				player_input == 'take springs'):
				print("What springs?")
				return()											

			### PILE OF DIRT ###
			if (player_input == 'take dirt' or 
				player_input == 'take pile of dirt' or
				player_input == 'take dirt pile' or
				player_input == 'take pile dirt' or
				player_input == 'look dirt' or 
				player_input == 'look pile of dirt' or
				player_input == 'look dirt pile' or
				player_input == 'look pile dirt'):
				print("What dirt?")
				return()	

			### PILE OF DUST ###
			if (player_input == 'take dust' or 
				player_input == 'take pile of dust' or
				player_input == 'take dust pile' or
				player_input == 'take pile dust' or
				player_input == 'look dust' or 
				player_input == 'look pile of dust' or
				player_input == 'look dust pile' or
				player_input == 'look pile dust'):
				print("What dust?")
				return()					

			### PILE OF RUBBISH / RUBBISH ###
			if (player_input == 'look rubbish' or 
				player_input == 'take rubbish'):
				print("What rubbish?")
				return()		

			if (player_input == 'look pile of rubbish' or 
				player_input == 'take pile of rubbish'):
				print("What pile of rubbish?")
				return()

			### SWITCHES ###
			if (player_input == 'press blue switch' or 
				player_input == 'push blue switch' or
				player_input == 'press blue' or
				player_input == 'push blue' or
				player_input == 'look blue' or
				player_input == 'look blue switch' or
				player_input == 'take blue switch'):
				print("What blue switch?")
				return()	

			if (player_input == 'press red switch' or 
				player_input == 'push red switch' or
				player_input == 'press red' or
				player_input == 'push red' or
				player_input == 'look red' or
				player_input == 'look red switch' or
				player_input == 'take red switch'):
				print("What red switch?")
				return()							

		###################################################	
		# ANY ROOM EXCEPT FOR NORTH ROOM                  #
		###################################################	
		if game_states["roomid"] != 5:
								
			if (player_input == 'press gray switch' or 
				player_input == 'push gray switch' or
				player_input == 'press gray' or
				player_input == 'push gray' or
				player_input == 'look gray' or
				player_input == 'look gray switch' or
				player_input == 'take gray switch'):
				print("What gray switch?")
				return()	

			if (player_input == 'press whhite switch' or 
				player_input == 'push white switch' or
				player_input == 'press white' or
				player_input == 'push white' or
				player_input == 'look white' or
				player_input == 'look white switch' or
				player_input == 'take white switch'):
				print("What white switch?")
				return()				

			### SILVER BOX ###
			if (player_input == 'open silver box' or 
				player_input == 'open silver box' or
				player_input == 'unlock silver box'):
				print("What silver box?")
				return()		


			### IRON GATE ###
			if (player_input == 'open iron gate' or 
				player_input == 'open gate' or
				player_input == 'unlock iron gate' or
				player_input == 'unlock gate'):
				print("What iron gate?")
				return()				

		### PRESSURE PLATE ###
		if (player_input == 'look pressure plate' or
			player_input == 'look pressure' or
			player_input == 'look plate' or
			player_input == 'take pressure plate' or
			player_input == 'take pressure' or
			player_input == 'take plate'): 
			print("What pressure plate?")
			return()								

		###################################################
		# ANY ROOM EXCEPT FOR SOUTH AND NORTH ROOMS       #
		###################################################	
		if game_states["roomid"] != 4 and game_states["roomid"] != 5:	
			
			### METAL ACCESS PANEL ###
			if (player_input == 'open access panel' or 
				player_input == 'open metal access panel' or
				player_input == 'close access panel' or 
				player_input == 'close metal access panel' or
				player_input == 'take access panel'):
				print("What access panel?")
				return()

			if (player_input == 'open panel' or
				player_input == 'close panel' or
				player_input == 'take panel'):	
				print("What panel?")
				return()

			if (player_input == 'open metal panel' or
				player_input == 'close metal panel' or
				player_input == 'take metal panel'):	
				print("What metal panel?")
				return()

			if (player_input == 'open access' or
				player_input == 'close access' or
				player_input == 'take access'):	
				print("What access?")
				return()			

		###################################################
		# ANY ROOM EXCEPT FOR EAST, WEST, AND NORTH ROOMS #
		###################################################	
		if (game_states["roomid"] != 2 and game_states["roomid"] != 3 and
		    game_states["roomid"] != 5):

			### BOX ###
			if (player_input == 'open box' or 
				player_input == 'unlock box' or
				player_input == 'take box'):
				print("What box?")
				return()	

		###################################################
		# ANY ROOM EXCEPT FOR WEST AND NORTH ROOMS        #
		###################################################	
		if game_states["roomid"] != 3 and game_states["roomid"] != 5:

			### USE KEY ###		
			if ((player_input == 'use key') and 
				("gold key" in inventory or 
				 "silver key" in inventory or
				 "iron key" in inventory)):	
				print("There's no lock in this room to use the key on.")
				return()					

		###################################################
		# ANY ROOM EXCEPT FOR EAST, WEST, AND SOUTH ROOMS #
		###################################################	
		if (game_states["roomid"] != 2 and game_states["roomid"] != 3 and 
			game_states["roomid"] != 4):		

			### TAKE KEY ###
			if ((player_input == 'take key') and 
				("gold key" not in inventory or 
				 "silver key" not in inventory or
				 "iron key" not in inventory)):	
				print("What key?")
				return()						


		###################################################
		# QUITTING THE GAME                               #
		###################################################		
		if player_input == 'q' or player_input == 'quit':
			end()		

		###################################################
		# CATCH-ALL FOR EVERY OTHER INPUTS                #
		###################################################	
		else:
			print("I don't understand \""+player_input+"\"")
			return()			

#######################################################################
#                              END GAME                               #
#######################################################################
def end():
	if game_states["escaped"] == 0:
		while True:
			clear()
			print("\t\t-----------------------------------------------")
			print("\n\t\t\t\t   ESCAPE\n")
			print("\t\t-----------------------------------------------")
			print("\n\n\nThanks for playing.")
			player_input = input("")
			clear()
			exit()

	if game_states["escaped"] == 1:
		while True:
			clear()
			print("\t\t-----------------------------------------------")
			print("\n\t\t\t\t   THE ESCAPE\n")
			print("\t\t-----------------------------------------------")
			print("\n\n\nAfter pushing the iron gate open, you run down the "
				  "passage...")
			print("and you step out of the passage into an open grassy "
				  "meadows!")
			print("\n")
			print("You have escaped!  Congratulations!")			
			player_input = input("")
			clear()
			exit()		


#######################################################################
#                            INVENTORY                                #
#######################################################################
def playerinventory():
	if len(inventory) != 0:
		print("\n-----------------------------")
		print("\t  INVENTORY")
		print("-----------------------------")
		print("You're carrying: ")
		for item in inventory:
			print(item)

	if len(inventory) == 0:
		print("\n-----------------------------")
		print("\t  INVENTORY")
		print("-----------------------------")
		print("You're not carrying anything.\n")


#######################################################################
#                              DEBUG                                  #
#######################################################################
def debug():
		clear()
		print("\t\t-----------------------------------------------")
		print("\n\t\t\t\t   DEBUG\n")
		print("\t\t-----------------------------------------------\n\n")
		while True:
			print("Which action do you want to take?")
			print("1: Add items to inventory")
			print("2: Change game states")
			print("3: Change room")
			print("4: Exit to the game")
			debug_input = input("\n> ")
			debug_input = debug_input.strip()
			debug_input = debug_input.lower()
			clear()
			
			if debug_input == "1":
				print("\t\t-----------------------------------------------")
				print("\n\t\t\t\tDEBUG - ADD ITEMS\n")
				print("\t\t-----------------------------------------------")				
				print("\n\nEnter the item to add to inventory.")
				print("List of items in the game:")
				print('"paper", "flashlight", "silver key", "gold key", '
					  '"iron key", "batteries"')
				print('Enter "all" to add everything to inventory.')
				print('Type "exit" when you are done.')	
				while True:
					debug_input = input("\n> ")
					debug_input = debug_input.strip()
					debug_input = debug_input.lower()
					if debug_input == "paper":
						inventory.append("paper")
						print("Paper added to inventory.")
						continue
					if debug_input == "flashlight":
						inventory.append("flashlight")
						print("Flashlight added to inventory.")
						continue						
					if debug_input == "silver key":
						inventory.append("silver key")
						print("Silver key added to inventory.")
						continue
					if debug_input == "gold key":
						inventory.append("gold key")
						print("Gold key added to inventory.")
						continue						
					if debug_input == "iron key":
						inventory.append("iron key")
						print("Iron key added to inventory.")
						continue
					if debug_input == "batteries":
						inventory.append("batteries")
						print("Batteries added to inventory.")
						continue
					if debug_input == "all":
						inventory.append("paper")
						inventory.append("flashlight")
						inventory.append("silver key")
						inventory.append("gold key")
						inventory.append("iron key")
						inventory.append("batteries")	
						print("All items added to inventory.")						
						continue						
					if debug_input == "exit":
						debug()
					else:
						print("Not a valid item or input.")
						continue		

			if debug_input == "2":
				print("\t\t-----------------------------------------------")
				print("\n\t\t\t     DEBUG - MODIFY STATES\n")
				print("\t\t-----------------------------------------------")
				print("\n\nEnter the state to modify.")
				print("List of states in the game:")
				print('"roomid", "northdoor", "southdoor", "eastdoor", '
					  '"westdoor", \n"blackbox", "northaccesspanel", '
					  '"silverbox", "southaccesspanel", \n"deadplant", ' 
					  '"planter", "flashlight", "flashlightbatteries", ' 
					  '\n"goldenbox", "irongate", "escaped"')
				print('Type "exit" when you are done.')								
				while True:
					debug_input = input("\n> ")
					debug_input = debug_input.strip()
					debug_input = debug_input.lower()
					if debug_input == "roomid":
						print("Current state is "
							 f"{game_states['roomid']}")
						print("Enter the desired state.")
						print("1 - Center, 2 - East, 3 - West, 4 - South,"
							  " 5 - North)")
						debug_input = input("\n> ")
						try:
							debug_input = debug_input.strip()
							debug_input = int(debug_input)
							game_states['roomid'] = debug_input
							print("State modified.")
							continue
						except:
							print("Invalid input.  Returning to modify state menu.")
							continue					
					if debug_input == "northdoor":
						print("Current state is "
							 f"{game_states['northdoor']}")
						print("Enter the desired state (0 (locked) "
							  "or 1 (open))")
						debug_input = input("\n> ")						
						try:
							debug_input = debug_input.strip()
							debug_input = int(debug_input)
							game_states['northdoor'] = debug_input
							print("State modified.")
							continue
						except:
							print("Invalid input.  Returning to modify state menu.")
							continue
					if debug_input == "southdoor":
						print("Current state is "
							 f"{game_states['southdoor']}")
						print("Enter the desired state (0 (locked) "
							  "or 1 (open))")
						debug_input = input("\n> ")
						try:
							debug_input = debug_input.strip()
							debug_input = int(debug_input)
							game_states['southdoor'] = debug_input
							print("State modified.")
							continue
						except:
							print("Invalid input.  Returning to modify state menu.")
							continue
					if debug_input == "eastdoor":
						print(f"Current state is {game_states['eastdoor']}")
						print("Enter the desired state (0 (locked) "
							  "or 1 (open))")
						debug_input = input("\n> ")
						try:
							debug_input = debug_input.strip()
							debug_input = int(debug_input)
							game_states['eastdoor'] = debug_input
							print("State modified.")
							continue
						except:
							print("Invalid input.  Returning to modify state menu.")
							continue
					if debug_input == "westdoor":
						print("Current state is "
							 f"{game_states['westdoor']}")
						print("Enter the desired state (0 (locked) "
							  "or 1 (open))")
						debug_input = input("\n> ")
						try:
							debug_input = debug_input.strip()
							debug_input = int(debug_input)
							game_states['westdoor'] = debug_input
							print("State modified.")
							continue
						except:
							print("Invalid input.  Returning to modify state menu.")
							continue
					if debug_input == "blackbox":
						print(f"Current state is {game_states['blackbox']}")
						print("Enter the desired state (0 (locked) "
							  "or 1 (unlocked) or 2 (open))")
						debug_input = input("\n> ")
						try:
							debug_input = debug_input.strip()
							debug_input = int(debug_input)
							game_states['blackbox'] = debug_input
							print("State modified.")
							continue
						except:
							print("Invalid input.  Returning to modify state menu.")
							continue
					if debug_input == "northaccesspanel":
						print("Current state is "
							 f"{game_states['northaccesspanel']}")
						print("Enter the desired state (0 (locked) or "
						      "1 (open))")
						debug_input = input("\n> ")
						try:
							debug_input = debug_input.strip()
							debug_input = int(debug_input)
							game_states['northaccesspanel'] = debug_input
							print("State modified.")
						except:
							print("Invalid input.  Returning to modify state menu.")
							continue		
					if debug_input == "southaccesspanel":
						print("Current state is "
							 f"{game_states['southaccesspanel']}")
						print("Enter the desired state (0 (locked) "
							  "or 1 (unlocked) or 2 (open))")
						debug_input = input("\n> ")
						try:
							debug_input = debug_input.strip()
							debug_input = int(debug_input)
							game_states['southaccesspanel'] = debug_input
							print("State modified.")
							continue
						except:
							print("Invalid input.  Returning to modify state menu.")
							continue	
					if debug_input == "silverbox":
						print("Current state is "
							 f"{game_states['silverbox']}")
						print("Enter the desired state (0 (locked) "
							  "or 1 (open))")
						debug_input = input("\n> ")
						try:
							debug_input = debug_input.strip()
							debug_input = int(debug_input)
							game_states['silverbox'] = debug_input
							print("State modified.")
							continue
						except:
							print("Invalid input.  Returning to modify state menu.")
							continue				
					if debug_input == "goldenbox":
						print("Current state is "
							 f"{game_states['goldenbox']}")
						print("Enter the desired state (0 (locked) or "
							  "1 (open))")
						debug_input = input("\n> ")
						try:
							debug_input = debug_input.strip()
							debug_input = int(debug_input)
							game_states['goldenbox'] = debug_input
							print("State modified.")
							continue
						except:
							print("Invalid input.  Returning to modify state menu.")
							continue		
					if debug_input == "deadplant":
						print("Current state is "
							 f"{game_states['deadplant']}")
						print("Enter the desired state (0 (not crumbled) "
							  "or 1 (crumbled))")
						debug_input = input("\n> ")
						try:
							debug_input = debug_input.strip()
							debug_input = int(debug_input)
							game_states['deadplant'] = debug_input
							print("State modified.")
							continue
						except:
							print("Invalid input.  Returning to modify state menu.")
							continue	
					if debug_input == "planter":
						print(f"Current state is {game_states['planter']}")
						print("Enter the desired state (0 (not crumbled) "
							  "or 1 (crumbled))")
						debug_input = input("\n> ")
						try:
							debug_input = debug_input.strip()
							debug_input = int(debug_input)
							game_states['planter'] = debug_input
							print("State modified.")
							continue
						except:
							print("Invalid input.  Returning to modify state menu.")
							continue		
					if debug_input == "flashlight":
						print("Current state is "
							 f"{game_states['flashlight']}")
						print("Enter the desired state (1 (not on) or "
							  "1 (on))")
						debug_input = input("\n> ")
						try:
							debug_input = debug_input.strip()
							debug_input = int(debug_input)
							game_states['flashlight'] = debug_input
							print("State modified.")
							continue
						except:
							print("Invalid input.  Returning to modify state menu.")
							continue	
					if debug_input == "flashlightbatteries":
						print("Current state is "
							 f"{game_states['flashlightbatteries']}")
						print("Enter the desired state (0 (not in "
							  "flashlight) or 1 (in flashlight))")
						debug_input = input("\n> ")
						try:
							debug_input = debug_input.strip()
							debug_input = int(debug_input)
							game_states['flashlightbatteries'] = debug_input
							print("State modified.")
							continue
						except:
							print("Invalid input.  Returning to modify state menu.")
							continue	
					if debug_input == "irongate":
						print("Current state is "
							 f"{game_states['irongate']}")
						print("Enter the desired state (0 (locked) "
							  "or 1 (unlocked))")
						debug_input = input("\n> ")
						try:
							debug_input = debug_input.strip()
							debug_input = int(debug_input)
							game_states['irongate'] = debug_input
							print("State modified.")
							continue
						except:
							print("Invalid input.  Returning to modify state menu.")
							continue	
					if debug_input == "escaped":
						print("Current state is "
							 f"{game_states['escaped']}")
						print("Enter the desired state (0 (not escaped) "
							  "or 1 (escaped))")
						debug_input = input("\n> ")
						try:
							debug_input = debug_input.strip()
							debug_input = int(debug_input)
							game_states['escaped'] = debug_input
							print("State modified.")
							continue
						except:
							print("Invalid input.  Returning to modify state menu.")
							continue																																																										
					if debug_input == "exit":
						debug()
					else:
						print("Not a valid input.")
						continue		

			if debug_input == "3":
				print("\t\t-----------------------------------------------")
				print("\n\t\t\t      DEBUG - CHANGE ROOM\n")
				print("\t\t-----------------------------------------------")
				print("\n\nEnter the name of the area you want to go to: ")
				print('List of rooms: Center, North, East, South, West')	
				print('Type "exit" to go back to debug main menu.')												
				while True:
					debug_input = input("\n> ")
					debug_input = debug_input.strip()
					debug_input = debug_input.lower()
					if debug_input == 'center':
						centerroom()
					if debug_input == 'north':
						northroom()
					if debug_input == 'south':
						southroom()
					if debug_input == 'east':
						eastroom()
					if debug_input == 'west':
						westroom()
					if debug_input == 'exit':
						debug()
					else:
						print("Not a valid input.")
						continue

			if debug_input == '4':
				if game_states["roomid"] == 1:
					centerroom()
				if game_states["roomid"] == 2:
					eastroom()	
				if game_states["roomid"] == 3:
					westroom()	
				if game_states["roomid"] == 4:
					southroom()	
				if game_states["roomid"] == 5:
					northroom()		
				else:
					print("\t\t-----------------------------------------------")
					print("\n\t\t\t\t   DEBUG\n")
					print("\t\t-----------------------------------------------\n\n")
					print("Invalid room id.\n")
					continue                                                            

			else:
				print("Not a valid input.\n")
				continue

#######################################################################
#                              OPENING                                #
#######################################################################
def opening():
	while True:
		clear()
		print("\t\t-----------------------------------------------")
		print("\n\t\t\t\t   ESCAPE\n")
		print("\t\t-----------------------------------------------")
		print("\n\n\nSomehow you have ended up in this strange area.")
		print("\nYou have no recollection of how you ended up in here, "
		      "\nbut you do know that you need to escape.")
		print("\nCan you escape?")
		print('\n\n\n\nPress enter to begin the game or type "HELP"'
			  'and press enter to see \ninstruction on how to '
                          'interact with the game.\n')
		player_input = input("> ")
		player_input = player_input.strip()		
		player_input = player_input.lower()
		if player_input == "help":
			clear()
			print("\t\t-----------------------------------------------")
			print("\n\t\t\t\t   ESCAPE")
			print("\n\t\t-----------------------------------------------")          
			print('\n"Escape" is a text advetnure game. You type what you '
				  'would like to do.')
			print("\nHere's a list of commands you can type in the game:")
			print("LOOK, TAKE, PRESS or PUSH, SEARCH, INSERT, OPEN, CLOSE, "
				  "\nTURN ON, TURN OFF, USE, UNLOCK")
			print("\nSome examples of commands: LOOK DIAMOND, TAKE DIAMOND,")
			print("OPEN BOX WITH KEY, TURN ON LANTERN, INSERT COIN INTO TUBE")
			print('\nAvoid using words such as "the", "a", "an", and "at". '
				  'Keep it simple.')
			print('\nType "n" or "north", "s" or "south", "e" or "east", and '
				  '"w" or "west" \nto go to a room in that direction.')                 
			print('\nType "inventory" or "i" to see your inventory at any '
				  'time.')              
			print('\nType "quit" or "q" to quit the game at any time.')         
			print("\nPress enter to begin the game.")
			input("")
			centerroom()
		else:
			centerroom()

#######################################################################
#                               MAIN                                  #
#######################################################################
def main():
	opening()


# Game begins here.
main()	
