from sys import argv
from direct.task import Task
from direct.actor.Actor import Actor
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.showbase.InputStateGlobal import inputState
from direct.controls.GravityWalker import GravityWalker

class CameraViews:
    def changeView(self):
        if self.objectId != 7:
            base.camera.posHprInterval(0.5, self.posList[self.objectId], self.hprList[self.objectId]).start()
            self.objectId += 1
        else:
            self.objectId = 0
            base.camera.posHprInterval(0.5, self.posList[self.objectId], self.hprList[self.objectId]).start()
            self.objectId += 1
 
    def changeViewRev(self):
        if self.objectId != -1:
            base.camera.posHprInterval(0.5, self.posList[self.objectId], self.hprList[self.objectId]).start()
            self.objectId -= 1
        else:
            self.objectId = 6
            base.camera.posHprInterval(0.5, self.posList[self.objectId], self.hprList[self.objectId]).start()
            self.objectId -= 1
 
    def __init__(self):
        self.objectId = 0
 
        self.posList = [(0,-6,3),
                        (0, 1, 3.5),
                        (8, 15, 5.5),
                        (0, 17, 2.5),
                        (0, -30.42, 5),
                        (0, -19, 6.5),
                        (0, -13.5, 3.0),
                        (0, -13.5, 3.0)]
 
        self.hprList = [(0,15,0),
                         (0, 0, 0),
                         (150, -5.5, 0),
                         (180, 5.5, 0),
                         (0, 0, 0),
                         (0, -8.0, 0),
                         (0, 0, 0),
                         (0, 0, 0)]
 
        base.accept('tab', self.changeView, [])
        base.accept('shift-tab', self.changeViewRev, [])
CameraViews()

