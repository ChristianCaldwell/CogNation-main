from direct.directbase import DirectStart
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from panda3d.core import PandaNode,NodePath,Camera,TextNode
from direct.actor.Actor import Actor
from direct.showbase.ShowBase import ShowBase
from cognation.main.cogbase.CogNationTex import *

suitA = Actor("phase_3.5/models/char/suitA-mod.bam",{
          "walk":"phase_4/models/char/suitA-walk.bam",
          "run":"phase_4/models/char/suitA-walk.bam",
          "neutral":"phase_4/models/char/suitA-neutral.bam",
          "running-jump":"phase_5/models/char/suitA-landing.bam",
          "jump":"phase_5/models/char/suitA-landing.bam"
 })
suitA.reparentTo(render)
suitA.loop('neutral')
shadowtex = loader.loadTexture('phase_3/maps/drop-shadow.jpg', 'phase_3/maps/drop-shadow_a.rgb')
shadowcm = CardMaker('shadow')
shadowcm.setFrame(2, -2, 2, -2)
shadow1 = render.attachNewNode(shadowcm.generate())
jointshadow1 = suitA.find('**/joint_shadow')
shadow1.reparentTo(jointshadow1)
shadow1.setTexture(shadowtex)
shadow1.setP(270)
shadow1.setTransparency(True)
shadow1.setBin('fixed', 40)
shadow1.setColor(1, 1, 1, 0.45)
jointshadow1.setBin('fixed', 50)
suitA.hide()
suitB = Actor("phase_3.5/models/char/suitB-mod.bam",{
          "walk":"phase_4/models/char/suitB-walk.bam",
          "run":"phase_4/models/char/suitB-walk.bam",
          "neutral":"phase_4/models/char/suitB-neutral.bam",
          "running-jump":"phase_5/models/char/suitB-landing.bam",
          "jump":"phase_5/models/char/suitB-landing.bam"
 })
suitB.reparentTo(render)
suitB.loop('neutral')
shadow2 = render.attachNewNode(shadowcm.generate())
jointshadow2 = suitB.find('**/joint_shadow')
shadow2.reparentTo(jointshadow2)
shadow2.setTexture(shadowtex)
shadow2.setP(270)
shadow2.setTransparency(True)
shadow2.setBin('fixed', 40)
shadow2.setColor(1, 1, 1, 0.45)
jointshadow2.setBin('fixed', 50)
suitB.hide()
suitC = Actor("phase_3.5/models/char/suitC-mod.bam",{
          "walk":"phase_3.5/models/char/suitC-walk.bam",
          "run":"phase_3.5/models/char/suitC-walk.bam",
          "neutral":"phase_3.5/models/char/suitC-neutral.bam",
          "running-jump":"phase_5/models/char/suitC-landing.bam",
          "jump":"phase_5/models/char/suitC-landing.bam"
 })
suitC.reparentTo(render)
suitC.loop('neutral')
shadow3 = render.attachNewNode(shadowcm.generate())
jointshadow3 = suitC.find('**/joint_shadow')
shadow3.reparentTo(jointshadow3)
shadow3.setTexture(shadowtex)
shadow3.setP(270)
shadow3.setTransparency(True)
shadow3.setBin('fixed', 40)
shadow3.setColor(1, 1, 1, 0.45)
jointshadow3.setBin('fixed', 50)
suitC.hide()
cogplayer = suitC
localAvatar = cogplayer
base.localAvatar = localAvatar
