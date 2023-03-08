# Variables
minVolume = 0
maxVolume = 100
currentVolume = 30
#

# Functions

# Changes the current volume
def ChangeVolume(newVolume):
	
	# Checks if the new volume is more then the max volume
	if newVolume >= maxVolume:
		
	    # Sets the current volume to the max volume
	    currentVolume = maxVolume
		
	# Checks if the new volume is less then the min volume
	elif newVolume <= minVolume:
		
 	    # Sets the current volume to the min volume
	    currentVolume = minVolume

	else:
		
	    # Sets the current volume to the new volume
	    currentVolume = newVolume
	
#
