# Introduction #

This is DamnVid's changelog. While you might want to look at [DamnVid's SVN Commit log](http://code.google.com/p/damnvid/source/list) for a more in-depth look at DamnVid's code evolution, this page regroups the changes on a version basis, and not a revision-basis.

# Details #

[Version 0.1](http://code.google.com/p/damnvid/downloads/detail?name=DamnVid-setup.exe), released on June 21st, 2008:
  * Initial release. Supports local files, YouTube. Only one encoding profiles for all.
  * Available for Windows only
  * Became relatively popular to its own demise. The download link was never posted anywhere, yet this (poor) version received hundreds of downloads.

[Version 0.2](http://code.google.com/p/damnvid/downloads/detail?name=DamnVid-setup-0.2.exe), released on January 23rd, 2009:
  * Breakthrough: Multiple encoding profiles
  * Added auto-update mechanism
  * Added support for dual-pass encoding. The option was there in v0.1, but didn't actually do anything.
  * Completely revamped preferences panel, now dynamic, with a hierarchical tree and support for importing/exporting preferences.
  * Fixed some interface bugs
  * Available for Windows only

[Version 0.2.1](http://code.google.com/p/damnvid/downloads/detail?name=DamnVid-setup-0.2.1.exe), released on February 7th, 2009:
  * Improved YouTube support, movies would sometimes not download
  * Fixed "moov atom not found" FFmpeg error
  * Added YouTube HD support
  * Added fallback to alternative video streams if available (for example, multiple-quality video)
  * Added old preferences handling system
  * Available for Windows only

[Version 0.2.2](http://damnvid.googlecode.com/files/DamnVid-setup-0.2.2.exe), released on February 8th, 2009:
  * Updated YouTube icon
  * Added YouTube HD icon
  * DamnVid now shows the pass number in dual-pass encoding
  * When closing the preferences pane, HD videos don't fall back to normal quality YouTube videos.
  * DamnVid's icon now shows up in Windows Vista.
  * Available for Windows only

[Version 0.3](http://code.google.com/p/damnvid/downloads/detail?name=DamnVid-setup-0.3.exe), released on March 14th, 2009:
  * Added "Same quality as source" option in bitrate preference.
  * Added minimum/maximum quantizers control
  * Added aspect ratio control
  * Added .deb and .rpm packages
  * Available for Windows, and for Linux (!) as a .deb and .rpm package.

[Version 0.3.1](http://code.google.com/p/damnvid/downloads/detail?name=DamnVid-setup-0.3.1.exe), released on March 17th, 2009:
  * Added option to not encode audio and/or video stream. This allows the user to extract only the audio from a video file and save it as an MP3 file, for instance.
  * Added new audio-only preset
  * Available for Windows, and for Linux as a .deb and .rpm package.

[Version 0.3.2](http://code.google.com/p/damnvid/downloads/detail?name=DamnVid-setup-0.3.2.exe), released on March 26th, 2009:
  * Added droptarget for files, that doubles as a loading indicator
  * Made "Done" dialog more verbose, telling users where each video went
  * Available for Windows, Mac OS X (!), and for Linux as a .deb and .rpm package.

[Version 1.0.2](http://code.google.com/p/damnvid/downloads/detail?name=DamnVid-setup-1.0.2.exe), released on April 16th, 2009:
  * Integrated YouTube browser: You can now search and browse YouTube videos right from DamnVid, no need to open your browser.
  * Fixed FFmpeg library linking on OS X
  * Added YouTube playlist parsing capabilities
  * Added clipboard monitoring feature, you can now simply copy a URL and DamnVid will pick it up, no need to paste.
  * DamnVid is now **modular**: All supported external sites are now available as "modules", which can be separately installed, updated, uninstalled, configured, independently from DamnVid. This is a huge improvement.
  * It's version 1! At last! Available for Windows, Mac OS X, and for Linux as a .deb and .rpm package.

[Version 1.5](http://code.google.com/p/damnvid/downloads/detail?name=DamnVid-setup-1.5.exe), released on December 7th, 2009:
  * Lots and lots of new modules
  * Localization support
  * Added french translation
  * The dialog shown at the end of the video conversion is now a lot clearer, and it lets you open the converted videos (and their respective folders) directly
  * YouTube module supports 1080p videos
  * DamnVid can now be minimized to the tray
  * Bug Report in the application itself
  * Added Video only mode (no audio)
  * Added iPhone 3GS video preset
  * Video history: DamnVid remembers the last videos you added to it
  * Fancy new splashscreen
  * Lots of updates to out-of-date modules
  * Additional preferences available
  * Even more bug fixes
  * Small interface changes

[Version 1.6](http://code.google.com/p/damnvid/downloads/detail?name=DamnVid-setup-1.6.exe), released on May 25th, 2010:
  * DamnVid now has a formal [Ubuntu PPA](LinuxDownload.md).
  * Added Spanish, Brazilian Portuguese, and Norwegian (Bokmål) translations
  * Added HTTP proxy and SOCKS proxy support
  * Made configuration directory customizable to make DamnVid portable
  * Added .mov format to the profile preferences
  * Video history now has its own dialog and is much easier to use
  * Small logic changes to main window interface
  * Fixed lots of bugs and interface quirks