from sys import argv
from panda3d.core import Vec3
from pandac.PandaModules import loadPrcFileData
loadPrcFileData('configurate', 'window-title Loading')
from direct.directbase import DirectStart
from direct.task import Task
from direct.actor.Actor import Actor
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.showbase.InputStateGlobal import inputState
from direct.controls.GravityWalker import GravityWalker
from direct.showbase import DirectObject
from direct.interval.IntervalGlobal import *
import urllib, os, __main__, random
from pandac.PandaModules import *
from random import choice
base.disableMouse()
from direct.directbase.DirectStart import *
from direct.actor.Actor import Actor
from pandac.PandaModules import *
from direct.task import Task
import math
from math import pi, sin, cos
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.interval.IntervalGlobal import *
from pandac.PandaModules import Point3
from pandac.PandaModules import *
from panda3d.core import CollisionTraverser,CollisionNode
from panda3d.core import CollisionHandlerQueue,CollisionRay
from panda3d.core import Filename,AmbientLight,DirectionalLight
from panda3d.core import PandaNode,NodePath,Camera,TextNode
from panda3d.core import Vec3,Vec4,BitMask32
from direct.showbase.Transitions import *
from direct.gui.DirectGui import *
from direct.actor.Actor import Actor
from direct.showbase.DirectObject import DirectObject
from direct.filter.CommonFilters import *
from panda3d.ai import *
import sys
from random import randint
import webbrowser
from cognation.main.gui.chat.CNChat import *
from cognation.main.gui.cogMeter.cogmeter import *
from cognation.main.gui.cogBook.cogBook import *

background = OnscreenImage(image = 'data/background.jpg', pos = (0, 0, 0), parent=render2d)
background.hide()
loadingtext = OnscreenText(text='Now Loading...', scale=0.08, pos=(-1.065, -0.775, -0.775), align=TextNode.ALeft, font=loader.loadFont("data/vtRemingtonPortable.ttf"))
loadingtext.hide()
progressbar = DirectWaitBar(value=0, range=100, pos=(0, 0, -0.85))
progressbar.hide()
progressbar.setSx(1.065)
progressbar.setSz(0.38)

def ShowLoading():
  background.show()
  loadingtext.show()
  progressbar.show()
  base.graphicsEngine.renderFrame()
  base.graphicsEngine.renderFrame()
  base.localAvatar.ClassicChatBox.OldChatBoxOpen.hide()
  meter.hide()
  bookButton.hide()
  
def addTime():
  progressbar['value'] += 20
  
def AreaLoaded():
  background.hide()
  loadingtext.hide()
  progressbar.hide()
  base.localAvatar.ClassicChatBox.OldChatBoxOpen.show()
  meter.show()
  bookButton.show()

 
def resetTime():
  progressbar['value'] -= 100
  
def RunScreen():
  loadseq = Sequence()
  loadseq.append(Func(ShowLoading))
  loadseq.append(Wait(1))
  loadseq.append(Func(addTime))
  loadseq.append(Wait(.1))
  loadseq.append(Func(addTime))
  loadseq.append(Wait(.1))
  loadseq.append(Func(addTime))
  loadseq.append(Wait(.1))
  loadseq.append(Func(addTime))
  loadseq.append(Wait(.1))
  loadseq.append(Func(addTime))
  loadseq.append(Wait(.1))
  loadseq.append(Func(AreaLoaded))
  loadseq.append(Func(resetTime))
  loadseq.start()

