import pygame
import image
from settings import *
#from PIL import image 


class Choose:
    def __init__(self1):    

        self1.image = image.load("Assets/choose.jpg", size=(SCREEN_WIDTH, SCREEN_HEIGHT),
                                convert="default")

    def draw(self1, surface):
        image.draw(surface, self1.image, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2), pos_mode="center")   



    

       
   
    
        
    
class Loading:
    def __init__(self1):    

        self1.image = image.load("Assets/loading.jpg", size=(SCREEN_WIDTH, SCREEN_HEIGHT),
                                convert="default")

    def draw(self1, surface):
        image.draw(surface, self1.image, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2), pos_mode="center")   




