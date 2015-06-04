##########Created by johnTzan 05-25-2015###########
## Circle display gauges for Brake and Gas Pedal ##
###################################################
import ac
import acsys
import sys

sys.path.insert(len(sys.path), 'apps/python/pedalCircles/third_party')

from sim_info import info


def acMain(ac_version):

	appWindow = ac.newApp("Pedal Circles")
	ac.setSize(appWindow, 412, 250)
	ac.setTitle(appWindow, "")
	# ac.setBackgroundOpacity(appWindow, 0) ~ doesn't change anything
	ac.setIconPosition(appWindow, 0, -10000)
	ac.console("Hello Assetto, this is Pedal Circles")

	brake_display = ac.addLabel(appWindow, "")
	ac.setPosition(brake_display, 3, 25)
	ac.setSize(brake_display, 200, 200)

	gas_display = ac.addLabel(appWindow, "")
	ac.setPosition(gas_display, 207, 25)
	ac.setSize(gas_display, 200, 200) 

	return "brake"
	
def acUpdate(deltaT):
	global brake_display
	global gas_display

	steps = 20
	
	ac_brake = round(ac.getCarState(0, acsys.CS.Brake) * 100)
	
	current_brake_step = str(round(steps * ac_brake / 100)).zfill(2)
	# ac.console(current_brake_step)
	ac.setBackgroundTexture(brake_display, "apps/python/pedalCircles/textures/brake_steps/brake_" + current_brake_step + ".png")

	ac_gas = round(ac.getCarState(0, acsys.CS.Gas) * 100)
	current_gas_step = str(round(steps * ac_gas / 100)).zfill(2)
	# ac.console(current_gas_step)
	ac.setBackgroundTexture(gas_display, "apps/python/pedalCircles/textures/gas_steps/gas_" + current_gas_step + ".png")

	## test sim_info ##
	# ac.console("RPMS: " + str(info.physics.rpms))


