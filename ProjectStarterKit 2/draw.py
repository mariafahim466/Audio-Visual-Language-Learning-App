# Final project part 1 
# Maria fahim and Sayna Naghavi 
# 2023/11/20

import cmpt120image
import random
import pygame
import numpy

def getWhiteImage(width, height):
    # from cmpt120 get black image function: 
    return [[[255,255,255] for i in range(width)] for j in range(height)] 

def recolorImage(img, color):
    new_img = getWhiteImage(len(img[0]), len(img))
    h = len(img)
    w = len(img[0])

    for y in range(h):
        for x in range(w): # checking for white pixels
            not_white = False # assuming the background is white 
            for value in img[y][x]:
                if value < 250:
                    not_white = True
                    break

            if not_white:
                new_img[y][x] = color

    return new_img

def minify(img):
    height = len(img)
    width = len(img[0])

    new_h= height // 2
    new_w= width // 2

    # half the size
    result_img = getWhiteImage(new_h,new_w)
  
    for y in range(0, height, 2): 
        for x in range(0, width, 2): # help of chatgpt for the next 4 lines 
            pixel1 = img[y][x]
            pixel2 = img[y][x + 1]
            pixel3 = img[y + 1][x]
            pixel4 = img[y + 1][x + 1]

            avg_R = (pixel1[0] + pixel2[0] + pixel3[0] + pixel4[0]) // 4
            avg_G = (pixel1[1] + pixel2[1] + pixel3[1] + pixel4[1]) // 4
            avg_B = (pixel1[2] + pixel2[2] + pixel3[2] + pixel4[2]) // 4

            # result image
            result_img[y // 2][x // 2] = (avg_R, avg_G, avg_B)

    return result_img
  
def mirror(img):

   height = len(img)
   width = len(img[0])
   # create a new window(image)
   new_img = getWhiteImage(height, width)

   for x in range(width):
       for y in range(height):
           pixel_colour= img[y][x]

           new_img[y][width-1-x]= pixel_colour
   return new_img
  
def drawItem(canvas, img, row, col):
    height = len(img)
    width = len(img[0])

    for y in range(height):
        for x in range(width):
         pixel= img[y][x] 
         # help from peer tutor (ernest wong for the line below)
         if pixel[0] < 250 or pixel[1] < 250 or pixel[2] < 250:
                canvas[row + y][col + x] = pixel
  
def distributeItems(canvas, img, n):
    # img = cmpt120image.getImage(img)
    img_height = len(img)
    img_width = len(img[0])
    canvas_height = len(canvas)
    canvas_width = len(canvas[0])

    for i in range(n):
        # got help from chatgpt for the minus part of the bracket 
        row = random.randint(0, canvas_height-img_height) 
        col = random.randint(0, canvas_width-img_width)


        drawItem(canvas, img, row, col)