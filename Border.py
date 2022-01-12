import pygame
import math


class Border:
    def __init__(self, POS, img):
        self.x, self.y = POS
        self.image = img

    def get_mask(self):
        border = self.image.convert_alpha()
        return pygame.mask.from_surface(border)

    def collide(self, driverCar):
        movingCarMask = driverCar.get_mask()
        parkedCarMask = self.get_mask()

        offset = (self.x - driverCar.x, self.y - driverCar.y)

        overlap = movingCarMask.overlap(parkedCarMask, offset)

        if overlap:
            return True

        return False

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))