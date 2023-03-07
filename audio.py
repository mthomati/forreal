minVolume = 0
maxVolume = 100
currentVolume = 30

def ChangeVolume(newVolume):

	if newVolume >= maxVolume:

		currentVolume = maxVolume

	elif newVolume <= minVolume:

		currentVolume = minVolume

	else:

		currentVolume = newVolume
