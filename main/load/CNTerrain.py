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
from cognation.main.cogbase.CogTypes import *
from cognation.main.load.loading_Screens import *

sewerTex = loader.loadTexture('phase_3.5/maps/waiter_m_sleeve.jpg')

waitersleeve = loader.loadTexture('phase_3.5/maps/waiter_m_sleeve.jpg')
waiterlegs = loader.loadTexture('phase_3.5/maps/waiter_m_leg.jpg')
waitertorso = loader.loadTexture('phase_3.5/maps/waiter_m_blazer.jpg')

sellbotTorso = loader.loadTexture('phase_3.5/maps/s_blazer.jpg')
sellbotLeg = loader.loadTexture('phase_3.5/maps/s_sleeve.jpg')
sellbotArm = loader.loadTexture('phase_3.5/maps/s_leg.jpg')

COACH_DIAL = base.loader.loadSfx('phase_9/audio/sfx/Boss_COG_VO_statement.mp3')



base.disableMouse()

sellbotHQ = loader.loadSfx('phase_14/sbhq_pg.mp3')
sellbotHQ.setLoop(True)


daisygardenstreet = loader.loadSfx('phase_14/dg_st.ogg')
daisygardenstreet.setLoop(True)


daisygardenspg = loader.loadSfx('phase_14/dg_pg.ogg')
daisygardenspg.setLoop(True)

toontowncentralstreet = loader.loadSfx('phase_14/ttc_st.ogg')
toontowncentralstreet.setLoop(True)

toontowncentralpg = loader.loadSfx('phase_14/ttc_pg.ogg')
toontowncentralpg.setLoop(True)

flippy = Actor({"torso":"phase_3/models/char/tt_a_chr_dgm_shorts_torso_1000.bam", \
             "legs":"phase_3/models/char/tt_a_chr_dgm_shorts_legs_1000.bam"}, \
             {"torso":{"walk": "phase_3/models/char/tt_a_chr_dgm_shorts_torso_1000.bam", \
             "torsoAnimation":"phase_3/models/char/tt_a_chr_dgm_shorts_torso_neutral.bam"}, \
             "legs":{"walk":"phase_3/models/char/tt_a_chr_dgm_shorts_legs_1000.bam",
             "legsAnimation":"phase_3/models/char/tt_a_chr_dgm_shorts_legs_neutral.bam"}})
 
flippy.attach("torso", "legs", "joint_hips")
 

 

flippy.setPos(0, 0, 0)
flippy.setHpr(0, 0, 0)
 

gloves = flippy.find('**/hands')
gloves.setColor(0.99,0.99,0.99)


mySleeve = loader.loadTexture("phase_3/maps/desat_sleeve_4.jpg")
flippy.find('**/sleeves').setTexture(mySleeve, 1)
  

myShirt = loader.loadTexture("phase_3/maps/desat_shirt_4.jpg")
flippy.find('**/torso-top').setTexture(myShirt, 1)


myShort = loader.loadTexture("phase_3/maps/desat_shorts_10.jpg")
flippy.find('**/torso-bot').setTexture(myShort, 1)
  

flippy.find('**/boots_long').hide()
flippy.find('**/shoes').hide()
flippy.find('**/boots_short').hide()
flippy.find('**/torso-top').setColor(0.992188, 0.480469, 0.167969, 1.0)
flippy.find('**/sleeves').setColor(0.992188, 0.480469, 0.167969, 1.0)
flippy.find('**/torso-bot').setColor(0.726562, 0.472656, 0.859375, 1.0)

Head = Actor("phase_3/models/char/tt_a_chr_dgm_skirt_head_1000.bam")


Head.find('**/head-front').setColor(0.347656, 0.820312, 0.953125, 1.0)
Head.find('**/head').setColor(0.347656, 0.820312, 0.953125, 1.0)

  
Neck = flippy.find('**/def_head')
Head.reparentTo(Neck)
 


flippy.find('**/neck').setColor(0.347656, 0.820312, 0.953125, 1.0)
flippy.find('**/arms').setColor(0.347656, 0.820312, 0.953125, 1.0)
flippy.find('**/legs').setColor(0.347656, 0.820312, 0.953125, 1.0)
flippy.find('**/feet').setColor(0.347656, 0.820312, 0.953125, 1.0)
flippy.loop('torsoAnimation')
flippy.loop('legsAnimation')




vtwocog2 = Actor("phase_3.5/models/char/suitA-mod.bam",{
                "neutral":"phase_4/models/char/suitA-neutral.bam",


})

mrhollywoodhead2 = loader.loadModel("phase_4/models/char/suitA-heads.bam").find("**/yesman")
mrhollywoodhead2.reparentTo(vtwocog2.find("**/joint_head"))

vtwocog2.findAllMatches('**/torso').setTexture(waitertorso , 1)
vtwocog2.findAllMatches('**/arms').setTexture(waitersleeve , 1)
vtwocog2.findAllMatches('**/legs').setTexture(waiterlegs , 1)
vtwocog2.reparentTo(render)
vtwocog2.setPos(-28.2638, -41.6913, 10.0956)
vtwocog2.setHpr(180, 0, 0)
vtwocog2.loop('neutral')

#cog 2:
cogfont = loader.loadFont('fonts/vtRemingtonPortable.ttf')

vtwocog = Actor("phase_3.5/models/char/suitA-mod.bam",{
                "neutral":"phase_4/models/char/suitA-neutral.bam",


})

mrhollywoodhead = loader.loadModel("phase_4/models/char/suitA-heads.bam").find("**/yesman")
mrhollywoodhead.reparentTo(vtwocog.find("**/joint_head"))


vtwocog.findAllMatches('**/torso').setTexture(waitertorso , 1)
vtwocog.findAllMatches('**/arms').setTexture(waitersleeve , 1)
vtwocog.findAllMatches('**/legs').setTexture(waiterlegs , 1)
vtwocog.reparentTo(render)
vtwocog.setPos(27.1725, -41.6913, 10.0956)
vtwocog.setHpr(180, 0, 0)
vtwocog.loop('neutral')

cs = CollisionSphere(0, 0, 2, 3)
cnodePath = vtwocog.attachNewNode(CollisionNode('cnode'))
cnodePath.node().addSolid(cs)

cs2 = CollisionSphere(0, 0, 2, 3)
cnodePath = vtwocog2.attachNewNode(CollisionNode('cnode'))
cnodePath.node().addSolid(cs2)

shadowtex = loader.loadTexture('phase_3/maps/drop-shadow.jpg', 'phase_3/maps/drop-shadow_a.rgb')
shadowcm = CardMaker('shadow')
shadowcm.setFrame(2, -2, 2, -2)
shadow = render.attachNewNode(shadowcm.generate())
jointshadow = vtwocog2.find('**/joint_shadow')
shadow.reparentTo(jointshadow)
shadow.setTexture(shadowtex)
shadow.setP(270)
shadow.setTransparency(True)
shadow.setZ(-0.01)
shadow.setBin('fixed', 40)
shadow.setColor(1, 1, 1, 0.6)
jointshadow.setBin('fixed', 50)
jointshadow.setDepthWrite(True)
jointshadow.setDepthTest(True)
shadow.setDepthWrite(False)
shadow.setDepthTest(False)
shadow.setScale(1.20)

shadowtex = loader.loadTexture('phase_3/maps/drop-shadow.jpg', 'phase_3/maps/drop-shadow_a.rgb')
shadowcm = CardMaker('shadow')
shadowcm.setFrame(2, -2, 2, -2)
shadow = render.attachNewNode(shadowcm.generate())
jointshadow = vtwocog.find('**/joint_shadow')
shadow.reparentTo(jointshadow)
shadow.setTexture(shadowtex)
shadow.setP(270)
shadow.setTransparency(True)
shadow.setZ(-0.01)
shadow.setBin('fixed', 40)
shadow.setColor(1, 1, 1, 0.6)
jointshadow.setBin('fixed', 50)
jointshadow.setDepthWrite(True)
jointshadow.setDepthTest(True)
shadow.setDepthWrite(False)
shadow.setDepthTest(False)
shadow.setScale(1.20)

cogcursor = Filename("customtex/cogmono.cur")
cogiconscreen = Filename("icon.ico")
winprop = WindowProperties()
winprop.setCursorFilename(cogcursor)
winprop.setIconFilename("icon.ico")
base.win.requestProperties(winprop)

base.camera.setPos(0,-30.42,5)


shadowtex = loader.loadTexture('phase_3/maps/drop-shadow.jpg', 'phase_3/maps/drop-shadow_a.rgb')
shadowcm = CardMaker('shadow')
shadowcm.setFrame(2, -2, 2, -2)
shadow = render.attachNewNode(shadowcm.generate())
jointshadow = cogplayer.find('**/joint_shadow')
shadow.reparentTo(jointshadow)
shadow.setTexture(shadowtex)
shadow.setP(270)
shadow.setTransparency(True)
shadow.setZ(-0.01)
shadow.setBin('fixed', 40)
shadow.setColor(1, 1, 1, 0.6)
jointshadow.setBin('fixed', 50)
jointshadow.setDepthWrite(True)
jointshadow.setDepthTest(True)
shadow.setDepthWrite(False)
shadow.setDepthTest(False)
shadow.setScale(1.20)

SBHQ = loader.loadModel('phase_9/models/cogHQ/SellbotHQExterior.bam')
SBHQ.reparentTo(render)
SBHQ.find('**/doors').setPosHpr(0, -80, 0, 180, 0, 0)

CogPlayerHelper = Actor("phase_3.5/models/char/suitA-mod.bam",{
          "walk":"phase_4/models/char/suitA-walk.bam",
          "run":"phase_4/models/char/suitA-walk.bam",
          "neutral":"phase_4/models/char/suitA-neutral.bam",
          "running-jump-idle":"phase_5/models/char/suitA-landing.bam",
          "jump-idle":"phase_5/models/char/suitA-landing.bam",
          "magic1":"phase_5/models/char/suitA-magic1.bam",
          "magic2":"phase_5/models/char/suitA-magic2.bam",
          "magic3":"phase_5/models/char/suitA-magic3.bam",
          "magic3":"phase_5/models/char/suitA-magic3.bam",
          "magic3":"phase_5/models/char/suitA-magic3.bam",
          "magic3":"phase_5/models/char/suitA-magic3.bam",
          "magic3":"phase_5/models/char/suitA-magic3.bam",
          "magic3":"phase_5/models/char/suitA-magic3.bam",
          "sitting":"phase_12/models/char/suitA-sit.bam"
		
 })
CogPlayerHelper.reparentTo(render)
CogPlayerHelper.setPos(0.1, 1, -0.3)
CogPlayerHelper.setHpr(180,0,0)
CogPlayerHelper.loop('sitting')
CogPlayerHelper.hide()

CogPlayerHelperHead = loader.loadModel('phase_12/models/bossbotHQ/mole_cog.bam')
CogPlayerHelperHead.reparentTo(CogPlayerHelper.find('**/joint_head'))
CogPlayerHelperHead.setHpr(180,0,0)
CogPlayerHelperHead.setPos(0,0,-0.8)
CogPlayerHelper.find('**/hands').setColor(0.807843137254902,0.0156862745098039,0.0156862745098039)
CogPlayerHelper.setScale(1.2)

cs = CollisionSphere(0, 0, 0, 2)
cnodePath1 = CogPlayerHelper.find('**/legs').attachNewNode(CollisionNode('cnode'))
cnodePath1.node().addSolid(cs)
cnodePath1.hide()

cs2 = CollisionSphere(0, 0, 0, 2)
cnodePath2 = CogPlayerHelper.find('**/hands').attachNewNode(CollisionNode('cnode'))
cnodePath2.node().addSolid(cs2)
cnodePath2.hide()

cs3 = CollisionSphere(0, 0, 0, 2)
cnodePath3 = CogPlayerHelperHead.attachNewNode(CollisionNode('cnode'))
cnodePath3.node().addSolid(cs3)
cnodePath3.hide()

cs4 = CollisionSphere(0, 0, 0, 3)
cnodePath4 = CogPlayerHelper.find('**/arms').attachNewNode(CollisionNode('cnode'))
cnodePath4.node().addSolid(cs4)
cnodePath4.hide()

ColdCaller = Actor('phase_3.5/models/char/suitC-mod.bam',{
            'neutral':'phase_3.5/models/char/suitC-neutral.bam'

})
ColdCaller.find('**/torso').setTexture(sellbotTorso, 1)
ColdCaller.find('**/arms').setTexture(sellbotArm, 1)
ColdCaller.find('**/legs').setTexture(sellbotLeg, 1)
ColdCallerHead = loader.loadModel('phase_3.5/models/char/suitC-heads.bam').find('**/coldcaller')
ColdCallerHead.reparentTo(ColdCaller.find('**/joint_head'))
ColdCaller.reparentTo(render)
ColdCaller.hide()

shadowtex = loader.loadTexture('phase_3/maps/drop-shadow.jpg', 'phase_3/maps/drop-shadow_a.rgb')
shadowcm = CardMaker('shadow')
shadowcm.setFrame(2, -2, 2, -2)
shadow = render.attachNewNode(shadowcm.generate())
jointshadow = ColdCaller.find('**/joint_shadow')
shadow.reparentTo(jointshadow)
shadow.setTexture(shadowtex)
shadow.setP(270)
shadow.setTransparency(True)
shadow.setZ(-0.01)
shadow.setBin('fixed', 40)
shadow.setColor(1, 1, 1, 0.6)
jointshadow.setBin('fixed', 50)
jointshadow.setDepthWrite(True)
jointshadow.setDepthTest(True)
shadow.setDepthWrite(False)
shadow.setDepthTest(False)
shadow.setScale(1.20)

nflippy = False
TaskNum = 'NeedTask'
loadedArea = 'sbhq'
def updateTunnel(task):
	global loadedArea
	global SBHQ	
	global streetDG3300
	global daisygardens
	global sewer
	global factory
	global streetDG3100
	global streetTTC1100
	global toontowncentral
	global lobby
	global flippyNum
	global BossRoomHQ
	global toonhall
	global nflippy
	global toontowncentraltoonhall
	global TaskNum
	global ChairmanOffice
	
	x = localAvatar.getPos().get_x()
	y = localAvatar.getPos().get_y()
	
	if x <= 7.7911 and x >= -7.7911 and y <= -297.143 and y >= -329.135 and loadedArea == 'sbhq':
		RunScreen()
		SBHQ.remove()
		SBHQ = loader.unloadModel('phase_9/models/cogHQ/SellbotHQExterior.bam')
		vtwocog.hide()
		vtwocog2.hide()
		cog.hide()
		cog1.hide()
		cog3.hide()
		cog6.hide()
		cog11.hide()
		sellbotHQ.stop()
		daisygardenstreet.play()
		streetDG3300 = loader.loadModel('phase_15/street/DG3300.bam')
		loadedArea = 'DG3300'
		streetDG3300.reparentTo(render)
		localAvatar.setPos(0.18, -281.24, 0.50)
		loadingtext['text'] = 'Loading Maple Street. . .'
		localAvatar.setPosHpr(-310.387, 307.961, -0.474977, -180.00, 0, 0)
		
	if x <= -302.622 and x >= -319.235  and y >= 317.68 and y <= 327.335 and loadedArea == 'DG3300':
		RunScreen()
		streetDG3300.remove()
		streetDG3300 = loader.unloadModel('phase_15/street/DG3300.bam')
		daisygardenstreet.stop()
		sellbotHQ.play()
		loadedArea = 'sbhq'
		cog.show()
		cog1.show()
		cog3.show()
		cog6.show()
		cog11.show()
		SBHQ = loader.loadModel('phase_9/models/cogHQ/SellbotHQExterior.bam')
		SBHQ.reparentTo(render)
		SBHQ.find('**/doors').setPosHpr(0, -80, 0, 180, 0, 0)
		cogplayer.setPos(0.18,-281.24,0.50)
		vtwocog.show()
		vtwocog2.show()
		loadingtext['text'] = 'Loading SellbotHQ. . .'
		
	if x <= -86.4406 and x >= -93.0742  and y <= -31.8523  and y >= -47.7283 and loadedArea == 'DG3300':
		RunScreen()
		streetDG3300.remove()
		streetDG3300 = loader.unloadModel('phase_15/street/DG3300.bam')
		daisygardenstreet.stop()
		daisygardenspg.play()
		vtwocog.hide()
		vtwocog2.hide()
		loadedArea = 'daisygardens'
		daisygardens = loader.loadModel('phase_15/hood/daisys_garden.bam')
		daisygardens.reparentTo(render)
		localAvatar.setPosHpr(0.559869, 15.3223, 0.025,0, 0, 0)
		loadingtext['text'] = "Loading Daisy's Garden. . ."
		
	if x >= -8.22 and x <= 8.0277  and y <= 6.82479 and y >= 3.3676 and loadedArea == 'daisygardens':
		RunScreen()
		daisygardens.remove()
		daisygardens = loader.unloadModel('phase_15/hood/daisys_garden.bam')
		daisygardenspg.stop()
		daisygardenstreet.play()
		vtwocog.hide()
		vtwocog2.hide()
		loadedArea = 'DG3300'
		streetDG3300 = loader.loadModel('phase_15/street/DG3300.bam')
		streetDG3300.reparentTo(render)
		localAvatar.setPosHpr(-79.5311, -40.8007, -0.475,-90.000, 0, 0)
		loadingtext['text'] = 'Loading Maple Street. . .'
		
	if x >= 45.2842 and x <= 50.1814 and y <= -93.7887 and y >= -98.1948 and loadedArea == 'sbhq':
		RunScreen()
		SBHQ.remove()
		SBHQ = loader.unloadModel('phase_9/models/cogHQ/SellbotHQExterior.bam')
		vtwocog.hide()
		vtwocog2.hide()	
		cog.hide()
		cog1.hide()
		cog3.hide()
		cog6.hide()
		cog11.hide()
		loadedArea = 'sewer'
		sewer = loader.loadModel ('phase_16/models/cogHQ/SewerModel.obj')
		sewer.reparentTo(render)
		CogPlayerHelper.hide()
		sewer.setTexture(sewerTex, 1)
		sewer.setScale(.5)
		localAvatar.setPosHpr(-56.5077,-44.775,0.128398,-449.338,0,0)
		loadingtext['text'] = 'Loading The Sewer. . .'
		
	if x >= 148.051 and x <= 152.452 and y >= -162.175 and y <= -147.354 and loadedArea == 'sbhq':
		RunScreen()
		SBHQ.remove()
		SBHQ = loader.unloadModel('phase_9/models/cogHQ/SellbotHQExterior.bam')
		cog.hide()
		cog1.hide()
		cog3.hide()
		cog6.hide()
		cog11.hide()
		vtwocog.show()
		vtwocog2.show()
		sellbotHQ.stop()
		sellbotHQ.play()
		loadedArea = 'ChairmanOffice'
		CogPlayerHelper.show()
		ChairmanOffice = loader.loadModel ('Cog_Office.bam')
		ChairmanOffice.reparentTo(render)
		localAvatar.setPosHpr(-0.43287,-34.2996,9.76548e-005,-13.2338,0,0)
		loadingtext['text'] = "The Chairman's Office. . ."

	if x <= 7.23568 and x >= -7.6803 and y >= -44.4896 and y <= -36.2516 and loadedArea == 'ChairmanOffice':
		RunScreen()
		ChairmanOffice.remove()
		ChairmanOffice = loader.unloadModel ('Cog_Office.bam')
		vtwocog.show()
		vtwocog2.show()
		sellbotHQ.stop()
		sellbotHQ.play()
		loadedArea = 'sbhq'
		CogPlayerHelper.hide()
		SBHQ = loader.unloadModel('phase_9/models/cogHQ/SellbotHQExterior.bam')
		SBHQ.reparentTo(render)
		localAvatar.setPosHpr(-0.43287,-34.2996,9.76548e-005,-13.2338,0,0)
		loadingtext['text'] = "Sellbot HQ. . ."
	
	if x <= 8.22912 and x >= -8.31603 and y <= -351.307 and y >= -360.594 and loadedArea == 'ChairmanOffice':
		RunScreen()
		factory.remove()
		factory = loader.unloadModel('phase_9/models/cogHQ/SellbotFactoryExterior.bam')
		sellbotHQ.stop()
		sellbotHQ.play()
		cog.show()
		cog1.show()
		cog3.show()
		cog6.show()
		cog11.show()
		loadedArea = 'sbhq'
		CogPlayerHelper.show()
		SBHQ = loader.loadModel ('phase_9/models/cogHQ/SellbotHQExterior.bam')
		SBHQ.reparentTo(render)
		SBHQ.find('**/doors').setPosHpr(0, -80, 0, 180, 0, 0)
		vtwocog.show()
		vtwocog2.show()
		localAvatar.setPosHpr(141.719,-155.332,0.324422,90.000,0,0)	
		loadingtext['text'] = 'Loading SellbotHQ. . .'
	
	if x <= 86.6749 and x >= 70.3627 and y >= 182.983 and y <= 191.215 and loadedArea == 'daisygardens':
		RunScreen()
		daisygardens.remove()
		daisygardens = loader.unloadModel('phase_15/street/daisys_garden.bam')
		daisygardenspg.stop()
		daisygardenstreet.play()
		loadedArea = 'streetDG3100'
		streetDG3100 = loader.loadModel('phase_15/street/DG3100.bam')
		vtwocog.hide()
		vtwocog2.hide()
		streetDG3100.reparentTo(render)
		localAvatar.setPosHpr(-49.6464,28.7311,-0.474992,-89.2095,0,0)
		loadingtext['text'] = 'Loading a Street. . .'
		
	if x <= -61.0835 and x >= -65.8696 and y <= 36.3326 and y >= 20.1 and loadedArea == 'streetDG3100':
		RunScreen()
		streetDG3100.remove()
		daisygardens = loader.unloadModel('phase_15/street/DG3100.bam')
		daisygardenstreet.stop()
		daisygardenspg.play()
		loadedArea = 'daisygardens'
		daisygardens = loader.loadModel('phase_15/hood/daisys_garden.bam')
		vtwocog.hide()
		vtwocog2.hide()
		daisygardens.reparentTo(render)
		localAvatar.setPosHpr(72.5971,182.18,10.0211,121.496,0,0)
		loadingtext['text'] = "Loading Daisy's Garden. . ."
		
	if x >= 678.659 and x <= 683.74 and y <= 106.85 and y >= 89.65 and loadedArea == 'streetDG3100':
		RunScreen()
		streetDG3100.remove()
		streetDG3100 = loader.unloadModel('phase_15/street/DG3100.bam')
		daisygardenstreet.stop()
		toontowncentralstreet.play()
		loadedArea = 'streetTTC1100'
		streetTTC1100 = loader.loadModel('phase_15/street/TTC1100.bam')
		vtwocog.hide()
		vtwocog2.hide()
		streetTTC1100.reparentTo(render)
		localAvatar.setPosHpr(-359.361,-383.161,-0.475,358.272,0,0)
		loadingtext['text'] = 'Loading Toontown Central. . .'
		

	if x >= -368.6 and x <= -351.476 and y >= -405.6 and y <= -400.998 and loadedArea == 'streetTTC1100':
		RunScreen()
		streetTTC1100.remove()
		streetTTC1100 = loader.loadModel('phase_15/street/TTC1100.bam')
		toontowncentralstreet.stop()
		daisygardenstreet.play()
		loadedArea = 'streetDG3100'
		streetDG3100 = loader.loadModel('phase_15/street/DG3100.bam')
		vtwocog.hide()
		vtwocog2.hide()
		streetDG3100.reparentTo(render)
		localAvatar.setPosHpr(672.324,98.0413,-0.474922,90.0000,0,0)
		loadingtext['text'] = 'Loading a Street. . .'
		
	if x >= -90.4662 and x <= -80.5745 and y >= -108.012 and y <= -91.84 and loadedArea == 'streetTTC1100':
		RunScreen()
		streetTTC1100.remove()
		streetTTC1100 = loader.unloadModel('phase_15/street/TTC1100.bam')
		toontowncentralstreet.stop()
		toontowncentralpg.play()
		loadedArea = 'toontowncentral'
		toontowncentral = loader.loadModel('phase_15/hood/toontown_central.bam')
		vtwocog.hide()
		vtwocog2.hide()
		toontowncentral.reparentTo(render)
		localAvatar.setPosHpr(44.5512,-137.705,2.525,-137.702,0,0)
		loadingtext['text'] = 'Loading Toontown Central. . .'
		
	if x >= 20.6063 and x <= 38.3928 and y <= -155.311 and y >= -157.256 and loadedArea == 'toontowncentral':
		RunScreen()
		toontowncentral.remove()
		toontowncentral = loader.unloadModel('phase_15/hood/toontown_central.bam')
		toontowncentralpg.stop()
		toontowncentralstreet.play()
		loadedArea = 'streetTTC1100'
		streetTTC1100 = loader.loadModel('phase_15/street/TTC1100.bam')
		vtwocog.hide()
		vtwocog2.hide()
		streetTTC1100.reparentTo(render)
		localAvatar.setPosHpr(-96.1273,-100.143,-0.475,90.0000,0,0)
		loadingtext['text'] = 'Loading a Street. . .'
		
	if x <= 112.26 and x >= 111.204 and y <= 5.13884 and y >= -2.37903 and loadedArea == 'toontowncentral':
		RunScreen()
		toontowncentral.remove()
		toontowncentral = loader.unloadModel('phase_15/hood/toontown_central.bam')
		toontowncentralpg.stop()
		toontowncentralstreet.play()
		loadedArea = 'toonhall'
		toonhall = loader.loadModel('phase_3.5/models/modules/tt_m_ara_int_toonhall.bam')
		door = loader.loadModel('phase_3.5/models/modules/doors_practical.bam').find('**/door_double_round_ur')
		door.reparentTo(toonhall.find('**/door_origin'))
		door.setColor(0.88, 0.45, 0.38, 1)
		vtwocog.hide()
		vtwocog2.hide()
		toonhall.reparentTo(render)
		flippy.reparentTo(toonhall.find('**/npc_origin_0'))
		localAvatar.setPosHpr(-1.67989,0.0923404,-0.025,403.538,0,0)
		loadingtext['text'] = 'Loading Toon Hall. . .'
		
	if x <= 28.4731 and x >= 22.5326 and y <= -23.5991 and y >= -27.4781 and loadedArea == 'toonhall':
		RunScreen()
		toonhall.removeNode()
		toonhall = loader.unloadModel('phase_3.5/models/modules/tt_m_ara_int_toonhall.bam')
		toontowncentralstreet.stop()
		toontowncentralpg.play()
		loadedArea = 'toontowncentral'
		toontowncentral = loader.loadModel('phase_15/hood/toontown_central.bam')
		toontowncentral.reparentTo(render)
		toontowncentral.reparentTo(render)
		localAvatar.setPosHpr(86.6284,0.956559,4.025,90.0000,0,0)
		loadingtext['text'] = 'Loading Toontown Central. . .'
		
	if x >= -20.6062 and x <= 19.0758 and y <= -41.6913 and y >= -46.5296 and loadedArea == 'sbhq':
		RunScreen()
		SBHQ.remove()
		cog.hide()
		cog1.hide()
		cog3.hide()
		cog6.hide()
		cog11.hide()
		SBHQ = loader.unloadModel('phase_9/models/cogHQ/SellbotHQExterior.bam')
		vtwocog.hide()
		vtwocog2.hide()
		sellbotHQ.stop()
		sellbotHQ.play()
		loadedArea = 'sbhqlobby'
		lobby = loader.loadModel('phase_9/models/cogHQ/SellbotHQLobby.bam')
		lobbyElevator = loader.loadModel('phase_9/models/cogHQ/cogHQ_elevator.bam')
		lobbyElevator.reparentTo(lobby.find('**/elevator_locator'))
		lobbyElevator.setHpr(180,0,0)
		lobby.reparentTo(render)
		localAvatar.setPosHpr(-11.537,83.2849,23.4603,92.015,0,0)
		ColdCaller.show()
		ColdCaller.setPosHpr(-0.570246, 14.6351, 0.025, 0, 0, 0)
		ColdCaller.loop('neutral')
		ColdCallerHead.setColor(0.0941176470588235,0.2313725490196078, 1)
		ColdCaller.find('**/hands').setColor(0.5490196078431373,0.6431372549019608,0.9882352941176471)

		cnodePath1 = ColdCaller.find('**/legs').attachNewNode(CollisionNode('cnode'))
		cnodePath1.node().addSolid(cs)
		cnodePath1.hide()


		cnodePath2 = ColdCaller.find('**/hands').attachNewNode(CollisionNode('cnode'))
		cnodePath2.node().addSolid(cs2)
		cnodePath2.hide()
		loadingtext['text'] = 'Loading The Lobby. . .'


		cnodePath4 = ColdCaller.find('**/arms').attachNewNode(CollisionNode('cnode'))
		cnodePath4.node().addSolid(cs4)
		cnodePath4.hide()
		
		
	if x >= -6.55657 and x <= 7.07995 and y <= 92.228 and y >= 90.8954 and loadedArea == 'sbhqlobby':
		RunScreen()
		lobby.remove()
		lobby = loader.unloadModel ('phase_9/models/cogHQ/SellbotHQLobby.bam')
		sellbotHQ.stop()
		sellbotHQ.play()
		loadedArea = 'sbhq'
		cog.show()
		cog1.show()
		cog3.show()
		cog6.show()
		cog11.show()
		SBHQ = loader.loadModel('phase_9/models/cogHQ/SellbotHQExterior.bam')
		SBHQ.reparentTo(render)
		SBHQ.find('**/doors').setPosHpr(0, -80, 0, 180, 0, 0)
		CogPlayerHelper.show()
		ColdCaller.hide()
		vtwocog.show()
		vtwocog2.show()
		localAvatar.setPosHpr(-7.70738,-51.7273,10.0956,109.814,0,0)
		loadingtext['text'] = 'Loading SellbotHQ. . .'
		
	if x >= -11.1152 and x <= 10.1215 and y <= -75.5536 and y >= -82.1215 and loadedArea == 'sbhqlobby':
		RunScreen()
		lobby.remove()
		lobby = loader.unloadModel ('phase_9/models/cogHQ/SellbotHQLobby.bam')
		sellbotHQ.stop()
		sellbotHQ.play()
		loadedArea = 'BossRoomHQ'
		BossRoomHQ = loader.loadModel('phase_9/models/cogHQ/BossRoomHQ.bam')
		BossRoomHQ.reparentTo(render)
		BossRoomElevator = loader.loadModel('phase_9/models/cogHQ/cogHQ_elevator.bam')
		BossRoomElevator.reparentTo(BossRoomHQ.find('**/elevatorEntrance'))
		BossRoomElevator.setScale(0.5)
		vtwocog.hide()
		vtwocog2.hide()
		localAvatar.setPosHpr(-4.16988,60.8268,17.952,-178.163,0,0)
		loadingtext['text'] = 'Loading The Boss Room. . .'
		
	if x >= -12.175 and x <= 12.0653 and y <= 84.2456 and y >= 80.5549 and loadedArea == 'BossRoomHQ':
		RunScreen()
		BossRoomHQ.remove()
		BossRoomHQ = loader.unloadModel('phase_9/models/cogHQ/BossRoomHQ.bam')
		sellbotHQ.stop()
		vtwocog.hide()
		vtwocog2.hide()
		sellbotHQ.play()
		loadedArea = 'sbhqlobby'
		lobby = loader.loadModel('phase_9/models/cogHQ/SellbotHQLobby.bam')
		lobbyElevator = loader.loadModel('phase_9/models/cogHQ/cogHQ_elevator.bam')
		lobbyElevator.reparentTo(lobby.find('**/elevator_locator'))
		lobbyElevator.setHpr(180,0,0)
		lobby.reparentTo(render)
		localAvatar.setPosHpr(0.159549,-72.0753,27.9362,-2.5893,0,0)
		loadingtext['text'] = 'Loading The Lobby. . .'
		
	if x >= -69.5587 and x <= -62.3538 and y >= -53.0759 and y <= -36.298 and loadedArea == 'sewer':
		RunScreen()
		sewer.remove()
		sewer = loader.unloadModel ('phase_16/models/cogHQ/SewerModel.obj')
		loadedArea = 'sbhq'
		cog.show()
		cog1.show()
		cog3.show()
		cog6.show()
		cog11.show()
		SBHQ = loader.loadModel('phase_9/models/cogHQ/SellbotHQExterior.bam')
		SBHQ.reparentTo(render)
		SBHQ.find('**/doors').setPosHpr(0, -80, 0, 180, 0, 0)
		vtwocog.show()
		vtwocog2.show()
		localAvatar.setPosHpr(48.1971,-103.434,0.284907,180.00,0,0)
		loadingtext['text'] = 'Loading SellbotHQ. . .'
		
	if x >= -8.22 and x <= 8.0277  and y <= 6.82479 and y >= 3.3676 and loadedArea == 'daisygardens':
		RunScreen()
		daisygardens.remove()
		daisygardens = loader.unloadModel('phase_15/hood/daisys_garden.bam')
		daisygardenspg.stop()
		daisygardenstreet.play()
		vtwocog.hide()
		vtwocog2.hide()
		loadedArea = 'DG3300'
		streetDG3300 = loader.loadModel('phase_15/street/DG3300.bam')
		streetDG3300.reparentTo(render)
		localAvatar.setPosHpr(-79.5311, -40.8007, -0.475,-90.000, 0, 0)
		loadingtext['text'] = 'Loading a Street. . .'

		
	if x >= -71.2782 and x <= -67.0609  and y >= 28.8998 and y <= 33.9408 and loadedArea == 'toonhall':
		if nflippy == False:
			
			flippyNum = random.randint(0, 5)
			print flippyNum
			nflippy = True
		
	else:
		nflippy = False


	if x >= -40.8298 and x <= -35.9567  and y >= 16.9 and y <= 33.1477 and loadedArea == 'DG3200':
		RunScreen()
		DG3200.remove()
		DG3200 = loader.unloadModel('phase_15/street/DG3200.bam')
		daisygardenstreet.stop()
		daisygardenspg.play()
		loadedArea = 'daisygardens'
		daisygardens = loader.loadModel('phase_15/hood/daisys_garden.bam')
		daisygardens.reparentTo(render)
		localAvatar.setPosHpr(-63.7202,177.233,10.025,233.946,0,0)

	if x <= 700.65 and x >= 695.331 and y <= 93.4 and y >= 76.2314 and loadedArea == 'DG3200':
		RunScreen()
		DG3200.remove()
		DG3200 = loader.unloadModel('phase_15/street/DG3200.bam')
		daisygardenstreet.stop()
		donaldsdockstreet.play()
		loadedArea = 'DD2200'
		DD2200 = loader.loadModel('phase_15/street/DD2200.bam')
		DD2200.reparentTo(render)
		localAvatar.setPosHpr(-312.625,-429.969,-0.474962,92.4067,0,0)

	if x <= -289.4 and x >= -293.016 and y <= -421.4 and y >= -438.6 and loadedArea == 'DD2200':
		RunScreen()
		DD2200.remove()
		DD2200 = loader.unloadModel('phase_15/street/DD2200.bam')
		donaldsdockstreet.stop()
		daisygardenstreet.play()
		loadedArea = 'DG3200'
		DG3200 = loader.loadModel('phase_15/street/DG3200.bam')
		DG3200.reparentTo(render)
		localAvatar.setPosHpr(684.46,85.332,-0.475,447.542,0,0)

	if x >= -173.1 and x <= -156.852 and y <= -117.005 and y >= -124.257 and loadedArea == 'DD2200':
		RunScreen()
		DD2200.remove()
		DD2200 = loader.unloadModel('phase_15/street/DD2200.bam')
		donaldsdockstreet.stop()
		donaldsdockpg.play()
		loadedArea = 'donaldsdock'
		donaldsdock = loader.loadModel('phase_15/hood/donalds_dock.bam')
		donaldsdock.reparentTo(render)
		localAvatar.setPosHpr(-114.459,15.1203,5.69199,270.62,0,0)
		
	if x >= -128.59 and x <= -121.684 and y >= 6.83231 and y <= 23.08 and loadedArea == 'donaldsdock':
		RunScreen()
		donaldsdock.remove()
		donaldsdock = loader.unloadModel('phase_15/hood/donalds_dock.bam')
		donaldsdockpg.stop()
		donaldsdockstreet.play()
		loadedArea = 'DD2200'
		DD2200 = loader.loadModel('phase_15/street/DD2200.bam')
		DD2200.reparentTo(render)
		localAvatar.setPosHpr(-163.713,-136.705,-0.475,185.46,0,0)		
			
	if x >= -93.4415 and x <= -103.004 and y >= -75.1768 and y <= -60.3687 and loadedArea == 'donaldsdock':
		RunScreen()
		donaldsdock.remove()
		donaldsdock = loader.unloadModel('phase_15/hood/donalds_dock.bam')
		donaldsdockpg.stop()
		donaldsdockstreet.play()
		loadedArea == 'DD2100'
		DD2100 = loader.loadModel('phase_15/street/DD2100.bam')
		DD2100.reparentTo(render)
	

	return Task.cont
	

base.taskMgr.add(updateTunnel, 'UpdateTunnel')
base.setFrameRateMeter(True)
