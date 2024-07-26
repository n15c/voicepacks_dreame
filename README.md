# Dreame Vacuum Cleaner Soundpacks and Scripts

Welcome to the Dreame Vacuum Cleaner Soundpacks and Scripts repository! This repository provides a variety of soundpacks for Dreame vacuum cleaners and useful scripts to manage and customize your device.

## Contents

- [Soundpacks](#soundpacks)
- [Scripts](#scripts)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

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

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Enjoy customizing your Dreame vacuum cleaner with new sounds and scripts!


## Filenames

| Filename       | Sound Description                                                                                              |
|----------------|---------------------------------------------------------------------------------------------------------------|
| 0.ogg          | Startup sound                                                                                                 |
| 1.ogg          | Waiting for the network configuration.                                                                        |
| 2.ogg          | Unable to connect to the wifi network. Please check wifi password and try again later.                        |
| 3.ogg          | Unable to connect to the server. Please check your local network and try again later.                         |
| 4.ogg          | Robot has exited network configuration mode.                                                                  |
| 5.ogg          | Network connected successfully.                                                                               |
| 6.ogg          | Network connection failed. Please try again later.                                                            |
| 7.ogg          | Start cleaning.                                                                                               |
| 8.ogg          | Start spot cleaning.                                                                                          |
| 9.ogg          | Start scheduled cleaning.                                                                                     |
| 10.ogg         | Start resuming cleaning.                                                                                      |
| 11.ogg         | Paused.                                                                                                       |
| 12.ogg         | Cleaning task completed.                                                                                      |
| 13.ogg         | Returning to the dock to charge.                                                                              |
| 14.ogg         | Low battery. Returning to the dock to charge. Robot will resume working after charging.                       |
| 15.ogg         | I'm about to return to the starting point.                                                                    |
| 16.ogg         | Low battery. I'm about to return to the starting point. Please charge me.                                     |
| 17.ogg         | Please move robot to the dock to charge.                                                                      |
| 18.ogg         | Charging.                                                                                                     |
| 19.ogg         | Please move robot from the dock before turning it off.                                                        |
| 20.ogg         | Low battery.                                                                                                  |
| 21.ogg         | Low battery. Robot will turn off.                                                                             |
| 22.ogg         | Please move robot to an area that needs to be cleaned.                                                        |
| 23.ogg         | Water tank has been installed.                                                                                |
| 24.ogg         | Please check whether water tank is installed properly.                                                        |
| 25.ogg         | Low battery. Unable to carry out the scheduled cleanup.                                                       |
| 26.ogg         | Restoring to factory settings.                                                                                |
| 27.ogg         | Updating. Taking about five minutes. Do not turn off nor start a cleaning task.                               |
| 28.ogg         | Updated successfully.                                                                                         |
| 29.ogg         | Update failed, please try again later.                                                                        |
| 30.ogg         | Positioning, please wait.                                                                                     |
| 31.ogg         | Positioning failed. Map is invalid. Robot will start a new cleanup.                                           |
| 32.ogg         | I’ve detected changes to the environment. Please push the button and start a new cleaning cycle.              |
| 33.ogg         | Visual navigation sensor error. Please wipe it clean and restart.                                             |
| 34.ogg         | Dustbin not installed. Please install it.                                                                     |
| 35.ogg         | Main brush error. Please check and clean it.                                                                  |
| 36.ogg         | Side brush error. Please check and clean it.                                                                  |
| 37.ogg         | Right wheel error. Please check and clean it.                                                                 |
| 38.ogg         | Left wheel error. Please check and clean it.                                                                  |
| 39.ogg         | Please clean cliff sensor.                                                                                    |
| 40.ogg         | Robot stuck. Please move it to a new position to restart.                                                     |
| 41.ogg         | Robot's wheels suspended. Please move robot back on the ground.                                               |
| 42.ogg         | Please check and clean filter.                                                                                |
| 43.ogg         | Bumper error. Please gently tap to see if it rebounds.                                                        |
| 44.ogg         | Error. Please check the user manual or contact customer service.                                              |
| 45.ogg         | I am here.                                                                                                    |
| 46.ogg         | Robot and phone connected. Please return to App to wait for the result.                                       |
| 47.ogg         | Start charging.                                                                                               |
| 48.ogg         | Low battery. Returning to the dock.                                                                           |
| 49.ogg         | High intensity magnetic field detected. Please move robot away and restart.                                   |
| 50.ogg         | Charging error. Please clean charging contacts.                                                               |
| 51.ogg         | Battery overheating or overcooling. Please wait until the battery's temperature returns to normal. Then continue to use. |
| 52.ogg         | Robot tilted. Please put it on a level ground to restart.                                                     |
| 53.ogg         | Virtual no-go zone detected. Please move robot away and restart.                                              |
| 54.ogg         | Positioning succeeded. Resuming cleaning.                                                                     |
| 55.ogg         | Positioning succeeded. Resuming returning to the dock.                                                        |
| 56.ogg         | Start selected room cleaning.                                                                                 |
| 57.ogg         | Start zoned cleaning.                                                                                         |
| 58.ogg         | Proceed with cleaning task.                                                                                   |
| 59.ogg         | Mopping completed. Please remove water tank timely.                                                           |
| 60.ogg         | Optical flow sensor error. Please wipe the optical flow sensor clean and restart.                             |
| 61.ogg         | Start mopping.                                                                                                |
| 62.ogg         | Start remote control cleaning.                                                                                |
| 63.ogg         | Water tank has been removed.                                                                                  |
| 64.ogg         | Positioning failed. Map is invalid. Robot will return to dock.                                                |
| 65.ogg         | Resume returning to the dock.                                                                                 |
| 66.ogg         | Filter worn out. Please replace it timely.                                                                    |
| 67.ogg         | Side brush worn out. Please replace it timely.                                                                |
| 68.ogg         | Main brush worn out. Please replace it timely.                                                                |
| 69.ogg         | Cleanup path blocked. Please move robot to a new position to restart.                                         |
| 70.ogg         | Please remove and clean mop pad.                                                                              |
| 71.ogg         | Laser sensor error. Please check and clean the laser sensor.                                                  |
| 72.ogg         | Please check whether laser distance sensor cover is jammed.                                                   |
| 73.ogg         | Edge sensor error. Please check and clean it.                                                                 |
| 74.ogg         | Please try to clean the obstacle sensors.                                                                     |
| 75.ogg         | Filter may not be dry or may be blocked.                                                                      |
| 76.ogg         | Spot cleanup is starting.                                                                                     |
| 77.ogg         | Please start robot in non-carpet area.                                                                        |
| 78.ogg         | Please clean 3D obstacle avoidance sensor.                                                                    |
| 79.ogg         | 3D obstacle avoidance sensor error. Please restart robot or contact customer service.                         |
| 80.ogg         | The transmitter of 3D obstacle avoidance sensor is malfunctioning. Please restart the robot or contact the after-sales service department. |
| 81.ogg         | Ultrasonic sensor error. Please restart robot or contact customer service.                                    |
| 82.ogg         | Start mapping.                                                                                                |
| 83.ogg         | Proceed with mapping.                                                                                         |
| 84.ogg         | Mapping completed.                                                                                            |
| 85.ogg         | Positioning succeeded. Proceeding with mapping.                                                               |
| 86.ogg         | Positioning failed. Restarting mapping.                                                                       |
| 87.ogg         | Low battery. Returning to the dock.                                                                           |
| 88.ogg         | Enter remote control mode.                                                                                    |
| 89.ogg         | Resume recharging.                                                                                            |
| 90.ogg         | Proceed with cleaning task.                                                                                   |
| 91.ogg         | The clean water tank is not installed. Please install it before the robot carries on working.                 |
| 92.ogg         | The dirty water tank is not installed. Please install it before the robot carries on working.                 |
| 93.ogg         | There is not enough water in the clean water tank. Add water to the tank before the robot carries on working. |
| 94.ogg         | The dirty water tank is full. Pour off the dirty water before the robot carries on working.                   |
| 95.ogg         | The mop pad washboard is not installed. The robot can not return to the charging dock.                        |
| 96.ogg         | The mop pad washboard is overflowing. Please check whether the water outlet of the pad is blocked.            |
| 97.ogg         | The dust collection bag is not installed. Please install it before the robot carries on working.              |
| 98.ogg         | The dust collection bag is full. Please empty it.                                                             |
| 99.ogg         | The upper cover of charging and dust collection compartment is not closed. Please close the upper cover before the robot carries on working. |
| 100.ogg        | The air duct of charging and dust collection compartment is blocked. Please have a check.                     |
| 101.ogg        | The upper cover of auto-empty base is not closed or the dust collection bag is not installed. Please close the upper cover or install the bag. |
| 102.ogg        | The dust collection bag is full or the air duct is blocked. Please replace the bag with a new one or clean the air duct in time. |
| 103.ogg        | The mop pad wash board is installed. The robot resumes working.                                               |
| 104.ogg        | The mop pad wash board is not installed. Please ensure that a wash board is installed and clasps on its both sides are tightly fastened. |
| 105.ogg        | Start cleaning.                                                                                               |
| 106.ogg        | Start cleaning the mop.                                                                                       |
| 107.ogg        | Start dehydrating the mop.                                                                                    |
| 108.ogg        | The water level of mop pad wash board is abnormal. Please clean it in time to avoid blockage.                 |
| 109.ogg        | An exception occurred in the dirty water tank. Please ensure that a dirty water tank is installed and timely empty the dirty water inside. |
| 110.ogg        | Start auto empty.                                                                                             |
| 111.ogg        | Mop pads off. Please install them before resuming working.                                                    |
| 112.ogg        | Place robot back onto the self-wash base before use.                                                          |
| 113.ogg        | Task completed. Please empty waste tank timely.                                                               |
| 114.ogg        | Mop pads installed.                                                                                           |
| 115.ogg        | Mop pads removed.                                                                                             |
| 116.ogg        | Child lock on. Buttons locked.                                                                                |
| 117.ogg        | Child lock off. Buttons unlocked.                                                                             |
| 118.ogg        | Buttons locked. Press and hold the dock button to unlock.                                                     |
| 119.ogg        | Buttons locked.                                                                                               |
| 120.ogg        | Buttons unlocked.                                                                                             |
| 121.ogg        | The robot and the phone are connected. Please return to the Fantic app and wait for the network connection to complete. |
| 122.ogg        | Continuous positioning, please wait.                                                                          |
| 126.ogg        | Start cleaning.                                                                                               |
| 127.ogg        | Start spot cleaning.                                                                                          |
| 128.ogg        | Start spot mopping.                                                                                           |
| 129.ogg        | Start scheduled cleaning.                                                                                     |
| 130.ogg        | Start scheduled mopping.                                                                                      |
| 131.ogg        | Start spot cleaning.                                                                                          |
| 132.ogg        | Start spot mopping.                                                                                           |
| 133.ogg        | Start selected room cleaning.                                                                                 |
| 134.ogg        | Start selected room mopping.                                                                                  |
| 135.ogg        | Start zoned cleaning.                                                                                         |
| 136.ogg        | Start zoned mopping.                                                                                          |
| 137.ogg        | Resume cleaning.                                                                                              |
| 138.ogg        | Resume mopping.                                                                                               |
| 139.ogg        | Resume returning to the base for self-cleaning.                                                               |
| 140.ogg        | New environment is detected. Returning to the self-wash base.                                                 |
| 141.ogg        | Mop pad error. Please check and clean it.                                                                     |
| 142.ogg        | Mop pad worn out. Please replace it timely.                                                                   |
| 143.ogg        | Cleaning completed.                                                                                           |
| 144.ogg        | Mopping completed.                                                                                            |
| 145.ogg        | Positioning successful. Resume cleaning.                                                                      |
| 146.ogg        | Positioning successful. Resume mopping.                                                                       |
| 148.ogg        | Return to the base for self-cleaning.                                                                         |
| 149.ogg        | Unable to reach the specified area. Please try to clear obstacles in the path.                                |
| 150.ogg        | Unable to reach the specified area. Please try to delete no-go zones in the path.                             |
| 151.ogg        | The path is blocked. Please try to clear obstacles around your robot.                                         |
| 152.ogg        | The path is blocked. Please try to delete no-go zones or move your robot out of this area.                    |
| 153.ogg        | Your robot is detected in the no-go zone. Please move your robot out of this area.                            |
| 154.ogg        | Operated too frequently. Please try again later.                                                              |
| 155.ogg        | Start to return to the charging and the mop cleaning dock.                                                    |
| 156.ogg        | Mop pad tray uninstalled.                                                                                     |
| 157.ogg        | Am already at the charging and the mop cleaning dock.                                                         |
| 200.ogg        | Shutdown sound                                                                                                |
