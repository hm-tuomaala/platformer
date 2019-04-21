import unittest
import json
import sys

from map import Map
from player import Player
from scene import Scene
from PyQt5.QtWidgets import QApplication

class Test(unittest.TestCase):


    def test_highscore_file(self):
        with open('static/highscore.json') as f:
            data = json.load(f)
        highscore = data["highscore"]
        self.assertIsInstance(highscore, float)

    def test_map_tiles(self):
        list = [0,1,2,3,4,5,6,7]
        map = Map()
        for i in range(int(600 / 40)):
            for j in range(int((800*4) / 40)):
                self.assertIn(map.map[i][j], list)

    def test_animations(self):
        app = QApplication(sys.argv)
        player = Player()
        self.assertIs(len(player.animations_left), 4)
        self.assertIs(len(player.animations_right), 4)



if __name__ == '__main__':
    unittest.main()
