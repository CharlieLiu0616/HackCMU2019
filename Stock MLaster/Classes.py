import pygame
import os
import random
import math
import pandas



class Player(object):
    def __init__(self,market):
        self.money = 10000
        self.stocksInHand = [market[0].stock, market[1].stock, market[2].stock]
        self.stockAmount = [0,0,0]

        self.numStocks = 0
        self.maxNumStocks = 10
        
    def buyStocks(self, i, market):
        if market[i].amount <= 0 or self.money < market[i].stock.buyPrice:
            return
        market[i].amount -= 1 #asset
        self.stockAmount[i] += 1
        self.money -= market[i].stock.buyPrice

    def sellStocks(self, i, market):
        if self.stockAmount[i] <= 0:
            return
        market[i].amount += 1 #asset
        self.stockAmount[i] -= 1
        self.money += market[i].stock.sellPrice

class Stock(object):
    def __init__(self, name, buyPrice):
        self.name = name
        self.buyPrice = round(buyPrice,2)
        self.sellPrice = round(buyPrice,2)
    
    def updateStock(self, newPrice):
        self.sellPrice = round(newPrice,2)
        
    def updateMarketStock(self, newPrice):
        self.buyPrice = round(newPrice,2)
        self.sellPrice = round(newPrice,2)
    def __eq__(self,other):
        return type(other) == type(self) and self.name == other.name
            
    
    
class Asset(object):
    def __init__(self, amount, stock):
        self.amount = amount
        self.stock = stock
        
    def __repr__(self):
        return self.stock.name + "         " + str(self.amount) + "         " + str(self.stock.buyPrice) + " " + str(self.stock.sellPrice) +\
            "     "
        
class Calendar(object):
    def __init__(self):
        self.month = 1
        self.day = 1
        self.year = 2000
        
    def nextDay(self):
        self.day += 1
        
class Background(pygame.sprite.Sprite):
    def __init__(self, filePath):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale (pygame.image.load(os.path.join('Assets',
                                        'Backgrounds',filePath)).convert(), (1200, 800))
        self.rect = self.image.get_rect()
        self.image.set_colorkey((0,0,0))
        self.rect.left = 0
        self.rect.top = 0
        
class Layer(pygame.sprite.Sprite):
    def __init__(self, x, y, filePath, scale):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Backgrounds', filePath)).convert(), scale)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        
class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, filePath, scale, action):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Backgrounds',filePath)).convert(), scale)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.action = action
        
    def update(self,mousePos,click):
        if self.rect.left <= mousePos[0] <= self.rect.right and self.rect.top <= mousePos[1] <= self.rect.bottom:
            if click[0]:
                print("Click!")
                self.action()
class SellButton(Button):
    def __init__(self, x, y, filePath, scale, action, player,market, index):
        super().__init__(x, y, filePath,scale, action)
        #self.action = {sell, buy}
        self.index = index
        self.player = player
        self.market = market

    def update(self, mousePos, click):
        if self.rect.left <= mousePos[0] <= self.rect.right and self.rect.top <= mousePos[1] <= self.rect.bottom:
            if click[0]:
                print("Click!")
                if self.action == "sell":
                    self.player.sellStocks(self.index, self.market)
                elif self.action == "buy":
                    self.player.buyStocks(self.index, self.market)
