# Introduction #
Encountered a problem in DamnVid? Something you can't get to work? This is the place before banging your head on the keyboard. Want to report a bug? Then head to the [Issues tab](http://code.google.com/p/damnvid/issues/list).


# Installation #
## Windows ##
Installation on Windows is pretty straightforward. DamnVid is packaged using a standard [NSIS](http://nsis.sourceforge.net/) installer with the [Modern User Interface 2 (MUI2)](http://nsis.sourceforge.net/Docs/Modern%20UI%202/Readme.html). If you can't figure it out, just keep pressing Next until installation is complete.
**On Vista**, you need to grant permissions to the installer in order to allow it to write files. Vista should prompt you about it when you run the installer.
## Mac OS X ##
Todo
## Linux ##
Todo


# Running the program #
## Windows ##
On Windows, the installer should give you the ability to run DamnVid at the end of installation, if you leave the "Run DamnVid" checkbox checked.
Otherwise, you can launch DamnVid using these methods:
  * If you created a start menu entry, click on Start -> All Programs -> DamnVid (or whatever name you gave to the start menu entry) -> DamnVid.
  * To launch DamnVid directly from the executable, open Windows Explorer (Hold on the Windows Key and press E) and navigate to DamnVid's installation directory (by default, C:\Program Files\DamnVid). From there, double-click DamnVid.exe.
  * You can create a Desktop shortcut to DamnVid by going into DamnVid's installation directory as explained above, then right-clicking on DamnVid.exe and selecting "Send To -> Desktop (create shortcut)". You can then rename the shortcut on your desktop, and eventually drag it in your quick launch bar.

# Main window structure #
DamnVid is made of three areas.
  * The largest one, on the top left, is a list in which you can add videos.
  * The buttons on the right of this list are the action buttons. They will let you add, move, rename, and delete videos. The bottom button lets you start processing the video list, which will not prevent you from adding additional videos.
  * Under the list is a progress bar, which shows the progress of the current conversion. On the right of this progress bar is a "Stop" button, which cancels the conversion.
On top of that, DamnVid's main window also has a menu bar, which lets you execute the same actions as the aforementioned buttons as well as other things like checking for updates, displaying this help page, tuning DamnVid's preferences, or ending the program.
### Note ###
> You can also right-click on the list to perform certain actions on the selected videos. If you didn't select any video, right-clicking on the list will let you add more videos.

# Preferences #
DamnVid's preferences can be access using DamnVid's menubar. Click on "DamnVid", then "Preferences".

![http://damnvid.googlecode.com/files/preferences.png](http://damnvid.googlecode.com/files/preferences.png)

From this dialog, you can fine-tune DamnVid's settings. They are divided in three parts:
  * Video preferences. These allow you to control various visual aspects of the converted videos.
  * Audio preferences. These allow you to control various auditive aspects of the converted videos.
  * Miscellaneous preferences. These allow you to configure other things.
## Video preferences ##
  * **Codec**: This is the video codec that will be used to encode the video stream. Changing this will affect quality and playback compatibility. Default: **MPEG-4**. Recommended: **MPEG-4**.
  * **Frames per second**: This is the number of images per second. Higher values make a smoother video but yield a larger file. Default: **30**. Recommended: **24 to 40**.
  * **Bitrate**: This is the size allocated per fragment of the video. Higher values yield higher-quality videos, but with a larger file size. Default: **768k**. Recommended: **512k to 1024k**. _Note_: If the quality of the source video is poor, it is useless to increase the bitrate too much. The output video quality will never surpass the source video's quality.
  * **Minimum bitrate**: Since the bitrate varies, this is the lower bitrate bound. This will be automatically determined if not specified, which is why it is better to leave it as it is. Default: **(default)**. Recommended: **(default)**.
  * **Maximum bitrate**: Since the bitrate varies, this is the highest bitrate bound. This will be automatically determined if not specified, which is why it is better to leave it as it is. Default: **(default)**. Recommended: **(default)**.
  * **Buffer size**: This is the video buffer size. Recommended that you leave it as it is. Default: **(default)**. Recommended: **(default)**.
  * **Number of passes**: This is the number of passes that will be done on the video stream. It's either 1 or 2. Since 2 passes makes converting a lot longer, and 1 pass is in most cases way enough, it is recommended to leave it to 1 pass. Default: **(default)**. Recommended **(default)** or **1 pass** (same thing).
  * **Group of pictures size**: For video codecs that uses groups of pictures (GOP), notably MPEG, this sets the GOP length, the distance between two intra frames. More info about this [here](http://en.wikipedia.org/wiki/Group_of_pictures). Default: **(default)**. Recommended: **(default)** (Can vary much).
## Audio preferences ##
  * **Codec**: This is the audio codec that will be used to encode the audio stream. Changing this will affect quality and playback compatibility. Default: **MP3**. Recommended: **MP3**, **MP2**.
  * **Volume**: This can be used to modify the output video's volume. The value is a percentage, meaning that 100 will cause no change in the volume. Default : **100%**. Recommended: **100%**.
  * **Bitrate**: This is the size allocated to each fragment of the audio stream. Higher values yield better-sounding audio, but the file size increases. Default: **128k**. Recommended: **96k to 256k**. _Note_: If the quality of the source audio is poor, it is useless to increase the bitrate too much. The output audio quality will never surpass the source audio's quality.
  * **Sampling frequency**: This is the audio sampling frequency. More information [here](http://en.wikipedia.org/wiki/Sampling_rate). Higher values produce better-sounding but bigger files. Default: **44100 Hz**. Recommended: **22050 Hz to 48000 Hz**.
  * **Channels**: This is the number of audio channels to use. Either one (single sound stream) or two (double sound stream, one for the left speaker and one for the right speaker). 2 channels will double the audio size. Default: **1 (Mono)**. Recommended: **Any**.
## Miscellaneous preferences ##
  * **Enable directory recursion**: When you drag a folder and drop it into DamnVid, one of two things may happen:
    * f this options is **enabled**, the directory will be scanned and everyone of its files will be added. If the directory contains subdirectories, all of them will be added as well.
    * f this option is **disabled**, adding a directory in DamnVid will have no effect.
> Default: **Enabled**. Recommended: **Enabled**.
  * **Output directory**: This is a folder where all videos will be saved. It is recommended to change this to your favorite video folder. Default: **{program installation directory}/output**. Recommended: **Any video folder**.
  * **Minimize to tray**: Allows you instead of minimizing DamnVid’s window to taskbar, it appears in tray. You can maximize back the window by clicking once on DamnVid’s icon.
  * **Language**: Allows you to switch between English and French (for now) as DamnVid’s language.
  * **Show splashscreen at startup**: By checking this checkbox, you can choose whether or not you want DamnVid's splashscreen to appear at startup.
  * **Warn when removing a video from the list**: Allows you to choose if you want to be warned when removing a video or all of them.
  * **Main Window**: Allows you to choose if you want DamnVid to remember between each startup its older postion and size or to always be recentered.
  * **Video History size**: Allows you to choose the number of videos saved into the history. Default: **8**. Recommended: **Whatever between 0 et 50**.
## Reset to default config ##
At the bottom of the preferences dialog is a **dropdown menu** that contains two entries. Here's what happens if you select one of them:
  * **DamnVid (some version) default**: This will reset all settings to all the "Defaut" values on this page, which are also the ones DamnVid starts with.
  * **[FFmpeg](FFmpeg.md) default**: This will reset all video/audio settings to **(default)**, meaning that the argument will not be passed to [FFmpeg](FFmpeg.md), letting it decide.

# Uninstallation #
## Windows ##
Just like installing, uninstalling is pretty straightforward, if not more. To uninstall DamnVid, do one of the following:
  * Open the start menu -> All programs -> DamnVid, and click on "Uninstall".
  * If you didn't create a start menu entry, open Windows Explorer and navigate to DamnVid's installation directory as described in the installation section. Then double-click on "uninstaller.exe".
  * You can go into Control Panel -> Programs, and click on DamnVid to uninstall it.
## Mac OS X ##
Todo
## Linux ##
Todo


# Need help? #
If you want to ask for help or are having trouble with DamnVid, head to the [Support page](Support.md).