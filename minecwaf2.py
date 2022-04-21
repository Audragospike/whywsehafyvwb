from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

x, y, z = mc.player.getTilePos()

while True:
    z += 1
    mc.player.setTilePos(x, y, z)
    time.sleep(0.1)
    