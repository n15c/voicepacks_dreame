# Dreame Vacuum Cleaner Soundpacks and Scripts

Welcome to the Dreame Vacuum Cleaner Soundpacks and Scripts repository! This repository provides a variety of soundpacks for Dreame vacuum cleaners and useful scripts to manage and customize your device.

## Contents

- [Soundpacks](#soundpacks)
- [Scripts](#scripts)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Filenames](#filenames)

## Soundpacks

This repository includes multiple soundpacks that can be used to customize the audio feedback of your Dreame vacuum cleaner. Each soundpack contains a set of sound files that correspond to different actions and alerts of the vacuum cleaner.

### Available Soundpacks

- **Original Soundpack**: The standard set of sounds provided by Dreame.
- **R2D2 Soundpack**: A custom set of sounds stolen from a Roborock Soundpack.
- **GLADOS**: Another custom set of sounds from https://github.com/Findus23/voice_pack_dreame.
- **Memes**: Another custom set of sounds using meme sounds.

Each soundpack is organized in its own directory.

## Scripts

Along with the soundpacks, this repository contains useful scripts to manage and customize the sound settings of your Dreame vacuum cleaner.

### Available Scripts

- **CreateSoundFromYoutube.py**: A script to download a youtube video, extract the sound and add it to a chosen soundpack.

## Installation

To get started with using the soundpacks and scripts, follow these steps:

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/dreame-vacuum-soundpacks.git
   ```
2. Navigate to the cloned directory:
   ```bash
   cd dreame-vacuum-soundpacks
   ```

## Usage

### Downloading a sound from Youtube and add it to a soundpack

To install a new soundpack on your Dreame vacuum cleaner, run the following script:

```bash
python CreateSoundFromYoutube.py [-h] --youtube_url YOUTUBE_URL --soundpack SOUNDPACK --sound_id SOUND_ID
```

### Using a soundpack in Valetudo
1. Get the URL of the wanted soundpack: 
[GlaDOS Pack](https://github.com/n15c/voicepacks_dreame/releases/latest/download/glados.tar.gz)
[Meme Soundpack](https://github.com/n15c/voicepacks_dreame/releases/latest/download/memes.tar.gz)
[R2D2 Soundpack](https://github.com/n15c/voicepacks_dreame/releases/download/v0.1/r2d2.tar.gz)
[Original Sounds](https://github.com/n15c/voicepacks_dreame/releases/download/v0.1/original-en.tar.gz)

2. Get the corresponding MD5 hash of this file, either by using this [file](https://github.com/n15c/voicepacks_dreame/releases/download/v0.1/md5sums.txt) or calculate it by yourself
3. Go to your Valetudo page <IP/HOSTNAME>/#/options/robot/misc
4. Write down the data (the language code can be chosen by you, just don't use an official language like DE, EN, ...)

## Contributing

We welcome contributions to this repository! If you have a new soundpack or a useful script to share, please follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add some feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature
   ```
5. Open a pull request.

## Other Stuff

The csv was stolen from [ccoors](https://raw.githubusercontent.com/ccoors/dreame_voice_packs/main/sound_list.csv)


---

Enjoy customizing your Dreame vacuum cleaner with new sounds and scripts!



## Filenames

| Filename       | Sound Description                                                                                             |
|----------------|---------------------------------------------------------------------------------------------------------------|
|0|Startup sound|
|1|Waiting for the network configuration.|
|2|Unable to connect to the wifi network. Please check wifi password and try again later.|
|3|Unable to connect to the server. Please check your local network and try again later.|
|4|Robot has exited network configuration mode.|
|5|Network connected successfully.|
|6|Network connection failed. Please try again later.|
|7|Start cleaning.|
|8|Start spot cleaning.|
|9|Start scheduled cleaning.|
|10|Start resuming cleaning.|
|11|Paused.|
|12|Cleaning task completed.|
|13|Returning to the dock to charge.|
|14|Low battery. Returning to the dock to charge. Robot will resume working after charging.|
|15|I'm about to return to the starting point.|
|16|Low battery. I'm about to return to the starting point. Please charge me.|
|17|Please move robot to the dock to charge.|
|18|Charging.|
|19|Please move robot from the dock before turning it off.|
|20|Low battery.|
|21|Low battery. Robot will turn off.|
|22|Please move robot to an area that needs to be cleaned.|
|23|Water tank has been installed.|
|24|Please check whether water tank is installed properly.|
|25|Low battery. Unable to carry out the scheduled cleanup.|
|26|Restoring to factory settings.|
|27|Updating. Taking about five minutes. Do not turn off nor start a cleaning task.|
|28|Updated successfully.|
|29|Update failed| please try again.|
|30|Positioning| please wait.|
|31|Positioning failed. Map is invalid. Robot will start a new cleanup.|
|32|I’ve detected changes to the environment. Please push the button and start a new cleaning cycle.|
|33|Visual navigation sensor error. Please wipe it clean and restart.|
|34|Dustbin not installed. Please install it.|
|35|Main brush error. Please check and clean it.|
|36|Side brush error. Please check and clean it.|
|37|Right wheel error. Please check and clean it.|
|38|Left wheel error. Please check and clean it.|
|39|Please clean cliff sensor.|
|40|Robot stuck. Please move it to a new position to restart.|
|41|Robot's wheels suspended. Please move robot back on the ground.|
|42|Please check and clean filter.|
|43|Bumper error. Please gently tap to see if it rebounds.|
|44|Error. Please check the user manual or contact customer service.|
|45|I am here.|
|46|Robot and phone connected. Please return to App to wait for the result.|
|47|Start charging.|
|48|Low battery. Returning to the dock.|
|49|High intensity magnetic field detected. Please move robot away and restart.|
|50|Charging error. Please clean charging contacts.|
|51|Battery overheating or overcooling. Please wait until the battery's temperature returns to normal. Then continue to use.|
|52|Robot tilted. Please put it on a level ground to restart.|
|53|Virtual no-go zone detected. Please move robot away and restart.|
|54|Positioning succeeded. Resuming cleaning.|
|55|Positioning succeeded. Resuming returning to the dock.|
|56|Start selected room cleaning.|
|57|Start zoned cleaning.|
|58|Proceed with cleaning task.|
|59|Mopping completed. Please remove water tank timely.|
|60|Optical flow sensor error. Please wipe the optical flow sensor clean and restart.|
|61|Start mopping.|
|62|Start remote control cleaning.|
|63|Water tank has been removed.|
|64|Positioning failed. Map is invalid. Robot will return to dock.|
|65|Resume returning to the dock.|
|66|Filter worn out. Please replace it timely.|
|67|Side brush worn out. Please replace it timely.|
|68|Main brush worn out. Please replace it timely.|
|69|Cleanup path blocked. Please move robot to a new position to restart.|
|70|Please remove and clean mop pad.|
|71|Laser sensor error. Please check and clean the laser sensor.|
|72|Please check whether laser distance sensor cover is jammed.|
|73|Edge sensor error. Please check and clean it.|
|74|Please try to clean the obstacle sensors.|
|75|Filter may not be dry or may be blocked.|
|76|Spot cleanup is starting.|
|77|Please start robot in non-carpet area.|
|78|Please clean 3D obstacle avoidance sensor.|
|79|3D obstacle avoidance sensor error. Please restart robot or contact customer service.|
|80|The transmitter of 3D obstacle avoidance sensor is malfunctioning. Please restart the robot or contact the after-sales service department.|
|81|Ultrasonic sensor error. Please restart robot or contact customer service.|
|82|Start mapping.|
|83|Proceed with mapping.|
|84|Mapping completed.|
|85|Positioning succeeded. Proceeding with mapping.|
|86|Positioning failed. Restarting mapping.|
|87|Low battery. Returning to the dock.|
|88|Enter remote control mode.|
|89|Resume recharging.|
|90|Proceed with cleaning task.|
|91|The clean water tank is not installed. Please install it before the robot carries on working.|
|92|The dirty water tank is not installed. Please install it before the robot carries on working.|
|93|There is not enough water in the clean water tank. Add water to the tank before the robot carries on working.|
|94|The dirty water tank is full. Pour off the dirty water before the robot carries on working.|
|95|The mop pad washboard is not installed. The robot can not return to the charging dock.|
|96|The mop pad washboard is overflowing. Please check whether the water outlet of the pad is blocked.|
|97|The dust collection bag is not installed. Please install it before the robot carries on working.|
|98|The dust collection bag is full. Please empty it.|
|99|The upper cover of charging and dust collection compartment is not closed. Please close the upper cover before the robot carries on working.|
|100|The air duct of charging and dust collection compartment is blocked. Please have a check.|
|101|The upper cover of auto-empty base is not closed or the dust collection bag is not installed. Please close the upper cover or install the bag.|
|102|The dust collection bag is full or the air duct is blocked. Please replace the bag with a new one or clean the air duct in time.|
|103|The mop pad wash board is installed. The robot resumes working.|
|104|The mop pad wash board is not installed. Please ensure that a wash board is installed and clasps on its both sides are tightly fastened.|
|105|Start cleaning.|
|106|Start cleaning the mop.|
|107|Start dehydrating the mop.|
|108|The water level of mop pad wash board is abnormal. Please clean it in time to avoid blockage.|
|109|An exception occurred in the dirty water tank. Please ensure that a dirty water tank is installed and timely empty the dirty water inside.|
|110|Start auto empty.|
|111|Mop pads off. Please install them before resuming working.|
|112|Place robot back onto the self-wash base before use.|
|113|Task completed. Please empty waste tank timely.|
|114|Mop pads installed.|
|115|Mop pads removed.|
|116|Child lock on. Buttons locked.|
|117|Child lock off. Buttons unlocked.|
|118|Buttons locked. Press and hold the dock button to unlock.|
|119|Buttons locked.|
|120|Buttons unlocked.|
|121|The robot and the phone are connected. Please return to the Fantic app and wait for the network connection to complete.|
|122|Continuous positioning| please wait.|
|126|Start cleaning.|
|127|Start spot cleaning.|
|128|Start spot mopping.|
|129|Start scheduled cleaning.|
|130|Start scheduled mopping.|
|131|Start spot cleaning.|
|132|Start spot mopping.|
|133|Start selected room cleaning.|
|134|Start selected room mopping.|
|135|Start zoned cleaning.|
|136|Start zoned mopping.|
|137|Resume cleaning.|
|138|Resume mopping.|
|139|Resume returning to the base for self-cleaning.|
|140|New environment is detected. Returning to the self-wash base.|
|141|Mop pad error. Please check and clean it.|
|142|Mop pad worn out. Please replace it timely.|
|143|Cleaning completed.|
|144|Mopping completed.|
|145|Positioning successful. Resume cleaning.|
|146|Positioning successful. Resume mopping.|
|148|Return to the base for self-cleaning.|
|149|Unable to reach the specified area. Please try to clear obstacles in the path.|
|150|Unable to reach the specified area. Please try to delete no-go zones in the path.|
|151|The path is blocked. Please try to clear obstacles around your robot.|
|152|The path is blocked. Please try to delete no-go zones or move your robot out of this area.|
|153|Your robot is detected in the no-go zone. Please move your robot out of this area.|
|154|Operated too frequently. Please try again later.|
|155|Start to return to the charging and the mop cleaning dock.|
|156|Mop pad tray uninstalled.|
|157|Am already at the charging and the mop cleaning dock.|
|162|Camera is on|
|163|Camera monitoring|
|164|Task ends|
|166|Please clean the foreign objects tangled in the mop pad|
|169|Mop pad drying complete|
|170|All the buttons are locked. Please press and hold the buttons on the base station to unlock|
|171|AI recognition function on|
|172|AI recognition function off|
|173|Please replace the Silver Ion sterilizer|
|177|Leaving the base station|
|179|Mop pad cleaned. The water in the clean water tank is insufficient. Please fill the clean water tank and empty the used water tank|
|181|Insufficient water. Please fill the clean water tank|
|186|Please check the fresh tank|
|187|It will about 5 to 10 minutes|
|188|Automatic docking engaged|
|200|Shutdown sound|
|244|Detergent bottle installed|
|257|Camera monitoring exited|
|258|Self-positioned. Cruising started|
|259|Self-positioned. Proceeding to the designated location|
|260|Self-positioned. Cruising resumed|
|261|Self-positioned. Resume proceeding to the designated location|
|262|Self-positioning failed|
|263|Please clean the foreign objects tangled in the main brush. Reposition the robot and start it again|
|264|Task complete. Please clean the dust bin and the wash board|
|266|Please replace the detergent|
|267|Please clean the sensors|
|274|*Ding sound*|
|280|Start custom cleaning|
|281|The robot is auto emptying. Please try again later|
|282|The robot is cleaning the mop pad. Please try again later|
|283|The robot is not in the base station. Please try again later|
|293|Calling enabled|
|294|Calling disabled|