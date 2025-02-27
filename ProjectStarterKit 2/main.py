# Part two of final project
# 2023-12-04
# Sayna Naghavi and Maria Fahim

import cmpt120image
import draw
import pygame
import os
import random

def playSound(soundfilename):
    dir = os.path.dirname(os.path.abspath(__file__))
    pygame.mixer.init()
    pygame.mixer.music.load(dir + "/sounds/" + soundfilename + ".wav")
    pygame.mixer.music.play()

def getCurrentPath():
    dir = os.path.dirname(os.path.abspath(__file__))
    return dir + "/"
###############################################################


full_path = getCurrentPath() + "blackfoot.csv"
my_csv_file = open(full_path)
# Now use `my_csv_file` to read all the values.
pictures= []
for line in my_csv_file:
     pictures.append(line.strip("\n"))


def main_menu():
   menu_options = [
       "1. Learn     - Word flashcards",
       "2. Play      - Seek and Find Game",
       "3. Settings  - Change difficulty",
       "4. Exit\n"
   ]
   print("\nMAIN MENU")
   for option in menu_options:
       print(option)

def getWhiteImage(width, height): # to help with making the canvas
    # from cmpt120 get black image function:
    return [[[255,255,255] for i in range(width)] for j in range(height)]
 
def learn(num_items_to_teach):
   canvas_height = 400
   canvas_width = 400

   for i in range(num_items_to_teach):
       img_name = pictures[i]
       img_path = getCurrentPath()  + "images/" + img_name + ".png"


       image_list = cmpt120image.getImage(img_path)
   
       cmpt120image.showImage(image_list, f"Showing picture for {img_name}")  
       canvas= getWhiteImage(canvas_width,canvas_height)
       
       draw.distributeItems(canvas,image_list,1)
       cmpt120image.showImage(canvas, f"Learning {img_name}")
       playSound(img_name)
       input("Press enter when sound has finished to exit...")

def get_random_rgb_colour():
   # returns a tuple of three values: r, g, b
   r = random.randint(0,250)
   g = random.randint(0,250)
   b = random.randint(0,250)
   return (r,g,b)          

def play(rounds, pics):  
    canvas_height = 400
    canvas_width = 400
    for j in range(rounds):
        chosen_image_number = random.randint(0,num_items_to_teach-1)
        chosen_image= pics[chosen_image_number]
        # to display
        canvas= getWhiteImage(canvas_width,canvas_height)
       
        correct_displayed_count=0
       
        for i in range(num_items_to_teach):
           
            img_name = pics[i]
            img_path = getCurrentPath()  + "images/" + img_name + ".png"
               
            image_list = cmpt120image.getImage(img_path)
            # choosing a random color
            image_list= draw.recolorImage(image_list,get_random_rgb_colour())
            # randomly mirrored and minified if num items to teach are even
            if num_items_to_teach%2==0:
                image_list= draw.minify(image_list)
                image_list= draw.mirror(image_list)
           
            number_of_display = random.randint(1, 4)
            draw.distributeItems(canvas,image_list,number_of_display)


            if img_name==chosen_image:
                correct_displayed_count= number_of_display
           
        cmpt120image.showImage(canvas, f"Round: {j+1} - Count the items")


        playSound(chosen_image)
        nums_guessed= int(input(f"\nHow many of the items are shown? \
\nCHEAT: look for {chosen_image}! "))
        if nums_guessed == correct_displayed_count:
                print(f"Correct! there were exactly {correct_displayed_count}\
 of {chosen_image}\n")
        else:
                print(f"im sorry! There were {correct_displayed_count} of \
{chosen_image}!")

# MAIN MENU
num_items_to_teach= 3
user_opt = 0
while user_opt != 4:
    main_menu()
    user_opt = int(input("Choose an option: "))
    if user_opt==1:
        learn(num_items_to_teach)
    elif user_opt==2:
        rounds= int(input("How many rounds do you want to play? "))
      
        play(rounds,pictures)
    elif user_opt ==3:
        num_items_to_teach=int(input("How many words do you want to work on? \
(3-12) "))
        if num_items_to_teach < 3 or num_items_to_teach > 12:
            print("OH no try another number! We reset it to 3!")
            num_items_to_teach= 3