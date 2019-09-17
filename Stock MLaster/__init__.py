import pygame
import os
import sys
import random
import time
import copy
import numpy
import pandas as pd
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



s1 = pd.read_csv(os.path.join("CSVs", "ACAD.csv"), usecols = [0,1])
s2 = pd.read_csv(os.path.join("CSVs", "BBBY.csv"), usecols = [0,1])
s3 = pd.read_csv(os.path.join("CSVs", "FLEX.csv"), usecols = [0,1])
price1 = s1.values[98].item(1)
price2 = s2.values[98].item(1)
price3 = s3.values[98].item(1)
stock1 = Stock("ACAD", price1)
stock2 = Stock("BBBY", price2)
stock3 = Stock("FLEX", price3)
asset1 = Asset(500, stock1)
asset2 = Asset(500, stock2)
asset3 = Asset(500, stock3)
market = [asset1, asset2, asset3]

player = Player(market)

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
    lGroup.add(Layer(600, 375, "AppleDefault.jpeg", (910, 650))) #This is the screen of the macbook
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
    todaysDate = hpFont.render(str(Today.month) + "/" + str(Today.day) + "/" + str(Today.year), False, (255,255,255))
    
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
        window.blit(hpFont.render("Money: $" + str(player.money), False, (255, 255, 255)), (900, 100))
        window.blit(hpFont.render("Stock Name | Amount | Buy Price | Sell Price ", False, (255,255,255)), (300, 140))
        
        for i in range(len(player.stocksInHand)):
            window.blit(hpFont.render(market[i].__repr__(), False, (0, 0, 0)), (300, 200 + 50 * i))
        pygame.display.update()
    return
    
def buyScreen():
    todaysDate = hpFont.render(str(Today.month) + "/" + str(Today.day) + "/" + str(Today.year), False, (255,255,255))
    
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
        for i in range(len(market)):
            window.blit(hpFont.render(market[i].__repr__(), False, (255, 255, 255)), (300, 200 + 50 * i))
            buttonGroup.add(SellButton(800, 200 + 50 * i, "Sell.png", (20, 20), "buy", player, market, i))
        window.blit(hpFont.render("Money: $" + str(player.money), False, (255, 255, 255)), (900, 100))
        window.blit(hpFont.render("Stock Name | Amount | Buy Price | Sell Price", False, (255,255,255)), (300, 140))
        pygame.display.update()
    return
    
def sellScreen():
    todaysDate = hpFont.render(str(Today.month) + "/" + str(Today.day) + "/" + str(Today.year), False, (255,255,255))
    
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
        window.fill((0,0,0))
        for button in buttonGroup:
            button.update(mouse,click)
        
        
        bgGroup.draw(window)
        lGroup.draw(window)
        buttonGroup.draw(window)
        window.blit(todaysDate, (970, 40))
        window.blit(hpFont.render("Money: $" + str(player.money), False, (255, 255, 255)), (900, 100))
        window.blit(hpFont.render("Stock Name | Amount | Buy Price | Sell Price", False, (255,255,255)), (300, 140))
        for i in range(len(player.stocksInHand)):
            
            asset = market[i]
            assName = asset.stock.name
            assAmount = str(player.stockAmount[i])
            assPrice = str(asset.stock.buyPrice)
            thing = assName+"           "+assAmount+"         "+assPrice
            print(thing)
            window.blit(hpFont.render(thing, False, (255, 255, 255)), (300, 200 + 50 * i))
            buttonGroup.add(SellButton(800, 200 + 50 * i, "Sell.png", (20, 20), "sell", player, market, i))
        pygame.display.update()
    return

def dowScreen():
    todaysDate = hpFont.render(str(Today.month) + "/" + str(Today.day) + "/" + str(Today.year), False, (255,255,255))
    
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
        window.blit(hpFont.render("Coming Soon!", False, (255, 255, 255)), (600, 400))
        pygame.display.update()
    return
    
def apple():
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
        window.blit(hpFont.render("Money: $" + str(player.money), False, (255, 255, 255)), (900, 100))
        pygame.display.update()
    return
    
def newDay():
    
    if Today.day == 31:
        endGameScreen()
    else:
        Today.nextDay()
        newPrice = [] #stock prices
        
        for i in range(len(market)):
            df = pd.read_csv(os.path.join("CSVs", market[i].stock.name + ".csv"), usecols = [0,1])
            newPrice.append(df.values[Today.day+98].item(1))
            market[i].stock.updateMarketStock(newPrice[i])
        mainGameScreen()
    return
    
def endGameScreen():
    todaysDate = hpFont.render(str(Today.month) + "/" + str(Today.day) + "/" + str(Today.year), False, (255,255,255))
    
    bgGroup = pygame.sprite.Group()
    bgGroup.add(Background("Wooden Table Background.jpg"))
    bgGroup.add(Background("Blank Macbook.png"))
    
    lGroup = pygame.sprite.Group()
    lGroup.add(Layer(600, 375, "Blue.png", (910, 650))) #This is the screen of the macbook
    lGroup.add(Layer(1010, 670, "Cat2.png", (90, 66)))
    lGroup.add(Layer(600, 50, "GreyBar.png", (910, 25)))
    
    buttonGroup = pygame.sprite.Group()
    buttonGroup.add(Button(895, 670, "Quit.png", (140, 66), sys.exit))
    
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
        winText = "This is the end of the game. Your end money: " + str(player.money)
        winText2 = "You've earned $" + str(player.money - 10000) + " this month!"
    
        window.blit(hpFont.render(winText, False, (255, 255, 255)), (300, 400))
        window.blit(hpFont.render(winText2, False, (255, 255, 255)), (300, 550))

        pygame.display.update()
    return

titleScreen()