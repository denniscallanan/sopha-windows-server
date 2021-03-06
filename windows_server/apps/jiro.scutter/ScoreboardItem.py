import pyglet
import res, batch, group
from Vector import *

class ScoreboardItem(pyglet.sprite.Sprite):

    def __init__(self, name, y):
        pyglet.sprite.Sprite.__init__(self, res.IMG_COLOR_BLACK, batch=batch.main, group=group.overlay1)
        self.y = y
        self.scale_y = 30
        self.name = name
        self.score = 0
        self.nameLabel = pyglet.text.Label(name, font_name='Tahoma', y=self.y+8, font_size=12, batch=batch.main, group=group.overlay2, height=self.scale_y)
        self.scoreLabel = pyglet.text.Label("0", font_name='Tahoma', y=self.y+8, font_size=12, batch=batch.main, group=group.overlay2, height=self.scale_y, anchor_x="right", bold=True)
        self.scale_x = self.nameLabel.content_width + 60

    def reposition(self, x):
        self.x = x
        self.nameLabel.x = x + 10
        self.scoreLabel.x = x + self.scale_x - 10
        return self.scale_x