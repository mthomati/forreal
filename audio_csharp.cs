using System;

namespace AudioManager{

    class Audio{

	// Variables
	int minVolume = 0;
	int maxVolume = 100;
	int currentVolume = 30;


	// Functions

	// Changes the current volume
	public void ChangeVolume(int newVolume){

	    // Checks if the new volume is more then the max volume
	    if (newVolume >= maxVolume){

	        // Sets the current volume to the max volume
		currentVolume = maxVolume;
	    }

	    // Checks if the new volume is less then the min volume
	    else if (newVolume <= minVolume){

		// Sets the current volume to the min volume
		currentVolume = minVolume;
	    }

	    else{

		// Sets the current volume to the new volume
		currentVolume = newVolume;
	    }
	}
    }
}
