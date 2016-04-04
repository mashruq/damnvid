# Introduction #

Perhaps DamnVid's latest and greatest feature has already been coded and is in the code repository but not released yet. Perhaps you don't like precompiled binaries. Perhaps you just want a challenge. In any case, here's a guide to compile DamnVid from source.

# Foreword #
It's a mess, it really is.

# All platforms #
No matter your OS, grab Python 2.5 from http://www.python.org/ or use your distribution's package repository to get it.
Python modules dependencies:
  * wxPython 2.8 - http://www.wxpython.org/
  * Beautiful Soup - http://www.crummy.com/software/BeautifulSoup/
  * GData Python client - http://code.google.com/p/gdata-python-client/

# Linux #
On Debian/Ubuntu, you should be able to grab the dependencies from your distro's repositories:
  * wxPython2.8 - `python-wxgtk2.8`
  * Beautiful Soup - `python-beautifulsoup`
  * GData Python client - `python-gdata`
Or you could simply run the "dependencies.sh" script in the build-deb directory.
However, if you use Ubuntu, the Python GData client is _outdated_ and doesn't have the latest APIs, such as the Google Code API used in DamnVid's bug report feature, so you'll have to install it yourself by going to http://code.google.com/p/gdata-python-client/ and downloading the latest .tar.gz, or by installing it from the DamnVid PPA:
```
sudo apt-add-repository ppa:damnvid/ppa
sudo apt-get update
sudo apt-get install python-gdata
```
(If anyone knows the corresponding RPM package names, tell me.)
Now... Now what? Hey, this is Linux, right? You don't need to compile the whole stuff, just run it through the interpreter:
```
python DamnVid.py
```
However, if it's the first time you run it, it won't have any module, because those need to be compiled too. You can either compile them yourself one by one and then install them, or if you did a clean checkout and they're in ./modules/, you can simply run:
```
python DamnVid.py --rebuild-modules
```
Which will recompile and reinstall all modules. Then you may start it again without arguments, it'll have all modules.

Now if you do want to compile it, you'll need BBFreeze - http://pypi.python.org/pypi/bbfreeze/
If you ran the dependencies.sh script, you already have it installed and you should be able to run build-deb.sh, it'll compile it and package it just fine. It will build the .rpm package too, if you have the `rpm` tool installed.

# Windows #
After installing Python 2.5 and all the required modules, you'll need to install [PyWin32](http://sourceforge.net/projects/pywin32), and then you should be able to launch DamnVid.py. Now if you want a nice .exe, you need to install more stuff:
  * NSIS - http://nsis.sourceforge.net/Main_Page - Install it in the default directory, otherwise you'll have to edit build-exe.bat with the appropriate path.
  * py2exe - http://www.py2exe.org/ - If UAC is on, run its installer as admin, otherwise it won't work.
  * Make sure Python is in your PATH environment variable.
Then go to the build-exe directory and run build-exe.bat, you'll get a nice DamnVid-someversion-setup.exe in the root source directory.

# Mac OS X #
Make sure you do not use the Python interpreter that comes with Mac OS X. It's outdated and it sucks, and if you break it, some system stuff that rely on it might break.
Todo