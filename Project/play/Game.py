import json
import os
import random
from pico2d import *

#Manager
from Manager import collision_manager
from Manager import camera_manager

#Scene
from Scene import pause_state
from Scene import title_state

#Object
from Object import player_object
from Object import guard_object
from Object import map_object
from Object import wall_object

name = "Game"

player = None

map = None
wall = None
font = None

collisionManager = None
cameraManager = None

class Game:
    def __init__(self):
        pass

    def enter(self):
        global player,  wall
        global collisionManager, cameraManager
        global map

        player = player_object.Player()
        wall = wall_object.Wall()
        collisionManager = collision_manager.Collision()
        cameraManager = camera_manager.Camera()

        map = map_object.Map()

        pass

    def exit(self):
        #일단 나중에 꼭 추가하기!
        global player, map
        del(player)
        del(map)
        pass


    def pauses(self):
        pass

    def resume(self):
        pass

    def handle_events(self, event):
            player.handle_events(event)
            collisionManager.handle_events(event)

    def update(self, frame_time):
        player.update(frame_time)
        map.update(frame_time)
        collisionManager.update()
        cameraManager.update()


    def draw_scene(self):
        wall.draw()
        map.draw()
        player.draw()






