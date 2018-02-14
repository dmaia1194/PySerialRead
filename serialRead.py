from time import sleep
import sys
import os
import keyboard
import serial

system = sys.argv[1]
emulator = sys.argv[2]
path = sys.argv[3]

arcade_path = '/home/arcade/RetroPie/roms/arcade'
megadrive_path = '/home/arcade/RetroPie/roms/n64'

arduino = serial.Serial('/dev/ttyACM0', 115200)

setColors = '00'
if system == 'arcade':
	exitBtn = 'shift+enter'

	# A = vermelho
	# B = vermelho | amarelo
	# C = vermelho | amarelo | verde
	# D = vermelho | amarelo | verde | azul
	# E = vermelho | amarelo | azul (2x)
	# F = amarelo | vermelho | verde
	# G = amarelo | vermelho | verde | azul
	# H = verde | vermelho | amarelo
	# Z = sem cor

	if path == '%s/aerofgt.zip' % (arcade_path):
		setColors = '2b'
	if path == '%s/aliens3.zip' % (arcade_path):
		setColors = '2b'
	if path == '%s/alpham2.zip' % (arcade_path):
		setColors = '2c'
	if path == '%s/alphamis.zip' % (arcade_path):
		setColors = '2c'
	if path == '%s/aof.zip' % (arcade_path):
		setColors = '2d'
	if path == '%s/aof2.zip' % (arcade_path):
		setColors = '2d'
	if path == '%s/aof3.zip' % (arcade_path):
		setColors = '2d'
	if path == '%s/aoh.zip' % (arcade_path):
		setColors = '2d'
	if path == '%s/armwaru.zip' % (arcade_path):
		setColors = '3c'
	if path == '%s/avsp.zip' % (arcade_path):
		setColors = '3c'

	if path == '%s/batman.zip' % (arcade_path):
		setColors = '1b'
	if path == '%s/bbmanwj.zip' % (arcade_path):
		setColors = '4b'
	if path == '%s/bionicc2.zip' % (arcade_path):
		setColors = '2b'
	if path == '%s/bldyroar.zip' % (arcade_path):
		setColors = '2c'
	if path == '%s/bldyror2u.zip' % (arcade_path):
		setColors = '2d'
	if path == '%s/bmaster.zip' % (arcade_path):
		setColors = '2b'
	if path == '%s/bombrman.zip' % (arcade_path):
		setColors = '2b'
	if path == '%s/btoads.zip' % (arcade_path):
		setColors = '3b'

	if path == '%s/captavenu.zip' % (arcade_path):
		setColors = '4b'
	if path == '%s/captcomm.zip' % (arcade_path):
		setColors = '4b'
	if path == '%s/choplift.zip' % (arcade_path):
		setColors = '2b'
	if path == '%s/chopperb.zip' % (arcade_path):
		setColors = '2b'
	if path == '%s/ckong.zip' % (arcade_path):
		setColors = '2a'
	if path == '%s/commandou2.zip' % (arcade_path):
		setColors = '2b'
	if path == '%s/contrae.zip' % (arcade_path):
		setColors = '2b'
	if path == '%s/cyberlip.zip' % (arcade_path):
		setColors = '2b'
	if path == '%s/cybots.zip' % (arcade_path):
		setColors = '2d'
		
	if path == '%s/dbz.zip' % (arcade_path):
		setColors = '2c'
	if path == '%s/dbz2.zip' % (arcade_path):
		setColors = '2d'
	if path == '%s/ddragon.zip' % (arcade_path):
		setColors = '2c'
	if path == '%s/dragon2u.zip' % (arcade_path):
		setColors = '2c'
	if path == '%s/ddragon3.zip' % (arcade_path):
		setColors = '3c'
	if path == '%s/ddsom.zip' % (arcade_path):
		setColors = '4d'
	if path == '%s/ddtod.zip' % (arcade_path):
		setColors = '4d'
	if path == '%s/digdug1.zip' % (arcade_path):
		setColors = '2a'
	if path == '%s/dino.zip' % (arcade_path):
		setColors = '3b'
	if path == '%s/dynwar.zip' % (arcade_path):
		setColors = '2c'

	if path == '%s/elevator.zip' % (arcade_path):
		setColors = '2b'
	if path == '%s/elvactr.zip' % (arcade_path):
		setColors = '4b'

	if path == '%s/fatfursp.zip' % (arcade_path):
		setColors = '2d'
	if path == '%s/fatfury1.zip' % (arcade_path):
		setColors = '2c'
	if path == '%s/fatfury3.zip' % (arcade_path):
		setColors = '2d'
	if path == '%s/ffight.zip' % (arcade_path):
		setColors = '2b'

	if path == '%s/ga2u.zip' % (arcade_path):
		setColors = '2c'
	if path == '%s/gaiden.zip' % (arcade_path):
		setColors = '2b'
	if path == '%s/galaxyfg.zip' % (arcade_path):
		setColors = '2d'
	if path == '%s/ghouls.zip' % (arcade_path):
		setColors = '2b'
	if path == '%s/gngc.zip' % (arcade_path):
		setColors = '2b'
	if path == '%s/gunforc2.zip' % (arcade_path):
		setColors = '2b'
	if path == '%s/gunforce.zip' % (arcade_path):
		setColors = '2b'

	if path == '%s/hcastle.zip' % (arcade_path):
		setColors = '2b'
	if path == '%s/hyprduel2.zip' % (arcade_path):
		setColors = '2b'

	if path == '%s/knights.zip' % (arcade_path):
		setColors = '3b'
	if path == '%s/kod.zip' % (arcade_path):
		setColors = '2b'
	if path == '%s/kof98.zip' % (arcade_path):
		setColors = '2d'
	if path == '%s/kof2002.zip' % (arcade_path):
		setColors = '2d'
	if path == '%s/kotm.zip' % (arcade_path):
		setColors = '2c'
	if path == '%s/kotm2.zip' % (arcade_path):
		setColors = '2c'

	if path == '%s/macross2.zip' % (arcade_path):
		setColors = '2b'
	if path == '%s/mk2r32e.zip' % (arcade_path):
		setColors = '2e'
	if path == '%s/mk3.zip' % (arcade_path):
		setColors = '2e'
	if path == '%s/mkla1.zip' % (arcade_path):
		setColors = '2e'
	if path == '%s/mp_gaxe2a.zip' % (arcade_path):
		setColors = '2c'
	if path == '%s/mpatrolw.zip' % (arcade_path):
		setColors = '2b'
	if path == '%s/msh.zip' % (arcade_path):
		setColors = '2e'
	if path == '%s/mshvsf.zip' % (arcade_path):
		setColors = '2e'
	if path == '%s/mslug.zip' % (arcade_path):
		setColors = '2f'
	if path == '%s/mslug2.zip' % (arcade_path):
		setColors = '2f'
	if path == '%s/mslug3.zip' % (arcade_path):
		setColors = '2f'
	if path == '%s/mslug4.zip' % (arcade_path):
		setColors = '2f'
	if path == '%s/mslug5.zip' % (arcade_path):
		setColors = '2f'
	if path == '%s/mslugx.zip' % (arcade_path):
		setColors = '2f'
	if path == '%s/msword.zip' % (arcade_path):
		setColors = '2b'
	if path == '%s/mvsc.zip' % (arcade_path):
		setColors = '2e'

	if path == '%s/pacman.zip' % (arcade_path):
		setColors = '2z'
	if path == '%s/punisher.zip' % (arcade_path):
		setColors = '2b'

	if path == '%s/rmpgwt.zip' % (arcade_path):
		setColors = '3c'

	if path == '%s/samsho.zip' % (arcade_path):
		setColors = '2d'
	if path == '%s/samsho2.zip' % (arcade_path):
		setColors = '2d'
	if path == '%s/samsho3.zip' % (arcade_path):
		setColors = '2d'
	if path == '%s/scontra.zip' % (arcade_path):
		setColors = '2b'
	if path == '%s/sf2.zip' % (arcade_path):
		setColors = '2e'
	if path == '%s/sf2ceuc.zip' % (arcade_path):
		setColors = '2e'
	if path == '%s/sfa.zip' % (arcade_path):
		setColors = '2e'
	if path == '%s/sfa2.zip' % (arcade_path):
		setColors = '2e'
	if path == '%s/sfa3.zip' % (arcade_path):
		setColors = '2e'
	if path == '%s/shdancer.zip' % (arcade_path):
		setColors = '2c'
	if path == '%s/shinobi.zip' % (arcade_path):
		setColors = '2c'
	if path == '%s/shocktroa.zip' % (arcade_path):
		setColors = '2g'
	if path == '%s/shocktr2.zip' % (arcade_path):
		setColors = '2h'
	if path == '%s/simpsons.zip' % (arcade_path):
		setColors = '4b'
	if path == '%s/simpsons2p3.zip' % (arcade_path):
		setColors = '2b'
	if path == '%s/sonicwi2.zip' % (arcade_path):
		setColors = '2b'
	if path == '%s/souledge.zip' % (arcade_path):
		setColors = '2d'
	if path == '%s/spidmanu.zip' % (arcade_path):
		setColors = '4b'
	if path == '%s/ssf2.zip' % (arcade_path):
		setColors = '2e'
	if path == '%s/ssriderseaa.zip' % (arcade_path):
		setColors = '4b'
	if path == '%s/ssridersubc.zip' % (arcade_path):
		setColors = '2b'
	if path == '%s/strider.zip' % (arcade_path):
		setColors = '2b'
	if path == '%s/svc.zip' % (arcade_path):
		setColors = '2d'

	if path == '%s/tekken3ua.zip' % (arcade_path):
		setColors = '2d'
	if path == '%s/tmht2p.zip' % (arcade_path):
		setColors = '2b'
	if path == '%s/tmnt2.zip' % (arcade_path):
		setColors = '4b'
	if path == '%s/tmnt22pu.zip' % (arcade_path):
		setColors = '2b'
	if path == '%s/tmntua.zip' % (arcade_path):
		setColors = '4b'

	if path == '%s/umk3.zip' % (arcade_path):
		setColors = '2e'

	if path == '%s/willow.zip' % (arcade_path):
		setColors = '2b'
	if path == '%s/wof.zip' % (arcade_path):
		setColors = '3b'
		
	if path == '%s/xmcota.zip' % (arcade_path):
		setColors = '2e'
	if path == '%s/xmen.zip' % (arcade_path):
		setColors = '4c'
	if path == '%s/xmvsf.zip' % (arcade_path):
		setColors = '2e'

if system == 'megadrive':
	setColors = '0m'
	exitBtn = 'shift+enter'

if system == 'n64':
	setColors = '0n'
	exitBtn = 'esc'

if system == 'snes':
	setColors = '0s'
	exitBtn = 'shift+enter'

if system == 'exit':
	setColors = '00'

arduino.write(setColors)
sleep(1)
arduino.write(setColors)

if system != 'exit':
	sleep(1)
	keyboard.press('shift+p')
	sleep(.1)
	keyboard.release('shift+p')

	while True:
		key = arduino.readline()
		
		if key[:-2] == 'menu':
			keyboard.press('shift+x')
		if key[:-2] == 'menuOFF':
			keyboard.release('shift+x')

		if key[:-2] == 'exit':
			keyboard.press(exitBtn)
		if key[:-2] == 'exitOFF':
			keyboard.release(exitBtn)

		if key[:-2] == 'pause':
			keyboard.press('shift+p')
		if key[:-2] == 'pauseOFF':
			keyboard.release('shift+p')

		if key[:-2] == 'coin1':
			keyboard.press('q')
		if key[:-2] == 'coin1OFF':
			keyboard.release('q')

		if key[:-2] == 'coin2':
			keyboard.press('w')
		if key[:-2] == 'coin2OFF':
			keyboard.release('w')

		if key[:-2] == 'coin3':
			keyboard.press('e')
		if key[:-2] == 'coin3OFF':
			keyboard.release('e')

		if key[:-2] == 'coin4':
			keyboard.press('r')
		if key[:-2] == 'coin4OFF':
			keyboard.release('r')

quit()