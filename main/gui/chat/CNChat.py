import jsonpickle
import os
import sys
import time
from random import randint
from random import choice
from random import *
import random
from sys import argv
from direct.directbase import DirectStart
from direct.task import Task
from direct.actor.Actor import Actor
from direct.gui.DirectGui import *
from direct.interval.IntervalGlobal import *
from direct.showbase.InputStateGlobal import inputState
from direct.controls.GravityWalker import GravityWalker
from random import choice
from random import *
import random
from sys import argv
from direct.directbase import DirectStart
from direct.task import Task
from direct.actor.Actor import Actor
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.showbase.InputStateGlobal import inputState
from direct.controls.GravityWalker import GravityWalker
from sys import argv
from direct.task import Task
from direct.actor.Actor import Actor
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.showbase.InputStateGlobal import inputState
from direct.controls.GravityWalker import GravityWalker
from cognation.main.cogbase.CogTypes import *
from cognation.main.cogbase.Walker import *
password = '4322'



onScreenDebug.enabled = False
def updateOnScreenDebug(task):
 
	onScreenDebug.add('Avatar Position', localAvatar.getPos())
	onScreenDebug.add('Avatar Angle', localAvatar.getHpr())
 
	return Task.cont
 
base.taskMgr.add(updateOnScreenDebug, 'UpdateOSD')



cog = loader.loadModel('phase_3.5/models/char/suitC-mod.bam')
cog1 = loader.loadModel('phase_3.5/models/char/suitC-mod.bam')
cog3 = loader.loadModel('phase_3.5/models/char/suitC-mod.bam')
cog6 = loader.loadModel('phase_3.5/models/char/suitC-mod.bam')
cog11 = loader.loadModel('phase_3.5/models/char/suitC-mod.bam')

cog.reparentTo(render)
cog1.reparentTo(render)
cog3.reparentTo(render)
cog6.reparentTo(render)
cog11.reparentTo(render)

cog.setScale(0.0000000000000001)
cog1.setScale(0.0000000000000001)
cog3.setScale(0.0000000000000001)
cog6.setScale(0.0000000000000001)
cog11.setScale(0.0000000000000001)

SAVEGAME_FILENAME = 'cognation/saves/CN_WORLD_R00_SV.wad'
FONT2 = loader.loadFont('phase_3/models/fonts/vtRemingtonPortable.ttf')
game_state = dict()

class Toon(object):
	def __init__(self, gmIcon, name):
		self.gmIcon = gmIcon
		
		
def load_game():
    with open(SAVEGAME_FILENAME, 'r') as savegame:
        state = jsonpickle.decode(savegame.read())
    return state


def save_game():
    global game_state
    with open(SAVEGAME_FILENAME, 'w') as savegame:
        savegame.write(jsonpickle.encode(game_state))
    print "Game Saved"
def SaveLeGame():
    game_state = save_game()


def initialize_game():
    global game_state
    player = Toon('0')
    
    


    state = dict()
    state['toons'] = [player]
    return state

def main():
    global game_state
    
    if not os.path.isfile(SAVEGAME_FILENAME):
        game_state = initialize_game()
    else:
        game_state = load_game()
main()
player = game_state['toons'][0]
        
if player.gmIcon == '1':
	getEmblemSource = loader.loadModel("phase_3.5/models/gui/tt_m_gui_gm_toontroop_whistle.bam")
	getEmblemSource.reparentTo(render)
	getEmblemSource.hide()
	emblem = getEmblemSource.find('**/whistleIcon')
	emblem.show()
	emblem.reparentTo(suitC.find('**/joint_nameTag'))
	emblem.setScale(2.5)
	emblem.setBillboardAxis()
	emblem.setZ(14)
	emblemSpin = emblem.hprInterval(3, Vec3(360, 0, 0))
	emblemSpin.loop()
	emblem.setPos(0,0,7.16)
if player.gmIcon == '2':
	getEmblemSource = loader.loadModel("phase_3.5/models/gui/tt_m_gui_gm_toontroop_getConnected.bam")
	getEmblemSource.reparentTo(render)
	getEmblemSource.hide()
	emblem = getEmblemSource.find('**/whistleIcon')
	emblem.show()
	emblem.reparentTo(suitC.find('**/joint_nameTag'))
	emblem.setScale(2.5)
	emblem.setBillboardAxis()
	emblem.setZ(14)
	emblemSpin = emblem.hprInterval(3, Vec3(360, 0, 0))
	emblemSpin.loop()
	emblem.setPos(0,0,7.16)
if player.gmIcon == '3':
	getEmblemSource = loader.loadModel("phase_3.5/models/gui/tt_m_gui_gm_toonResistance_fist.bam")
	getEmblemSource.reparentTo(render)
	getEmblemSource.hide()
	emblem = getEmblemSource.find('**/fistIcon')
	emblem.show()
	emblem.reparentTo(suitC.find('**/joint_nameTag'))
	emblem.setScale(2.5)
	emblem.setBillboardAxis()
	emblem.setZ(14)
	emblemSpin = emblem.hprInterval(3, Vec3(360, 0, 0))
	emblemSpin.loop()
	emblem.setPos(0,0,7.16)

	
	
	

class CogTags:
    def setTalk(self, message):
        if hasattr(self, 'chatbubble'):
            self.chatbubble.removeNode()
        self.chatbubble = loader.loadModel('phase_3/models/props/chatbox.bam')
        self.chatbubble.reparentTo(localAvatar)
        self.chatbubble.setPos(0,0,5.5)
        self.chatbubble.setBillboardAxis(3)
        self.chatbubble.setScale(0.6)
        self.chatbubble.find('**/chatBalloon').setPos(0,0.05,0)
        self.chatbubble.find('**/chatBalloon').setSx(0.8)#0.8 is the main
        self.talk = OnscreenText(scale=.70,font=loader.loadFont('phase_3/models/fonts/vtRemingtonPortable.ttf'),pos=(0.9,3),text=message,wordwrap=10,decal=True,parent=self.chatbubble,align=TextNode.ALeft)
        self.tag.hide()
        Sequence(Wait(5),Func(self.chatbubble.removeNode),Func(self.tag.show)).start()
        if len(message) <= 4:
			self.chatbubble.find('**/chatBalloon').setSx(0.3)
			self.chatbubble.find('**/chatBalloon').setSz(0.46)
			self.talk['pos'] = (0.6,1)
        elif len(message) == 5:
			self.chatbubble.find('**/chatBalloon').setSx(0.3)
			self.chatbubble.find('**/chatBalloon').setSz(0.46)
			self.talk['pos'] = (0.6,1)
	elif len(message) >= 6 and len(message) <= 9:
		self.chatbubble.find('**/chatBalloon').setSx(0.5)
		self.chatbubble.find('**/chatBalloon').setSz(0.46)
		self.talk['pos'] = (0.5,1)
	elif len(message) >= 10 and len(message) <= 15:
		self.chatbubble.find('**/chatBalloon').setSx(0.8)
		self.chatbubble.find('**/chatBalloon').setSz(0.5)
		self.talk['pos'] = (0.9,1)
	elif len(message) >= 27:
		self.chatbubble.find('**/chatBalloon').setSx(0.8)
		self.chatbubble.find('**/chatBalloon').setSz(1)
		self.talk['pos'] = (0.9,3)
 
    def toonSound(self, species, type):
        loader.loadSfx("phase_3.5/audio/dial/COG_{0}_{1}".format(species, type)).play()
 
    def sendChat(self, message):
        self.toonSpecies = 'VO'
        
	if (message) == '~speed' and password == '4322':
		walkControls.setWalkSpeed(128.0, 50.0, 40.0, 80.0)
	elif (message) == '~speed' and password != '4322':
		print 'You need the password!'
				
	if (message) == '~speedOff' and password == '4322':
		walkControls.setWalkSpeed(32.0, 28.0, 16.0, 80.0)
	elif (message) == '~speedOff' and password != '4322':
		print 'You need the password!'
		
	if (message) == '~gmIcon 1' and password == '4322':
		global emblem
		getEmblemSource = loader.loadModel("phase_3.5/models/gui/tt_m_gui_gm_toontroop_whistle.bam")
		getEmblemSource.reparentTo(render)
		getEmblemSource.hide()
		emblem = getEmblemSource.find('**/whistleIcon')
		emblem.show()
		emblem.reparentTo(suitC.find('**/joint_nameTag'))
		emblem.setScale(2.5)
		emblem.setBillboardAxis()
		emblem.setZ(14)
		emblemSpin = emblem.hprInterval(3, Vec3(360, 0, 0))
		emblemSpin.loop()
		emblem.setPos(0,0,7.16)
		player.gmIcon = '1'
		SaveLeGame()
		
	if (message) == '~gmIcon 2' and password == '4322':
		getEmblemSource = loader.loadModel("phase_3.5/models/gui/tt_m_gui_gm_toontroop_getConnected.bam")
		getEmblemSource.reparentTo(render)
		getEmblemSource.hide()
		emblem = getEmblemSource.find('**/whistleIcon')
		emblem.show()
		emblem.reparentTo(suitC.find('**/joint_nameTag'))
		emblem.setScale(2.5)
		emblem.setBillboardAxis()
		emblem.setZ(14)
		emblemSpin = emblem.hprInterval(3, Vec3(360, 0, 0))
		emblemSpin.loop()
		emblem.setPos(0,0,7.16)
		player.gmIcon = '2'
		SaveLeGame()
			
	if (message) == '~gmIcon 3' and password == '4322':
		getEmblemSource = loader.loadModel("phase_3.5/models/gui/tt_m_gui_gm_toonResistance_fist.bam")
		getEmblemSource.reparentTo(render)
		getEmblemSource.hide()
		emblem = getEmblemSource.find('**/fistIcon')
		emblem.show()
		emblem.reparentTo(suitC.find('**/joint_nameTag'))
		emblem.setScale(2.5)
		emblem.setBillboardAxis()
		emblem.setZ(14)
		emblemSpin = emblem.hprInterval(3, Vec3(360, 0, 0))
		emblemSpin.loop()
		emblem.setPos(0,0,7.16)
		player.gmIcon = '3'
		SaveLeGame()
		global headspin
		global Sequence2
	
	if (message) == '~gmIcon 0':
		emblem.hide()
		player.gmIcon = '0'
		SaveLeGame()
		
	if (message) == '~collisionsOff' and password == '4322':
		base.localAvatar.physControls.setCollisionsActive(False)
		
	if (message) == '~collisionsOn' and password == '4322':
		base.localAvatar.physControls.setCollisionsActive(True)
		global daisygardens
		global SBHQ
	if (message) == '~SBHQ2DG' and password == '4322':
		SBHQ.remove()
		SBHQ = loader.unloadModel('phase_9/models/cogHQ/SellbotHQExterior.bam')
		sellbotHQ.stop()
		daisygardenspg.play()
		loadedArea = 'daisygardens'
		daisygardens = loader.loadModel('phase_15/hood/daisys_garden.bam')
		daisygardens.reparentTo(render)
		localAvatar.setPosHpr(0.559869, 15.3223, 0.025,0, 0, 0)
		
	if (message) == '~site':
		webbrowser.open('http://www.cog-nation.net')
		
	if (message) == '~forums':
		webbrowser.open('http://cog-nation.net/forums/')
		
	if (message) == '~troll' and password == '4322':
		webbrowser.open('http://trololololololololololo.com/')
		
	if (message) == '~osd':
		onScreenDebug.enabled = True
		
	if (message) == '~osdOff':
		onScreenDebug.enabled = False
	
	if (message) == '~cogv2':
		suitC.find('**/torso').setTexture(waitertorso, 1)
		suitC.find('**/legs').setTexture(waiterlegs, 1)
		suitC.find('**/arms').setTexture(waitersleeve, 1)
		
	if (message) == '~a' and password == '4322':
		suitC.find('**/torso').setTexture(waitertorso, 1)
		suitC.find('**/legs').setTexture(waiterlegs, 1)
		suitC.find('**/arms').setTexture(waitersleeve, 1)
		
		getEmblemSource = loader.loadModel("phase_3.5/models/gui/tt_m_gui_gm_toontroop_getConnected.bam")
		getEmblemSource.reparentTo(render)
		getEmblemSource.hide()
		emblem = getEmblemSource.find('**/whistleIcon')
		emblem.show()
		emblem.reparentTo(suitC.find('**/joint_nameTag'))
		emblem.setScale(2)
		emblem.setZ(1.7)
		emblemSpin = emblem.hprInterval(3, Vec3(360, 0, 0))
		emblemSpin.loop()
		emblem.setPos(0,0,6.7)
		
		walkControls.setWalkSpeed(128.0, 50.0, 40.0, 80.0)
		
	if (message) == '~spin':
		headSpin = head.hprInterval(3, Vec3(360, 0, 0))
		headSpin.loop()
		
	if (message) == '~spinOff':
		headSpinO = head.hprInterval(0, Vec3(0, 0, 0))
		headSpinO.loop()
		
	if (message) == '~bot':
		suitC.copyTo(render)
	
	if (message) == '~num':
		num = random.randint(0, 5)
		print num
		
	if (message) == 'magic':
		suitCHelper.loop('magic1')
		
	if (message) == 'neutral':
		suitCHelper.loop('neutral')
		
	if (message) == 'jump':
		suitCHelper.play('jump-idle')
		
	if (message) == 'hello':
		Chair_chatbubble = loader.loadModel('phase_3/models/props/chatbox.bam')
		Chair_chatbubble.reparentTo(suitCHelper)
		Chair_chatbubble.setPos(0,0,8.5)
		Chair_chatbubble.setBillboardAxis(3)
		Chair_chatbubble.setScale(0.6)
		Chair_chatbubble.find('**/chatBalloon').setPos(0,0.05,0)
		Chair_chatbubble.find('**/chatBalloon').setSx(0.8)
		Chair_talk = OnscreenText(scale=.70,font=loader.loadFont('phase_3/models/fonts/vtRemingtonPortable.ttf'),pos=(0.9,3),text=Chairman1,wordwrap=10,decal=True,parent=Chair_chatbubble,align=TextNode.ALeft)
		Sequence(Wait(5),Func(Chair_chatbubble.removeNode)).start()
	
	if (message) == '~quickSummon Flunky':
		FONT2 = loader.loadFont('phase_3/models/fonts/vtRemingtonPortable.ttf')
		cog = Actor("phase_3.5/models/char/suitC-mod.bam",{
          "walk":"phase_3.5/models/char/suitC-walk.bam",
          "run":"phase_3.5/models/char/suitC-walk.bam",
          "neutral":"phase_3.5/models/char/suitC-neutral.bam",
          "running-jump":"phase_5/models/char/suitC-landing.bam",
          "jump":"phase_5/models/char/suitC-landing.bam"})

		cog.reparentTo(render)
		cog.pose('jump', 10)
		cog.setPosHpr(0, -243.13, 0, 270, 0, 0)
		cog.setScale(1)
		cog.findAllMatches('**/torso').setTexture(bossbot1, 1)
		cog.findAllMatches('**/legs').setTexture(bossbot2, 1)
		cog.findAllMatches('**/arms').setTexture(bossbot3, 1)
		Flunky = loader.loadModel('phase_3.5/models/char/suitC-heads.bam')
		Flunky.reparentTo(cog.find('**/joint_head'))
		Flunky.find('**/coldcaller').hide()
		Flunky.find('**/gladhander').hide()
		Flunky.find('**/micromanager').hide()
		Flunky.find('**/moneybags').hide()
		Flunky.find('**/tightwad').hide()
		cog.find('**/hands').setColor(0.95, 0.75, 0.75, 1.0)
		cogicon = loader.loadModel("phase_3/models/gui/cog_icons.bam").find('**/CorpIcon')
		cogicon.reparentTo(cog.find('**/joint_attachMeter'))
		cogicon.setHpr(180.00, 0, 0)
		cogicon.setScale(.50)
		shadowtex = loader.loadTexture('phase_3/maps/drop-shadow.jpg', 'phase_3/maps/drop-shadow_a.rgb')
		shadowcm = CardMaker('shadow')
		shadowcm.setFrame(2, -2, 2, -2)
		shadow = render.attachNewNode(shadowcm.generate())
		jointshadow1 = cog.find('**/joint_shadow')
		shadow.reparentTo(jointshadow1)
		shadow.setTexture(shadowtex)
		shadow.setP(270)
		shadow.setTransparency(True)
		shadow.setBin('fixed', 40)
		shadow.setColor(1, 1, 1, 0.45)
		jointshadow1.setBin('fixed', 50)
		COG_TN = TextNode('AV_Nametag')
		COG_TN.setText('Flunky\nBossbot\nLevel 82')
		COG_TN.setAlign(TextNode.ACenter)
		COG_TN.setCardColor(0.8, 0.8, 0.8, 0.5)
		COG_TN.setCardAsMargin(0.1, 0, 0, -0.2)
		COG_TN.setCardDecal(True)
		COG_TN.setTextColor(0, 0, 0, 1.0)
		COG_TN.setFont(FONT2)
		textNodePath = render.attachNewNode(COG_TN)
		textNodePath.reparentTo(cog.find('**/joint_nameTag'))
		textNodePath.setBillboardAxis()
		textNodePath.setZ(7.5)
		textNodePath.setScale(.5)
		pos1 = cog.posInterval(5, (24.48, -243.13, 0))
		pos2 = cog.posInterval(5, (59.68, -226.02, 0))
		pos3 = cog.posInterval(5, (82.19, -187.23, 0))
		pos4 = cog.posInterval(5, (55.23, -130.55, 0))
		pos5 = cog.posInterval(5, (6.12, -118.02, 0))
		pos6 = cog.posInterval(5, (-38.19, -126.33, 0))
		pos7 = cog.posInterval(5, (-76.85, -177.61, 0))
		pos8 = cog.posInterval(5, (-63.23, -230.70, 0))
		pos9 = cog.posInterval(5, (0, -243.13, 0))

		hpr1 = cog.hprInterval(5, (270, 0, 0), (270, 0, 0))
		hpr2 = cog.hprInterval(5, (297.76, 0, 0), (297.76, 0, 0))
		hpr3 = cog.hprInterval(5, (330.26, 0, 0), (330.26, 0, 0))
		hpr4 = cog.hprInterval(5, (19.65, 0, 0), (19.65, 0, 0))
		hpr5 = cog.hprInterval(5, (77.28, 0, 0), (77.28, 0, 0))
		hpr6 = cog.hprInterval(5, (98.75, 0, 0), (98.75, 0, 0))
		hpr7 = cog.hprInterval(5, (135.00, 0, 0), (135.00, 0, 0))
		hpr8 = cog.hprInterval(5, (187.59, 0, 0), (187.59, 0, 0))
		hpr9 = cog.hprInterval(5, (238.78, 0, 0), (238.78, 0, 0))
		walkSeq = Sequence(pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9)
		hprSeq = Sequence(hpr1, hpr2, hpr3, hpr4, hpr5, hpr6, hpr7, hpr8, hpr9)
		cog.posInterval(7, (0, -243.13, 0), (0, -243.13, 80)).start()
		def cogSummonz():
			walkSeq.loop()
			hprSeq.loop()
			cog.actorInterval('walk').loop()
		def summonCog():
			CWCW = Sequence()
			CWCW.append(Wait(7))
			CWCW.append(Func(cogSummonz))
			CWCW.start()
		summonCog()
	
	if (message) == '~quickSummon CC':
		FONT2 = loader.loadFont('phase_3/models/fonts/vtRemingtonPortable.ttf')
		cog = Actor("phase_3.5/models/char/suitC-mod.bam",{
          "walk":"phase_3.5/models/char/suitC-walk.bam",
          "run":"phase_3.5/models/char/suitC-walk.bam",
          "neutral":"phase_3.5/models/char/suitC-neutral.bam",
          "running-jump":"phase_5/models/char/suitC-landing.bam",
          "jump":"phase_5/models/char/suitC-landing.bam"})

		cog.reparentTo(render)
		cog.pose('jump', 10)
		cog.setPosHpr(0, -243.13, 0, 270, 0, 0)
		cog.setScale(1)
		cog.findAllMatches('**/torso').setTexture(sellbot1, 1)
		cog.findAllMatches('**/legs').setTexture(sellbot2, 1)
		cog.findAllMatches('**/arms').setTexture(sellbot3, 1)
		ColdCaller = loader.loadModel('phase_3.5/models/char/suitC-heads.bam').find('**/coldcaller')
		ColdCaller.reparentTo(cog.find('**/joint_head'))
		ColdCaller.setColor(0.0941176470588235,0.2313725490196078, 1)
		cog.find('**/hands').setColor(0.5490196078431373,0.6431372549019608,0.9882352941176471)
		cogicon = loader.loadModel("phase_3/models/gui/cog_icons.bam").find('**/SalesIcon')
		cogicon.reparentTo(cog.find('**/joint_attachMeter'))
		cogicon.setHpr(180.00, 0, 0)
		cogicon.setScale(.50)
		shadowtex = loader.loadTexture('phase_3/maps/drop-shadow.jpg', 'phase_3/maps/drop-shadow_a.rgb')
		shadowcm = CardMaker('shadow')
		shadowcm.setFrame(2, -2, 2, -2)
		shadow = render.attachNewNode(shadowcm.generate())
		jointshadow1 = cog.find('**/joint_shadow')
		shadow.reparentTo(jointshadow1)
		shadow.setTexture(shadowtex)
		shadow.setP(270)
		shadow.setTransparency(True)
		shadow.setBin('fixed', 40)
		shadow.setColor(1, 1, 1, 0.45)
		jointshadow1.setBin('fixed', 50)
		COG_TN = TextNode('AV_Nametag')
		COG_TN.setText('Cold Caller\nSellbot\nLevel 3')
		COG_TN.setAlign(TextNode.ACenter)
		COG_TN.setCardColor(0.8, 0.8, 0.8, 0.5)
		COG_TN.setCardAsMargin(0.1, 0, 0, -0.2)
		COG_TN.setCardDecal(True)
		COG_TN.setTextColor(0, 0, 0, 1.0)
		COG_TN.setFont(FONT2)
		textNodePath = render.attachNewNode(COG_TN)
		textNodePath.reparentTo(cog.find('**/joint_nameTag'))
		textNodePath.setBillboardAxis()
		textNodePath.setZ(7)
		textNodePath.setScale(0.35)
		pos1 = cog.posInterval(5, (24.48, -243.13, 0))
		pos2 = cog.posInterval(5, (59.68, -226.02, 0))
		pos3 = cog.posInterval(5, (82.19, -187.23, 0))
		pos4 = cog.posInterval(5, (55.23, -130.55, 0))
		pos5 = cog.posInterval(5, (6.12, -118.02, 0))
		pos6 = cog.posInterval(5, (-38.19, -126.33, 0))
		pos7 = cog.posInterval(5, (-76.85, -177.61, 0))
		pos8 = cog.posInterval(5, (-63.23, -230.70, 0))
		pos9 = cog.posInterval(5, (0, -243.13, 0))

		hpr1 = cog.hprInterval(5, (270, 0, 0), (270, 0, 0))
		hpr2 = cog.hprInterval(5, (297.76, 0, 0), (297.76, 0, 0))
		hpr3 = cog.hprInterval(5, (330.26, 0, 0), (330.26, 0, 0))
		hpr4 = cog.hprInterval(5, (19.65, 0, 0), (19.65, 0, 0))
		hpr5 = cog.hprInterval(5, (77.28, 0, 0), (77.28, 0, 0))
		hpr6 = cog.hprInterval(5, (98.75, 0, 0), (98.75, 0, 0))
		hpr7 = cog.hprInterval(5, (135.00, 0, 0), (135.00, 0, 0))
		hpr8 = cog.hprInterval(5, (187.59, 0, 0), (187.59, 0, 0))
		hpr9 = cog.hprInterval(5, (238.78, 0, 0), (238.78, 0, 0))
		walkSeq = Sequence(pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9)
		hprSeq = Sequence(hpr1, hpr2, hpr3, hpr4, hpr5, hpr6, hpr7, hpr8, hpr9)
		cog.posInterval(7, (0, -243.13, 0), (0, -243.13, 80)).start()
		def cogSummonz():
			walkSeq.loop()
			hprSeq.loop()
			cog.actorInterval('walk').loop()
		def summonCog():
			CWCW = Sequence()
			CWCW.append(Wait(7))
			CWCW.append(Func(cogSummonz))
			CWCW.start()
		summonCog()
	
	if (message) == '~quickSummon TM':
		FONT2 = loader.loadFont('phase_3/models/fonts/vtRemingtonPortable.ttf')
		cog11 = Actor("phase_3.5/models/char/suitB-mod.bam",{
          "walk":"phase_4/models/char/suitB-walk.bam",
          "run":"phase_4/models/char/suitB-walk.bam",
          "neutral":"phase_4/models/char/suitB-neutral.bam",
          "running-jump":"phase_5/models/char/suitB-landing.bam",
          "jump":"phase_5/models/char/suitB-landing.bam"})

		cog11.reparentTo(render)
		cog11.pose('jump', 10)
		cog11.find('**/hands').setColor(Sellbot)
		cog11.setPosHpr(0, -243.13, 0, 270, 0, 0)
		cog11.setScale(.85)
		cog11.findAllMatches('**/torso').setTexture(sellbot1, 1)
		cog11.findAllMatches('**/legs').setTexture(sellbot2, 1)
		cog11.findAllMatches('**/arms').setTexture(sellbot3, 1)
		Telemarketer = loader.loadModel('phase_4/models/char/suitB-heads.bam').find('**/telemarketer')
		Telemarketer.reparentTo(cog11.find('**/joint_head'))
		cogicon = loader.loadModel("phase_3/models/gui/cog_icons.bam").find('**/SalesIcon')
		cogicon.reparentTo(cog11.find('**/joint_attachMeter'))
		cogicon.setHpr(180.00, 0, 0)
		cogicon.setScale(.50)
		shadowtex = loader.loadTexture('phase_3/maps/drop-shadow.jpg', 'phase_3/maps/drop-shadow_a.rgb')
		shadowcm = CardMaker('shadow')
		shadowcm.setFrame(2, -2, 2, -2)
		shadow = render.attachNewNode(shadowcm.generate())
		jointshadow1 = cog11.find('**/joint_shadow')
		shadow.reparentTo(jointshadow1)
		shadow.setTexture(shadowtex)
		shadow.setP(270)
		shadow.setTransparency(True)
		shadow.setBin('fixed', 40)
		shadow.setColor(1, 1, 1, 0.45)
		jointshadow1.setBin('fixed', 50)
		COG_TN = TextNode('AV_Nametag')
		COG_TN.setText('Telemarketer\nSellbot\nLevel 3')
		COG_TN.setAlign(TextNode.ACenter)
		COG_TN.setCardColor(0.8, 0.8, 0.8, 0.5)
		COG_TN.setCardAsMargin(0.1, 0, 0, -0.2)
		COG_TN.setCardDecal(True)
		COG_TN.setTextColor(0, 0, 0, 1.0)
		COG_TN.setFont(FONT2)
		textNodePath = render.attachNewNode(COG_TN)
		textNodePath.reparentTo(cog11.find('**/joint_nameTag'))
		textNodePath.setBillboardAxis()
		textNodePath.setZ(9)
		textNodePath.setScale(0.35)
		pos1 = cog11.posInterval(5, (24.48, -243.13, 0))
		pos2 = cog11.posInterval(5, (59.68, -226.02, 0))
		pos3 = cog11.posInterval(5, (82.19, -187.23, 0))
		pos4 = cog11.posInterval(5, (55.23, -130.55, 0))
		pos5 = cog11.posInterval(5, (6.12, -118.02, 0))
		pos6 = cog11.posInterval(5, (-38.19, -126.33, 0))
		pos7 = cog11.posInterval(5, (-76.85, -177.61, 0))
		pos8 = cog11.posInterval(5, (-63.23, -230.70, 0))
		pos9 = cog11.posInterval(5, (0, -243.13, 0))

		hpr1 = cog11.hprInterval(5, (270, 0, 0), (270, 0, 0))
		hpr2 = cog11.hprInterval(5, (297.76, 0, 0), (297.76, 0, 0))
		hpr3 = cog11.hprInterval(5, (330.26, 0, 0), (330.26, 0, 0))
		hpr4 = cog11.hprInterval(5, (19.65, 0, 0), (19.65, 0, 0))
		hpr5 = cog11.hprInterval(5, (77.28, 0, 0), (77.28, 0, 0))
		hpr6 = cog11.hprInterval(5, (98.75, 0, 0), (98.75, 0, 0))
		hpr7 = cog11.hprInterval(5, (135.00, 0, 0), (135.00, 0, 0))
		hpr8 = cog11.hprInterval(5, (187.59, 0, 0), (187.59, 0, 0))
		hpr9 = cog11.hprInterval(5, (238.78, 0, 0), (238.78, 0, 0))

		walkSeq11 = Sequence(pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9)
		hprSeq11 = Sequence(hpr1, hpr2, hpr3, hpr4, hpr5, hpr6, hpr7, hpr8, hpr9)
		cog11.posInterval(7, (0, -243.13, 0), (0, -243.13, 80)).start()
		def cogSummonz():
			walkSeq11.loop()
			hprSeq11.loop()
			cog11.actorInterval('walk').loop()
		def summonCog():
			CWCW = Sequence()
			CWCW.append(Wait(7))
			CWCW.append(Func(cogSummonz))
			CWCW.start()
		summonCog()
	
	if (message) == '~quickSummon ND':
		FONT2 = loader.loadFont('phase_3/models/fonts/vtRemingtonPortable.ttf')
		cog6 = Actor('phase_3.5/models/char/suitA-mod.bam', 
			{'neutral':'phase_4/models/char/suitA-neutral.bam', 
			'walk':'phase_4/models/char/suitA-walk.bam', 
			'run':'phase_4/models/char/suitA-walk.bam', 
			'jump':'phase_5/models/char/suitA-landing.bam', 
			'running-jump':'phase_5/models/char/suitA-landing.bam'})

		cog6.reparentTo(render)
		cog6.pose('jump', 10)
		cog6.setPosHpr(0, -243.13, 0, 270, 0, 0)
		cog6.setScale(.85)
		cog6.findAllMatches('**/torso').setTexture(sellbot1, 1)
		cog6.findAllMatches('**/legs').setTexture(sellbot2, 1)
		cog6.findAllMatches('**/arms').setTexture(sellbot3, 1)
		cog6.find('**/hands').setColor(Sellbot)
		NameDropper = loader.loadModel('phase_4/models/char/suitA-heads.bam').find('**/numbercruncher')
		NameDropper.reparentTo(cog6.find('**/joint_head'))
		NameDropper.setTexture(nameDropper, 1)
		cogicon = loader.loadModel("phase_3/models/gui/cog_icons.bam").find('**/SalesIcon')
		cogicon.reparentTo(cog6.find('**/joint_attachMeter'))
		cogicon.setHpr(180.00, 0, 0)
		cogicon.setScale(.50)
		shadowtex = loader.loadTexture('phase_3/maps/drop-shadow.jpg', 'phase_3/maps/drop-shadow_a.rgb')
		shadowcm = CardMaker('shadow')
		shadowcm.setFrame(2, -2, 2, -2)
		shadow = render.attachNewNode(shadowcm.generate())
		jointshadow1 = cog6.find('**/joint_shadow')
		shadow.reparentTo(jointshadow1)
		shadow.setTexture(shadowtex)
		shadow.setP(270)
		shadow.setTransparency(True)
		shadow.setBin('fixed', 40)
		shadow.setColor(1, 1, 1, 0.45)
		jointshadow1.setBin('fixed', 50)
		COG_TN = TextNode('AV_Nametag')
		COG_TN.setText('Name Dropper\nSellbot\nLevel 3')
		COG_TN.setAlign(TextNode.ACenter)
		COG_TN.setCardColor(0.8, 0.8, 0.8, 0.5)
		COG_TN.setCardAsMargin(0.1, 0, 0, -0.2)
		COG_TN.setCardDecal(True)
		COG_TN.setTextColor(0, 0, 0, 1.0)
		COG_TN.setFont(FONT2)
		textNodePath = render.attachNewNode(COG_TN)
		textNodePath.reparentTo(cog6.find('**/joint_nameTag'))
		textNodePath.setBillboardAxis()
		textNodePath.setZ(10)
		textNodePath.setScale(0.35)
		pos1 = cog6.posInterval(5, (24.48, -243.13, 0))
		pos2 = cog6.posInterval(5, (59.68, -226.02, 0))
		pos3 = cog6.posInterval(5, (82.19, -187.23, 0))
		pos4 = cog6.posInterval(5, (55.23, -130.55, 0))
		pos5 = cog6.posInterval(5, (6.12, -118.02, 0))
		pos6 = cog6.posInterval(5, (-38.19, -126.33, 0))
		pos7 = cog6.posInterval(5, (-76.85, -177.61, 0))
		pos8 = cog6.posInterval(5, (-63.23, -230.70, 0))
		pos9 = cog6.posInterval(5, (0, -243.13, 0))

		hpr1 = cog6.hprInterval(5, (270, 0, 0), (270, 0, 0))
		hpr2 = cog6.hprInterval(5, (297.76, 0, 0), (297.76, 0, 0))
		hpr3 = cog6.hprInterval(5, (330.26, 0, 0), (330.26, 0, 0))
		hpr4 = cog6.hprInterval(5, (19.65, 0, 0), (19.65, 0, 0))
		hpr5 = cog6.hprInterval(5, (77.28, 0, 0), (77.28, 0, 0))
		hpr6 = cog6.hprInterval(5, (98.75, 0, 0), (98.75, 0, 0))
		hpr7 = cog6.hprInterval(5, (135.00, 0, 0), (135.00, 0, 0))
		hpr8 = cog6.hprInterval(5, (187.59, 0, 0), (187.59, 0, 0))
		hpr9 = cog6.hprInterval(5, (238.78, 0, 0), (238.78, 0, 0))

		walkSeq6 = Sequence(pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9)
		hprSeq6 = Sequence(hpr1, hpr2, hpr3, hpr4, hpr5, hpr6, hpr7, hpr8, hpr9)
		
		cog6.posInterval(7, (0, -243.13, 0), (0, -243.13, 80)).start()
		def cogSummonz():
			walkSeq6.loop()
			hprSeq6.loop()
			cog6.actorInterval('walk').loop()
		def summonCog():
			CWCW = Sequence()
			CWCW.append(Wait(7))
			CWCW.append(Func(cogSummonz))
			CWCW.start()
		summonCog()
	
	if (message) == '~quickSummon GH':
		FONT2 = loader.loadFont('phase_3/models/fonts/vtRemingtonPortable.ttf')
		cog3 = Actor("phase_3.5/models/char/suitC-mod.bam",{
          "walk":"phase_3.5/models/char/suitC-walk.bam",
          "run":"phase_3.5/models/char/suitC-walk.bam",
          "neutral":"phase_3.5/models/char/suitC-neutral.bam",
          "running-jump":"phase_5/models/char/suitC-landing.bam",
          "jump":"phase_5/models/char/suitC-landing.bam"})

		cog3.reparentTo(render)
		cog3.pose('jump', 10)
		cog3.setPosHpr(0, -243.13, 0, 270, 0, 0)
		cog3.find('**/hands').setColor(Sellbot)
		cog3.setScale(1.20)
		cog3.findAllMatches('**/torso').setTexture(sellbot1, 1)
		cog3.findAllMatches('**/legs').setTexture(sellbot2, 1)
		cog3.findAllMatches('**/arms').setTexture(sellbot3, 1)
		GladHander = loader.loadModel('phase_3.5/models/char/suitC-heads.bam').find('**/gladhander')
		GladHander.reparentTo(cog3.find('**/joint_head'))
		cogicon = loader.loadModel("phase_3/models/gui/cog_icons.bam").find('**/SalesIcon')
		cogicon.reparentTo(cog3.find('**/joint_attachMeter'))
		cogicon.setHpr(180.00, 0, 0)
		cogicon.setScale(.50)
		shadowtex = loader.loadTexture('phase_3/maps/drop-shadow.jpg', 'phase_3/maps/drop-shadow_a.rgb')
		shadowcm = CardMaker('shadow')
		shadowcm.setFrame(2, -2, 2, -2)
		shadow = render.attachNewNode(shadowcm.generate())
		jointshadow1 = cog3.find('**/joint_shadow')
		shadow.reparentTo(jointshadow1)
		shadow.setTexture(shadowtex)
		shadow.setP(270)
		shadow.setTransparency(True)
		shadow.setBin('fixed', 40)
		shadow.setColor(1, 1, 1, 0.45)
		jointshadow1.setBin('fixed', 50)
		COG_TN = TextNode('AV_Nametag')
		COG_TN.setText('Glad Hander\nSellbot\nLevel 4')
		COG_TN.setAlign(TextNode.ACenter)
		COG_TN.setCardColor(0.8, 0.8, 0.8, 0.5)
		COG_TN.setCardAsMargin(0.1, 0, 0, -0.2)
		COG_TN.setCardDecal(True)
		COG_TN.setTextColor(0, 0, 0, 1.0)
		COG_TN.setFont(FONT2)
		textNodePath = render.attachNewNode(COG_TN)
		textNodePath.reparentTo(cog3.find('**/joint_nameTag'))
		textNodePath.setBillboardAxis()
		textNodePath.setZ(7)
		textNodePath.setScale(0.35)

		pos1 = cog3.posInterval(5, (24.48, -243.13, 0))
		pos2 = cog3.posInterval(5, (59.68, -226.02, 0))
		pos3 = cog3.posInterval(5, (82.19, -187.23, 0))
		pos4 = cog3.posInterval(5, (55.23, -130.55, 0))
		pos5 = cog3.posInterval(5, (6.12, -118.02, 0))
		pos6 = cog3.posInterval(5, (-38.19, -126.33, 0))
		pos7 = cog3.posInterval(5, (-76.85, -177.61, 0))
		pos8 = cog3.posInterval(5, (-63.23, -230.70, 0))
		pos9 = cog3.posInterval(5, (0, -243.13, 0))

		hpr1 = cog3.hprInterval(5, (270, 0, 0), (270, 0, 0))
		hpr2 = cog3.hprInterval(5, (297.76, 0, 0), (297.76, 0, 0))
		hpr3 = cog3.hprInterval(5, (330.26, 0, 0), (330.26, 0, 0))
		hpr4 = cog3.hprInterval(5, (19.65, 0, 0), (19.65, 0, 0))
		hpr5 = cog3.hprInterval(5, (77.28, 0, 0), (77.28, 0, 0))
		hpr6 = cog3.hprInterval(5, (98.75, 0, 0), (98.75, 0, 0))
		hpr7 = cog3.hprInterval(5, (135.00, 0, 0), (135.00, 0, 0))
		hpr8 = cog3.hprInterval(5, (187.59, 0, 0), (187.59, 0, 0))
		hpr9 = cog3.hprInterval(5, (238.78, 0, 0), (238.78, 0, 0))

		walkSeq3 = Sequence(pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9)
		hprSeq3 = Sequence(hpr1, hpr2, hpr3, hpr4, hpr5, hpr6, hpr7, hpr8, hpr9)
		cog3.posInterval(7, (0, -243.13, 0), (0, -243.13, 80)).start()
		def cogSummonz():
			walkSeq3.loop()
			hprSeq3.loop()
			cog3.actorInterval('walk').loop()
		def summonCog():
			CWCW = Sequence()
			CWCW.append(Wait(7))
			CWCW.append(Func(cogSummonz))
			CWCW.start()
		summonCog()
	
	if (message) == '~quickSummon MS':
		FONT2 = loader.loadFont('phase_3/models/fonts/vtRemingtonPortable.ttf')
		cog9 = Actor("phase_3.5/models/char/suitB-mod.bam",{
          "walk":"phase_4/models/char/suitB-walk.bam",
          "run":"phase_4/models/char/suitB-walk.bam",
          "neutral":"phase_4/models/char/suitB-neutral.bam",
          "running-jump":"phase_5/models/char/suitB-landing.bam",
          "jump":"phase_5/models/char/suitB-landing.bam"})

		cog9.reparentTo(render)
		cog9.pose('jump', 10)
		cog9.find('**/hands').setColor(Sellbot)
		cog9.setPosHpr(0, -243.13, 0, 270, 0, 0)
		cog9.setScale(1.08)
		cog9.findAllMatches('**/torso').setTexture(sellbot1, 1)
		cog9.findAllMatches('**/legs').setTexture(sellbot2, 1)
		cog9.findAllMatches('**/arms').setTexture(sellbot3, 1)
		MoverShaker = loader.loadModel('phase_4/models/char/suitB-heads.bam').find('**/movershaker')
		MoverShaker.reparentTo(cog9.find('**/joint_head'))
		cogicon = loader.loadModel("phase_3/models/gui/cog_icons.bam").find('**/SalesIcon')
		cogicon.reparentTo(cog9.find('**/joint_attachMeter'))
		cogicon.setHpr(180.00, 0, 0)
		cogicon.setScale(.50)
		shadowtex = loader.loadTexture('phase_3/maps/drop-shadow.jpg', 'phase_3/maps/drop-shadow_a.rgb')
		shadowcm = CardMaker('shadow')
		shadowcm.setFrame(2, -2, 2, -2)
		shadow = render.attachNewNode(shadowcm.generate())
		jointshadow1 = cog9.find('**/joint_shadow')
		shadow.reparentTo(jointshadow1)
		shadow.setTexture(shadowtex)
		shadow.setP(270)
		shadow.setTransparency(True)
		shadow.setBin('fixed', 40)
		shadow.setColor(1, 1, 1, 0.45)
		jointshadow1.setBin('fixed', 50)
		COG_TN = TextNode('AV_Nametag')
		COG_TN.setText('Mover&Shaker\nSellbot\nLevel 5')
		COG_TN.setAlign(TextNode.ACenter)
		COG_TN.setCardColor(0.8, 0.8, 0.8, 0.5)
		COG_TN.setCardAsMargin(0.1, 0, 0, -0.2)
		COG_TN.setCardDecal(True)
		COG_TN.setTextColor(0, 0, 0, 1.0)
		COG_TN.setFont(FONT2)
		textNodePath = render.attachNewNode(COG_TN)
		textNodePath.reparentTo(cog9.find('**/joint_nameTag'))
		textNodePath.setBillboardAxis()
		textNodePath.setZ(9)
		textNodePath.setScale(0.35)
		pos1 = cog9.posInterval(5, (24.48, -243.13, 0))
		pos2 = cog9.posInterval(5, (59.68, -226.02, 0))
		pos3 = cog9.posInterval(5, (82.19, -187.23, 0))
		pos4 = cog9.posInterval(5, (55.23, -130.55, 0))
		pos5 = cog9.posInterval(5, (6.12, -118.02, 0))
		pos6 = cog9.posInterval(5, (-38.19, -126.33, 0))
		pos7 = cog9.posInterval(5, (-76.85, -177.61, 0))
		pos8 = cog9.posInterval(5, (-63.23, -230.70, 0))
		pos9 = cog9.posInterval(5, (0, -243.13, 0))

		hpr1 = cog9.hprInterval(5, (270, 0, 0), (270, 0, 0))
		hpr2 = cog9.hprInterval(5, (297.76, 0, 0), (297.76, 0, 0))
		hpr3 = cog9.hprInterval(5, (330.26, 0, 0), (330.26, 0, 0))
		hpr4 = cog9.hprInterval(5, (19.65, 0, 0), (19.65, 0, 0))
		hpr5 = cog9.hprInterval(5, (77.28, 0, 0), (77.28, 0, 0))
		hpr6 = cog9.hprInterval(5, (98.75, 0, 0), (98.75, 0, 0))
		hpr7 = cog9.hprInterval(5, (135.00, 0, 0), (135.00, 0, 0))
		hpr8 = cog9.hprInterval(5, (187.59, 0, 0), (187.59, 0, 0))
		hpr9 = cog9.hprInterval(5, (238.78, 0, 0), (238.78, 0, 0))

		walkSeq9 = Sequence(pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9)
		hprSeq9 = Sequence(hpr1, hpr2, hpr3, hpr4, hpr5, hpr6, hpr7, hpr8, hpr9)
		
		cog9.posInterval(7, (0, -243.13, 0), (0, -243.13, 80)).start()
		def cogSummonz():
			walkSeq9.loop()
			hprSeq9.loop()
			cog9.actorInterval('walk').loop()
		def summonCog():
			CWCW = Sequence()
			CWCW.append(Wait(7))
			CWCW.append(Func(cogSummonz))
			CWCW.start()
		summonCog()
	
	if (message) == '~quickSummon TF':
		FONT2 = loader.loadFont('phase_3/models/fonts/vtRemingtonPortable.ttf')
		cog = Actor('phase_3.5/models/char/suitA-mod.bam', 
			{'neutral':'phase_4/models/char/suitA-neutral.bam', 
			'walk':'phase_4/models/char/suitA-walk.bam', 
			'run':'phase_4/models/char/suitA-walk.bam', 
			'jump':'phase_5/models/char/suitA-landing.bam', 
			'running-jump':'phase_5/models/char/suitA-landing.bam'})

		cog.reparentTo(render)
		cog.pose('jump', 10)
		cog.find('**/hands').setColor(Sellbot)
		cog.setPosHpr(0, -243.13, 0, 270, 0, 0)
		cog.setScale(1.15)
		cog.findAllMatches('**/torso').setTexture(sellbot1, 1)
		cog.findAllMatches('**/legs').setTexture(sellbot2, 1)
		cog.findAllMatches('**/arms').setTexture(sellbot3, 1)
		TwoFace = loader.loadModel('phase_4/models/char/suitA-heads.bam').find('**/twoface')
		TwoFace.reparentTo(cog.find('**/joint_head'))
		cogicon = loader.loadModel("phase_3/models/gui/cog_icons.bam").find('**/SalesIcon')
		cogicon.reparentTo(cog.find('**/joint_attachMeter'))
		cogicon.setHpr(180.00, 0, 0)
		cogicon.setScale(.50)
		shadowtex = loader.loadTexture('phase_3/maps/drop-shadow.jpg', 'phase_3/maps/drop-shadow_a.rgb')
		shadowcm = CardMaker('shadow')
		shadowcm.setFrame(2, -2, 2, -2)
		shadow = render.attachNewNode(shadowcm.generate())
		jointshadow1 = cog.find('**/joint_shadow')
		shadow.reparentTo(jointshadow1)
		shadow.setTexture(shadowtex)
		shadow.setP(270)
		shadow.setTransparency(True)
		shadow.setBin('fixed', 40)
		shadow.setColor(1, 1, 1, 0.45)
		jointshadow1.setBin('fixed', 50)
		COG_TN = TextNode('AV_Nametag')
		COG_TN.setText('Two-Face\nSellbot\nLevel 6')
		COG_TN.setAlign(TextNode.ACenter)
		COG_TN.setCardColor(0.8, 0.8, 0.8, 0.5)
		COG_TN.setCardAsMargin(0.1, 0, 0, -0.2)
		COG_TN.setCardDecal(True)
		COG_TN.setTextColor(0, 0, 0, 1.0)
		COG_TN.setFont(FONT2)
		textNodePath = render.attachNewNode(COG_TN)
		textNodePath.reparentTo(cog.find('**/joint_nameTag'))
		textNodePath.setBillboardAxis()
		textNodePath.setZ(9)
		textNodePath.setScale(0.35)
		pos1 = cog.posInterval(5, (24.48, -243.13, 0))
		pos2 = cog.posInterval(5, (59.68, -226.02, 0))
		pos3 = cog.posInterval(5, (82.19, -187.23, 0))
		pos4 = cog.posInterval(5, (55.23, -130.55, 0))
		pos5 = cog.posInterval(5, (6.12, -118.02, 0))
		pos6 = cog.posInterval(5, (-38.19, -126.33, 0))
		pos7 = cog.posInterval(5, (-76.85, -177.61, 0))
		pos8 = cog.posInterval(5, (-63.23, -230.70, 0))
		pos9 = cog.posInterval(5, (0, -243.13, 0))

		hpr1 = cog.hprInterval(5, (270, 0, 0), (270, 0, 0))
		hpr2 = cog.hprInterval(5, (297.76, 0, 0), (297.76, 0, 0))
		hpr3 = cog.hprInterval(5, (330.26, 0, 0), (330.26, 0, 0))
		hpr4 = cog.hprInterval(5, (19.65, 0, 0), (19.65, 0, 0))
		hpr5 = cog.hprInterval(5, (77.28, 0, 0), (77.28, 0, 0))
		hpr6 = cog.hprInterval(5, (98.75, 0, 0), (98.75, 0, 0))
		hpr7 = cog.hprInterval(5, (135.00, 0, 0), (135.00, 0, 0))
		hpr8 = cog.hprInterval(5, (187.59, 0, 0), (187.59, 0, 0))
		hpr9 = cog.hprInterval(5, (238.78, 0, 0), (238.78, 0, 0))
		walkSeq = Sequence(pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9)
		hprSeq = Sequence(hpr1, hpr2, hpr3, hpr4, hpr5, hpr6, hpr7, hpr8, hpr9)
		cog.posInterval(7, (0, -243.13, 0), (0, -243.13, 80)).start()
		def cogSummonz():
			walkSeq.loop()
			hprSeq.loop()
			cog.actorInterval('walk').loop()
		def summonCog():
			CWCW = Sequence()
			CWCW.append(Wait(7))
			CWCW.append(Func(cogSummonz))
			CWCW.start()
		summonCog()
		
	if (message) == '~oobe':
		base.oobe()
		
	if (message) == '~camHide':
		base.camera.hide()
	
	if (message) == '~camShow':
		base.camera.show() 
	
	if (message) == '~TP DG':
		if loadedArea == 'sbhq':
			RunScreen()
			SBHQ.remove()
			SBHQ = loader.unloadModel('phase_9/models/cogHQ/SellbotHQExterior.bam')
			vtwocog.hide()
			vtwocog2.hide()
			loadedArea = 'daisygardens'
			daisygardens = loader.loadModel('phase_15/hood/daisys_garden.bam')
			daisygardens.reparentTo(render)
			localAvatar.setPosHpr(0.559869, 15.3223, 0.025,0, 0, 0)
			loadingtext['text'] = "Loading Daisy's Garden. . ."

        try:
            self.setTalk(message)
            if len(message) <= 4:
                if '?' in message:
                    self.toonSound(self.toonSpecies,'question.mp3')
                elif 'ooo' in message:
                    self.toonSound(self.toonSpecies,'murmur.mp3')
                elif '!' in message:
                    self.toonSound(self.toonSpecies,'exclaim.mp3')
                else:
                    self.toonSound(self.toonSpecies,'grunt.mp3')
 
            elif len(message) >= 5 and len(message) <=9:
                if '?' in message:
                    self.toonSound(self.toonSpecies,'question.mp3')
                elif 'ooo' in message:
                    self.toonSound(self.toonSpecies,'murmur.mp3')
                elif '!' in message:
                    self.toonSound(self.toonSpecies,'statement.mp3')
                else:
                    self.toonSound(self.toonSpecies,'statement.mp3')
 
            elif len(message) >= 10:
                if '?' in message:
                    self.toonSound(self.toonSpecies,'question.mp3')
                elif 'ooo' in message:
                    self.toonSound(self.toonSpecies,'murmur.mp3')
                elif '!' in message:
                    self.toonSound(self.toonSpecies,'statement.mp3')
                else:
                    self.toonSound(self.toonSpecies,'statement.mp3')
				
			
        except Exception, e:print e#base.localAvatar.ToonTAGS.setName('a')
        
    def setName(self, name):
        if hasattr(self, 'tag'):
            self.tag.removeNode()
        self.tag = OnscreenText(scale=0.35,font=loader.loadFont('phase_3/models/fonts/vtRemingtonPortable.ttf'),pos=(0,6.5),text=name,bg=(0.8, 0.8, 0.8, 0.5),fg=(0, 0, 0, 1.0),wordwrap=7,decal=True,parent=suitC.find('**/joint_nameTag'))
        self.tag.setBillboardAxis()
        self.tag.setPos(0,7.5)
        if len(name) > 11:
			self.tag.setPos(0,8.0)
			
        
 
    def __init__(self):
        self.setName('')
class ClassicChatBox(CogTags):
 
    ChatBox = loader.loadModel("phase_3.5/models/gui/chat_input_gui.bam")
    SlipOpen = loader.loadSfx("phase_3.5/audio/sfx/GUI_quicktalker.mp3")
 
    def __setNone__(self):
 
        text = self.OldChatBoxEntry['text']
        self.OldChatBoxEntry.set(text)
 
        return True
 
    def __action__(self, message):
 
        self.OldChatBoxGui.removeNode()
        self.OldChatBoxEntry.removeNode()
        self.OldChatBoxClose.removeNode()
        self.OldChatBoxTalk.removeNode()
 
        self.__addOnButton__()
 
        if message != '':
            base.localAvatar.CogTags.sendChat(message)
        else:return None
 
        return True
 
    def __delNavs__(self):
 
        self.OldChatBoxGui.removeNode()
        self.OldChatBoxEntry.removeNode()
        self.OldChatBoxClose.removeNode()
        self.OldChatBoxTalk.removeNode()
 
        self.__addOnButton__()
 
        return True
 
    def __sayIt__(self):
 
        self.OldChatBoxGui.removeNode()
        self.OldChatBoxEntry.removeNode()
        self.OldChatBoxClose.removeNode()
        self.OldChatBoxTalk.removeNode()
 
        self.__addOnButton__()
 
        base.localAvatar.CogTags.sendChat(self.OldChatBoxEntry.get(1.0))
 
        return True
 
    def __addNavs__(self):
 
        self.OldChatBoxOpen.removeNode()
        self.OldChatBoxGui = DirectFrame(pos=(-1.083, 0, 0.804), scale=1, frameSize=(0,0,0,0), image=self.ChatBox.find("**/Chat_Bx_FNL"))
        
        self.OldChatBoxEntry = DirectEntry(text = "", \
        scale=.04, \
        command=self.__action__, \
        frameSize = (-.0, 32.6, 1, -0.5), \
        frameColor=(0,0,0,0), \
        cursorKeys = 1, \
        initialText = '', \
        numLines = 3, \
        width = 7.8,  \
        focus=1, \
        text_scale=1.5, \
        pos = (-1.293, 0, 0.904))
    
        self.OldChatBoxClose = DirectButton(frameSize=None, \
        image=(self.ChatBox.find('**/CloseBtn_UP'), \
        self.ChatBox.find('**/CloseBtn_DN'), \
        self.ChatBox.find('**/CloseBtn_Rllvr')), \
        relief=None, \
        command=self.__delNavs__, \
        text = ("", "Cancel", "Cancel", "Cancel"), \
        text_pos=(0, -0.09), \
        geom=None, \
        scale=1.1, \
        pad=(0.01, 0.01), \
        suppressKeys=0, \
        pos = (-1.233, 0, 0.713), \
        hpr = (0,0,0), \
        text_scale=0.05, \
        borderWidth=(0.015, 0.01))
 
        self.OldChatBoxTalk = DirectButton(frameSize=None, \
        image=(self.ChatBox.find('**/ChtBx_ChtBtn_UP'), \
        self.ChatBox.find('**/ChtBx_ChtBtn_DN'), \
        self.ChatBox.find('**/ChtBx_ChtBtn_RLVR')), \
        relief=None, \
        command=self.__sayIt__, \
        text = ("", "Say It", "Say It", "Say It"), \
        text_pos=(0, -0.09), \
        geom=None, \
        scale=1.1, \
        pad=(0.01, 0.01), \
        suppressKeys=0, \
        pos = (-0.903, 0, 0.713), \
        hpr = (0,0,0), \
        text_scale=0.05, \
        borderWidth=(0.015, 0.01))
 
        return True
 
    def __addOnButton__(self):
 
        self.OldChatBoxOpen = DirectButton(frameSize=None, \
        image=(self.ChatBox.find('**/ChtBx_ChtBtn_UP'), \
        self.ChatBox.find('**/ChtBx_ChtBtn_DN'), \
        self.ChatBox.find('**/ChtBx_ChtBtn_RLVR')), \
        command=self.__addNavs__, \
        relief=None, \
        text = ("", "Chat", "Chat", "Chat"), \
        text_pos=(0, -0.09), \
        clickSound=self.SlipOpen, \
        geom=None, \
        scale=1.2, \
        pad=(0.01, 0.01), \
        suppressKeys=0, \
        pos = (-0.99,0,0.928), \
        hpr = (0,0,0), \
        text_scale=0.059999999999999998, \
        borderWidth=(0.015, 0.01))
 
        return True
 
    def __init__(self):
 
        self.__addOnButton__()
 
base.localAvatar.CogTags = CogTags()
base.localAvatar.ClassicChatBox = ClassicChatBox()


	
