import pygame, sys
from pygame.locals import *
import random
#importing libraries(pygame,random)
mainClock = pygame.time.Clock()

pygame.init()
#Initialisation pygame modules 
pygame.display.set_caption("Battleship")
#The window screen name
screen = pygame.display.set_mode((800, 800),0,32)
#The size of screen, 800 by 800.
title = pygame.font.SysFont(None, 60)
Ntitle = pygame.font.SysFont(None, 30)
#Differnt type of text sizes/fonts. Title is font 60 whereas Ntitle is font 30
 
def draw_text(text, title, color, surface, x, y):
  textobj = title.render(text, 1, color)
  textrect = textobj.get_rect()
  textrect.topleft = (x, y)
  surface.blit(textobj, textrect)
#This function outputs text onto the screen. The parameters in the function are text,title,color,surface,x,y. Text is the actual text outputted and speach marks "" 
#are put around the text to indicate what the text is. The title is the font/ font size and the two things that can be entered is title and Ntitle(look above to see what
#those do). Color allows the colour of the text to be changed, this can be entered as a hexadecimal value IE FF,FF,FF for white or a variable that is set as a 
#hexadecimal value for example if the variable white=(255,255,255), white can be written as the color. Surface is just where the text is being displayed normally screen
#and x/y is the x and y cordinates of the text. The x and y cordinates are written as numbers.
def username():
	running = True
	while running:
		font = pygame.font.Font(None, 32)
		input_box = pygame.Rect(20, 100, 140, 32)
#This the actual input box and its dimentions. The first two values are X and Y respectively and the last two values are the the size of the input box. The third value
#is the length of the box and the forth value is the height of the box.
		color_inactive = pygame.Color("lightskyblue3")
# This is the colour of the box when the user hasnt clicked on the box.
		color_active = pygame.Color("dodgerblue2")
#This is the colour of the box when the user has clicked on the box.
		color = color_inactive
#Presets the color to color inactive so the box is that colour by default.
		active = False
		text = ""
		done = False
		
		while not done:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					done = True
				if event.type == pygame.MOUSEBUTTONDOWN:
					if input_box.collidepoint(event.pos):
#This firstly checks if the mousebutton is pressed down. If it is it will go to the next if statement which saying if the mouse position is on the text box active=not
#active. This will then get used in another if statement.
						active = not active
					else:
						active = False
					color = color_active if active else color_inactive
#Changing the colour of the input box depending if active is True or False. 
				if event.type == pygame.KEYDOWN:
					if active:
						if event.key == pygame.K_RETURN:
							if text=="":
								print("Please enter a username")
#Checks if the text box is empty
							else:
								name=text
								gamemodes(name)
#This gives the name the value of text and then the function gamemodes is ran with name being sent with it.
						elif event.key == pygame.K_BACKSPACE:
							text = text[:-1]
#Checks if the user backspaces the type box. If they do it removes one letter from the end of the text. 
						else:
							text += event.unicode
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				if event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						running = False
						main_menu()
			screen.fill((0, 0, 0))
			draw_text("Login", title, (255, 255, 255), screen, 320, 20)
			draw_text("Your username:", Ntitle, (255,255,255),screen , 20, 80)
#Outputting the login and username text on the screen
			txt_surface = font.render(text, True, color)
#This is place where the text is getting outputted on.
			width = max(150, txt_surface.get_width()+10)
			input_box.w = width
			screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
#outputting the text box on the screen
			pygame.draw.rect(screen, color, input_box, 2)

			pygame.display.flip()
			mainClock.tick(60)
#function for a username 
def gamemodes(name):
	click=False
	running = True
	computerlvl="medium"
	gametype="classic"
	board="10x10"
#Default variables. This means that if the user forgets to choose choose something like the board size it will default to 10x10.
	while running == True:
		screen.fill((0,0,0))
		font=pygame.font.Font(None,32)
		mx, my = pygame.mouse.get_pos()
#Find the position of the mouse 
		def boardsize(x, y):
			boardS= font.render("The board size is going to be : "+ str(board),True,(255,255,255))
			screen.blit(boardS,(x,y))
		def complevel(x, y):
			complvl= font.render("The computer difficulty is : "+ str(computerlvl),True,(255,255,255))
			screen.blit(complvl,(x,y))
		def mode(x, y):
			modetype= font.render("The game type is : "+ str(gametype),True,(255,255,255))
			screen.blit(modetype,(x,y))
		draw_text("What size board do you want?", Ntitle, (255, 255, 255), screen, 50, 10)
		draw_text("8x8", Ntitle, (255, 255, 255), screen, 50, 30)
		draw_text("10x10", Ntitle, (255, 255, 255), screen, 250, 30)
		draw_text("12x12", Ntitle, (255, 255, 255), screen, 450, 30)
		draw_text("What level do you want the computer to be?", Ntitle, (255, 255, 255), screen, 50, 110)
		draw_text("Easy", Ntitle, (255, 255, 255), screen, 50, 130)
		draw_text("Medium", Ntitle, (255, 255, 255), screen, 250, 130)
		draw_text("Hard", Ntitle, (255, 255, 255), screen, 450, 130)
		draw_text("What gamemode do you want to play?", Ntitle, (255, 255, 255), screen, 50, 210)
		draw_text("Classic", Ntitle, (255, 255, 255), screen, 50, 230)
		draw_text("Advanced", Ntitle, (255, 255, 255), screen, 250, 230)
		draw_text("Salvo", Ntitle, (255, 255, 255), screen, 450, 230)
		draw_text("Ready?", title, (255, 255, 255), screen, 250, 310)
		draw_text("Help?", title, (255, 255, 255), screen, 600, 130)
#This outputs the text on the screen. The last two values are the X and Y coordinates.
		button_8x8 = pygame.Rect(50, 50, 100, 30)
		button_10x10 = pygame.Rect(250, 50, 100, 30)
		button_12x12 = pygame.Rect(450, 50, 100, 30)
		button_easy = pygame.Rect(50, 150, 100, 30)
		button_medium = pygame.Rect(250, 150, 100, 30)
		button_hard = pygame.Rect(450, 150, 100, 30)
		button_classic = pygame.Rect(50, 250, 100, 30)
		button_advanced = pygame.Rect(250, 250, 100, 30)
		button_salvo = pygame.Rect(450, 250, 100, 30)
		button_ready = pygame.Rect(50, 350, 500, 30)
		button_help = pygame.Rect(600, 170, 100, 30)
#Creating the clickable buttons. The first two values are the X and Y coordiantes and the last two values are the size of the box in terms of width and height.
		pygame.draw.rect(screen, (255, 0, 0), button_8x8)
		pygame.draw.rect(screen, (255, 0, 0), button_10x10)
		pygame.draw.rect(screen, (255, 0, 0), button_12x12) 
		pygame.draw.rect(screen, (255, 0, 0), button_easy)
		pygame.draw.rect(screen, (255, 0, 0), button_medium)
		pygame.draw.rect(screen, (255, 0, 0), button_hard)
		pygame.draw.rect(screen, (255, 0, 0), button_classic)
		pygame.draw.rect(screen, (255, 0, 0), button_advanced) 
		pygame.draw.rect(screen, (255, 0, 0), button_salvo)
		pygame.draw.rect(screen, (255, 0, 0), button_ready)
		pygame.draw.rect(screen, (255, 0, 0), button_help)
#Outputting the buttons on the screen. The first value tells which screen the box is getting outputted to if you have multiple screens. In this case it just outputtes 
#it onto screen which is basically the background. THe second value is the colour of the box.
		boardsize(50,400)
		complevel(50,450)
		mode(50,500)
#Tells the user what the game settings are
		pygame.display.flip()
		mainClock.tick(60)
		if button_8x8.collidepoint((mx, my)):
			if click:
				board="8x8"
		if button_10x10.collidepoint((mx, my)):
			if click:
				board="10x10"
		if button_12x12.collidepoint((mx, my)):
			if click:
				board="12x12"	
		if button_easy.collidepoint((mx, my)):
			if click:
				computerlvl="easy"
		if button_medium.collidepoint((mx, my)):
			if click:
				computerlvl="medium"
		if button_hard.collidepoint((mx, my)):
			if click:
				computerlvl="hard"
		if button_classic.collidepoint((mx, my)):
			if click:
				gametype="classic"
		if button_advanced.collidepoint((mx, my)):
			if click:
				gametype="advanced"
		if button_salvo.collidepoint((mx, my)):
			if click:
				gametype="salvo"
#These if statments firstly checks if the mouse is on top of a button for example if the mouse is on top of the button_8x8. If this is true then the code checks if the
#left mouse button is clicked or not. If it is then board=8x8. All of this is within a while statement and is constantly checking if left mouse button is clicked and if
#its over a box.
		if button_ready.collidepoint((mx, my)):
			if click:
				print("The board size is,",board)
				if computerlvl=="easy":
					print("The computer level is easy")
				elif computerlvl=="medium":
					print("The computer level is medium")
				else:
					print("The computer level is hard")
				if gametype=="classic":
					print("The game mode is classic")
				elif gametype=="advanced":
					print("The game mode is advanced")
				else:
					print("The game mode is salvo")
#This checks if the button ready is clicked. If it is then it goes though a series of if statements to tell the user what the game rules and setting are.
				setup(board,name,gametype,computerlvl,)
#This goes to the function setup and gives the varibles board,name,gametype with it.(computerlvl)
		if button_help.collidepoint((mx, my)):
			if click:
				help2(name)
#Checks if the user clicks on the help button.
		click = False
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					username()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True
#function for selection different options for the game
def main_menu():
	click=False
	background=pygame.image.load("Main menu background.jpg")
	while True:
		screen.fill((0,0,0))
		screen.blit(background,(0,0))
		draw_text('Battleship, the online board game!', title, (0, 0, 0), screen, 50, 150, )
		draw_text("login:" , title, (0, 0, 0), screen, 300, 600, )
		draw_text("Help:" , title, (0, 0, 0), screen, 55, 650, )
		draw_text("Credits:",title,(0,0,0),screen, 545,650,)
#Outputs the text battleship,login and help onto the screen.
		mx, my = pygame.mouse.get_pos()
#Finds the x and y postion of the mouse and puts it in the variables mx and my
		button_login = pygame.Rect(305, 650, 100, 30)
		button_username = pygame.Rect(60, 700, 100, 30)
		button_credits = pygame.Rect(550,700,100,30)
#Creating the buttons for login and username.
		if button_login.collidepoint((mx, my)):
			if click:
				username()	
		if button_username.collidepoint((mx, my)):
			if click:
				help()
		if button_credits.collidepoint((mx,my)):
			if click:
				credits()
#Checks if the buttons have been clicked on with mouse left button
		pygame.draw.rect(screen, (255, 0, 0, ), button_login)
		pygame.draw.rect(screen, (34, 102, 186 ), button_username) 
		pygame.draw.rect(screen, (34, 102, 186 ), button_credits) 
#Draws the two boxes of button_login and button_username.
		click = False
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True
#Checking for the users clicks with mouse left button. Also it checks if the user wants to close the game window and if so it quits the program and if the user presses 
#the esc key.
		pygame.display.update()
		mainClock.tick(60)
#function for the main menu screen. This is the first screen that the user sees.
def help():
	running = True
	while running:
		screen.fill((0,0,0))
		draw_text('Help/instructions', title, (255, 255, 255), screen, 5, 20)
		draw_text("Battleship-The complete help and instructions guide",Ntitle, (255,255,255), screen,5, 60 )
		draw_text("The goal is to destroy all of your enemy ships before they destroy yours. ",Ntitle, (255,255,255), screen,5, 80 )
		draw_text("The game is round based where each player has one guess per round.",Ntitle, (255,255,255), screen,5, 100 )
		draw_text("The players should start by placing all of their ships.",Ntitle, (255,255,255), screen,5, 120 )
		draw_text("If a player guesses a square and hits an enemy ship it displays hit.",Ntitle, (255,255,255), screen,5, 140 )
		draw_text("It will also change the square guessed to red.",Ntitle, (255,255,255), screen,5, 160 )
		draw_text("If the guess was a miss the square will be changed to blue.",Ntitle, (255,255,255), screen,5, 180 )
		draw_text("The main objective is to destroy your enemy's battleships.",Ntitle, (255,255,255), screen,5, 200 )
		draw_text("Once you destroy all of your enemy's ships, you win!",Ntitle, (255,255,255), screen,5, 220 )
		draw_text("There are three main game types: Classic, Advanced and salvo.",Ntitle, (255,255,255), screen,5, 240 )
		draw_text("The basic and arguably the hardest game type is classic.",Ntitle, (255,255,255), screen,5, 260 )
		draw_text("This is the base version of the game where you guess the location of the ships.",Ntitle, (255,255,255), screen,5, 280 )
		draw_text("Salvo is similar to classic where nothing major has changed. The only- ",Ntitle, (255,255,255), screen,5, 300 )
		draw_text("-difference is that when a player hits a ship, they are able to guess again.",Ntitle, (255,255,255), screen,5, 320 )
		draw_text("This just allows players to snowball the game or give then a chance of winning-",Ntitle, (255,255,255), screen,5, 340 )
		draw_text("-regardless of the situation.",Ntitle, (255,255,255), screen,5, 360 )
		draw_text("Advanced incorporates a new game mechanic.",Ntitle, (255,255,255), screen,5, 380 )
		draw_text("Abilities are enabled in the advanced mode and these abilities have the power-",Ntitle, (255,255,255), screen,5, 400 )
		draw_text("-Of changing the winner of the game.",Ntitle, (255,255,255), screen,5, 420 )
		draw_text("More on abilties below.",Ntitle, (255,255,255), screen,5, 440 )
		draw_text("In this version of battleship you will have the options of chosing the board size,",Ntitle, (255,255,255), screen,5, 460 )
		draw_text("the difficulty of the computer,",Ntitle, (255,255,255), screen,5, 480 )
		draw_text("And The game type(Classic,Advanced,Salvo).",Ntitle, (255,255,255), screen,5, 500 )
		draw_text("Abilities:",title, (255,255,255), screen,5, 520 )
		draw_text("Abilities are bought through coins which are earnt by hitting and destoying ship.",Ntitle, (255,255,255), screen,5, 560 )		
		draw_text("Ability 1-Air superiority(horizontal), price-50 coins.",Ntitle, (255,255,255), screen,5, 580 )
		draw_text("Ability 2-Air superiority(verical), price-50 coins.",Ntitle, (255,255,255), screen,5, 600 )
		draw_text("Ability 3-Grid shot, price-30 coins.",Ntitle, (255,255,255), screen,5, 620 )
		draw_text("Ability 1 Hits an entire row horizontally. Careful, to get the maximun value of-",Ntitle, (255,255,255), screen,5, 640 )
		draw_text("-this ability aim it at the top row.",Ntitle, (255,255,255), screen,5, 660 )
		draw_text("Ability 2 Hits an entire row vertically. Careful, to get the maximun value of-",Ntitle, (255,255,255), screen,5, 680 )
		draw_text("-this ability aim it at the left hand side column.",Ntitle, (255,255,255), screen,5, 700 )
		draw_text("Ability 3 Hits an area in a 3x3 grid. Aim this at as many unguessed locations-",Ntitle, (255,255,255), screen,5, 720 )
		draw_text("-to get the maximun value out of this ability.",Ntitle, (255,255,255), screen,5, 740 )
#All the text outputted on the help menu screen.

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					running = False
        
		pygame.display.update()
		mainClock.tick(60)
#function for the help screen
def help2(name):
	running = True
	while running:
		screen.fill((0,0,0))
		draw_text('Help/instructions', title, (255, 255, 255), screen, 5, 20)
		draw_text("Battleship-The complete help and instructions guide",Ntitle, (255,255,255), screen,5, 60 )
		draw_text("The goal is to destroy all of your enemy ships before they destroy yours. ",Ntitle, (255,255,255), screen,5, 80 )
		draw_text("The game is round based where each player has one guess per round.",Ntitle, (255,255,255), screen,5, 100 )
		draw_text("The players should start by placing all of their ships.",Ntitle, (255,255,255), screen,5, 120 )
		draw_text("If a player guesses a square and hits an enemy ship it displays hit.",Ntitle, (255,255,255), screen,5, 140 )
		draw_text("It will also change the square guessed to red.",Ntitle, (255,255,255), screen,5, 160 )
		draw_text("If the guess was a miss the square will be changed to blue.",Ntitle, (255,255,255), screen,5, 180 )
		draw_text("The main objective is to destroy your enemy's battleships.",Ntitle, (255,255,255), screen,5, 200 )
		draw_text("Once you destroy all of your enemy's ships, you win!",Ntitle, (255,255,255), screen,5, 220 )
		draw_text("There are three main game types: Classic, Advanced and salvo.",Ntitle, (255,255,255), screen,5, 240 )
		draw_text("The basic and arguably the hardest game type is classic.",Ntitle, (255,255,255), screen,5, 260 )
		draw_text("This is the base version of the game where you guess the location of the ships.",Ntitle, (255,255,255), screen,5, 280 )
		draw_text("Salvo is similar to classic where nothing major has changed. The only- ",Ntitle, (255,255,255), screen,5, 300 )
		draw_text("-difference is that when a player hits a ship, they are able to guess again.",Ntitle, (255,255,255), screen,5, 320 )
		draw_text("This just allows players to snowball the game or give then a chance of winning-",Ntitle, (255,255,255), screen,5, 340 )
		draw_text("-regardless of the situation.",Ntitle, (255,255,255), screen,5, 360 )
		draw_text("Advanced incorporates a new game mechanic.",Ntitle, (255,255,255), screen,5, 380 )
		draw_text("Abilities are enabled in the advanced mode and these abilities have the power-",Ntitle, (255,255,255), screen,5, 400 )
		draw_text("-Of changing the winner of the game.",Ntitle, (255,255,255), screen,5, 420 )
		draw_text("More on abilties below.",Ntitle, (255,255,255), screen,5, 440 )
		draw_text("In this version of battleship you will have the options of chosing the board size,",Ntitle, (255,255,255), screen,5, 460 )
		draw_text("the difficulty of the computer,",Ntitle, (255,255,255), screen,5, 480 )
		draw_text("And The game type(Classic,Advanced,Salvo).",Ntitle, (255,255,255), screen,5, 500 )
		draw_text("Abilities:",title, (255,255,255), screen,5, 520 )
		draw_text("Abilities are bought through coins which are earnt by hitting and destoying ship.",Ntitle, (255,255,255), screen,5, 560 )		
		draw_text("Ability 1-Air superiority(horizontal), price-50 coins.",Ntitle, (255,255,255), screen,5, 580 )
		draw_text("Ability 2-Air superiority(verical), price-50 coins.",Ntitle, (255,255,255), screen,5, 600 )
		draw_text("Ability 3-Grid shot, price-30 coins.",Ntitle, (255,255,255), screen,5, 620 )
		draw_text("Ability 1 Hits an entire row horizontally. Careful, to get the maximun value of-",Ntitle, (255,255,255), screen,5, 640 )
		draw_text("-this ability aim it at the top row.",Ntitle, (255,255,255), screen,5, 660 )
		draw_text("Ability 2 Hits an entire row vertically. Careful, to get the maximun value of-",Ntitle, (255,255,255), screen,5, 680 )
		draw_text("-this ability aim it at the left hand side column.",Ntitle, (255,255,255), screen,5, 700 )
		draw_text("Ability 3 Hits an area in a 3x3 grid. Aim this at as many unguessed locations-",Ntitle, (255,255,255), screen,5, 720 )
		draw_text("-to get the maximun value out of this ability.",Ntitle, (255,255,255), screen,5, 740 )
#All the text outputted on the help menu screen.

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					running = False
					gamemodes(name)
        
		pygame.display.update()
		mainClock.tick(60)
#function for the help screen for gamemodes
def credits():
	running = True
	while running:
		screen.fill((0,0,0))
		draw_text("Game created and coded by:", title, (255, 255, 255), screen, 5, 20)
		draw_text("Christopher, K1ngCT ,Tang", title, (255, 255, 255), screen, 5, 60)
		draw_text("All sprites and background images were found online.", Ntitle, (255, 255, 255), screen, 5, 100)
		draw_text("Special thanks to David for being my beta tester and stakeholder.", Ntitle, (255, 255, 255), screen, 5, 120)
#All the text outputted on the credits screen
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					running = False
        
		pygame.display.update()
		mainClock.tick(60)
#credits function
def setup(board,name,gametype,computerlvl):
	click=False
	abilitycount=0
	background=(255,255,255)
	backpng=pygame.image.load("background.png")
	img1 = pygame.image.load("Ship1.png")
	img2 = pygame.image.load("Ship2.png")
	img3 = pygame.image.load("Ship3.png")
	img4 = pygame.image.load("Ship4.png")
	img5 = pygame.image.load("Ship5.png")
#loading all the images and storing them in variables.
	images = [img5, img3, img4, img1, img2]
#Creating a list of all of the images. This will make it easier to program the images in the future.
	button_ready = pygame.Rect(400, 170, 100, 30)
#Creating a ready button which the user clicks when they have done setting up their ships
	pygame.draw.rect(screen, (255, 0, 0), button_ready)
#Outputting the button, ready,  on the screen.
	current_image = -1
	img_rects = [images[i].get_rect(topleft = (20+110*i, 20)) for i in range(len(images))]
#Makes every image a rect. You need to get_rect images so you can move them around. The for statement just goes through every image in images.

	LeftButton = 0
	while 1:
		mx, my = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				exit(0)

			if event.type == pygame.MOUSEBUTTONDOWN:
				mouse_rect = pygame.Rect(event.pos, (1, 1))
				current_image = mouse_rect.collidelist(img_rects)
#Checks firstly if the mouse left button is clicked. If it is it finds the mouse position and if the mouse position is on a image then current image=that image.

			if event.type == MOUSEMOTION:
				if event.buttons[LeftButton]:
					rel = event.rel
#Checks if the mouse is moving and if the left button is getting pressed down.
					if 0 <= current_image < len(images):
						img_rects[current_image].x += rel[0]
						img_rects[current_image].y += rel[1]
#Moves the image in the Y and X coordinaes acording to the new mouse position

			if button_ready.collidepoint((mx,my)):
				if event.type == pygame.MOUSEBUTTONDOWN:
					Guessphase(board,name,gametype,computerlvl,abilitycount)
#Checks if the user clicks on the ready button or not. If they do then the function guessphase now runs with the variables board, name and gametype sent along with it.
#These variables are not used in this function but will be used later on in the program.
		screen.fill(background)
		for i in range(len(images)):
			screen.blit(backpng,(0,0))
			screen.blit(images[i], img_rects[i],)
			screen.blit(images[i-1], img_rects[i-1],)
			screen.blit(images[i-2], img_rects[i-2],)
			screen.blit(images[i-3], img_rects[i-3],)
			screen.blit(images[i-4], img_rects[i-4],)
#Outputs the images onto the screen. Also outputs the background png which is the grid.
			draw_text("Ready?", Ntitle, (0,0,0),screen , 400, 150)
			pygame.draw.rect(screen, (255, 0, 0), button_ready)
#Outputs the text ready and outputs the button, ready, underneath it.

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					gamemodes(name)
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True

		pygame.display.flip()
		pygame.time.delay(60)
#Placing ships function
def Guessphase(board,name,gametype,computerlvl,abilitycount):
	black = (0,0,0)
	white = (255, 255, 255)
	red = (255, 0, 0)
	blue =(0,0,255)
	WIDTH = 40
	HEIGHT = 40
	MARGIN = 5
	
	grid = []
	background=(black)
	running=True
	guess_value=0
	if board=="8x8" and gametype=="classic":
		font=pygame.font.Font(None,32)
		def guess(x, y):
			guesses= font.render("Guess : "+ str(guess_value),True,(white))
			screen.blit(guesses,(x,y))

		shipsdestroyed=0

		def ShipDestroyed(x, y):
			shipsDes=font.render("Ships destroyed : "+str(shipsdestroyed),True,(white))
			screen.blit(shipsDes,(x,y))

		shipsalive=5

		def ShipsAlive(x, y):
			ShipsAli=font.render("Ships left : " +str(shipsalive),True,(white))
			screen.blit(ShipsAli,(x,y))
			
		x1=random.randint(0,2)
		x2=random.randint(3,5)
		x3=random.randint(6,7)
		x4=random.randint(0,4)
		x5=random.randint(5,7)
		y1=random.randint(0,2)
		y2=random.randint(0,2)
		y3=random.randint(0,1)
		y4=random.randint(3,7)
		y5=random.randint(3,4)
		y6=random.randint(0,2)
		directionShip1=random.randint(1,2)
		directionShip2=random.randint(1,2)
		directionShip3=random.randint(1,2)
		directionShip4=random.randint(1,2)
		screen = pygame.display.set_mode((800, 800),0,32)
		running=True
		
		while running==True:
			if running==True:
				for row in range(8):
					grid.append([0])
					for column in range(8):
						grid[row].append(0) 
				done = False
				clock = pygame.time.Clock()
				while not done: 
					for event in pygame.event.get(): 
						if event.type == pygame.QUIT: 
							done = True 
						elif event.type == pygame.MOUSEBUTTONDOWN:
							pos = pygame.mouse.get_pos()
							column = pos[0] // (WIDTH + MARGIN)
							row = pos[1] // (HEIGHT + MARGIN)
							if grid[row][column]==0:
								grid[row][column]=1
								print("Grid location: ",row,column)
								guess_value=guess_value+1
								if directionShip1==1:
									if grid[0][x1]==1 or grid[1][x1]==1 or grid[2][x1]==1:
										grid[row][column]=2
										print("Hit")
#vertical 3x1
								elif directionShip1==2:
									if grid[y1][0]==1 or grid[y1][1]==1 or grid[y1][2]==1:
										grid[row][column]=2
										print("Hit")
#horizontal	3x1									
								if directionShip2==1:	
									if grid[0][x2]==1 or grid[1][x2]==1 or grid[2][x2]==1:
										grid[row][column]=2
										print("Hit")
#vertical	3x1(2)
								elif directionShip2==2:
									if grid[y2][3]==1 or grid[y2][4]==1 or grid[y2][5]==1:
										grid[row][column]=2
										print("Hit")
#horizontal	3x1(2)								
								if directionShip3==1:
									if grid[y3][x3]==1 or grid[y3+1][x3]==1:
										grid[row][column]=2
										print("Hit")
#vertical 2x1
								elif directionShip3==2:
									if grid[y6][6]==1 or grid[y6][7]==1:
										grid[row][column]=2
										print("Hit")
#horizontal 2x1
								if directionShip4==1:
									if grid[3][x4]==1 or grid[4][x4]==1 or grid[5][x4]==1 or grid[6][x4]==1 or grid[7][x4]==1:
										grid[row][column]=2
										print("Hit")
#vertical 5x1									
								elif directionShip4==2:
									if grid[y4][0]==1 or grid[y4][1]==1 or grid[y4][2]==1 or grid[y4][3]==1 or grid[y4][4]==1:
										grid[row][column]=2
										print("Hit")
#horizontal 5x1										
								if grid[y5][x5]==1 or grid[y5+1][x5]==1 or grid[y5+2][x5]==1 or grid[y5+3][x5]==1:
									grid[row][column]=2
									print("Hit")
#vertical 4x1

#checking for ship sunk
								if directionShip1==1:
									if grid[0][x1]==2 and grid[1][x1]==2 and grid[2][x1]==2:
										grid[0][x1]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#vertical 3x1
								elif directionShip1==2:
									if grid[y1][0]==2 and grid[y1][1]==2 and grid[y1][2]==2:
										grid[y1][0]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#horizontal	3x1									
								if directionShip2==1:	
									if grid[0][x2]==2 and grid[1][x2]==2 and grid[2][x2]==2:
										grid[0][x2]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#vertical	3x1(2)
								elif directionShip2==2:
									if grid[y2][3]==2 and grid[y2][4]==2 and grid[y2][5]==2:
										grid[y2][3]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#horizontal	3x1(2)								
								if directionShip3==1:
									if grid[y3][x3]==2 and grid[y3+1][x3]==2:
										grid[y3][x3]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#vertical 2x1
								elif directionShip3==2:
									if grid[y6][6]==2 and grid[y6][7]==2:
										grid[y6][6]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#horizontal 2x1
								if directionShip4==1:
									if grid[3][x4]==2 and grid[4][x4]==2 and grid[5][x4]==2 and grid[6][x4]==2 and grid[7][x4]==2:
										grid[3][x4]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#vertical 5x1									
								elif directionShip4==2:
									if grid[y4][0]==2 and grid[y4][1]==2 and grid[y4][2]==2 and grid[y4][3]==2 and grid[y4][4]==2:
										grid[y4][0]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#horizontal 5x1										
								if grid[y5][x5]==2 and grid[y5+1][x5]==2 and grid[y5+2][x5]==2 and grid[y5+3][x5]==2:
									grid[y5][x5]=3
									shipsdestroyed=shipsdestroyed+1
									shipsalive=shipsalive-1
									print("Ship sunk")
#vertical 4x1
							elif grid[row][column]==1 or grid[row][column]==2 or grid[row][column]==3:
								print("Location already guessed. Try another location.")
							if shipsdestroyed==5:
								winning(guess_value,name,computerlvl,abilitycount,gametype)
							if computerlvl=="easy":
								if guess_value==48:
									losing(guess_value,shipsdestroyed,name,computerlvl,gametype,abilitycount,shipsalive)
							elif computerlvl=="medium":
								if guess_value==30:
									losing(guess_value,shipsdestroyed,name,computerlvl,gametype,abilitycount,shipsalive)
							elif computerlvl=="hard":
								if guess_value==24:
									losing(guess_value,shipsdestroyed,name,computerlvl,gametype,abilitycount,shipsalive)
		
					for row in range(8):
						for column in range(8):
							color = (white)
							if grid[row][column]==1 :
								color = blue
							elif grid[row][column]==2:
								color=red
							elif grid[row][column]==3:
								color=red
							pygame.draw.rect(screen, color,[(MARGIN + WIDTH) * column + MARGIN,(MARGIN + HEIGHT) * row + MARGIN,WIDTH, HEIGHT])
					clock.tick(60)
					guess(370, 20)
					ShipDestroyed(370,100)
					ShipsAlive(370,60)
					pygame.display.flip()
					pygame.display.update()
					screen.fill(background)
#8x8 classic					
	elif board=="10x10" and gametype=="classic":
		font=pygame.font.Font(None,32)
		def guess(x, y):
			guesses= font.render("Guess : "+ str(guess_value),True,(white))
			screen.blit(guesses,(x,y))

		shipsdestroyed=0

		def ShipDestroyed(x, y):
			shipsDes=font.render("Ships destroyed : "+str(shipsdestroyed),True,(white))
			screen.blit(shipsDes,(x,y))

		shipsalive=5

		def ShipsAlive(x, y):
			ShipsAli=font.render("Ships left : " +str(shipsalive),True,(white))
			screen.blit(ShipsAli,(x,y))
			
		x1=random.randint(0,5)
		x2=random.randint(6,9)
		x3=random.randint(0,2)
		x4=random.randint(3,5)
		x5=random.randint(6,9)
		x6=random.randint(0,1)
		x7=random.randint(0,0)
		x8=random.randint(0,1)
		x9=random.randint(0,0)
		x10=random.randint(6,7)
		y1=random.randint(0,5)
		y2=random.randint(0,3)
		y3=random.randint(6,8)
		y4=random.randint(6,7)
		y5=random.randint(0,0)
		y6=random.randint(0,1)
		y7=random.randint(0,6)
		y8=random.randint(6,9)
		y9=random.randint(6,9)
		y10=random.randint(7,9)
		directionShip1=random.randint(1,2)
		directionShip2=random.randint(1,2)
		directionShip3=random.randint(1,2)
		directionShip4=random.randint(1,2)
		directionShip5=random.randint(1,2)
		screen = pygame.display.set_mode((800, 800),0,32)
		running=True
		
		while running==True:
			if running==True:
				for row in range(10):
					grid.append([0])
					for column in range(10):
						grid[row].append(0) 
				done = False
				clock = pygame.time.Clock()
				while not done: 
					for event in pygame.event.get(): 
						if event.type == pygame.QUIT: 
							done = True 
						elif event.type == pygame.MOUSEBUTTONDOWN:
							pos = pygame.mouse.get_pos()
							column = pos[0] // (WIDTH + MARGIN)
							row = pos[1] // (HEIGHT + MARGIN)
							if grid[row][column]==0:
								grid[row][column]=1
								print("Grid location: ",row,column)
								guess_value=guess_value+1
								if directionShip1==1:
									if grid[y6][x1]==1 or grid[y6+1][x1]==1 or grid[y6+2][x1]==1 or grid[y6+3][x1]==1 or grid[y6+4][x1]==1:
										grid[row][column]=2
										print("Hit")
#vertical 5x1
								elif directionShip1==2:
									if grid[y1][x6]==1 or grid[y1][x6+1]==1 or grid[y1][x6+2]==1 or grid[y1][x6+3]==1 or grid[y1][x6+4]==1:
										grid[row][column]=2
										print("Hit")
#horizontal	5x1									
								if directionShip2==1:	
									if grid[y2][x2]==1 or grid[y2+1][x2]==1 or grid[y2+2][x2]==1 or grid[y2+3][x2]==1:
										grid[row][column]=2
										print("Hit")
#vertical	4x1
								elif directionShip2==2:
									if grid[y7][6]==1 or grid[y7][7]==1 or grid[y7][8]==1 or grid[y7][9]==1:
										grid[row][column]=2
										print("Hit")
#horizontal	4x1								
								if directionShip3==1:
									if grid[y3][x3]==1 or grid[y3+1][x3]==1:
										grid[row][column]=2
										print("Hit")
#vertical 2x1
								elif directionShip3==2:
									if grid[y8][x8]==1 or grid[y8][x8+1]==1:
										grid[row][column]=2
										print("Hit")
#horizontal 2x1
								if directionShip4==1:
									if grid[y4][x4]==1 or grid[y4+1][x4]==1 or grid[y4+2][x4]==1:
										grid[row][column]=2
										print("Hit")
#vertical 3x1(1)									
								elif directionShip4==2:
									if grid[y9][3]==1 or grid[y9][4]==1 or grid[y9][5]==1:
										grid[row][column]=2
										print("Hit")
#horizontal 3x1(1)	
								if directionShip5==1:
									if grid[7][x5]==1 or grid[8][x5]==1 or grid[9][x5]==1:
										grid[row][column]=2
										print("Hit")
#vertical 3x1(2)
								elif directionShip5==2:
									if grid[y10][x10]==1 or grid[y10][x10+1]==1 or grid[y10][x10+2]==1:
										grid[row][column]=2
										print("Hit")
#hotizontal 3x1(2)

#checking for ship sunk
								if directionShip1==1:
									if grid[y6][x1]==2 and grid[y6+1][x1]==2 and grid[y6+2][x1]==2 and grid[y6+3][x1]==2 and grid[y6+4][x1]==2:
										grid[y6][x1]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#vertical 5x1
								elif directionShip1==2:
									if grid[y1][x6]==2 and grid[y1][x6+1]==2 and grid[y1][x6+2]==2 and grid[y1][x6+3]==2 and grid[y1][x6+4]==2:
										grid[y1][x6]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#horizontal	5x1									
								if directionShip2==1:	
									if grid[y2][x2]==2 and grid[y2+1][x2]==2 and grid[y2+2][x2]==2 and grid[y2+3][x2]==2:
										grid[y2][x2]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#vertical	4x1
								elif directionShip2==2:
									if grid[y7][6]==2 and grid[y7][7]==2 and grid[y7][8]==2 and grid[y7][9]==2:
										grid[y7][6]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#horizontal	4x1								
								if directionShip3==1:
									if grid[y3][x3]==2 and grid[y3+1][x3]==2:
										grid[y3][x3]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#vertical 2x1
								elif directionShip3==2:
									if grid[y8][x8]==2 and grid[y8][x8+1]==2:
										grid[y8][x8]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#horizontal 2x1
								if directionShip4==1:
									if grid[y4][x4]==2 and grid[y4+1][x4]==2 and grid[y4+2][x4]==2:
										grid[y4][x4]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#vertical 3x1(1)									
								elif directionShip4==2:
									if grid[y9][3]==2 and grid[y9][4]==2 and grid[y9][5]==2:
										grid[y9][3]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#horizontal 3x1(1)	
								if directionShip5==1:
									if grid[7][x5]==2 and grid[8][x5]==2 and grid[9][x5]==2:
										grid[7][x5]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#vertical 3x1(2)
								elif directionShip5==2:
									if grid[y10][x10]==2 and grid[y10][x10+1]==2 and grid[y10][x10+2]==2:
										grid[y10][x10]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#hotizontal 3x1(2)
							elif grid[row][column]==1 or grid[row][column]==2 or grid[row][column]==3:
								print("Location already guessed. Try another location.")
							if shipsdestroyed==5:
								winning(guess_value,name,computerlvl,abilitycount,gametype)
							if computerlvl=="easy":
								if guess_value==65:
									losing(guess_value,shipsdestroyed,name,computerlvl,gametype,abilitycount,shipsalive)
							elif computerlvl=="medium":
								if guess_value==45:
									losing(guess_value,shipsdestroyed,name,computerlvl,gametype,abilitycount,shipsalive)
							elif computerlvl=="hard":
								if guess_value==35:
									losing(guess_value,shipsdestroyed,name,computerlvl,gametype,abilitycount,shipsalive)
		
					for row in range(10):
						for column in range(10):
							color = (white)
							if grid[row][column]==1 :
								color = blue
							elif grid[row][column]==2:
								color=red
							elif grid[row][column]==3:
								color=red
							pygame.draw.rect(screen, color,[(MARGIN + WIDTH) * column + MARGIN,(MARGIN + HEIGHT) * row + MARGIN,WIDTH, HEIGHT])
					clock.tick(60)
					guess(460, 20)
					ShipDestroyed(460,100)
					ShipsAlive(460,60)
					pygame.display.flip()
					pygame.display.update()
					screen.fill(background)
#10x10 classic					
	elif board=="12x12" and gametype=="classic":
		font=pygame.font.Font(None,32)
		def guess(x, y):
			guesses= font.render("Guess : "+ str(guess_value),True,(white))
			screen.blit(guesses,(x,y))

		shipsdestroyed=0

		def ShipDestroyed(x, y):
			shipsDes=font.render("Ships destroyed : "+str(shipsdestroyed),True,(white))
			screen.blit(shipsDes,(x,y))

		shipsalive=5

		def ShipsAlive(x, y):
			ShipsAli=font.render("Ships left : " +str(shipsalive),True,(white))
			screen.blit(ShipsAli,(x,y))
			
		x1=random.randint(0,6)
		x2=random.randint(7,11)
		x3=random.randint(0,3)
		x4=random.randint(4,6)
		x5=random.randint(0,6)
		x6=random.randint(0,4)
		x7=random.randint(0,0)
		x8=random.randint(0,1)
		x9=random.randint(4,5)
		x10=random.randint(0,3)
		y1=random.randint(0,5)
		y2=random.randint(0,7)
		y3=random.randint(3,5)
		y4=random.randint(3,6)
		y5=random.randint(0,0)
		y6=random.randint(0,2)
		y7=random.randint(0,11)
		y8=random.randint(3,7)
		y9=random.randint(3,7)
		y10=random.randint(8,11)
		directionShip1=random.randint(1,2)
		directionShip2=random.randint(1,2)
		directionShip3=random.randint(1,2)
		directionShip4=random.randint(1,2)
		directionShip5=random.randint(1,2)
		screen = pygame.display.set_mode((800, 800),0,32)
		running=True
		
		while running==True:
			if running==True:
				for row in range(12):
					grid.append([0])
					for column in range(12):
						grid[row].append(0) 
				done = False
				clock = pygame.time.Clock()
				while not done: 
					for event in pygame.event.get(): 
						if event.type == pygame.QUIT: 
							done = True 
						elif event.type == pygame.MOUSEBUTTONDOWN:
							pos = pygame.mouse.get_pos()
							column = pos[0] // (WIDTH + MARGIN)
							row = pos[1] // (HEIGHT + MARGIN)
							if grid[row][column]==0:
								grid[row][column]=1
								print("Grid location: ",row,column)
								guess_value=guess_value+1
								if directionShip1==1:
									if grid[0][x1]==1 or grid[1][x1]==1 or grid[2][x1]==1:
										grid[row][column]=2
										print("Hit")
#vertical 3x1(1)
								elif directionShip1==2:
									if grid[y6][x6]==1 or grid[y6][x6+1]==1 or grid[y6][x6+2]==1:
										grid[row][column]=2
										print("Hit")
#horizontal	3x1(1)									
								if directionShip2==1:	
									if grid[y2][x2]==1 or grid[y2+1][x2]==1 or grid[y2+2][x2]==1 or grid[y2+3][x2]==1 or grid[y2+4][x2]:
										grid[row][column]=2
										print("Hit")
#vertical	5x1
								elif directionShip2==2:
									if grid[y7][7]==1 or grid[y7][8]==1 or grid[y7][9]==1 or grid[y7][10]==1 or grid[y7][11]==1:
										grid[row][column]=2
										print("Hit")
#horizontal	5x1								
								if directionShip3==1:
									if grid[y3][x3]==1 or grid[y3+1][x3]==1 or grid[y3+2][x3]==1:
										grid[row][column]=2
										print("Hit")
#vertical 3x1(2)
								elif directionShip3==2:
									if grid[y8][x8]==1 or grid[y8][x8+1]==1 or grid[y8][x8+2]==1:
										grid[row][column]=2
										print("Hit")
#horizontal 3x1(2)
								if directionShip4==1:
									if grid[y4][x4]==1 or grid[y4+1][x4]==1:
										grid[row][column]=2
										print("Hit")
#vertical 2x1									
								elif directionShip4==2:
									if grid[y9][x9]==1 or grid[y9][x9+1]==1:
										grid[row][column]=2
										print("Hit")
#horizontal 2x1	
								if directionShip5==1:
									if grid[8][x5]==1 or grid[9][x5]==1 or grid[10][x5]==1 or grid[11][x5]==1:
										grid[row][column]=2
										print("Hit")
#vertical 4x1
								elif directionShip5==2:
									if grid[y10][x10]==1 or grid[y10][x10+1]==1 or grid[y10][x10+2]==1 or grid[y10][x10+3]==1:
										grid[row][column]=2
										print("Hit")
#hotizontal 4x1

#checking for sunk ships
								if directionShip1==1:
									if grid[0][x1]==2 and grid[1][x1]==2 and grid[2][x1]==2:
										grid[0][x1]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#vertical 3x1(1)
								elif directionShip1==2:
									if grid[y6][x6]==2 and grid[y6][x6+1]==2 and grid[y6][x6+2]==2:
										grid[y6][x6]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#horizontal	3x1(1)									
								if directionShip2==1:	
									if grid[y2][x2]==2 and grid[y2+1][x2]==2 and grid[y2+2][x2]==2 and grid[y2+3][x2]==2 and grid[y2+4][x2]==2:
										grid[y2][x2]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#vertical	5x1
								elif directionShip2==2:
									if grid[y7][7]==2 and grid[y7][8]==2 and grid[y7][9]==2 and grid[y7][10]==2 and grid[y7][11]==2:
										grid[y7][7]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#horizontal	5x1								
								if directionShip3==1:
									if grid[y3][x3]==2 and grid[y3+1][x3]==2 and grid[y3+2][x3]==2:
										grid[y3][x3]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#vertical 3x1(2)
								elif directionShip3==2:
									if grid[y8][x8]==2 and grid[y8][x8+1]==2 and grid[y8][x8+2]==2:
										grid[y8][x8]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#horizontal 3x1(2)
								if directionShip4==1:
									if grid[y4][x4]==2 and grid[y4+1][x4]==2:
										grid[y4][x4]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#vertical 2x1									
								elif directionShip4==2:
									if grid[y9][x9]==2 and grid[y9][x9+1]==2:
										grid[y9][x9]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#horizontal 2x1	
								if directionShip5==1:
									if grid[8][x5]==2 and grid[9][x5]==2 and grid[10][x5]==2 and grid[11][x5]==2:
										grid[8][x5]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#vertical 4x1
								elif directionShip5==2:
									if grid[y10][x10]==2 and grid[y10][x10+1]==2 and grid[y10][x10+2]==2 and grid[y10][x10+3]==2:
										grid[y10][x10]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#hotizontal 4x1
							elif grid[row][column]==1 or grid[row][column]==2 or grid[row][column]==3:
								print("Location already guessed. Try another location.")
							if shipsdestroyed==5:
								winning(guess_value,name,computerlvl,abilitycount,gametype)
							if computerlvl=="easy":
								if guess_value==100:
									losing(guess_value,shipsdestroyed,name,computerlvl,gametype,abilitycount,shipsalive)
							elif computerlvl=="medium":
								if guess_value==65:
									losing(guess_value,shipsdestroyed,name,computerlvl,gametype,abilitycount,shipsalive)
							elif computerlvl=="hard":
								if guess_value==53:
									losing(guess_value,shipsdestroyed,name,computerlvl,gametype,abilitycount,shipsalive)
		
					for row in range(12):
						for column in range(12):
							color = (white)
							if grid[row][column]==1 :
								color = blue
							elif grid[row][column]==2:
								color=red
							elif grid[row][column]==3:
								color=red
							pygame.draw.rect(screen, color,[(MARGIN + WIDTH) * column + MARGIN,(MARGIN + HEIGHT) * row + MARGIN,WIDTH, HEIGHT])
					clock.tick(60)
					guess(560, 20)
					ShipDestroyed(560,100)
					ShipsAlive(560,60)
					pygame.display.flip()
					pygame.display.update()
					screen.fill(background)
#12x12 classic
	elif board=="8x8" and gametype=="salvo":
		font=pygame.font.Font(None,32)
		def guess(x, y):
			guesses= font.render("Round : "+ str(guess_value),True,(white))
			screen.blit(guesses,(x,y))

		shipsdestroyed=0

		def ShipDestroyed(x, y):
			shipsDes=font.render("Ships destroyed : "+str(shipsdestroyed),True,(white))
			screen.blit(shipsDes,(x,y))

		shipsalive=5

		def ShipsAlive(x, y):
			ShipsAli=font.render("Ships left : " +str(shipsalive),True,(white))
			screen.blit(ShipsAli,(x,y))
			
		x1=random.randint(0,2)
		x2=random.randint(3,5)
		x3=random.randint(6,7)
		x4=random.randint(0,4)
		x5=random.randint(5,7)
		y1=random.randint(0,2)
		y2=random.randint(0,2)
		y3=random.randint(0,1)
		y4=random.randint(3,7)
		y5=random.randint(3,4)
		y6=random.randint(0,2)
		directionShip1=random.randint(1,2)
		directionShip2=random.randint(1,2)
		directionShip3=random.randint(1,2)
		directionShip4=random.randint(1,2)
		screen = pygame.display.set_mode((800, 800),0,32)
		running=True
		
		while running==True:
			if running==True:
				for row in range(8):
					grid.append([0])
					for column in range(8):
						grid[row].append(0) 
				done = False
				clock = pygame.time.Clock()
				while not done: 
					for event in pygame.event.get(): 
						if event.type == pygame.QUIT: 
							done = True 
						elif event.type == pygame.MOUSEBUTTONDOWN:
							pos = pygame.mouse.get_pos()
							column = pos[0] // (WIDTH + MARGIN)
							row = pos[1] // (HEIGHT + MARGIN)
							if grid[row][column]==0:
								grid[row][column]=1
								print("Grid location: ",row,column)
								guess_value=guess_value+1
								if directionShip1==1:
									if grid[0][x1]==1 or grid[1][x1]==1 or grid[2][x1]==1:
										grid[row][column]=2
										guess_value=guess_value-1
										print("Hit")
#vertical 3x1
								elif directionShip1==2:
									if grid[y1][0]==1 or grid[y1][1]==1 or grid[y1][2]==1:
										grid[row][column]=2
										guess_value=guess_value-1
										print("Hit")
#horizontal	3x1									
								if directionShip2==1:	
									if grid[0][x2]==1 or grid[1][x2]==1 or grid[2][x2]==1:
										grid[row][column]=2
										guess_value=guess_value-1
										print("Hit")
#vertical	3x1(2)
								elif directionShip2==2:
									if grid[y2][3]==1 or grid[y2][4]==1 or grid[y2][5]==1:
										grid[row][column]=2
										guess_value=guess_value-1
										print("Hit")
#horizontal	3x1(2)								
								if directionShip3==1:
									if grid[y3][x3]==1 or grid[y3+1][x3]==1:
										grid[row][column]=2
										guess_value=guess_value-1
										print("Hit")
#vertical 2x1
								elif directionShip3==2:
									if grid[y6][6]==1 or grid[y6][7]==1:
										grid[row][column]=2
										guess_value=guess_value-1
										print("Hit")
#horizontal 2x1
								if directionShip4==1:
									if grid[3][x4]==1 or grid[4][x4]==1 or grid[5][x4]==1 or grid[6][x4]==1 or grid[7][x4]==1:
										grid[row][column]=2
										guess_value=guess_value-1
										print("Hit")
#vertical 5x1									
								elif directionShip4==2:
									if grid[y4][0]==1 or grid[y4][1]==1 or grid[y4][2]==1 or grid[y4][3]==1 or grid[y4][4]==1:
										grid[row][column]=2
										guess_value=guess_value-1
										print("Hit")
#horizontal 5x1										
								if grid[y5][x5]==1 or grid[y5+1][x5]==1 or grid[y5+2][x5]==1 or grid[y5+3][x5]==1:
									grid[row][column]=2
									guess_value=guess_value-1
									print("Hit")
#vertical 4x1

#checking for ship sunk
								if directionShip1==1:
									if grid[0][x1]==2 and grid[1][x1]==2 and grid[2][x1]==2:
										grid[0][x1]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#vertical 3x1
								elif directionShip1==2:
									if grid[y1][0]==2 and grid[y1][1]==2 and grid[y1][2]==2:
										grid[y1][0]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#horizontal	3x1									
								if directionShip2==1:	
									if grid[0][x2]==2 and grid[1][x2]==2 and grid[2][x2]==2:
										grid[0][x2]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#vertical	3x1(2)
								elif directionShip2==2:
									if grid[y2][3]==2 and grid[y2][4]==2 and grid[y2][5]==2:
										grid[y2][3]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#horizontal	3x1(2)								
								if directionShip3==1:
									if grid[y3][x3]==2 and grid[y3+1][x3]==2:
										grid[y3][x3]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#vertical 2x1
								elif directionShip3==2:
									if grid[y6][6]==2 and grid[y6][7]==2:
										grid[y6][6]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#horizontal 2x1
								if directionShip4==1:
									if grid[3][x4]==2 and grid[4][x4]==2 and grid[5][x4]==2 and grid[6][x4]==2 and grid[7][x4]==2:
										grid[3][x4]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#vertical 5x1									
								elif directionShip4==2:
									if grid[y4][0]==2 and grid[y4][1]==2 and grid[y4][2]==2 and grid[y4][3]==2 and grid[y4][4]==2:
										grid[y4][0]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#horizontal 5x1										
								if grid[y5][x5]==2 and grid[y5+1][x5]==2 and grid[y5+2][x5]==2 and grid[y5+3][x5]==2:
									grid[y5][x5]=3
									shipsdestroyed=shipsdestroyed+1
									shipsalive=shipsalive-1
									print("Ship sunk")
#vertical 4x1
							elif grid[row][column]==1 or grid[row][column]==2 or grid[row][column]==3:
								print("Location already guessed. Try another location.")
							if shipsdestroyed==5:
								winning(guess_value,name,computerlvl,abilitycount,gametype)
							if computerlvl=="easy":
								if guess_value==28:
									losing(guess_value,shipsdestroyed,name,computerlvl,gametype,abilitycount,shipsalive)
							elif computerlvl=="medium":
								if guess_value==20:
									losing(guess_value,shipsdestroyed,name,computerlvl,gametype,abilitycount,shipsalive)
							elif computerlvl=="hard":
								if guess_value==14:
									losing(guess_value,shipsdestroyed,name,computerlvl,gametype,abilitycount,shipsalive)
		
					for row in range(8):
						for column in range(8):
							color = (white)
							if grid[row][column]==1 :
								color = blue
							elif grid[row][column]==2:
								color=red
							elif grid[row][column]==3:
								color=red
							pygame.draw.rect(screen, color,[(MARGIN + WIDTH) * column + MARGIN,(MARGIN + HEIGHT) * row + MARGIN,WIDTH, HEIGHT])
					clock.tick(60)
					guess(370, 20)
					ShipDestroyed(370,100)
					ShipsAlive(370,60)
					pygame.display.flip()
					pygame.display.update()
					screen.fill(background)
#8x8 salvo					
	elif board=="10x10" and gametype=="salvo":
		font=pygame.font.Font(None,32)
		def guess(x, y):
			guesses= font.render("Round : "+ str(guess_value),True,(white))
			screen.blit(guesses,(x,y))

		shipsdestroyed=0

		def ShipDestroyed(x, y):
			shipsDes=font.render("Ships destroyed : "+str(shipsdestroyed),True,(white))
			screen.blit(shipsDes,(x,y))

		shipsalive=5

		def ShipsAlive(x, y):
			ShipsAli=font.render("Ships left : " +str(shipsalive),True,(white))
			screen.blit(ShipsAli,(x,y))
			
		x1=random.randint(0,5)
		x2=random.randint(6,9)
		x3=random.randint(0,2)
		x4=random.randint(3,5)
		x5=random.randint(6,9)
		x6=random.randint(0,1)
		x7=random.randint(0,0)
		x8=random.randint(0,1)
		x9=random.randint(0,0)
		x10=random.randint(6,7)
		y1=random.randint(0,5)
		y2=random.randint(0,3)
		y3=random.randint(6,8)
		y4=random.randint(6,7)
		y5=random.randint(0,0)
		y6=random.randint(0,1)
		y7=random.randint(0,6)
		y8=random.randint(6,9)
		y9=random.randint(6,9)
		y10=random.randint(7,9)
		directionShip1=random.randint(1,2)
		directionShip2=random.randint(1,2)
		directionShip3=random.randint(1,2)
		directionShip4=random.randint(1,2)
		directionShip5=random.randint(1,2)
		screen = pygame.display.set_mode((800, 800),0,32)
		running=True
		
		while running==True:
			if running==True:
				for row in range(10):
					grid.append([0])
					for column in range(10):
						grid[row].append(0) 
				done = False
				clock = pygame.time.Clock()
				while not done: 
					for event in pygame.event.get(): 
						if event.type == pygame.QUIT: 
							done = True 
						elif event.type == pygame.MOUSEBUTTONDOWN:
							pos = pygame.mouse.get_pos()
							column = pos[0] // (WIDTH + MARGIN)
							row = pos[1] // (HEIGHT + MARGIN)
							if grid[row][column]==0:
								grid[row][column]=1
								print("Grid location: ",row,column)
								guess_value=guess_value+1
								if directionShip1==1:
									if grid[y6][x1]==1 or grid[y6+1][x1]==1 or grid[y6+2][x1]==1 or grid[y6+3][x1]==1 or grid[y6+4][x1]==1:
										grid[row][column]=2
										guess_value=guess_value-1
										print("Hit")
#vertical 5x1
								elif directionShip1==2:
									if grid[y1][x6]==1 or grid[y1][x6+1]==1 or grid[y1][x6+2]==1 or grid[y1][x6+3]==1 or grid[y1][x6+4]==1:
										grid[row][column]=2
										guess_value=guess_value-1
										print("Hit")
#horizontal	5x1									
								if directionShip2==1:	
									if grid[y2][x2]==1 or grid[y2+1][x2]==1 or grid[y2+2][x2]==1 or grid[y2+3][x2]==1:
										grid[row][column]=2
										guess_value=guess_value-1
										print("Hit")
#vertical	4x1
								elif directionShip2==2:
									if grid[y7][6]==1 or grid[y7][7]==1 or grid[y7][8]==1 or grid[y7][9]==1:
										grid[row][column]=2
										guess_value=guess_value-1
										print("Hit")
#horizontal	4x1								
								if directionShip3==1:
									if grid[y3][x3]==1 or grid[y3+1][x3]==1:
										grid[row][column]=2
										guess_value=guess_value-1
										print("Hit")
#vertical 2x1
								elif directionShip3==2:
									if grid[y8][x8]==1 or grid[y8][x8+1]==1:
										grid[row][column]=2
										guess_value=guess_value-1
										print("Hit")
#horizontal 2x1
								if directionShip4==1:
									if grid[y4][x4]==1 or grid[y4+1][x4]==1 or grid[y4+2][x4]==1:
										grid[row][column]=2
										guess_value=guess_value-1
										print("Hit")
#vertical 3x1(1)									
								elif directionShip4==2:
									if grid[y9][3]==1 or grid[y9][4]==1 or grid[y9][5]==1:
										grid[row][column]=2
										guess_value=guess_value-1
										print("Hit")
#horizontal 3x1(1)	
								if directionShip5==1:
									if grid[7][x5]==1 or grid[8][x5]==1 or grid[9][x5]==1:
										grid[row][column]=2
										guess_value=guess_value-1
										print("Hit")
#vertical 3x1(2)
								elif directionShip5==2:
									if grid[y10][x10]==1 or grid[y10][x10+1]==1 or grid[y10][x10+2]==1:
										grid[row][column]=2
										guess_value=guess_value-1
										print("Hit")
#hotizontal 3x1(2)

#checking for ship sunk
								if directionShip1==1:
									if grid[y6][x1]==2 and grid[y6+1][x1]==2 and grid[y6+2][x1]==2 and grid[y6+3][x1]==2 and grid[y6+4][x1]==2:
										grid[y6][x1]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#vertical 5x1
								elif directionShip1==2:
									if grid[y1][x6]==2 and grid[y1][x6+1]==2 and grid[y1][x6+2]==2 and grid[y1][x6+3]==2 and grid[y1][x6+4]==2:
										grid[y1][x6]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#horizontal	5x1									
								if directionShip2==1:	
									if grid[y2][x2]==2 and grid[y2+1][x2]==2 and grid[y2+2][x2]==2 and grid[y2+3][x2]==2:
										grid[y2][x2]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#vertical	4x1
								elif directionShip2==2:
									if grid[y7][6]==2 and grid[y7][7]==2 and grid[y7][8]==2 and grid[y7][9]==2:
										grid[y7][6]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#horizontal	4x1								
								if directionShip3==1:
									if grid[y3][x3]==2 and grid[y3+1][x3]==2:
										grid[y3][x3]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#vertical 2x1
								elif directionShip3==2:
									if grid[y8][x8]==2 and grid[y8][x8+1]==2:
										grid[y8][x8]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#horizontal 2x1
								if directionShip4==1:
									if grid[y4][x4]==2 and grid[y4+1][x4]==2 and grid[y4+2][x4]==2:
										grid[y4][x4]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#vertical 3x1(1)									
								elif directionShip4==2:
									if grid[y9][3]==2 and grid[y9][4]==2 and grid[y9][5]==2:
										grid[y9][3]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#horizontal 3x1(1)	
								if directionShip5==1:
									if grid[7][x5]==2 and grid[8][x5]==2 and grid[9][x5]==2:
										grid[7][x5]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#vertical 3x1(2)
								elif directionShip5==2:
									if grid[y10][x10]==2 and grid[y10][x10+1]==2 and grid[y10][x10+2]==2:
										grid[y10][x10]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#hotizontal 3x1(2)
							elif grid[row][column]==1 or grid[row][column]==2 or grid[row][column]==3:
								print("Location already guessed. Try another location.")
							if shipsdestroyed==5:
								winning(guess_value,name,computerlvl,abilitycount,gametype)
							if computerlvl=="easy":
								if guess_value==55:
									losing(guess_value,shipsdestroyed,name,computerlvl,gametype,abilitycount,shipsalive)
							elif computerlvl=="medium":
								if guess_value==35:
									losing(guess_value,shipsdestroyed,name,computerlvl,gametype,abilitycount,shipsalive)
							elif computerlvl=="hard":
								if guess_value==25:
									losing(guess_value,shipsdestroyed,name,computerlvl,gametype,abilitycount,shipsalive)
		
					for row in range(10):
						for column in range(10):
							color = (white)
							if grid[row][column]==1 :
								color = blue
							elif grid[row][column]==2:
								color=red
							elif grid[row][column]==3:
								color=red
							pygame.draw.rect(screen, color,[(MARGIN + WIDTH) * column + MARGIN,(MARGIN + HEIGHT) * row + MARGIN,WIDTH, HEIGHT])
					clock.tick(60)
					guess(460, 20)
					ShipDestroyed(460,100)
					ShipsAlive(460,60)
					pygame.display.flip()
					pygame.display.update()
					screen.fill(background)
#10x10 salvo					
	elif board=="12x12" and gametype=="salvo":
		font=pygame.font.Font(None,32)
		def guess(x, y):
			guesses= font.render("Round : "+ str(guess_value),True,(white))
			screen.blit(guesses,(x,y))

		shipsdestroyed=0

		def ShipDestroyed(x, y):
			shipsDes=font.render("Ships destroyed : "+str(shipsdestroyed),True,(white))
			screen.blit(shipsDes,(x,y))

		shipsalive=5

		def ShipsAlive(x, y):
			ShipsAli=font.render("Ships left : " +str(shipsalive),True,(white))
			screen.blit(ShipsAli,(x,y))
		
		x1=random.randint(0,6)
		x2=random.randint(7,11)
		x3=random.randint(0,3)
		x4=random.randint(4,6)
		x5=random.randint(0,6)
		x6=random.randint(0,4)
		x7=random.randint(0,0)
		x8=random.randint(0,1)
		x9=random.randint(4,5)
		x10=random.randint(0,3)
		y1=random.randint(0,5)
		y2=random.randint(0,7)
		y3=random.randint(3,5)
		y4=random.randint(3,6)
		y5=random.randint(0,0)
		y6=random.randint(0,2)
		y7=random.randint(0,11)
		y8=random.randint(3,7)
		y9=random.randint(3,7)
		y10=random.randint(8,11)
		directionShip1=random.randint(1,2)
		directionShip2=random.randint(1,2)
		directionShip3=random.randint(1,2)
		directionShip4=random.randint(1,2)
		directionShip5=random.randint(1,2)
		screen = pygame.display.set_mode((800, 800),0,32)
		running=True
		
		while running==True:
			if running==True:
				for row in range(12):
					grid.append([0])
					for column in range(12):
						grid[row].append(0) 
				done = False
				clock = pygame.time.Clock()
				while not done: 
					for event in pygame.event.get(): 
						if event.type == pygame.QUIT: 
							done = True 
						elif event.type == pygame.MOUSEBUTTONDOWN:
							pos = pygame.mouse.get_pos()
							column = pos[0] // (WIDTH + MARGIN)
							row = pos[1] // (HEIGHT + MARGIN)
							if grid[row][column]==0:
								grid[row][column]=1
								print("Grid location: ",row,column)
								guess_value=guess_value+1
								if directionShip1==1:
									if grid[0][x1]==1 or grid[1][x1]==1 or grid[2][x1]==1:
										grid[row][column]=2
										guess_value=guess_value-1
										print("Hit")
#vertical 3x1(1)
								elif directionShip1==2:
									if grid[y6][x6]==1 or grid[y6][x6+1]==1 or grid[y6][x6+2]==1:
										grid[row][column]=2
										guess_value=guess_value-1
										print("Hit")
#horizontal	3x1(1)									
								if directionShip2==1:	
									if grid[y2][x2]==1 or grid[y2+1][x2]==1 or grid[y2+2][x2]==1 or grid[y2+3][x2]==1 or grid[y2+4][x2]:
										grid[row][column]=2
										guess_value=guess_value-1
										print("Hit")
#vertical	5x1
								elif directionShip2==2:
									if grid[y7][7]==1 or grid[y7][8]==1 or grid[y7][9]==1 or grid[y7][10]==1 or grid[y7][11]==1:
										grid[row][column]=2
										guess_value=guess_value-1
										print("Hit")
#horizontal	5x1								
								if directionShip3==1:
									if grid[y3][x3]==1 or grid[y3+1][x3]==1 or grid[y3+2][x3]==1:
										grid[row][column]=2
										guess_value=guess_value-1
										print("Hit")
#vertical 3x1(2)
								elif directionShip3==2:
									if grid[y8][x8]==1 or grid[y8][x8+1]==1 or grid[y8][x8+2]==1:
										grid[row][column]=2
										guess_value=guess_value-1
										print("Hit")
#horizontal 3x1(2)
								if directionShip4==1:
									if grid[y4][x4]==1 or grid[y4+1][x4]==1:
										grid[row][column]=2
										guess_value=guess_value-1
										print("Hit")
#vertical 2x1									
								elif directionShip4==2:
									if grid[y9][x9]==1 or grid[y9][x9+1]==1:
										grid[row][column]=2
										guess_value=guess_value-1
										print("Hit")
#horizontal 2x1	
								if directionShip5==1:
									if grid[8][x5]==1 or grid[9][x5]==1 or grid[10][x5]==1 or grid[11][x5]==1:
										grid[row][column]=2
										guess_value=guess_value-1
										print("Hit")
#vertical 4x1
								elif directionShip5==2:
									if grid[y10][x10]==1 or grid[y10][x10+1]==1 or grid[y10][x10+2]==1 or grid[y10][x10+3]==1:
										grid[row][column]=2
										guess_value=guess_value-1
										print("Hit")
#hotizontal 4x1

#checking for sunk ships
								if directionShip1==1:
									if grid[0][x1]==2 and grid[1][x1]==2 and grid[2][x1]==2:
										grid[0][x1]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#vertical 3x1(1)
								elif directionShip1==2:
									if grid[y6][x6]==2 and grid[y6][x6+1]==2 and grid[y6][x6+2]==2:
										grid[y6][x6]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#horizontal	3x1(1)									
								if directionShip2==1:	
									if grid[y2][x2]==2 and grid[y2+1][x2]==2 and grid[y2+2][x2]==2 and grid[y2+3][x2]==2 and grid[y2+4][x2]==2:
										grid[y2][x2]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#vertical	5x1
								elif directionShip2==2:
									if grid[y7][7]==2 and grid[y7][8]==2 and grid[y7][9]==2 and grid[y7][10]==2 and grid[y7][11]==2:
										grid[y7][7]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#horizontal	5x1								
								if directionShip3==1:
									if grid[y3][x3]==2 and grid[y3+1][x3]==2 and grid[y3+2][x3]==2:
										grid[y3][x3]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#vertical 3x1(2)
								elif directionShip3==2:
									if grid[y8][x8]==2 and grid[y8][x8+1]==2 and grid[y8][x8+2]==2:
										grid[y8][x8]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#horizontal 3x1(2)
								if directionShip4==1:
									if grid[y4][x4]==2 and grid[y4+1][x4]==2:
										grid[y4][x4]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#vertical 2x1									
								elif directionShip4==2:
									if grid[y9][x9]==2 and grid[y9][x9+1]==2:
										grid[y9][x9]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#horizontal 2x1	
								if directionShip5==1:
									if grid[8][x5]==2 and grid[9][x5]==2 and grid[10][x5]==2 and grid[11][x5]==2:
										grid[8][x5]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#vertical 4x1
								elif directionShip5==2:
									if grid[y10][x10]==2 and grid[y10][x10+1]==2 and grid[y10][x10+2]==2 and grid[y10][x10+3]==2:
										grid[y10][x10]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										print("Ship sunk")
#hotizontal 4x1
							elif grid[row][column]==1 or grid[row][column]==2 or grid[row][column]==3:
								print("Location already guessed. Try another location.")
							if shipsdestroyed==5:
								winning(guess_value,name,computerlvl,abilitycount,gametype)
							if computerlvl=="easy":
								if guess_value==85:
									losing(guess_value,shipsdestroyed,name,computerlvl,gametype,abilitycount,shipsalive)
							elif computerlvl=="medium":
								if guess_value==55:
									losing(guess_value,shipsdestroyed,name,computerlvl,gametype,abilitycount,shipsalive)
							elif computerlvl=="hard":
								if guess_value==40:
									losing(guess_value,shipsdestroyed,name,computerlvl,gametype,abilitycount,shipsalive)
		
					for row in range(12):
						for column in range(12):
							color = (white)
							if grid[row][column]==1 :
								color = blue
							elif grid[row][column]==2:
								color=red
							elif grid[row][column]==3:
								color=red
							pygame.draw.rect(screen, color,[(MARGIN + WIDTH) * column + MARGIN,(MARGIN + HEIGHT) * row + MARGIN,WIDTH, HEIGHT])
					clock.tick(60)
					guess(560, 20)
					ShipDestroyed(560,100)
					ShipsAlive(560,60)
					pygame.display.flip()
					pygame.display.update()
					screen.fill(background)
#12x12 salvo
	elif board=="8x8" and gametype=="advanced":
		font=pygame.font.Font(None,32)
		def guess(x, y):
			guesses= font.render("Guess : "+ str(guess_value),True,(white))
			screen.blit(guesses,(x,y))

		shipsdestroyed=0

		def ShipDestroyed(x, y):
			shipsDes=font.render("Ships destroyed : "+str(shipsdestroyed),True,(white))
			screen.blit(shipsDes,(x,y))

		shipsalive=5

		def ShipsAlive(x, y):
			ShipsAli=font.render("Ships left : " +str(shipsalive),True,(white))
			screen.blit(ShipsAli,(x,y))

		coins=0

		def CoinCounter(x,y):
			CoinsCount=font.render("Coins : " +str(coins),True,(white))
			screen.blit(CoinsCount,(x,y))
			
		x1=random.randint(0,2)
		x2=random.randint(3,5)
		x3=random.randint(6,7)
		x4=random.randint(0,4)
		x5=random.randint(5,7)
		y1=random.randint(0,2)
		y2=random.randint(0,2)
		y3=random.randint(0,1)
		y4=random.randint(3,7)
		y5=random.randint(3,4)
		y6=random.randint(0,2)
		directionShip1=random.randint(1,2)
		directionShip2=random.randint(1,2)
		directionShip3=random.randint(1,2)
		directionShip4=random.randint(1,2)
		screen = pygame.display.set_mode((800, 800),0,32)
		running=True
		ability1=False
		ability2=False
		ability3=False
		
		while running==True:
			button_abilityvertical = pygame.Rect(370, 190, 100, 30)
			button_abilityhorizontal = pygame.Rect(370, 270, 100, 30)
			button_ability3x3 = pygame.Rect(370, 330, 100, 30)
			if running==True:
				for row in range(200):
					grid.append([0])
					for column in range(200):
						grid[row].append(0) 
				done = False
				clock = pygame.time.Clock()
				while not done: 
					for event in pygame.event.get(): 
						if event.type == pygame.QUIT: 
							done = True 
						elif event.type == pygame.MOUSEBUTTONDOWN:
							pos = pygame.mouse.get_pos()
							column = pos[0] // (WIDTH + MARGIN)
							row = pos[1] // (HEIGHT + MARGIN)
							if ability1==True:
								ability1=False
								grid[row][column]=1
								grid[row+1][column]=1
								grid[row+2][column]=1
								grid[row+3][column]=1
								grid[row+4][column]=1
								grid[row+5][column]=1
								grid[row+6][column]=1
								grid[row+7][column]=1
								guess_value=guess_value+1
								if grid[4][8]==1 or grid[4][9]==1 or grid[4][10]==1:
									grid[4][8]=0 
									grid[4][9]=0
									grid[4][10]=0
								if grid[6][8]==1 or grid[6][9]==1 or grid[6][10]==1:
									grid[6][8]=0 
									grid[6][9]=0
									grid[6][10]=0
								if grid[7][8]==1 or grid[7][9]==1 or grid[7][10]==1:
									grid[7][8]=0
									grid[7][9]=0
									grid[7][10]=0
						
							
							elif ability2==True:
								ability2=False
								grid[row][column]=1
								grid[row][column+1]=1
								grid[row][column+2]=1
								grid[row][column+3]=1
								grid[row][column+4]=1
								grid[row][column+5]=1
								grid[row][column+6]=1
								grid[row][column+7]=1
								guess_value=guess_value+1
								if grid[4][8]==1 or grid[4][9]==1 or grid[4][10]==1:
									grid[4][8]=0 
									grid[4][9]=0
									grid[4][10]=0
								if grid[6][8]==1 or grid[6][9]==1 or grid[6][10]==1:
									grid[6][8]=0 
									grid[6][9]=0
									grid[6][10]=0
								if grid[7][8]==1 or grid[7][9]==1 or grid[7][10]==1:
									grid[7][8]=0
									grid[7][9]=0
									grid[7][10]=0
							

							elif ability3==True:
								ability3=False
								grid[row][column]=1
								grid[row-1][column-1]=1
								grid[row-1][column]=1
								grid[row-1][column+1]=1
								grid[row][column-1]=1
								grid[row][column+1]=1
								grid[row+1][column-1]=1
								grid[row+1][column]=1
								grid[row+1][column+1]=1
								guess_value=guess_value+1
								if grid[4][8]==1 or grid[4][9]==1 or grid[4][10]==1:
									grid[4][8]=0 
									grid[4][9]=0
									grid[4][10]=0
								if grid[6][8]==1 or grid[6][9]==1 or grid[6][10]==1:
									grid[6][8]=0 
									grid[6][9]=0
									grid[6][10]=0
								if grid[7][8]==1 or grid[7][9]==1 or grid[7][10]==1:
									grid[7][8]=0
									grid[7][9]=0
									grid[7][10]=0

							if directionShip1==1:
								if grid[0][x1]==1:
									grid[0][x1]=2
									coins=coins+5
									print("Hit")
								if grid[1][x1]==1:
									grid[1][x1]=2
									coins=coins+5
									print("Hit")
								if grid[2][x1]==1:
									grid[2][x1]=2
									coins=coins+5
									print("Hit")
						
#vertical 3x1
							elif directionShip1==2:
								if grid[y1][0]==1:
									grid[y1][0]=2
									coins=coins+5
									print("Hit")
								if grid[y1][1]==1:
									grid[y1][1]=2
									coins=coins+5
									print("Hit")
								if grid[y1][2]==1:
									grid[y1][2]=2
									coins=coins+5
									print("Hit")
#horizontal	3x1									
							if directionShip2==1:	
								if grid[0][x2]==1:
									grid[0][x2]=2
									coins=coins+5
									print("Hit")
								if grid[1][x2]==1:
									grid[1][x2]=2
									coins=coins+5
									print("Hit")
								if grid[2][x2]==1:
									grid[2][x2]=2
									coins=coins+5
									print("Hit")
#vertical	3x1(2)
							elif directionShip2==2:
								if grid[y2][3]==1:
									grid[y2][3]=2
									coins=coins+5
									print("Hit")
								if grid[y2][4]==1:
									grid[y2][4]=2
									coins=coins+5
									print("Hit")
								if grid[y2][5]==1:
									grid[y2][5]=2
									coins=coins+5
									print("Hit")
#horizontal	3x1(2)								
							if directionShip3==1:
								if grid[y3][x3]==1:
									grid[y3][x3]=2
									coins=coins+5
									print("Hit")
								if grid[y3+1][x3]==1:
									grid[y3+1][x3]=2
									coins=coins+5
									print("Hit")
#vertical 2x1
							elif directionShip3==2:
								if grid[y6][6]==1:
									grid[y6][6]=2
									coins=coins+5
									print("Hit")
								if grid[y6][7]==1:
									grid[y6][7]=2
									coins=coins+5
									print("Hit")
#horizontal 2x1
							if directionShip4==1:
								if grid[3][x4]==1:
									grid[3][x4]=2
									coins=coins+5
									print("Hit")
								if grid[4][x4]==1:
									grid[4][x4]=2
									coins=coins+5
									print("Hit")
								if grid[5][x4]==1:
									grid[5][x4]=2
									coins=coins+5
									print("Hit")
								if grid[6][x4]==1:
									grid[6][x4]=2
									coins=coins+5
									print("Hit")
								if grid[7][x4]==1:
									grid[7][x4]=2
									coins=coins+5
									print("Hit")
#vertical 5x1									
							elif directionShip4==2:
								if grid[y4][0]==1:
									grid[y4][0]=2
									coins=coins+5
									print("Hit")
								if grid[y4][1]==1:
									grid[y4][1]=2
									coins=coins+5
									print("Hit")
								if grid[y4][2]==1:
									grid[y4][2]=2
									coins=coins+5
									print("Hit")
								if grid[y4][3]==1:
									grid[y4][3]=2
									coins=coins+5
									print("Hit")
								if grid[y4][4]==1:
									grid[y4][4]=2
									coins=coins+5
									print("Hit")

#horizontal 5x1										
							if grid[y5][x5]==1:
								grid[y5][x5]=2
								coins=coins+5
								print("Hit")
							if grid[y5+1][x5]==1:
								grid[y5+1][x5]=2
								coins=coins+5
								print("Hit")
							if grid[y5+2][x5]==1:
								grid[y5+2][x5]=2
								coins=coins+5
								print("Hit")
							if grid[y5+3][x5]==1:
								grid[y5+3][x5]=2
								coins=coins+5
								print("Hit")
												
#vertical 4x1

#checking for ship sunk
							if directionShip1==1:
								if grid[0][x1]==2 and grid[1][x1]==2 and grid[2][x1]==2:
									grid[0][x1]=3
									shipsdestroyed=shipsdestroyed+1
									shipsalive=shipsalive-1
									coins=coins+10
									print("Ship sunk")
#vertical 3x1
							elif directionShip1==2:
								if grid[y1][0]==2 and grid[y1][1]==2 and grid[y1][2]==2:
									grid[y1][0]=3
									shipsdestroyed=shipsdestroyed+1
									shipsalive=shipsalive-1
									coins=coins+10
									print("Ship sunk")
#horizontal	3x1									
							if directionShip2==1:	
								if grid[0][x2]==2 and grid[1][x2]==2 and grid[2][x2]==2:
									grid[0][x2]=3
									shipsdestroyed=shipsdestroyed+1
									shipsalive=shipsalive-1
									coins=coins+10
									print("Ship sunk")
#vertical	3x1(2)
							elif directionShip2==2:
								if grid[y2][3]==2 and grid[y2][4]==2 and grid[y2][5]==2:
									grid[y2][3]=3
									shipsdestroyed=shipsdestroyed+1
									shipsalive=shipsalive-1
									coins=coins+10
									print("Ship sunk")
#horizontal	3x1(2)								
							if directionShip3==1:
								if grid[y3][x3]==2 and grid[y3+1][x3]==2:
									grid[y3][x3]=3
									shipsdestroyed=shipsdestroyed+1
									shipsalive=shipsalive-1
									coins=coins+10
									print("Ship sunk")
#vertical 2x1
							elif directionShip3==2:
								if grid[y6][6]==2 and grid[y6][7]==2:
									grid[y6][6]=3
									shipsdestroyed=shipsdestroyed+1
									shipsalive=shipsalive-1
									coins=coins+10
									print("Ship sunk")
#horizontal 2x1
							if directionShip4==1:
								if grid[3][x4]==2 and grid[4][x4]==2 and grid[5][x4]==2 and grid[6][x4]==2 and grid[7][x4]==2:
									grid[3][x4]=3
									shipsdestroyed=shipsdestroyed+1
									shipsalive=shipsalive-1
									coins=coins+10
									print("Ship sunk")
#vertical 5x1									
							elif directionShip4==2:
								if grid[y4][0]==2 and grid[y4][1]==2 and grid[y4][2]==2 and grid[y4][3]==2 and grid[y4][4]==2:
									grid[y4][0]=3
									shipsdestroyed=shipsdestroyed+1
									shipsalive=shipsalive-1
									coins=coins+10
									print("Ship sunk")
#horizontal 5x1										
							if grid[y5][x5]==2 and grid[y5+1][x5]==2 and grid[y5+2][x5]==2 and grid[y5+3][x5]==2:
								grid[y5][x5]=3
								shipsdestroyed=shipsdestroyed+1
								shipsalive=shipsalive-1
								coins=coins+10
								print("Ship sunk")
#vertical 4x1									

							elif grid[row][column]==0 and ability1==False and ability2==False and ability3==False:
								grid[row][column]=1
								print("Grid location: ",row,column)
								guess_value=guess_value+1								
								if (grid[4][8]==1 or grid[4][9]==1 or grid[4][10]==1) and coins>=50:
									grid[row][column]=0
									ability1=True
									guess_value=guess_value-1
									coins=coins-50
									abilitycount=abilitycount+1
									print("Ability 1.")
								elif (grid[4][8]==1 or grid[4][9]==1 or grid[4][10]==1) and coins<50:
									grid[row][column]=0
									guess_value=guess_value-1
									print("Not enough coins")
								if (grid[6][8]==1 or grid[6][9]==1 or grid[6][10]==1 ) and coins>=50:
									grid[row][column]=0
									ability2=True
									guess_value=guess_value-1
									coins=coins-50
									print("Ability 2")
									abilitycount=abilitycount+1
								elif (grid[6][8]==1 or grid[6][9]==1 or grid[6][10]==1 ) and coins<50:
									grid[row][column]=0
									guess_value=guess_value-1
									print("Not enough coins")
								if (grid[7][8]==1 or grid[7][9]==1 or grid[7][10]==1) and coins>=30:
									grid[row][column]=0
									ability3=True
									guess_value=guess_value-1
									coins=coins-30
									print("Ability 3 activated")
									abilitycount=abilitycount+1
								elif (grid[7][8]==1 or grid[7][9]==1 or grid[7][10]==1) and coins<30:
									grid[row][column]=0
									guess_value=guess_value-1
									print("Not enough coins")
								if directionShip1==1:
									if grid[0][x1]==1:
										grid[0][x1]=2
										coins=coins+5
										print("Hit")
									if grid[1][x1]==1:
										grid[1][x1]=2
										coins=coins+5
										print("Hit")
									if grid[2][x1]==1:
										grid[2][x1]=2
										coins=coins+5
										print("Hit")
						
#vertical 3x1
								elif directionShip1==2:
									if grid[y1][0]==1:
										grid[y1][0]=2
										coins=coins+5
										print("Hit")
									if grid[y1][1]==1:
										grid[y1][1]=2
										coins=coins+5
										print("Hit")
									if grid[y1][2]==1:
										grid[y1][2]=2
										coins=coins+5
										print("Hit")
#horizontal	3x1									
								if directionShip2==1:	
									if grid[0][x2]==1:
										grid[0][x2]=2
										coins=coins+5
										print("Hit")
									if grid[1][x2]==1:
										grid[1][x2]=2
										coins=coins+5
										print("Hit")
									if grid[2][x2]==1:
										grid[2][x2]=2
										coins=coins+5
										print("Hit")
#vertical	3x1(2)
								elif directionShip2==2:
									if grid[y2][3]==1:
										grid[y2][3]=2
										coins=coins+5
										print("Hit")
									if grid[y2][4]==1:
										grid[y2][4]=2
										coins=coins+5
										print("Hit")
									if grid[y2][5]==1:
										grid[y2][5]=2
										coins=coins+5
										print("Hit")
#horizontal	3x1(2)								
								if directionShip3==1:
									if grid[y3][x3]==1:
										grid[y3][x3]=2
										coins=coins+5
										print("Hit")
									if grid[y3+1][x3]==1:
										grid[y3+1][x3]=2
										coins=coins+5
										print("Hit")
#vertical 2x1
								elif directionShip3==2:
									if grid[y6][6]==1:
										grid[y6][6]=2
										coins=coins+5
										print("Hit")
									if grid[y6][7]==1:
										grid[y6][7]=2
										coins=coins+5
										print("Hit")
#horizontal 2x1
								if directionShip4==1:
									if grid[3][x4]==1:
										grid[3][x4]=2
										coins=coins+5
										print("Hit")
									if grid[4][x4]==1:
										grid[4][x4]=2
										coins=coins+5
										print("Hit")
									if grid[5][x4]==1:
										grid[5][x4]=2
										coins=coins+5
										print("Hit")
									if grid[6][x4]==1:
										grid[6][x4]=2
										coins=coins+5
										print("Hit")
									if grid[7][x4]==1:
										grid[7][x4]=2
										coins=coins+5
										print("Hit")
#vertical 5x1									
								elif directionShip4==2:
									if grid[y4][0]==1:
										grid[y4][0]=2
										coins=coins+5
										print("Hit")
									if grid[y4][1]==1:
										grid[y4][1]=2
										coins=coins+5
										print("Hit")
									if grid[y4][2]==1:
										grid[y4][2]=2
										coins=coins+5
										print("Hit")
									if grid[y4][3]==1:
										grid[y4][3]=2
										coins=coins+5
										print("Hit")
									if grid[y4][4]==1:
										grid[y4][4]=2
										coins=coins+5
										print("Hit")
#horizontal 5x1										
								if grid[y5][x5]==1:
									grid[y5][x5]=2
									coins=coins+5
									print("Hit")
								if grid[y5+1][x5]==1:
									grid[y5+1][x5]=2
									coins=coins+5
									print("Hit")
								if grid[y5+2][x5]==1:
									grid[y5+2][x5]=2
									coins=coins+5
									print("Hit")
								if grid[y5+3][x5]==1:
									grid[y5+3][x5]=2
									coins=coins+5
									print("Hit")
												
#vertical 4x1

#checking for ship sunk
								if directionShip1==1:
									if grid[0][x1]==2 and grid[1][x1]==2 and grid[2][x1]==2:
										grid[0][x1]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										coins=coins+10
										print("Ship sunk")
#vertical 3x1
								elif directionShip1==2:
									if grid[y1][0]==2 and grid[y1][1]==2 and grid[y1][2]==2:
										grid[y1][0]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										coins=coins+10
										print("Ship sunk")
#horizontal	3x1									
								if directionShip2==1:	
									if grid[0][x2]==2 and grid[1][x2]==2 and grid[2][x2]==2:
										grid[0][x2]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										coins=coins+10
										print("Ship sunk")
#vertical	3x1(2)
								elif directionShip2==2:
									if grid[y2][3]==2 and grid[y2][4]==2 and grid[y2][5]==2:
										grid[y2][3]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										coins=coins+10
										print("Ship sunk")
#horizontal	3x1(2)								
								if directionShip3==1:
									if grid[y3][x3]==2 and grid[y3+1][x3]==2:
										grid[y3][x3]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										coins=coins+10
										print("Ship sunk")
#vertical 2x1
								elif directionShip3==2:
									if grid[y6][6]==2 and grid[y6][7]==2:
										grid[y6][6]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										coins=coins+10
										print("Ship sunk")
#horizontal 2x1
								if directionShip4==1:
									if grid[3][x4]==2 and grid[4][x4]==2 and grid[5][x4]==2 and grid[6][x4]==2 and grid[7][x4]==2:
										grid[3][x4]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										coins=coins+10
										print("Ship sunk")
#vertical 5x1									
								elif directionShip4==2:
									if grid[y4][0]==2 and grid[y4][1]==2 and grid[y4][2]==2 and grid[y4][3]==2 and grid[y4][4]==2:
										grid[y4][0]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										coins=coins+10
										print("Ship sunk")
#horizontal 5x1										
								if grid[y5][x5]==2 and grid[y5+1][x5]==2 and grid[y5+2][x5]==2 and grid[y5+3][x5]==2:
									grid[y5][x5]=3
									shipsdestroyed=shipsdestroyed+1
									shipsalive=shipsalive-1
									coins=coins+10
									print("Ship sunk")
#vertical 4x1									
							elif grid[row][column]==1 or grid[row][column]==2 or grid[row][column]==3:
								print("Location already guessed. Try another location")
							if shipsdestroyed==5:
								winning(guess_value,name,computerlvl,abilitycount,gametype)
							if computerlvl=="easy":
								if guess_value==35:
									losing(guess_value,shipsdestroyed,name,computerlvl,abilitycount,gametype,shipsalive)
							elif computerlvl=="medium":
								if guess_value==25:
									losing(guess_value,shipsdestroyed,name,computerlvl,abilitycount,gametype,shipsalive)
							elif computerlvl=="hard":
								if guess_value==17:
									losing(guess_value,shipsdestroyed,name,computerlvl,abilitycount,gametype,shipsalive)
							
									
					for row in range(8):
						for column in range(8):
							color = (white)
							if grid[row][column]==1 :
								color = blue
							elif grid[row][column]==2:
								color=red
							elif grid[row][column]==3:
								color=red
							pygame.draw.rect(screen, color,[(MARGIN + WIDTH) * column + MARGIN,(MARGIN + HEIGHT) * row + MARGIN,WIDTH, HEIGHT])
					pygame.draw.rect(screen, (255, 0, 0), button_abilityvertical)
					pygame.draw.rect(screen, (255, 0, 0), button_abilityhorizontal)
					pygame.draw.rect(screen, (255, 0, 0), button_ability3x3)
					clock.tick(60)
					guess(370, 20)
					ShipDestroyed(370,100)
					ShipsAlive(370,60)
					CoinCounter(370,140)
					draw_text("Ability 1(50) (Vertical)", Ntitle, (255, 255, 255), screen, 370, 170)
					draw_text("Ability 2(50) (Horizontal)", Ntitle, (255, 255, 255), screen, 370, 250)
					draw_text("Ability 3(30) ", Ntitle, (255, 255, 255), screen, 370, 310)
					pygame.display.flip()
					pygame.display.update()
					screen.fill(background)
#8x8 advanced					
	elif board=="10x10" and gametype=="advanced":
		font=pygame.font.Font(None,32)
		def guess(x, y):
			guesses= font.render("Guess : "+ str(guess_value),True,(white))
			screen.blit(guesses,(x,y))

		shipsdestroyed=0

		def ShipDestroyed(x, y):
			shipsDes=font.render("Ships destroyed : "+str(shipsdestroyed),True,(white))
			screen.blit(shipsDes,(x,y))

		shipsalive=5

		def ShipsAlive(x, y):
			ShipsAli=font.render("Ships left : " +str(shipsalive),True,(white))
			screen.blit(ShipsAli,(x,y))

		coins=0

		def CoinCounter(x,y):
			CoinsCount=font.render("Coins : " +str(coins),True,(white))
			screen.blit(CoinsCount,(x,y))
			
		x1=random.randint(0,5)
		x2=random.randint(6,9)
		x3=random.randint(0,2)
		x4=random.randint(3,5)
		x5=random.randint(6,9)
		x6=random.randint(0,1)
		x7=random.randint(0,0)
		x8=random.randint(0,1)
		x9=random.randint(0,0)
		x10=random.randint(6,7)
		y1=random.randint(0,5)
		y2=random.randint(0,3)
		y3=random.randint(6,8)
		y4=random.randint(6,7)
		y5=random.randint(0,0)
		y6=random.randint(0,1)
		y7=random.randint(0,6)
		y8=random.randint(6,9)
		y9=random.randint(6,9)
		y10=random.randint(7,9)
		directionShip1=random.randint(1,2)
		directionShip2=random.randint(1,2)
		directionShip3=random.randint(1,2)
		directionShip4=random.randint(1,2)
		directionShip5=random.randint(1,2)
		screen = pygame.display.set_mode((800, 800),0,32)
		running=True
		ability1=False
		ability2=False
		ability3=False
		
		while running==True:
			button_abilityvertical = pygame.Rect(460, 190, 100, 30)
			button_abilityhorizontal = pygame.Rect(460, 270, 100, 30)
			button_ability3x3 = pygame.Rect(460, 330, 100, 30)
			if running==True:
				for row in range(200):
					grid.append([0])
					for column in range(200):
						grid[row].append(0) 
				done = False
				clock = pygame.time.Clock()
				while not done: 
					for event in pygame.event.get(): 
						if event.type == pygame.QUIT: 
							done = True 
						elif event.type == pygame.MOUSEBUTTONDOWN:
							pos = pygame.mouse.get_pos()
							column = pos[0] // (WIDTH + MARGIN)
							row = pos[1] // (HEIGHT + MARGIN)
							if ability1==True:
								ability1=False
								grid[row][column]=1
								grid[row+1][column]=1
								grid[row+2][column]=1
								grid[row+3][column]=1
								grid[row+4][column]=1
								grid[row+5][column]=1
								grid[row+6][column]=1
								grid[row+7][column]=1
								grid[row+8][column]=1
								grid[row+9][column]=1
								guess_value=guess_value+1
								if grid[4][10]==1 or grid[4][11]==1 or grid[4][12]==1:
									grid[4][10]=0 
									grid[4][11]=0
									grid[4][12]=0
								if grid[6][10]==1 or grid[6][11]==1 or grid[6][12]==1:
									grid[6][10]=0 
									grid[6][11]=0
									grid[6][12]=0
								if grid[7][10]==1 or grid[7][11]==1 or grid[7][12]==1:
									grid[7][10]=0
									grid[7][11]=0
									grid[7][12]=0
							
							elif ability2==True:
								ability2=False
								grid[row][column]=1
								grid[row][column+1]=1
								grid[row][column+2]=1
								grid[row][column+3]=1
								grid[row][column+4]=1
								grid[row][column+5]=1
								grid[row][column+6]=1
								grid[row][column+7]=1
								grid[row][column+8]=1
								grid[row][column+9]=1
								guess_value=guess_value+1
								if grid[4][10]==1 or grid[4][11]==1 or grid[4][12]==1:
									grid[4][10]=0 
									grid[4][11]=0
									grid[4][12]=0
								if grid[6][10]==1 or grid[6][11]==1 or grid[6][12]==1:
									grid[6][10]=0 
									grid[6][11]=0
									grid[6][12]=0
								if grid[7][10]==1 or grid[7][11]==1 or grid[7][12]==1:
									grid[7][10]=0
									grid[7][11]=0
									grid[7][12]=0

							elif ability3==True:
								ability3=False
								grid[row][column]=1
								grid[row-1][column-1]=1
								grid[row-1][column]=1
								grid[row-1][column+1]=1
								grid[row][column-1]=1
								grid[row][column+1]=1
								grid[row+1][column-1]=1
								grid[row+1][column]=1
								grid[row+1][column+1]=1
								guess_value=guess_value+1
								if grid[4][10]==1 or grid[4][11]==1 or grid[4][12]==1:
									grid[4][10]=0 
									grid[4][11]=0
									grid[4][12]=0
								if grid[6][10]==1 or grid[6][11]==1 or grid[6][12]==1:
									grid[6][10]=0 
									grid[6][11]=0
									grid[6][12]=0
								if grid[7][10]==1 or grid[7][11]==1 or grid[7][12]==1:
									grid[7][10]=0
									grid[7][11]=0
									grid[7][12]=0
							
							if directionShip1==1:
								if grid[y6][x1]==1:
									grid[y6][x1]=2
									coins=coins+5
									print("Hit")
								if grid[y6+1][x1]==1:
									grid[y6+1][x1]=2
									coins=coins+5
									print("Hit")
								if grid[y6+2][x1]==1:
									grid[y6+2][x1]=2
									coins=coins+5
									print("Hit")
								if grid[y6+3][x1]==1:
									grid[y6+3][x1]=2
									coins=coins+5
									print("Hit")
								if grid[y6+4][x1]==1:
									grid[y6+4][x1]=2
									coins=coins+5
									print("Hit")									
#vertical 5x1
							elif directionShip1==2:
								if grid[y1][x6]==1:
									grid[y1][x6]=2
									coins=coins+5
									print("Hit")
								if grid[y1][x6+1]==1:
									grid[y1][x6+1]=2
									coins=coins+5
									print("Hit")
								if grid[y1][x6+2]==1:
									grid[y1][x6+2]=2
									coins=coins+5
									print("Hit")
								if grid[y1][x6+3]==1:
									grid[y1][x6+3]=2
									coins=coins+5
									print("Hit")
								if grid[y1][x6+4]==1:
									grid[y1][x6+4]=2
									coins=coins+5
									print("Hit")
#horizontal	5x1									
							if directionShip2==1:	
								if grid[y2][x2]==1:
									grid[y2][x2]=2
									coins=coins+5
									print("Hit")
								if grid[y2+1][x2]==1:
									grid[y2+1][x2]=2
									coins=coins+5
									print("Hit")
								if grid[y2+2][x2]==1:
									grid[y2+2][x2]=2
									coins=coins+5
									print("Hit")
								if grid[y2+3][x2]==1:
									grid[y2+3][x2]=2
									coins=coins+5
									print("Hit")
#vertical	4x1
							elif directionShip2==2:
								if grid[y7][6]==1:
									grid[y7][6]=2
									coins=coins+5
									print("Hit")
								if grid[y7][7]==1:
									grid[y7][7]=2
									coins=coins+5
									print("Hit")
								if grid[y7][8]==1:
									grid[y7][8]=2
									coins=coins+5
									print("Hit")
								if grid[y7][9]==1:
									grid[y7][9]=2
									coins=coins+5
									print("Hit")

#horizontal	4x1								
							if directionShip3==1:
								if grid[y3][x3]==1:
									grid[y3][x3]=2
									coins=coins+5
									print("Hit")
								if grid[y3+1][x3]==1:
									grid[y3+1][x3]=2
									coins=coins+5
									print("Hit")
									
#vertical 2x1
							elif directionShip3==2:
								if grid[y8][x8]==1:
									grid[y8][x8]=2
									coins=coins+5
									print("Hit")
								if grid[y8][x8+1]==1:
									grid[y8][x8+1]=2
									coins=coins+5
									print("Hit")
#horizontal 2x1
							if directionShip4==1:
								if grid[y4][x4]==1:
									grid[y4][x4]=2
									coins=coins+5
									print("Hit")
								if grid[y4+1][x4]==1:
									grid[y4+1][x4]=2
									coins=coins+5
									print("Hit")
								if grid[y4+2][x4]==1:
									grid[y4+2][x4]=2
									coins=coins+5
									print("Hit")
									
#vertical 3x1(1)									
							elif directionShip4==2:
								if grid[y9][3]==1:
									grid[y9][3]=2
									coins=coins+5
									print("Hit")
								if grid[y9][4]==1:
									grid[y9][4]=2
									coins=coins+5
									print("Hit")
								if grid[y9][5]==1:
									grid[y9][5]=2
									coins=coins+5
									print("Hit")
#horizontal 3x1(1)	
							if directionShip5==1:
								if grid[7][x5]==1:
									grid[7][x5]=2
									coins=coins+5
									print("Hit")
								if grid[8][x5]==1:
									grid[8][x5]=2
									coins=coins+5
									print("Hit")
								if grid[9][x5]==1:
									grid[9][x5]=2
									coins=coins+5
									print("Hit")
#vertical 3x1(2)
							elif directionShip5==2:
								if grid[y10][x10]==1:
									grid[y10][x10]=2
									coins=coins+5
									print("Hit")
								if grid[y10][x10+1]==1:
									grid[y10][x10+1]=2
									coins=coins+5
									print("Hit")
								if grid[y10][x10+2]==1:
									grid[y10][x10+2]=2
									coins=coins+5
									print("Hit")

#hotizontal 3x1(2)

#checking for ship sunk
							if directionShip1==1:
								if grid[y6][x1]==2 and grid[y6+1][x1]==2 and grid[y6+2][x1]==2 and grid[y6+3][x1]==2 and grid[y6+4][x1]==2:
									grid[y6][x1]=3
									shipsdestroyed=shipsdestroyed+1
									shipsalive=shipsalive-1
									coins=coins+10
									print("Ship sunk")
#vertical 5x1
							elif directionShip1==2:
								if grid[y1][x6]==2 and grid[y1][x6+1]==2 and grid[y1][x6+2]==2 and grid[y1][x6+3]==2 and grid[y1][x6+4]==2:
									grid[y1][x6]=3
									shipsdestroyed=shipsdestroyed+1
									shipsalive=shipsalive-1
									coins=coins+10
									print("Ship sunk")
#horizontal	5x1									
							if directionShip2==1:	
								if grid[y2][x2]==2 and grid[y2+1][x2]==2 and grid[y2+2][x2]==2 and grid[y2+3][x2]==2:
									grid[y2][x2]=3
									shipsdestroyed=shipsdestroyed+1
									shipsalive=shipsalive-1
									coins=coins+10
									print("Ship sunk")
#vertical	4x1
							elif directionShip2==2:
								if grid[y7][6]==2 and grid[y7][7]==2 and grid[y7][8]==2 and grid[y7][9]==2:
									grid[y7][6]=3
									shipsdestroyed=shipsdestroyed+1
									shipsalive=shipsalive-1
									coins=coins+10
									print("Ship sunk")
#horizontal	4x1								
							if directionShip3==1:
								if grid[y3][x3]==2 and grid[y3+1][x3]==2:
									grid[y3][x3]=3
									shipsdestroyed=shipsdestroyed+1
									shipsalive=shipsalive-1
									coins=coins+10
									print("Ship sunk")
#vertical 2x1
							elif directionShip3==2:
								if grid[y8][x8]==2 and grid[y8][x8+1]==2:
									grid[y8][x8]=3
									shipsdestroyed=shipsdestroyed+1
									shipsalive=shipsalive-1
									coins=coins+10
									print("Ship sunk")
#horizontal 2x1
							if directionShip4==1:
								if grid[y4][x4]==2 and grid[y4+1][x4]==2 and grid[y4+2][x4]==2:
									grid[y4][x4]=3
									shipsdestroyed=shipsdestroyed+1
									shipsalive=shipsalive-1
									coins=coins+10
									print("Ship sunk")
#vertical 3x1(1)									
							elif directionShip4==2:
								if grid[y9][3]==2 and grid[y9][4]==2 and grid[y9][5]==2:
									grid[y9][3]=3
									shipsdestroyed=shipsdestroyed+1
									shipsalive=shipsalive-1
									coins=coins+10
									print("Ship sunk")
#horizontal 3x1(1)
							if directionShip5==1:
								if grid[7][x5]==2 and grid[8][x5]==2 and grid[9][x5]==2:
									grid[7][x5]=3
									shipsdestroyed=shipsdestroyed+1
									shipsalive=shipsalive-1
									coins=coins+10
									print("Ship sunk")
#vertical 3x1(2)
							elif directionShip5==2:
								if grid[y10][x10]==2 and grid[y10][x10+1]==2 and grid[y10][x10+2]==2:
									grid[y10][x10]=3
									shipsdestroyed=shipsdestroyed+1
									shipsalive=shipsalive-1
									coins=coins+10
									print("Ship sunk")
#horizontal 3x1(2)										
							
							
							if grid[row][column]==0 and ability1==False and ability2==False and ability3==False:
								grid[row][column]=1
								print("Grid location: ",row,column)
								guess_value=guess_value+1
								if (grid[4][10]==1 or grid[4][11]==1 or grid[4][12]==1) and coins>=50:
									grid[row][column]=0
									ability1=True
									guess_value=guess_value-1
									coins=coins-50
									print("Ability 1.")
									abilitycount=abilitycount+1
								elif (grid[4][10]==1 or grid[4][11]==1 or grid[4][12]==1) and coins<50:
									grid[row][column]=0
									guess_value=guess_value-1
									print("Not enough coins")
								if (grid[6][10]==1 or grid[6][11]==1 or grid[6][12]==1 ) and coins>=50:
									grid[row][column]=0
									ability2=True
									guess_value=guess_value-1
									coins=coins-50
									print("Ability 2")
									abilitycount=abilitycount+1
								elif (grid[6][10]==1 or grid[6][11]==1 or grid[6][12]==1 ) and coins<50:
									grid[row][column]=0
									guess_value=guess_value-1
									print("Not enough coins")
								if (grid[7][10]==1 or grid[7][11]==1 or grid[7][12]==1) and coins>=30:
									grid[row][column]=0
									ability3=True
									guess_value=guess_value-1
									coins=coins-30
									print("Ability 3 activated")
									abilitycount=abilitycount+1
								elif (grid[7][10]==1 or grid[7][11]==1 or grid[7][12]==1) and coins<30:
									grid[row][column]=0
									guess_value=guess_value-1
									print("Not enough coins")									
								if directionShip1==1:
									if grid[y6][x1]==1:
										grid[y6][x1]=2
										coins=coins+5
										print("Hit")
									if grid[y6+1][x1]==1:
										grid[y6+1][x1]=2
										coins=coins+5
										print("Hit")
									if grid[y6+2][x1]==1:
										grid[y6+2][x1]=2
										coins=coins+5
										print("Hit")
									if grid[y6+3][x1]==1:
										grid[y6+3][x1]=2
										coins=coins+5
										print("Hit")
									if grid[y6+4][x1]==1:
										grid[y6+4][x1]=2
										coins=coins+5
										print("Hit")									
#vertical 5x1
								elif directionShip1==2:
									if grid[y1][x6]==1:
										grid[y1][x6]=2
										coins=coins+5
										print("Hit")
									if grid[y1][x6+1]==1:
										grid[y1][x6+1]=2
										coins=coins+5
										print("Hit")
									if grid[y1][x6+2]==1:
										grid[y1][x6+2]=2
										coins=coins+5
										print("Hit")
									if grid[y1][x6+3]==1:
										grid[y1][x6+3]=2
										coins=coins+5
										print("Hit")
									if grid[y1][x6+4]==1:
										grid[y1][x6+4]=2
										coins=coins+5
										print("Hit")
#horizontal	5x1									
								if directionShip2==1:	
									if grid[y2][x2]==1:
										grid[y2][x2]=2
										coins=coins+5
										print("Hit")
									if grid[y2+1][x2]==1:
										grid[y2+1][x2]=2
										coins=coins+5
										print("Hit")
									if grid[y2+2][x2]==1:
										grid[y2+2][x2]=2
										coins=coins+5
										print("Hit")
									if grid[y2+3][x2]==1:
										grid[y2+3][x2]=2
										coins=coins+5
										print("Hit")
#vertical	4x1
								elif directionShip2==2:
									if grid[y7][6]==1:
										grid[y7][6]=2
										coins=coins+5
										print("Hit")
									if grid[y7][7]==1:
										grid[y7][7]=2
										coins=coins+5
										print("Hit")
									if grid[y7][8]==1:
										grid[y7][8]=2
										coins=coins+5
										print("Hit")
									if grid[y7][9]==1:
										grid[y7][9]=2
										coins=coins+5
										print("Hit")
#horizontal	4x1								
								if directionShip3==1:
									if grid[y3][x3]==1:
										grid[y3][x3]=2
										coins=coins+5
										print("Hit")
									if grid[y3+1][x3]==1:
										grid[y3+1][x3]=2
										coins=coins+5
										print("Hit")
									
#vertical 2x1
								elif directionShip3==2:
									if grid[y8][x8]==1:
										grid[y8][x8]=2
										coins=coins+5
										print("Hit")
									if grid[y8][x8+1]==1:
										grid[y8][x8+1]=2
										coins=coins+5
										print("Hit")
#horizontal 2x1
								if directionShip4==1:
									if grid[y4][x4]==1:
										grid[y4][x4]=2
										coins=coins+5
										print("Hit")
									if grid[y4+1][x4]==1:
										grid[y4+1][x4]=2
										coins=coins+5
										print("Hit")
									if grid[y4+2][x4]==1:
										grid[y4+2][x4]=2
										coins=coins+5
										print("Hit")									
#vertical 3x1(1)									
								elif directionShip4==2:
									if grid[y9][3]==1:
										grid[y9][3]=2
										coins=coins+5
										print("Hit")
									if grid[y9][4]==1:
										grid[y9][4]=2
										coins=coins+5
										print("Hit")
									if grid[y9][5]==1:
										grid[y9][5]=2
										coins=coins+5
										print("Hit")
#horizontal 3x1(1)	
								if directionShip5==1:
									if grid[7][x5]==1:
										grid[7][x5]=2
										coins=coins+5
										print("Hit")
									if grid[8][x5]==1:
										grid[8][x5]=2
										coins=coins+5
										print("Hit")
									if grid[9][x5]==1:
										grid[9][x5]=2
										coins=coins+5
										print("Hit")
#vertical 3x1(2)
								elif directionShip5==2:
									if grid[y10][x10]==1:
										grid[y10][x10]=2
										coins=coins+5
										print("Hit")
									if grid[y10][x10+1]==1:
										grid[y10][x10+1]=2
										coins=coins+5
										print("Hit")
									if grid[y10][x10+2]==1:
										grid[y10][x10+2]=2
										coins=coins+5
										print("Hit")
#hotizontal 3x1(2)

#checking for ship sunk
								if directionShip1==1:
									if grid[y6][x1]==2 and grid[y6+1][x1]==2 and grid[y6+2][x1]==2 and grid[y6+3][x1]==2 and grid[y6+4][x1]==2:
										grid[y6][x1]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										coins=coins+10
										print("Ship sunk")
#vertical 5x1
								elif directionShip1==2:
									if grid[y1][x6]==2 and grid[y1][x6+1]==2 and grid[y1][x6+2]==2 and grid[y1][x6+3]==2 and grid[y1][x6+4]==2:
										grid[y1][x6]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										coins=coins+10
										print("Ship sunk")
#horizontal	5x1									
								if directionShip2==1:	
									if grid[y2][x2]==2 and grid[y2+1][x2]==2 and grid[y2+2][x2]==2 and grid[y2+3][x2]==2:
										grid[y2][x2]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										coins=coins+10
										print("Ship sunk")
#vertical	4x1
								elif directionShip2==2:
									if grid[y7][6]==2 and grid[y7][7]==2 and grid[y7][8]==2 and grid[y7][9]==2:
										grid[y7][6]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										coins=coins+10
										print("Ship sunk")
#horizontal	4x1								
								if directionShip3==1:
									if grid[y3][x3]==2 and grid[y3+1][x3]==2:
										grid[y3][x3]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										coins=coins+10
										print("Ship sunk")
#vertical 2x1
								elif directionShip3==2:
									if grid[y8][x8]==2 and grid[y8][x8+1]==2:
										grid[y8][x8]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										coins=coins+10
										print("Ship sunk")
#horizontal 2x1
								if directionShip4==1:
									if grid[y4][x4]==2 and grid[y4+1][x4]==2 and grid[y4+2][x4]==2:
										grid[y4][x4]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										coins=coins+10
										print("Ship sunk")
#vertical 3x1(1)									
								elif directionShip4==2:
									if grid[y9][3]==2 and grid[y9][4]==2 and grid[y9][5]==2:
										grid[y9][3]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										coins=coins+10
										print("Ship sunk")
#horizontal 3x1(1)
								if directionShip5==1:
									if grid[7][x5]==2 and grid[8][x5]==2 and grid[9][x5]==2:
										grid[7][x5]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										coins=coins+10
										print("Ship sunk")
#vertical 3x1(2)
								elif directionShip5==2:
									if grid[y10][x10]==2 and grid[y10][x10+1]==2 and grid[y10][x10+2]==2:
										grid[y10][x10]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										coins=coins+10
										print("Ship sunk")
#horizontal 3x1(2)										
								
							elif grid[row][column]==1 or grid[row][column]==2 or grid[row][column]==3:
								print("Location already guessed. Try another location.")
							if shipsdestroyed==5:
								winning(guess_value,name,computerlvl,abilitycount,gametype)
							if computerlvl=="easy":
								if guess_value==60:
									losing(guess_value,shipsdestroyed,name,computerlvl,abilitycount,gametype,shipsalive)
							elif computerlvl=="medium":
								if guess_value==40:
									losing(guess_value,shipsdestroyed,name,computerlvl,abilitycount,gametype,shipsalive)
							elif computerlvl=="hard":
								if guess_value==30:
									losing(guess_value,shipsdestroyed,name,computerlvl,abilitycount,gametype,shipsalive)
		
					for row in range(10):
						for column in range(10):
							color = (white)
							if grid[row][column]==1 :
								color = blue
							elif grid[row][column]==2:
								color=red
							elif grid[row][column]==3:
								color=red
							pygame.draw.rect(screen, color,[(MARGIN + WIDTH) * column + MARGIN,(MARGIN + HEIGHT) * row + MARGIN,WIDTH, HEIGHT])
					pygame.draw.rect(screen, (255, 0, 0), button_abilityvertical)
					pygame.draw.rect(screen, (255, 0, 0), button_abilityhorizontal)
					pygame.draw.rect(screen, (255, 0, 0), button_ability3x3)
					clock.tick(60)
					guess(460, 20)
					ShipDestroyed(460,100)
					ShipsAlive(460,60)
					CoinCounter(460,140)
					draw_text("Ability 1(50) (Vertical)", Ntitle, (255, 255, 255), screen, 460, 170)
					draw_text("Ability 2(50) (Horizontal)", Ntitle, (255, 255, 255), screen, 460, 250)
					draw_text("Ability 3(30) ", Ntitle, (255, 255, 255), screen, 460, 310)
					pygame.display.flip()
					pygame.display.update()
					screen.fill(background)
#10x10 advanced					
	elif board=="12x12" and gametype=="advanced":
		font=pygame.font.Font(None,32)
		def guess(x, y):
			guesses= font.render("Guess : "+ str(guess_value),True,(white))
			screen.blit(guesses,(x,y))

		shipsdestroyed=0

		def ShipDestroyed(x, y):
			shipsDes=font.render("Ships destroyed : "+str(shipsdestroyed),True,(white))
			screen.blit(shipsDes,(x,y))

		shipsalive=5

		def ShipsAlive(x, y):
			ShipsAli=font.render("Ships left : " +str(shipsalive),True,(white))
			screen.blit(ShipsAli,(x,y))

		coins=0

		def CoinCounter(x,y):
			CoinsCount=font.render("Coins : " +str(coins),True,(white))
			screen.blit(CoinsCount,(x,y))
			
		x1=random.randint(0,6)
		x2=random.randint(7,11)
		x3=random.randint(0,3)
		x4=random.randint(4,6)
		x5=random.randint(0,6)
		x6=random.randint(0,4)
		x7=random.randint(0,0)
		x8=random.randint(0,1)
		x9=random.randint(4,5)
		x10=random.randint(0,3)
		y1=random.randint(0,5)
		y2=random.randint(0,7)
		y3=random.randint(3,5)
		y4=random.randint(3,6)
		y5=random.randint(0,0)
		y6=random.randint(0,2)
		y7=random.randint(0,11)
		y8=random.randint(3,7)
		y9=random.randint(3,7)
		y10=random.randint(8,11)
		directionShip1=random.randint(1,2)
		directionShip2=random.randint(1,2)
		directionShip3=random.randint(1,2)
		directionShip4=random.randint(1,2)
		directionShip5=random.randint(1,2)
		screen = pygame.display.set_mode((800, 800),0,32)
		running=True
		ability1=False
		ability2=False
		ability3=False
		
		while running==True:
			button_abilityvertical = pygame.Rect(560, 190, 100, 30)
			button_abilityhorizontal = pygame.Rect(560, 270, 100, 30)
			button_ability3x3 = pygame.Rect(560, 330, 100, 30)
			if running==True:
				for row in range(200):
					grid.append([0])
					for column in range(200):
						grid[row].append(0) 
				done = False
				clock = pygame.time.Clock()
				while not done: 
					for event in pygame.event.get(): 
						if event.type == pygame.QUIT: 
							done = True 
						elif event.type == pygame.MOUSEBUTTONDOWN:
							pos = pygame.mouse.get_pos()
							column = pos[0] // (WIDTH + MARGIN)
							row = pos[1] // (HEIGHT + MARGIN)
							if ability1==True:
								ability1=False
								grid[row][column]=1
								grid[row+1][column]=1
								grid[row+2][column]=1
								grid[row+3][column]=1
								grid[row+4][column]=1
								grid[row+5][column]=1
								grid[row+6][column]=1
								grid[row+7][column]=1
								grid[row+8][column]=1
								grid[row+9][column]=1
								grid[row+10][column]=1
								grid[row+11][column]=1
								guess_value=guess_value+1
								if grid[4][12]==1 or grid[4][13]==1 or grid[4][14]==1:
									grid[4][12]=0 
									grid[4][13]=0
									grid[4][14]=0
								if grid[6][12]==1 or grid[6][13]==1 or grid[6][14]==1:
									grid[6][12]=0 
									grid[6][13]=0
									grid[6][14]=0
								if grid[7][12]==1 or grid[7][13]==1 or grid[7][14]==1:
									grid[7][12]=0
									grid[7][13]=0
									grid[7][14]=0
							
							elif ability2==True:
								ability2=False
								grid[row][column]=1
								grid[row][column+1]=1
								grid[row][column+2]=1
								grid[row][column+3]=1
								grid[row][column+4]=1
								grid[row][column+5]=1
								grid[row][column+6]=1
								grid[row][column+7]=1
								grid[row][column+8]=1
								grid[row][column+9]=1
								grid[row][column+10]=1
								grid[row][column+11]=1
								guess_value=guess_value+1
								if grid[4][12]==1 or grid[4][13]==1 or grid[4][14]==1:
									grid[4][12]=0 
									grid[4][13]=0
									grid[4][14]=0
								if grid[6][12]==1 or grid[6][13]==1 or grid[6][14]==1:
									grid[6][12]=0 
									grid[6][13]=0
									grid[6][14]=0
								if grid[7][12]==1 or grid[7][13]==1 or grid[7][14]==1:
									grid[7][12]=0
									grid[7][13]=0
									grid[7][14]=0

							elif ability3==True:
								ability3=False
								grid[row][column]=1
								grid[row-1][column-1]=1
								grid[row-1][column]=1
								grid[row-1][column+1]=1
								grid[row][column-1]=1
								grid[row][column+1]=1
								grid[row+1][column-1]=1
								grid[row+1][column]=1
								grid[row+1][column+1]=1
								guess_value=guess_value+1
								if grid[4][12]==1 or grid[4][13]==1 or grid[4][14]==1:
									grid[4][12]=0 
									grid[4][13]=0
									grid[4][14]=0
								if grid[6][12]==1 or grid[6][13]==1 or grid[6][14]==1:
									grid[6][12]=0 
									grid[6][13]=0
									grid[6][14]=0
								if grid[7][12]==1 or grid[7][13]==1 or grid[7][14]==1:
									grid[7][12]=0
									grid[7][13]=0
									grid[7][14]=0
								
							
							if directionShip1==1:
								if grid[0][x1]==1:
									grid[0][x1]=2
									coins=coins+5
									print("Hit")
								if grid[1][x1]==1:
									grid[1][x1]=2
									coins=coins+5
									print("Hit")
								if grid[2][x1]==1:
									grid[2][x1]=2
									coins=coins+5
									print("Hit")
#vertical 3x1(1)
							elif directionShip1==2:
								if grid[y6][x6]==1:
									grid[y6][x6]=2
									coins=coins+5
									print("Hit")
								if grid[y6][x6+1]==1:
									grid[y6][x6+1]=2
									coins=coins+5
									print("Hit")
								if grid[y6][x6+2]==1:
									grid[y6][x6+2]=2
									coins=coins+5
									print("Hit")
#horizontal	3x1(1)								
							if directionShip2==1:	
								if grid[y2][x2]==1:
									grid[y2][x2]=2
									coins=coins+5
									print("Hit")
								if grid[y2+1][x2]==1:
									grid[y2+1][x2]=2
									coins=coins+5
									print("Hit")
								if grid[y2+2][x2]==1:
									grid[y2+2][x2]=2
									coins=coins+5
									print("Hit")
								if grid[y2+3][x2]==1:
									grid[y2+3][x2]=2
									coins=coins+5
									print("Hit")
								if grid[y2+4][x2]==1:
									grid[y2+4][x2]=2
									coins=coins+5
									print("Hit")
#vertical	5x1
							elif directionShip2==2:
								if grid[y7][7]==1:
									grid[y7][7]=2
									coins=coins+5
									print("Hit")
								if grid[y7][8]==1:
									grid[y7][8]=2
									coins=coins+5
									print("Hit")
								if grid[y7][9]==1:
									grid[y7][9]=2
									coins=coins+5
									print("Hit")
								if grid[y7][10]==1:
									grid[y7][10]=2
									coins=coins+5
									print("Hit")
								if grid[y7][11]==1:
									grid[y7][11]=2
									coins=coins+5
									print("Hit")
#horizontal	5x1								
							if directionShip3==1:
								if grid[y3][x3]==1:
									grid[y3][x3]=2
									coins=coins+5
									print("Hit")
								if grid[y3+1][x3]==1:
									grid[y3+1][x3]=2
									coins=coins+5
									print("Hit")
								if grid[y3+2][x3]==1:
									grid[y3+2][x3]=2
									coins=coins+5
									print("Hit")
#vertical 3x1(2)
							elif directionShip3==2:
								if grid[y8][x8]==1:
									grid[y8][x8]=2
									coins=coins+5
									print("Hit")
								if grid[y8][x8+1]==1:
									grid[y8][x8+1]=2
									coins=coins+5
									print("Hit")
								if grid[y8][x8+2]==1:
									grid[y8][x8+2]=2
									coins=coins+5
									print("Hit")
#horizontal 3x1(2)
							if directionShip4==1:
								if grid[y4][x4]==1:
									grid[y4][x4]=2
									coins=coins+5
									print("Hit")
								if grid[y4+1][x4]==1:
									grid[y4+1][x4]=2
									coins=coins+5
									print("Hit")
#vertical 2x1									
							elif directionShip4==2:
								if grid[y9][x9]==1:
									grid[y9][x9]=2
									coins=coins+5
									print("Hit")
								if grid[y9][x9+1]==1:
									grid[y9][x9+1]=2
									coins=coins+5
									print("Hit")
									
#horizontal 2x1	
							if directionShip5==1:
								if grid[8][x5]==1:
									grid[8][x5]=2
									coins=coins+5
									print("Hit")
								if grid[9][x5]==1:
									grid[9][x5]=2
									coins=coins+5
									print("Hit")
								if grid[10][x5]==1:
									grid[10][x5]=2
									coins=coins+5
									print("Hit")
								if grid[11][x5]==1:
									grid[11][x5]=2
									coins=coins+5
									print("Hit")
#vertical 4x1
							elif directionShip5==2:
								if grid[y10][x10]==1:
									grid[y10][x10]=2
									coins=coins+5
									print("Hit")
								if grid[y10][x10+1]==1:
									grid[y10][x10+1]=2
									coins=coins+5
									print("Hit")
								if grid[y10][x10+2]==1:
									grid[y10][x10+2]=2
									coins=coins+5
									print("Hit")
								if grid[y10][x10+3]==1:
									grid[y10][x10+3]=2
									coins=coins+5
									print("Hit")
#hotizontal 4x1

#checking for sunk ships
							if directionShip1==1:
								if grid[0][x1]==2 and grid[1][x1]==2 and grid[2][x1]==2:
									grid[0][x1]=3
									shipsdestroyed=shipsdestroyed+1
									shipsalive=shipsalive-1
									coins=coins+10
									print("Ship sunk")
#vertical 3x1(1)
							elif directionShip1==2:
								if grid[y6][x6]==2 and grid[y6][x6+1]==2 and grid[y6][x6+2]==2:
									grid[y6][x6]=3
									shipsdestroyed=shipsdestroyed+1
									shipsalive=shipsalive-1
									coins=coins+10
									print("Ship sunk")
#horizontal	3x1(1)									
							if directionShip2==1:	
								if grid[y2][x2]==2 and grid[y2+1][x2]==2 and grid[y2+2][x2]==2 and grid[y2+3][x2]==2 and grid[y2+4][x2]==2:
									grid[y2][x2]=3
									shipsdestroyed=shipsdestroyed+1
									shipsalive=shipsalive-1
									coins=coins+10
									print("Ship sunk")
#vertical 5x1
							elif directionShip2==2:
								if grid[y7][7]==2 and grid[y7][8]==2 and grid[y7][9]==2 and grid[y7][10]==2 and grid[y7][11]==2:
									grid[y7][7]=3
									shipsdestroyed=shipsdestroyed+1
									shipsalive=shipsalive-1
									coins=coins+10
									print("Ship sunk")
#horizontal	5x1								
							if directionShip3==1:
								if grid[y3][x3]==2 and grid[y3+1][x3]==2 and grid[y3+2][x3]==2:
									grid[y3][x3]=3
									shipsdestroyed=shipsdestroyed+1
									shipsalive=shipsalive-1
									coins=coins+10
									print("Ship sunk")
#vertical 3x1(2)
							elif directionShip3==2:
								if grid[y8][x8]==2 and grid[y8][x8+1]==2 and grid[y8][x8+2]==2:
									grid[y8][x8]=3
									shipsdestroyed=shipsdestroyed+1
									shipsalive=shipsalive-1
									coins=coins+10
									print("Ship sunk")
#horizontal 3x1(2)
							if directionShip4==1:
								if grid[y4][x4]==2 and grid[y4+1][x4]==2:
									grid[y4][x4]=3
									shipsdestroyed=shipsdestroyed+1
									shipsalive=shipsalive-1
									coins=coins+10
									print("Ship sunk")
#vertical 2x1									
							elif directionShip4==2:
								if grid[y9][x9]==2 and grid[y9][x9+1]==2:
									grid[y9][x9]=3
									shipsdestroyed=shipsdestroyed+1
									shipsalive=shipsalive-1
									coins=coins+10
									print("Ship sunk")
#horizontal 2x1	
							if directionShip5==1:
								if grid[8][x5]==2 and grid[9][x5]==2 and grid[10][x5]==2 and grid[11][x5]==2:
									grid[8][x5]=3
									shipsdestroyed=shipsdestroyed+1
									shipsalive=shipsalive-1
									coins=coins+10
									print("Ship sunk")
#vertical 4x1
							elif directionShip5==2:
								if grid[y10][x10]==2 and grid[y10][x10+1]==2 and grid[y10][x10+2]==2 and grid[y10][x10+3]==2:
									grid[y10][x10]=3
									shipsdestroyed=shipsdestroyed+1
									shipsalive=shipsalive-1
									coins=coins+10
									print("Ship sunk")
#horiziontal 4x1
							if grid[row][column]==0 and ability1==False and ability2==False and ability3==False:
								grid[row][column]=1
								print("Grid location: ",row,column)
								guess_value=guess_value+1
								if (grid[4][12]==1 or grid[4][13]==1 or grid[4][14]==1) and coins>=50:
									grid[row][column]=0
									ability1=True
									guess_value=guess_value-1
									coins=coins-50
									print("Ability 1.")
									abilitycount=abilitycount+1
								elif (grid[4][12]==1 or grid[4][13]==1 or grid[4][14]==1) and coins<50:
									grid[row][column]=0
									guess_value=guess_value-1
									print("Not enough coins")
								if (grid[6][12]==1 or grid[6][13]==1 or grid[6][14]==1 ) and coins>=50:
									grid[row][column]=0
									ability2=True
									guess_value=guess_value-1
									coins=coins-50
									print("Ability 2")
									abilitycount=abilitycount+1
								elif (grid[6][12]==1 or grid[6][13]==1 or grid[6][14]==1 ) and coins<50:
									grid[row][column]=0
									guess_value=guess_value-1
									print("Not enough coins")
								if (grid[7][12]==1 or grid[7][13]==1 or grid[7][14]==1) and coins>=30:
									grid[row][column]=0
									ability3=True
									guess_value=guess_value-1
									coins=coins-30
									print("Ability 3 activated")
									abilitycount=abilitycount+1
								elif (grid[7][12]==1 or grid[7][13]==1 or grid[7][14]==1) and coins<30:
									grid[row][column]=0
									guess_value=guess_value-1
									print("Not enough coins")
								if directionShip1==1:
									if grid[0][x1]==1:
										grid[0][x1]=2
										coins=coins+5
										print("Hit")
									if grid[1][x1]==1:
										grid[1][x1]=2
										coins=coins+5
										print("Hit")
									if grid[2][x1]==1:
										grid[2][x1]=2
										coins=coins+5
										print("Hit")
#vertical 3x1(1)
								elif directionShip1==2:
									if grid[y6][x6]==1:
										grid[y6][x6]=2
										coins=coins+5
										print("Hit")
									if grid[y6][x6+1]==1:
										grid[y6][x6+1]=2
										coins=coins+5
										print("Hit")
									if grid[y6][x6+2]==1:
										grid[y6][x6+2]=2
										coins=coins+5
										print("Hit")
#horizontal	3x1(1)									
								if directionShip2==1:	
									if grid[y2][x2]==1:
										grid[y2][x2]=2
										coins=coins+5
										print("Hit")
									if grid[y2+1][x2]==1:
										grid[y2+1][x2]=2
										coins=coins+5
										print("Hit")
									if grid[y2+2][x2]==1:
										grid[y2+2][x2]=2
										coins=coins+5
										print("Hit")
									if grid[y2+3][x2]==1:
										grid[y2+3][x2]=2
										coins=coins+5
										print("Hit")
									if grid[y2+4][x2]==1:
										grid[y2+4][x2]=2
										coins=coins+5
										print("Hit")
#vertical	5x1
								elif directionShip2==2:
									if grid[y7][7]==1:
										grid[y7][7]=2
										coins=coins+5
										print("Hit")
									if grid[y7][8]==1:
										grid[y7][8]=2
										coins=coins+5
										print("Hit")
									if grid[y7][9]==1:
										grid[y7][9]=2
										coins=coins+5
										print("Hit")
									if grid[y7][10]==1:
										grid[y7][10]=2
										coins=coins+5
										print("Hit")
									if grid[y7][11]==1:
										grid[y7][11]=2
										coins=coins+5
										print("Hit")
#horizontal	5x1								
								if directionShip3==1:
									if grid[y3][x3]==1:
										grid[y3][x3]=2
										coins=coins+5
										print("Hit")
									if grid[y3+1][x3]==1:
										grid[y3+1][x3]=2
										coins=coins+5
										print("Hit")
									if grid[y3+2][x3]==1:
										grid[y3+2][x3]=2
										coins=coins+5
										print("Hit")
#vertical 3x1(2)
								elif directionShip3==2:
									if grid[y8][x8]==1:
										grid[y8][x8]=2
										coins=coins+5
										print("Hit")
									if grid[y8][x8+1]==1:
										grid[y8][x8+1]=2
										coins=coins+5
										print("Hit")
									if grid[y8][x8+2]==1:
										grid[y8][x8+2]=2
										coins=coins+5
										print("Hit")
#horizontal 3x1(2)
								if directionShip4==1:
									if grid[y4][x4]==1:
										grid[y4][x4]=2
										coins=coins+5
										print("Hit")
									if grid[y4+1][x4]==1:
										grid[y4+1][x4]=2
										coins=coins+5
										print("Hit")
#vertical 2x1									
								elif directionShip4==2:
									if grid[y9][x9]==1:
										grid[y9][x9]=2
										coins=coins+5
										print("Hit")
									if grid[y9][x9+1]==1:
										grid[y9][x9+1]=2
										coins=coins+5
										print("Hit")
									
#horizontal 2x1	
								if directionShip5==1:
									if grid[8][x5]==1:
										grid[8][x5]=2
										coins=coins+5
										print("Hit")
									if grid[9][x5]==1:
										grid[9][x5]=2
										coins=coins+5
										print("Hit")
									if grid[10][x5]==1:
										grid[10][x5]=2
										coins=coins+5
										print("Hit")
									if grid[11][x5]==1:
										grid[11][x5]=2
										coins=coins+5
										print("Hit")
#vertical 4x1
								elif directionShip5==2:
									if grid[y10][x10]==1:
										grid[y10][x10]=2
										coins=coins+5
										print("Hit")
									if grid[y10][x10+1]==1:
										grid[y10][x10+1]=2
										coins=coins+5
										print("Hit")
									if grid[y10][x10+2]==1:
										grid[y10][x10+2]=2
										coins=coins+5
										print("Hit")
									if grid[y10][x10+3]==1:
										grid[y10][x10+3]=2
										coins=coins+5
										print("Hit")
#hotizontal 4x1

#checking for sunk ships
								if directionShip1==1:
									if grid[0][x1]==2 and grid[1][x1]==2 and grid[2][x1]==2:
										grid[0][x1]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										coins=coins+10
										print("Ship sunk")
#vertical 3x1(1)
								elif directionShip1==2:
									if grid[y6][x6]==2 and grid[y6][x6+1]==2 and grid[y6][x6+2]==2:
										grid[y6][x6]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										coins=coins+10
										print("Ship sunk")
#horizontal	3x1(1)									
								if directionShip2==1:	
									if grid[y2][x2]==2 and grid[y2+1][x2]==2 and grid[y2+2][x2]==2 and grid[y2+3][x2]==2 and grid[y2+4][x2]==2:
										grid[y2][x2]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										coins=coins+10
										print("Ship sunk")
#vertical	5x1
								elif directionShip2==2:
									if grid[y7][7]==2 and grid[y7][8]==2 and grid[y7][9]==2 and grid[y7][10]==2 and grid[y7][11]==2:
										grid[y7][7]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										coins=coins+10
										print("Ship sunk")
#horizontal	5x1								
								if directionShip3==1:
									if grid[y3][x3]==2 and grid[y3+1][x3]==2 and grid[y3+2][x3]==2:
										grid[y3][x3]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										coins=coins+10
										print("Ship sunk")
#vertical 3x1(2)
								elif directionShip3==2:
									if grid[y8][x8]==2 and grid[y8][x8+1]==2 and grid[y8][x8+2]==2:
										grid[y8][x8]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										coins=coins+10
										print("Ship sunk")
#horizontal 3x1(2)
								if directionShip4==1:
									if grid[y4][x4]==2 and grid[y4+1][x4]==2:
										grid[y4][x4]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										coins=coins+10
										print("Ship sunk")
#vertical 2x1									
								elif directionShip4==2:
									if grid[y9][x9]==2 and grid[y9][x9+1]==2:
										grid[y9][x9]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										coins=coins+10
										print("Ship sunk")
#horizontal 2x1	
								if directionShip5==1:
									if grid[8][x5]==2 and grid[9][x5]==2 and grid[10][x5]==2 and grid[11][x5]==2:
										grid[8][x5]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										coins=coins+10
										print("Ship sunk")
#vertical 4x1
								elif directionShip5==2:
									if grid[y10][x10]==2 and grid[y10][x10+1]==2 and grid[y10][x10+2]==2 and grid[y10][x10+3]==2:
										grid[y10][x10]=3
										shipsdestroyed=shipsdestroyed+1
										shipsalive=shipsalive-1
										coins=coins+10
										print("Ship sunk")
#hotizontal 4x1								

							elif grid[row][column]==1 or grid[row][column]==2 or grid[row][column]==3:
								print("Location already guessed. Try another location.")
							if shipsdestroyed==5:
								winning(guess_value,name,computerlvl,abilitycount,gametype)
							if computerlvl=="easy":
								if guess_value==90:
									losing(guess_value,shipsdestroyed,name,computerlvl,abilitycount,gametype,shipsalive)
							elif computerlvl=="medium":
								if guess_value==60:
									losing(guess_value,shipsdestroyed,name,computerlvl,abilitycount,gametype,shipsalive)
							elif computerlvl=="hard":
								if guess_value==45:
									losing(guess_value,shipsdestroyed,name,computerlvl,abilitycount,gametype,shipsalive)
		
					for row in range(12):
						for column in range(12):
							color = (white)
							if grid[row][column]==1 :
								color = blue
							elif grid[row][column]==2:
								color=red
							elif grid[row][column]==3:
								color=red
							pygame.draw.rect(screen, color,[(MARGIN + WIDTH) * column + MARGIN,(MARGIN + HEIGHT) * row + MARGIN,WIDTH, HEIGHT])
					pygame.draw.rect(screen, (255, 0, 0), button_abilityvertical)
					pygame.draw.rect(screen, (255, 0, 0), button_abilityhorizontal)
					pygame.draw.rect(screen, (255, 0, 0), button_ability3x3)
					clock.tick(60)
					guess(560, 20)
					ShipDestroyed(560,100)
					ShipsAlive(560,60)
					CoinCounter(560,140)
					draw_text("Ability 1(50) (Vertical)", Ntitle, (255, 255, 255), screen, 560, 170)
					draw_text("Ability 2(50) (Horizontal)", Ntitle, (255, 255, 255), screen, 560, 250)
					draw_text("Ability 3(30) ", Ntitle, (255, 255, 255), screen, 560, 310)
					pygame.display.flip()
					pygame.display.update()
					screen.fill(background)
#12x12 advanced
def winning(guess_value,name,computerlvl,abilitycount,gametype):
	running = True
	font=pygame.font.Font(None,32)
	while running==True:
		screen.fill((0,0,0))
		def guess(x, y):
			guesses= font.render("Guesses taken : "+ str(guess_value),True,(255,255,255))
			screen.blit(guesses,(x,y))
#function for guesses taken.
		def names(x, y):
			NamesOutput=font.render("Congratulations on winning, Captain "+ str(name),True ,(255,255,255) )
			screen.blit(NamesOutput,(x,y))
#function for winning message+name output
		def computerlevel(x, y):
			computer=font.render("The computer level was "+ str(computerlvl),True ,(255,255,255) )
			screen.blit(computer,(x,y))
#function for the computer level difficulty output
		def abilitycounter(x, y):
			ability=font.render("Ability used: "+ str(abilitycount),True ,(255,255,255) )
			screen.blit(ability,(x,y))
#function for the abilities used count output
		button_playagain = pygame.Rect(5, 280, 100, 30)
		pygame.draw.rect(screen, (255, 0, 0), button_playagain)
#Creating the play again button
		button_thanks = pygame.Rect(200, 280, 100, 30)
		pygame.draw.rect(screen, (255, 0, 0), button_thanks)
#Creating the thanks for playing button
		draw_text("Do you want to play again?", Ntitle, (255, 255, 255), screen, 5, 240)
		draw_text("yes", Ntitle, (255, 255, 255), screen, 5, 260)
		draw_text("no", Ntitle, (255, 255, 255), screen, 200, 260)
#play again text
		mx, my = pygame.mouse.get_pos()
#finding the position of the mouse.
		names(5,20)
		guess(5,80)
		computerlevel(5,140)
#Using the functions and outputting the text+variable values.
		if gametype=="advanced":
			abilitycounter(5,200)
#If the game type was advanced it outputs the ability used counter
		if button_playagain.collidepoint((mx, my)):
			if click:
				gamemodes(name)
#If the user clicks on the play again button it takes them to the gamemode screen
		if button_thanks.collidepoint((mx, my)):
			if click:
				thanksforplaying(name)
#If the user clicks on the thanks button it takes them to the thanks for playing screen
		pygame.display.flip()
		mainClock.tick(60)
		click = False
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					username()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True
#finding if the user clicks using mouse 1.		
def losing(guess_value,shipsdestroyed,name,computerlvl,abilitycount,gametype,shipsalive):
	running = True
	font=pygame.font.Font(None,32)
	while running==True:
		screen.fill((0,0,0))
		def guess(x, y):
			guesses= font.render("Guesses taken : "+ str(guess_value),True,(255,255,255))
			screen.blit(guesses,(x,y))
#function for guesses taken.
		def shipdes(x, y):
			ships= font.render("Ships destroyed : "+ str(shipsdestroyed),True,(255,255,255))
			screen.blit(ships,(x,y))
#function for the amount of ships destroyed counter output.
		def names(x, y):
			NamesOutput=font.render("You have lost, Captain "+ str(name),True ,(255,255,255) )
			screen.blit(NamesOutput,(x,y))
#function for losing message+name output
		def computerlevel(x, y):
			computer=font.render("The computer level was "+ str(computerlvl),True ,(255,255,255) )
			screen.blit(computer,(x,y))
#function for the computer level difficulty output
		def abilitycounter(x, y):
			ability=font.render("Abilities used: "+ str(abilitycount),True ,(255,255,255) )
			screen.blit(ability,(x,y))
#function for the ability counter output
		def shipali(x, y):
			ships=font.render("Ships left: "+ str(shipsalive),True ,(255,255,255) )
			screen.blit(ships,(x,y))
#function for the ships left counter output.
		button_playagain = pygame.Rect(5, 400, 100, 30)
		pygame.draw.rect(screen, (255, 0, 0), button_playagain)
#Creating the play again button
		button_thanks = pygame.Rect(200, 400, 100, 30)
		pygame.draw.rect(screen, (255, 0, 0), button_thanks)
#Creating the thanks for playing button
		draw_text("Do you want to play again?", Ntitle, (255, 255, 255), screen, 5, 360)
		draw_text("yes", Ntitle, (255, 255, 255), screen, 5, 380)
		draw_text("no", Ntitle, (255, 255, 255), screen, 200, 380)
#play again text
		mx, my = pygame.mouse.get_pos()
#finding the position of the mouse.
		names(5,20)
		guess(5,80)
		shipdes(5,140)
		computerlevel(5,260)
		shipali(5,200)
#Using the functions and outputting the text+variable values.
		if gametype=="advanced":
			abilitycounter(5,320)
#If the game type was advanced it outputs the ability used counter
		if button_playagain.collidepoint((mx, my)):
			if click:
				gamemodes(name)
#If the user clicks on the play again button it takes them to the gamemode screen
		if button_thanks.collidepoint((mx, my)):
			if click:
				thanksforplaying(name)
#If the user clicks on the thanks button it takes them to the thanks for playing screen
		pygame.display.flip()
		mainClock.tick(60)
		click=False
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					username()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True
#finding if the user clicks using mouse 1.
def thanksforplaying(name):
	running = True
	font=pygame.font.Font(None,50)
	while running:
		screen.fill((0,0,0))
		def thanks(x, y):
			thanksmsg= font.render("Thank you for playing my game: "+ str(name),True,(255,255,255))
			screen.blit(thanksmsg,(x,y))
#function fo the thanks for playing message+username
		thanks(5,20)
#using the thanks function 
		draw_text("Thanks for testing out my program.", Ntitle, (255, 255, 255), screen, 5, 80)
		draw_text("If you have any feedback, send it to my email-", Ntitle, (255, 255, 255), screen, 5, 100)
		draw_text("Ctang@hillhouse.doncaster.sch.uk", Ntitle, (255, 255, 255), screen, 5, 120)
#outputing text 
		pygame.display.flip()
		mainClock.tick(60)

main_menu()
#calls the main menu function at the start of the program.