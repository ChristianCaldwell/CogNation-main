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

waiter1 = loader.loadTexture('phase_3.5/maps/waiter_m_blazer.jpg')
waiter2 = loader.loadTexture('phase_3.5/maps/waiter_m_leg.jpg')
waiter3 = loader.loadTexture('phase_3.5/maps/waiter_m_sleeve.jpg')

bossbot1 = loader.loadTexture('phase_3.5/maps/c_blazer.jpg')
bossbot2 = loader.loadTexture('phase_3.5/maps/c_leg.jpg')
bossbot3 = loader.loadTexture('phase_3.5/maps/c_sleeve.jpg')

lawbot1 = loader.loadTexture('phase_3.5/maps/l_blazer.jpg')
lawbot2 = loader.loadTexture('phase_3.5/maps/l_leg.jpg')
lawbot3 = loader.loadTexture('phase_3.5/maps/l_sleeve.jpg')

cashbot1 = loader.loadTexture('phase_3.5/maps/m_blazer.jpg')
cashbot2 = loader.loadTexture('phase_3.5/maps/m_leg.jpg')
cashbot3 = loader.loadTexture('phase_3.5/maps/m_sleeve.jpg')

sellbot1 = loader.loadTexture('phase_3.5/maps/s_blazer.jpg')
sellbot2 = loader.loadTexture('phase_3.5/maps/s_leg.jpg')
sellbot3 = loader.loadTexture('phase_3.5/maps/s_sleeve.jpg')

nameDropper = loader.loadTexture('phase_4/maps/name-dropper.jpg')

Sellbot = (0.95, 0.75, 0.95, 1.0)
Cashbot = (0.65, 0.95, 0.85, 1.0)
Lawbot  = (0.75, 0.75, 0.95, 1.0)
Bossbot = (0.95, 0.75, 0.75, 1.0)
