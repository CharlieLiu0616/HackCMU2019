import pygame
import os
import random
import math



class Player(object):
    def __init__(self):
        self.money = 0
        self.stocksInHand = []
        self.numStocks = 0
        self.maxNumStocks = 10
        
        
        
    def buyStocks(self, amount, stock):
        if self.money >= amount * stock.buyPrice and numStocks < maxNumStocks:
            self.money -= amount * stock.buyPrice
            self.stocksInHand.append(Asset(amount, stock))
            self.numStocks += 1
        else: #The player does not have enough money or the player does not have room for more stocks. Give some kind of error?
            pass
        
    def sellStocks(self, amount, stock):
        for asset in self.assets:
            if asset.stock == stock and amount < asset.amount:
                self.money += amount * stock.sellPrice
                self.stocksInHand.append(Asset(asset.amount - amount, stock))
                self.stocksInHand.remove(asset)
                self.numStocks -= 1
            elif (asset.stock == stock and amount == asset.amount):
                self.money += amount * stock.sellPrice
                self.stocksInHand.remove(asset)
                self.numStocks -= 1
            else: #The player does not have the stock or does not have enough of a certain stock. Give some kind of error?
                pass

class Stock(object):
    def __init__(self, name, buyPrice):
        self.name = name
        self.buyPrice = buyPrice
        self.sellPrice = buyPrice
        self.difference = 0
    
    def update(self, change):
        if self.sellPrice + change > 0:
            self.sellPrice += change
            self.difference = self.buyPrice - self.sellPrice
    
class Asset(object):
    def __init__(self, amount, stock):
        self.amount = amount
        self.stock = stock
        
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
