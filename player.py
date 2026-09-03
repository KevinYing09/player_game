#Kevin Ying 8/27/26
import pygame

class Player:
    def __init__(self, name, x, y):
        self.name = name
        self.max_health = 100
        self.health = 100
        self.score = 0
        self.level = 1
        self.damage = 10
        self.defense = 10
        self.speed = 10
        self.x = x
        self.y = y
    
    def takeDamage(self, amount):
        self.health -= amount
        if self.health <= 0:
            return True

    def addScore(self, points):
        self.score += points
        if self.score // 100 > self.level - 1:
            self.levelUp()

    def status(self):
        return (self.name, self.health, self.level, self.score)

    def heal(self, amount):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health

#The player levels up for every 100 score points. This increases their max health by 10 for each level
    def levelUp(self):
        old_level = self.level
        self.level += self.score // 100 - old_level
        self.max_health += 10 * (self.level - old_level)
        self.damage += 5 * (self.level - old_level)
        self.defense += 5 * (self.level - old_level)
        return self.level

    def move(self, dx, dy):
        self.x += dx * self.speed
        self.y += dy * self.speed
