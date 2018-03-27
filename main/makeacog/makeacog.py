from sys import argv
from panda3d.core import Vec3
from pandac.PandaModules import loadPrcFileData
loadPrcFileData('configurate', 'window-title CogNation [DEV BUILD 4.0 Alpha]')
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
from cognation.main.cogbase.CogTypes import *
from cognation.main.cogbase.CogNationTex import *
from cognation.main.cogbase.Walker import *
from cognation.main.load.CNTerrain import *
from cognation.main.gui.chat.CNChat import *
from cognation.main.cogbase.CogTypes import *
from cognation.main.gui.cogMeter.cogmeter import *
from cognation.main.gui.cogBook.cogBook import *

makeatoonmusic = base.loadSfx('music/CHQ_FACT_bg.mp3')
makeatoonmusic.setLoop(True)
makeatoonmusic.play()

base.localAvatar.ClassicChatBox.OldChatBoxOpen.hide()
meter.hide()
bookButton.hide()

Type = 'None'
btmftex = loader.loadTexture('phase_3.5/maps/bottom-feeder.jpg')
Cheads = loader.loadModel('phase_3.5/models/char/suitC-heads.bam')
flunky = Cheads.find('**/flunky')
bottomfeeder = Cheads.find('**/flunky')
shortchange = Cheads.find('**/coldcaller')
coldcaller = Cheads.find('**/coldcaller')
Sellbot = loader.loadModel("phase_4/models/minigames/salesIcon.bam")
Cashbot = loader.loadModel("phase_4/models/minigames/moneyIcon.bam")
Lawbot = loader.loadModel("phase_4/models/minigames/legalIcon.bam")
Bossbot = loader.loadModel("phase_4/models/minigames/corpIcon.bam")
suitC.setPos(0.18,-281.24,0.50)

	
def sellbotFunc():
	global Type
	global namePanel
	suitC.show()
	suitC.findAllMatches('**/torso').setTexture(sellbot1, 1)
	suitC.findAllMatches('**/legs').setTexture(sellbot2, 1)
	suitC.findAllMatches('**/arms').setTexture(sellbot3, 1)
	coldcaller.reparentTo(suitC.find('**/joint_head'))
	coldcaller.setColor(0.0941176470588235,0.2313725490196078, 1)
	suitC.find('**/hands').setColor(0.5490196078431373,0.6431372549019608,0.9882352941176471)
	Sellbot.reparentTo(suitC.find('**/joint_attachMeter'))
	Sellbot.setScale(.6)
	Sellbot.setPosHpr(0,.03,.17,180,0,0)
	Type = 'Sellbot'
sellbotFunc()

def setText(text):
	global Type
	makeatoonmusic.stop()
	sellbotHQ.play()
	textEntryz.hide()
	namePanel.hide()
	RunScreen()
	base.taskMgr.add(handleMovement, 'controlManager')
	walkControls.enableAvatarControls()
	base.camera.setPosHpr(0,-30.42,5,0,0,0)
	camera.reparentTo(suitC)
	if Type == 'Sellbot':
		base.localAvatar.CogTags.setName(text+'\nSellbot\nLevel 1')



nameShopGui = loader.loadModel('phase_3/models/gui/tt_m_gui_mat_nameShop.bam')
panelImage = nameShopGui.find('**/tt_t_gui_mat_typeNamePanel')
namePanel = DirectFrame(image = panelImage, relief=None, scale = (0.75, 0.7, 0.7), pos = (0.55, 0, 0.019), 
text = 'Please type your name\nand press ENTER.', text_fg = (1, 1, 0, 1), text_scale = 0.09, 
text_pos = (0, 0.68), text_shadow = Vec4(0, 0, 0, 1))
textEntryz = DirectEntry(text = "", scale = 0.07, pos = (0.55, 0, 0.32), width = 7.5, numLines = 2, relief=None, 
text_align=TextNode.ACenter, autoCapitalize=1, focus = 1, command = setText)


camera.setPosHpr(-1.72,-267.64,3.57,180,0,0)
