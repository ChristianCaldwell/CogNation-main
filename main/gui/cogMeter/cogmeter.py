from sys import argv
from panda3d.core import Vec3
from pandac.PandaModules import loadPrcFileData
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

ButtonImage = loader.loadModel("phase_3/models/gui/cog_icons.bam")
gui = loader.loadModel('phase_3/models/gui/laff_o_meter.bam')
eyeImage = gui.find('**/eyes')

meter = DirectFrame(relief=None, pos=(-1.2, 0, -0.87), scale=.2, image=ButtonImage.find('**/SalesIcon'))
eyes = DirectFrame(parent=meter, relief=None, scale=.5, image=eyeImage)
maxLabel = DirectLabel(parent=eyes, relief=None, pos=(0.442, 0, 0.051), scale=1, text='6', text_font=loader.loadFont('phase_3/models/fonts/vtRemingtonPortable.ttf'), text_scale=0.4)
hpLabel = DirectLabel(parent=eyes, relief=None, pos=(-0.398, 0, 0.051), scale=1, text='6', text_font=loader.loadFont('phase_3/models/fonts/vtRemingtonPortable.ttf'), text_scale=0.4)
