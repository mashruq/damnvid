# Introduction #
Linux comes in many savory flavors. As a result, so does DamnVid for Linux.

![http://damnvid.googlecode.com/svn/trunk/img/download-linux.png](http://damnvid.googlecode.com/svn/trunk/img/download-linux.png)

# Ubuntu 10.10 (Maverick Meerkat), 10.04 (Lucid Lynx), and 9.10 (Karmic Koala) #
DamnVid now has a PPA on Launchpad. You can install DamnVid using the following commands:
```
sudo add-apt-repository ppa:damnvid/ppa
sudo apt-get update
sudo apt-get install damnvid
```
Type these 3 commands in a terminal window to install DamnVid.

# Linux Mint #
Follow the same instructions as for Ubuntu.

# Debian #
A Debian repository is up at: http://damnvid.biringa.com/
To use it, add the following lines to /etc/apt/sources.list
```
deb http://damnvid.biringa.com/ sid main
deb-src http://damnvid.biringa.com/ sid main
```
If you're using testing/squeeze; replace sid with squeeze in the above.
The repository is signed, so add the public key with:
```
wget http://damnvid.biringa.com/damnvid.key
su -c "apt-key add damnvid.key"
rm damnvid.key
```


# Arch Linux #
DamnVid is available on the AUR: http://aur.archlinux.org/packages.php?ID=39262

# Other Linux distributions #
Please follow the [Building from source](BuildingFromSource.md) instructions.

If you want to become a package maintainer for your distribution, please contact windypower@gmail.com. Thanks!