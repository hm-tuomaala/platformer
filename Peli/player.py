from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsRectItem
from PyQt5.QtGui import QBrush
from PyQt5.QtCore import Qt

SCREEN_WIDTH            = 800
SCREEN_HEIGHT           = 600
PLAYER_SPEED            = 3   # pix/frame
FRAME_TIME_MS           = 16  # ms/frame
GRAVITY                 = 0.6


class Player(QGraphicsRectItem):
    def __init__(self, parent = None):
        QGraphicsRectItem.__init__(self,parent)
        self.x = 0
        self.y = SCREEN_HEIGHT
        self.setRect(self.x, self.y, 30, 30)
        self.setBrush(QBrush(Qt.white))
        self.velocity = 0
        self.lift = -30
        self.can_jump = True
        self.on_platform = False

    def set_player(self, x, y):
        self.setRect(self.x, self.y, 30, 30)

    def player_update(self, keys_pressed, enemy, timer, platforms):

        print(self.can_jump)
        #Basic Gravity
        self.velocity += GRAVITY
        self.velocity *= 0.95
        self.y += self.velocity

        for pf in platforms:
            #print(pf.x, pf.y)
            if self.x + 30 > pf.x and self.x < pf.x + pf.width and self.y + 30 > pf.y and self.y < pf.y + 10:
                self.y = pf.y - 30
                self.set_player(self.x, self.y)
                print('hep')
                self.can_jump = True
                self.on_platform = True

            elif self.y + 30 < SCREEN_HEIGHT and not self.on_platform:
                self.set_player(self.x, self.y)
                self.can_jump = False
                print('jaaaaaaaaaaaaaaaaaapaaaaaaaaaaaaaaaaaaaaaa')

            else:
                self.y = SCREEN_HEIGHT - 30
                self.set_player(self.x, self.y)
                self.can_jump = True
                self.on_platform = False

        #Check if Player needs to move
        if Qt.Key_Left in keys_pressed:
            self.x -= PLAYER_SPEED
        if Qt.Key_Right in keys_pressed:
            self.x += PLAYER_SPEED
        if Qt.Key_Space in keys_pressed and self.can_jump:
            keys_pressed.remove(Qt.Key_Space)
            self.velocity += self.lift
            self.can_jump = False
        elif Qt.Key_Space in keys_pressed and not self.can_jump:
            keys_pressed.remove(Qt.Key_Space)
            self.can_jump = False


        if self.x + 30 > enemy.x and self.x < enemy.x + 30 and self.y + 30 > SCREEN_HEIGHT - 30:
            #Kuoltiin
            print('DEAD')
            timer.stop()
