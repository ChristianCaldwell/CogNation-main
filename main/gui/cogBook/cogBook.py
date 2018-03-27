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
from cognation.main.cogbase.CogTypes import *
from cognation.main.cogbase.Walker import *
from cognation.main.cogbase.Walker import *

book_open = loader.loadSfx('phase_3.5/audio/sfx/GUI_stickerbook_open.mp3')
book_close = loader.loadSfx('phase_3.5/audio/sfx/GUI_stickerbook_delete.mp3')
doorOpen = loader.loadSfx('phase_3.5/audio/sfx/Door_Open_1.mp3')
guiButton = loader.loadModel('phase_3/models/gui/quit_button.bam')
PageTurn = loader.loadSfx('phase_3.5/audio/sfx/GUI_stickerbook_turn.mp3')
OptionsPage = 'Options'
DistrictPage = 'Districts'
MapPage = 'Map'
GagPage = 'Cog Attacks'
ToonTasksPage = 'CogTasks'
currentPage = 'OptionsPage'

def openBook():
	global currentPage
	base.render.hide()
	base.setBackgroundColor(0.05, 0.15, 0.4)
	bookButton.hide()
	bigBook.show()
	openIcon.show()
	book_open.play()

def exitBook():
	global currentPage
	openIcon.hide()
	bigBook.hide()
	base.render.show()
	base.setBackgroundColor(Vec4(0.4, 0.4, 0.4, 1))
	bookButton.show()
	book_close.play()

	
book = loader.loadModel('phase_3.5/models/gui/stickerbook_gui.bam')
bookOpen = book.find('**/big_book')
bookClosed = book.find('**/BookIcon_CLSD')
bookPressed = book.find('**/BookIcon_OPEN')
bookRollover = book.find('**/BookIcon_RLVR')
bookRollover2 = book.find('**/BookIcon_RLVR2')
arrowOpen = book.find('**/arrow_button')
arrowPressed = book.find('**/arrow_down')
arrowRollover = book.find('**/arrow_rollover')
MainFont = loader.loadFont('phase_3/models/fonts/ImpressBT.ttf')
bookButton = DirectButton(image=(bookClosed, bookPressed, bookRollover), 
relief=None, pos = (1.175, 0, -0.83), scale = 0.305, command=openBook)

def RightArrow():
	global currentPage
	if currentPage == 'OptionsPage':
		Music_Label.hide()
		Music_toggleButton.hide()
		exitButton.hide()
		totalPopulationText.show()
		title['text'] = DistrictPage
		arrowLeft.show()
		currentPage = 'DistrictPage'
	elif currentPage == 'DistrictPage':
		totalPopulationText.hide()
		title['text'] = MapPage
		map.show()
		currentPage = 'MapPage'
	elif currentPage == 'MapPage':
		map.hide()
		title['text'] = GagPage
		currentPage = 'GagPage'
		row1.show()
		row2.show()
		row3.show()
		row4.show()
		row5.show()
		row6.show()
		row7.show()
		jar.show()
		JBAmount.show()
		Box1.show()
		Box2.show()
	elif currentPage == 'GagPage':
		title['text'] = ToonTasksPage
		currentPage = 'ToonTasksPage'
		row1.hide()
		row2.hide()
		row3.hide()
		row4.hide()
		row5.hide()
		row6.hide()
		row7.hide()
		jar.hide()
		JBAmount.hide()
		Box1.hide()
		Box2.hide()
		arrowRight.hide()
		
def LeftArrow():
	global currentPage
	if currentPage == 'DistrictPage':
		Music_Label.show()
		Music_toggleButton.show()
		exitButton.show()
		totalPopulationText.hide()
		title['text'] = OptionsPage
		arrowLeft.hide()
		currentPage = 'OptionsPage'
	elif currentPage == 'MapPage':
		map.hide()
		totalPopulationText.show()
		title['text'] = DistrictPage
		currentPage = 'DistrictPage'
	elif currentPage == 'GagPage':
		map.show()
		title['text'] = MapPage
		currentPage = 'MapPage'
		row1.hide()
		row2.hide()
		row3.hide()
		row4.hide()
		row5.hide()
		row6.hide()
		row7.hide()
		jar.hide()
		JBAmount.hide()
		Box1.hide()
		Box2.hide()
	elif currentPage == 'ToonTasksPage':
		title['text'] = GagPage
		row1.show()
		row2.show()
		row3.show()
		row4.show()
		row5.show()
		row6.show()
		row7.show()
		jar.show()
		JBAmount.show()
		Box1.show()
		Box2.show()
		currentPage = 'GagPage'
		arrowRight.show()

bigBook = DirectFrame(relief=None, image=bookOpen, image_scale=(2, 1, 1.5), pos=(0, 0, 0.1))
bigBook.hide()
openIcon = DirectButton(image=(bookPressed, bookRollover2), relief=None, pos = (1.175, 0, -0.83), scale = 0.305, command=exitBook)
openIcon.hide()
title = DirectLabel(parent=bigBook, relief=None, pos=(0, 0, .6), scale=0.3, text=OptionsPage, text_font=MainFont, text_scale=0.4)
pageTabFrame = DirectFrame(parent=bigBook, relief=None, pos=(0.93, 1, 0.575), scale=1.25)
#Arrows
arrowRight = DirectButton(parent=bigBook, image=(arrowOpen, arrowPressed, arrowRollover), relief=None, pos = (0.838, 0, -0.661), scale =0.1, clickSound =PageTurn, command=RightArrow)
arrowLeft = DirectButton(parent=bigBook, image=(arrowOpen, arrowPressed, arrowRollover), relief=None, pos = (-0.838, 0, -0.661), hpr = (180,0,0), scale =0.1, clickSound=PageTurn, command=LeftArrow)
arrowLeft.hide()
#Options Page
def ExitGame():
	sys.exit()
MusicOn = 'Music Is On.'
MusicOff = 'Music Is Off.'
TurnMusicOn = 'Turn On'
TurnMusicOff = 'Turn Off'
def MusicOnandOff():
	if Music_toggleButton['text'] == TurnMusicOff:
		Music_toggleButton['text'] = TurnMusicOn
		base.disableAllAudio()
		Music_Label['text'] = MusicOff
	elif Music_toggleButton['text'] == TurnMusicOn:
		Music_toggleButton['text'] = TurnMusicOff
		base.enableAllAudio()
		Music_Label['text'] = MusicOn
Music_Label = DirectLabel(parent=bigBook, relief=None, text=MusicOn, text_font=MainFont, text_align=TextNode.ALeft, text_scale=0.052, pos=(-0.72, 0, 0.45))
Music_toggleButton = DirectButton(parent=bigBook, relief=None, image=(guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale=(0.7, 1, 1), text=TurnMusicOff, text_font=MainFont, text_scale=0.052, text_pos=(0, -0.02), pos=(0.35, 0.0, 0.45), command=MusicOnandOff)
exitButton = DirectButton(parent=bigBook, relief=None, image=(guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale=1.15, text='Exit CogNation', text_font=MainFont, text_scale=0.052, text_pos=(0, -0.02), textMayChange=0, pos=(0.45, 0, -0.6), command=ExitGame)
#DistricsPage
totalPopulationText = DirectLabel(parent=bigBook, relief=None, text='Total CogNation\nPopulation:\n1', text_font=MainFont, text_scale=0.06, text_wordwrap=8, textMayChange=1, text_align=TextNode.ACenter, pos=(0.38, 0, -0.35))
totalPopulationText.hide()
#MapPage
mapModel = loader.loadModel('phase_3.5/models/gui/toontown_map.bam')
map = DirectFrame(parent=bigBook, relief=None, image=mapModel.find('**/toontown_map'), image_scale=(1.8, 1, 1.35), scale=0.97, pos=(0, 0, 0.0775))
map.hide()
Inventory = loader.loadModel('phase_3.5/models/gui/inventory_gui.bam')
toonupRow = Inventory.find('**/InventoryRow')
toonupRow.setColor(211 / 255.0, 148 / 255.0, 255 / 255.0)
row1 = DirectFrame(parent=bigBook, relief=None, image=toonupRow, pos=(0, 0, 0.50), scale=(0.9, 1, 1))
trapRow = Inventory.find('**/InventoryRow')
trapRow.setColor(249 / 255.0, 255 / 255.0, 93 / 255.0)
row2 = DirectFrame(parent=bigBook, relief=None, image=trapRow, pos=(0, 0, 0.389), scale=(0.9, 1, 1))
lureRow = Inventory.find('**/InventoryRow')
lureRow.setColor(79 / 255.0, 190 / 255.0, 76 / 255.0)
row3 = DirectFrame(parent=bigBook, relief=None, image=lureRow, pos=(0, 0, 0.278), scale=(0.9, 1, 1))
soundRow = Inventory.find('**/InventoryRow')
soundRow.setColor(93 / 255.0, 108 / 255.0, 239 / 255.0)
row4 = DirectFrame(parent=bigBook, relief=None, image=soundRow, pos=(0, 0, 0.167), scale=(0.9, 1, 1))
throwRow = Inventory.find('**/InventoryRow')
throwRow.setColor(255 / 255.0, 145 / 255.0, 66 / 255.0)
row5 = DirectFrame(parent=bigBook, relief=None, image=throwRow, pos=(0, 0, 0.056), scale=(0.9, 1, 1))
squirtRow = Inventory.find('**/InventoryRow')
squirtRow.setColor(255 / 255.0, 65 / 255.0, 199 / 255.0)
row6 = DirectFrame(parent=bigBook, relief=None, image=squirtRow, pos=(0, 0, -0.055), scale=(0.9, 1, 1))
dropRow = Inventory.find('**/InventoryRow')
dropRow.setColor(67 / 255.0, 243 / 255.0, 255 / 255.0)
row7 = DirectFrame(parent=bigBook, relief=None, image=dropRow, pos=(0, 0, -0.166), scale=(0.9, 1, 1))
JellyBeanJar = loader.loadModel('phase_3.5/models/gui/jar_gui.bam')
jar = DirectFrame(parent=bigBook, relief=None, image=JellyBeanJar, pos=(0.65, 0, -0.43), scale=0.65)
JBAmount = DirectLabel(parent=jar, relief=None, pos=(0, 0, -0.12), text='40', text_font=loader.loadFont('phase_3/models/fonts/MickeyFont.bam'), text_fg=(5, 0.94, 0, .89), text_scale=0.2)
DialBox = loader.loadModel('phase_3/models/gui/dialog_box_gui.bam')
Box1 = DirectFrame(parent=bigBook, relief=None, image=DialBox, pos=(0.25, 0, -0.45), scale=0.40)
Box2 = DirectFrame(parent=bigBook, relief=None, image=DialBox, pos=(-0.40, 0, -0.45), scale=0.40)
Box2.setSx(.6)
row1.hide()
row2.hide()
row3.hide()
row4.hide()
row5.hide()
row6.hide()
row7.hide()
jar.hide()
JBAmount.hide()
Box1.hide()
Box2.hide()
#ToonTasks Page
