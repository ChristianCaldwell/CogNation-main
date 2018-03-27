from pandac.PandaModules import *
from direct.actor.Actor import Actor
from direct.directbase import DirectStart
from direct.task import Task
from direct.actor.Actor import Actor
from direct.gui.DirectGui import *
from direct.interval.IntervalGlobal import *
from direct.showbase.InputStateGlobal import inputState
from direct.controls.GravityWalker import GravityWalker
from direct.gui.OnscreenText import OnscreenText
from CogTypes import *

geom = suitA.getGeomNode()
geom.getChild(0).setSx(0.930000019073)
geom.getChild(0).setSz(0.930000019073)

geom2 = suitB.getGeomNode()
geom2.getChild(0).setSx(0.930000019073)
geom2.getChild(0).setSz(0.930000019073)

geom3 = suitC.getGeomNode()
geom3.getChild(0).setSx(0.930000019073)
geom3.getChild(0).setSz(0.930000019073)

offset = 3.2375

wallBitmask = BitMask32(1)
floorBitmask = BitMask32(2)
base.cTrav = CollisionTraverser()
def getAirborneHeight():
	return offset + 0.025000000000000001

wallBitmask = BitMask32(1)
floorBitmask = BitMask32(2)
base.cTrav = CollisionTraverser()
def getAirborneHeight():
    return offset + 0.025000000000000001

walkControls = GravityWalker(legacyLifter=True)
walkControls.setWallBitMask(wallBitmask)
walkControls.setFloorBitMask(floorBitmask)
walkControls.initializeCollisions(base.cTrav, suitC, floorOffset=0.025, reach=4.0)
walkControls.setAirborneHeightFunc(getAirborneHeight)
walkControls.setWalkSpeed(32.0, 28.0, 16.0, 80.0)
#walkControls.enableAvatarControls()
suitC.physControls = walkControls

def setWatchKey(key, input, keyMapName):
	def watchKey(active=True):
		if active == True:
			inputState.set(input, True)
			keyMap[keyMapName] = 1
		else:
			inputState.set(input, False)
			keyMap[keyMapName] = 0
	base.accept(key, watchKey, [True])
	base.accept(key+'-up', watchKey, [False])
	  
		
keyMap = {'left':0, 'right':0, 'forward':0, 'backward':0, 'control':0}


setWatchKey('arrow_up', 'forward', 'forward')
setWatchKey('control-arrow_up', 'forward', 'forward')
setWatchKey('alt-arrow_up', 'forward', 'forward')
setWatchKey('shift-arrow_up', 'forward', 'forward')
setWatchKey('arrow_down', 'reverse', 'backward')
setWatchKey('control-arrow_down', 'reverse', 'backward')
setWatchKey('alt-arrow_down', 'reverse', 'backward')
setWatchKey('shift-arrow_down', 'reverse', 'backward')
setWatchKey('arrow_left', 'turnLeft', 'left')
setWatchKey('control-arrow_left', 'turnLeft', 'left')
setWatchKey('alt-arrow_left', 'turnLeft', 'left')
setWatchKey('shift-arrow_left', 'turnLeft', 'left')
setWatchKey('arrow_right', 'turnRight', 'right')
setWatchKey('control-arrow_right', 'turnRight', 'right')
setWatchKey('alt-arrow_right', 'turnRight', 'right')
setWatchKey('shift-arrow_right', 'turnRight', 'right')
setWatchKey('control', 'jump', 'control')

movingNeutral, movingForward = (False, False)
movingRotation, movingBackward = (False, False)
movingJumping = False

def setMovementAnimation(loopName, playRate=1.0):
	global movingNeutral
	global movingForward
	global movingRotation
	global movingBackward
	global movingJumping
	if 'jump' in loopName:
		movingJumping = True
		movingForward = False
		movingNeutral = False
		movingRotation = False
		movingBackward = False
	elif loopName == 'run':
		movingJumping = False
		movingForward = True
		movingNeutral = False
		movingRotation = False
		movingBackward = False
	elif loopName == 'walk':
		movingJumping = False
		movingForward = False
		movingNeutral = False
		if playRate == -1.0:
			movingBackward = True
			movingRotation = False
		else:
			movingBackward = False
			movingRotation = True
	elif loopName == 'neutral':
		movingJumping = False
		movingForward = False
		movingNeutral = True
		movingRotation = False
		movingBackward = False
	else:
		movingJumping = False
		movingForward = False
		movingNeutral = False
		movingRotation = False
		movingBackward = False
	ActorInterval(suitC, loopName, playRate=playRate).loop()
	
def handleMovement(task):
	global movingNeutral, movingForward
	global movingRotation, movingBackward, movingJumping
	if keyMap['control'] == 1:
		if keyMap['forward'] or keyMap['backward'] or keyMap['left'] or keyMap['right']:
			if movingJumping == False:
				if suitC.physControls.isAirborne:
					setMovementAnimation('running-jump')
				else:
					if keyMap['forward']:
						if movingForward == False:
							setMovementAnimation('run')
					elif keyMap['backward']:
						if movingBackward == False:
							setMovementAnimation('walk', playRate=-1.0)
					elif keyMap['left'] or keyMap['right']:
						if movingRotation == False:
							setMovementAnimation('walk')
			else:
				if not suitC.physControls.isAirborne:
					if keyMap['forward']:
						if movingForward == False:
							setMovementAnimation('run')
					elif keyMap['backward']:
						if movingBackward == False:
							setMovementAnimation('walk', playRate=-1.0)
					elif keyMap['left'] or keyMap['right']:
						if movingRotation == False:
							setMovementAnimation('walk')
		else:
			if movingJumping == False:
				if suitC.physControls.isAirborne:
					setMovementAnimation('jump')
				else:
					if movingNeutral == False:
						setMovementAnimation('neutral')
			else:
				if not suitC.physControls.isAirborne:
					if movingNeutral == False:
						setMovementAnimation('neutral')
	elif keyMap['forward'] == 1:
		if movingForward == False:
			if not suitC.physControls.isAirborne:
				setMovementAnimation('run')
	elif keyMap['backward'] == 1:
		if movingBackward == False:
			if not suitC.physControls.isAirborne:
				setMovementAnimation('walk', playRate=-1.0)
	elif keyMap['left'] or keyMap['right']:
		if movingRotation == False:
			if not suitC.physControls.isAirborne:
				setMovementAnimation('walk')
	else:
		if not suitC.physControls.isAirborne:
			if movingNeutral == False:
				setMovementAnimation('neutral')
	return Task.cont
#base.taskMgr.add(handleMovement, 'controlManager')

def collisionsOn():
	walkControls.setCollisionsActive(True)
	walkControls.isAirborne = True
	mainWalker.setCollisionsActive(True)
	mainWalker.isAirborne = True

def collisionsOff():
	walkControls.setCollisionsActive(False)
	walkControls.isAirborne = True
	mainWalker.setCollisionsActive(False)
	mainWalker.isAirborne = True


