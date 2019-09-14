import pygame
import os
import sys
import random
import time
import copy
from Classes import *

windowWidth = 1200
windowHeight = 800
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Stock Market Game")
clock = pygame.time.Clock()
gameSpeed = 30

pygame.font.init()
hpFont = pygame.font.SysFont('Comic Sans MS', 15)

Today = Calendar()

def titleScreen(): #Screen finished!
    bgGroup = pygame.sprite.Group()
    bgGroup.add(Background("Wooden Table Background.jpg"))
    bgGroup.add(Background("Blank Macbook.png"))
    
    lGroup = pygame.sprite.Group()
    lGroup.add(Layer(600, 375, "Money Background.jpg", (910, 650))) #This is the screen of the macbook
    lGroup.add(Layer(600, 300, "StockMarketGame.png", (900, 157)))
    
    buttonGroup = pygame.sprite.Group()
    buttonGroup.add(Button(600, 500, "Start.png", (200, 100), mainGameScreen))
        
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for button in buttonGroup:
            button.update(mouse,click)
        window.fill((0,0,0))
        bgGroup.draw(window)
        lGroup.draw(window)
        buttonGroup.draw(window)
        pygame.display.update()
    return
    
def mainGameScreen():
    todaysDate = hpFont.render(str(Today.month) + "/" + str(Today.day) + "/" + str(Today.year), False, (255,255,255))
    
    bgGroup = pygame.sprite.Group()
    bgGroup.add(Background("Wooden Table Background.jpg"))
    bgGroup.add(Background("Blank Macbook.png"))
    
    lGroup = pygame.sprite.Group()
    lGroup.add(Layer(600, 375, "AppleDefaultHD.jpg", (910, 650))) #This is the screen of the macbook
    lGroup.add(Layer(1010, 670, "Cat2.png", (90, 66)))
    lGroup.add(Layer(600, 50, "GreyBar.png", (910, 25)))
    
    buttonGroup = pygame.sprite.Group()
    buttonGroup.add(Button(215, 670, "ViewStocks.png", (140, 66), viewScreen))
    buttonGroup.add(Button(385, 670, "BuyStocks.png", (200, 66), buyScreen))
    buttonGroup.add(Button(585, 670, "SellStocks.png", (200, 66), sellScreen))
    buttonGroup.add(Button(755, 670, "Dow.png", (140, 66), dowScreen))
    buttonGroup.add(Button(895, 670, "Quit.png", (140, 66), sys.exit))
    buttonGroup.add(Button(158, 50, "Apple.jpg", (25, 25), apple))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for button in buttonGroup:
            button.update(mouse,click)
        window.fill((0,0,0))
        bgGroup.draw(window)
        lGroup.draw(window)
        buttonGroup.draw(window)
        window.blit(todaysDate, (970, 40))
        pygame.display.update()
    return

def viewScreen():
    bgGroup = pygame.sprite.Group()
    bgGroup.add(Background("Wooden Table Background.jpg"))
    bgGroup.add(Background("Blank Macbook.png"))
    
    lGroup = pygame.sprite.Group()
    lGroup.add(Layer(600, 375, "Blue.png", (910, 650)))
    lGroup.add(Layer(1010, 670, "Cat2.png", (90, 66)))
    lGroup.add(Layer(600, 50, "GreyBar.png", (910, 25)))
    
    buttonGroup = pygame.sprite.Group()
    buttonGroup.add(Button(215, 670, "ViewStocks.png", (140, 66), viewScreen))
    buttonGroup.add(Button(385, 670, "BuyStocks.png", (200, 66), buyScreen))
    buttonGroup.add(Button(585, 670, "SellStocks.png", (200, 66), sellScreen))
    buttonGroup.add(Button(755, 670, "Dow.png", (140, 66), dowScreen))
    buttonGroup.add(Button(895, 670, "Quit.png", (140, 66), sys.exit))
    buttonGroup.add(Button(158, 50, "Apple.jpg", (25, 25), apple))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for button in buttonGroup:
            button.update(mouse,click)
        window.fill((0,0,0))
        bgGroup.draw(window)
        lGroup.draw(window)
        buttonGroup.draw(window)
        window.blit(todaysDate, (970, 40))
        pygame.display.update()
    return
    
def buyScreen():
    lGroup = pygame.sprite.Group()
    lGroup.add(Layer(600, 375, "Blue.png", (910, 650)))
    lGroup.add(Layer(1010, 670, "Cat2.png", (90, 66)))
    lGroup.add(Layer(600, 50, "GreyBar.png", (910, 25)))
    
    buttonGroup = pygame.sprite.Group()
    buttonGroup.add(Button(215, 670, "ViewStocks.png", (140, 66), viewScreen))
    buttonGroup.add(Button(385, 670, "BuyStocks.png", (200, 66), buyScreen))
    buttonGroup.add(Button(585, 670, "SellStocks.png", (200, 66), sellScreen))
    buttonGroup.add(Button(755, 670, "Dow.png", (140, 66), dowScreen))
    buttonGroup.add(Button(895, 670, "Quit.png", (140, 66), sys.exit))
    buttonGroup.add(Button(158, 50, "Apple.jpg", (25, 25), apple))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for button in buttonGroup:
            button.update(mouse,click)
        window.fill((0,0,0))
        bgGroup.draw(window)
        lGroup.draw(window)
        buttonGroup.draw(window)
        window.blit(todaysDate, (970, 40))
        pygame.display.update()
    return
    
def sellScreen():
    lGroup = pygame.sprite.Group()
    lGroup.add(Layer(600, 375, "Blue.png", (910, 650)))
    lGroup.add(Layer(1010, 670, "Cat2.png", (90, 66)))
    lGroup.add(Layer(600, 50, "GreyBar.png", (910, 25)))
    
    buttonGroup = pygame.sprite.Group()
    buttonGroup.add(Button(215, 670, "ViewStocks.png", (140, 66), viewScreen))
    buttonGroup.add(Button(385, 670, "BuyStocks.png", (200, 66), buyScreen))
    buttonGroup.add(Button(585, 670, "SellStocks.png", (200, 66), sellScreen))
    buttonGroup.add(Button(755, 670, "Dow.png", (140, 66), dowScreen))
    buttonGroup.add(Button(895, 670, "Quit.png", (140, 66), sys.exit))
    buttonGroup.add(Button(158, 50, "Apple.jpg", (25, 25), apple))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for button in buttonGroup:
            button.update(mouse,click)
        window.fill((0,0,0))
        bgGroup.draw(window)
        lGroup.draw(window)
        buttonGroup.draw(window)
        window.blit(todaysDate, (970, 40))
        pygame.display.update()
    return

def dowScreen():
    lGroup = pygame.sprite.Group()
    lGroup.add(Layer(600, 375, "Blue.png", (910, 650)))
    lGroup.add(Layer(1010, 670, "Cat2.png", (90, 66)))
    lGroup.add(Layer(600, 50, "GreyBar.png", (910, 25)))
    
    buttonGroup = pygame.sprite.Group()
    buttonGroup.add(Button(215, 670, "ViewStocks.png", (140, 66), viewScreen))
    buttonGroup.add(Button(385, 670, "BuyStocks.png", (200, 66), buyScreen))
    buttonGroup.add(Button(585, 670, "SellStocks.png", (200, 66), sellScreen))
    buttonGroup.add(Button(755, 670, "Dow.png", (140, 66), dowScreen))
    buttonGroup.add(Button(895, 670, "Quit.png", (140, 66), sys.exit))
    buttonGroup.add(Button(158, 50, "Apple.jpg", (25, 25), apple))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for button in buttonGroup:
            button.update(mouse,click)
        window.fill((0,0,0))
        bgGroup.draw(window)
        lGroup.draw(window)
        buttonGroup.draw(window)
        window.blit(todaysDate, (970, 40))
        pygame.display.update()
    return
    
def apple(screenNum):
    todaysDate = hpFont.render(str(Today.month) + "/" + str(Today.day) + "/" + str(Today.year), False, (255,255,255))
    
    bgGroup = pygame.sprite.Group()
    bgGroup.add(Background("Wooden Table Background.jpg"))
    bgGroup.add(Background("Blank Macbook.png"))
    
    lGroup = pygame.sprite.Group()
    lGroup.add(Layer(600, 375, "Blue.png", (910, 650))) #This is the screen of the macbook
    lGroup.add(Layer(1010, 670, "Cat2.png", (90, 66)))
    lGroup.add(Layer(600, 50, "GreyBar.png", (910, 25)))
    
    buttonGroup = pygame.sprite.Group()
    buttonGroup.add(Button(215, 670, "ViewStocks.png", (140, 66), viewScreen))
    buttonGroup.add(Button(385, 670, "BuyStocks.png", (200, 66), buyScreen))
    buttonGroup.add(Button(585, 670, "SellStocks.png", (200, 66), sellScreen))
    buttonGroup.add(Button(755, 670, "Dow.png", (140, 66), dowScreen))
    buttonGroup.add(Button(895, 670, "Quit.png", (140, 66), sys.exit))
    buttonGroup.add(Button(158, 50, "Apple.jpg", (25, 25), mainGameScreen))
    buttonGroup.add(Button(245, 81, "ShutDownApple.png", (200, 35), newDay))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for button in buttonGroup:
            button.update(mouse,click)
        window.fill((0,0,0))
        bgGroup.draw(window)
        lGroup.draw(window)
        buttonGroup.draw(window)
        window.blit(todaysDate, (970, 40))
        pygame.display.update()
    return
    
def newDay():
    if Today.day == 31:
        endGameScreen()
    else:
        Today.nextDay()
        mainGameScreen()
    return
    
def endGameScreen():
    #show end game
    return

titleScreen()