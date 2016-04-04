# Portable installation #
A portable installation is one you can install on a removable device (thumb drive, etc) and have it work anywhere, with the same configuration.

## Method 1: The easy way ##
Inside DamnVid's installation directory (where DamnVid.exe is on Windows), create a folder named `portableConf` (lowercase "p", uppercase "C"). Now run DamnVid and it will store all its stuff there.

## Method 2: The configurable way ##
If you know how to use the console or how to write batch files/shell scripts, you can launch DamnVid with the following argument:
```
DamnVid.exe --config=X:\DamnVid\configuration\directory
```
Or on Linux:
```
python /path/to/DamnVid.py --config=/path/to/configuration/directory
```
And then DamnVid will read/store its configuration from `X:\DamnVid\configuration\directory` (or from `/path/to/configuration/directory` in the second example).
**Note**: If the path to your desired configuration directory has spaces in it, remember to put quotes around it, like so:
```
DamnVid.exe --config="X:\Portable applications\DamnVid sucks less"
```

## Common pitfalls ##
  * Make sure DamnVid has read/write access to the specified configuration directory. For example, on Windows Vista and above, DamnVid does not have write access to `C:\Program Files\DamnVid\portableConf`, so don't put your configuration there, or edit the folder's permissions to allow all users to write to that folder.
  * Also keep in mind that DamnVid stores videos in the user's Videos directory by default. You can change this in DamnVid's preferences so that it puts them on your thumb drive, but this is not always recommended, because thumb drives usually have slow read/write speeds, thus crippling DamnVid and your thumb drive itself with activity. Instead, you should move the videos from the Videos folder to your thumb drive once they are done downloading/converting.