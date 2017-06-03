'''
Created on 2017年6月3日

@author: Alex
'''

from sys import exit
from random import randint


class Scene(object):
    
    def enter(self):
        print("这里的场景尚未配置好. 添加enter().")
        exit(1)
        

class Engine(object):
    
    def __init__(self, scene_map):
        self.scene_map = scene_map
        
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('完成')
        
    
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
            
            
        # be sure to print out the last scene
        current_scene.enter()
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
