# Introduction #

This page is meant to be read by [developers, developers, developers, developers](http://www.youtube.com/watch?v=KMU0tzLwhbE) only. [Python](http://python.org/) developers, to be precise, because DamnVid modules are written in [Python](http://python.org/).

# Requirements #

  * Good knowledge of Python. "Good" as in knowing the basics, the syntax, and some of the packages included with Python like `urllib2`, `re`, `time`, `os`, etc.
  * This page. Yes, really.
  * A video site, for which you want to write a module.
  * A 72x72 PNG icon for your module, and a 16x16 PNG icon for your site. Usually, the same image is used for both. Alpha transparency is okay.
  * Skills in at least one of these areas (From one site to the other, the skill required varies. Some site can be easily figured out by packet analysis, others will require Flash decompilation and Actionscript knowledge):
    * Network packet analysis
    * JavaScript
    * Actionscript
  * The Python interpreter, version 2.5 (or 3.0, as the module packaging script should work with it too). You can get that [here](http://python.org/download/).
  * [DamnVid's module packaging script](http://code.google.com/p/damnvid/source/browse/trunk/build-any/module-package.py). You can grab the latest revision from [the SVN repository](http://code.google.com/p/damnvid/source/checkout), or by clicking [here](http://code.google.com/p/damnvid/source/browse/trunk/build-any/module-package.py).
  * Time!

# Getting to work #

First, let's get an idea of the what a DamnVid module looks like, shall we?
A DamnVid module is actually a gzipped tar archive in which there is only one folder, bearing the name of the module. In this folder are all of the module's required files, and a special file named `modulename.damnvid` (where `modulename` is the module's name), which is a Python script that DamnVid executes to register the module.
But rather than this boring explanation, let's take a more visual example. This is what the crunchyroll module looks like:
<table><tr>
<td><img src='http://damnvid.googlecode.com/svn/trunk/modules/crunchyroll/crunchyroll-large.png' /></td>
<td>
<code>crunchyroll-1.0.module.damnvid</code>: tar archive, containing:<br />
<code>/crunchyroll</code>: directory<br />
<code>/crunchyroll/icon-large.png</code>, 72x72 PNG icon for the module, viewable <a href='http://damnvid.googlecode.com/svn/trunk/modules/crunchyroll/crunchyroll-large.png'>here</a>.<br />
<code>/crunchyroll/icon.png</code>, 16x16 PNG icon for the Crunchyroll site, viewable <a href='http://damnvid.googlecode.com/svn/trunk/modules/crunchyroll/crunchyroll.png'>here</a>.<br />
<code>/crunchyroll/crunchyroll.damnvid</code>, Python script describing the module, viewable below.<br>
</td>
</tr></table>
Here are the contents of `crunchyroll/crunchyroll.damnvid`:
```
#~DamnVid-module:crunchyroll

class DamnModule_Crunchyroll(DamnVideoModule):
    def __init__(self,uri):
        DamnVideoModule.__init__(self,uri)
        self.name='crunchyroll'
        self.regex={
            'url':re.compile('crunchyroll\.com/media-(\d+)/?',re.IGNORECASE),
            'title':re.compile('<title>[^-<>"]*-\s*([^"<>]+)</title>',re.IGNORECASE),
            'ticket':re.compile('crunchyroll.com%2Fgetitem%3Fvideoid%3D(\w+)%26amp%3Bmediaid%3D(\w+)%3C%2Ffile%3E',re.IGNORECASE)
        }
        self.valid=self.regex['url'].search(uri)
        if self.valid:
            self.id='cr:'+self.valid.group(1)
            self.link='http://www.crunchyroll.com/media-'+self.valid.group(1)+'/'
    def renewTicket(self):
        if self.ticket is not None:
            return
        html=urllib2.urlopen(self.link+'?h264=1')
        for i in html:
            res=self.regex['ticket'].search(i)
            if res:
                self.newTicket('http://www.crunchyroll.com/getitem?videoid='+res.group(1)+'&mediaid='+res.group(2))
DamnRegisterModule({
    'name':'crunchyroll',
    'title':'Crunchyroll',
    'type':'video',
    'version':'1.0',
    'author':{
        'name':'Etienne Perot',
        'email':'admin@biringa.com',
        'url':'http://biringa.com/'
    },
    'icon':{
        'small':'crunchyroll.png',
        'large':'crunchyroll-large.png',
    },
    'about':{
        'short':'DamnVid module for Crunchyroll.',
        'long':"""This is a video plugin for DamnVid that adds video downloading capabilities from Crunchyroll.""",
        'url':'http://code.google.com/p/damnvid/wiki/Modules'
    },
    'sites':[
        {
            'title':'Crunchyroll',
            'icon':'crunchyroll.png',
            'url':'http://www.crunchyroll.com/anime'
        }
    ],
    'class':DamnModule_Crunchyroll,
    'preferences':{
        'profile':{
            'name':'Default profile',
            'type':DV.preference_type_profile,
            'kind':'profile',
            'strict':True,
            'default':3
        },
        'outdir':{
            'name':'Output directory',
            'type':DV.preference_type_misc,
            'kind':'dir',
            'strict':True,
            'default':'?DAMNVID_MY_VIDEOS?/DamnVid/Crunchyroll/'
        }
    },
    'preferences_order':['profile','outdir'],
    'register':{
        'listicons':{
            'crunchyroll':'crunchyroll.png'
        }
    }
})
```
The first thing you should notice is: oh look, there's more metadata than actual code! And you'd be correct: though this example is a bit simplistic, most modules don't have a lot of code. Now, let's go through that code.

## Pseudo-shebang ##

The first line of the script is a pseudo-[shebang](http://en.wikipedia.org/wiki/Shebang_(Unix)) that looks like this:
```
#~DamnVid-module:modulename
```
where modulename is the name of your module (more on that in the metadata section). This will help the module packaging script figure out what file is your module description file.

## Metadata ##

As you probably noticed, the metadata is a huge [Python dictionary](http://docs.python.org/tutorial/datastructures.html#dictionaries), passed as argument to the `DamnRegisterModule` function, which you don't really need to care about. You do not to call it, though, as it register your module (obviously). It takes one argument, the metadata dictionary. Let's go through it.
```
DamnRegisterModule({ # Call to the DamnRegisterModule function, with the metadata dictionary as argument.
    'name':'crunchyroll', # This is the name of your module. Please note: the NAME is an alphanumeric, all-lowercase name for your module. The user will never actually see this. It is only used by DamnVid, to manage modules.
    'title':'Crunchyroll', # This is the title of your module, the user-friendly version of the name, that your users will see. This may contain any Unicode character.
    'type':'video', # This is the module type. Currently, only video modules are supported.
    'version':'1.0', # This is the version of your module.
    'author':{ # This is a sub-dictionary with info about you, yourself, and you.
        'name':'Etienne Perot', # This is your name...
        'email':'admin@biringa.com', # ... and this is your email (optional)...
        'url':'http://biringa.com/' # ... and this is your website (optional as well).
    },
    'icon':{ # This is a sub-dictionary containing two entries about your module's icons.
        'small':'crunchyroll.png', # This is the small icon (the 16x16 one), visible on the left pane of the Preferences panel.
        'large':'crunchyroll-large.png', # This is the large icon (the 72x72 one), visible on the right pane of the Preferences panel when the user is on the "Modules" pane, or on your module's own configuration page.
    },
    'about':{ # This is some extra info about your module.
        'short':'DamnVid module for Crunchyroll.', # This is a short description for your module. It will appear on the Modules panel. May span multiple lines, but this is not recommended, as this description is supposed to be short.
        'long':"""This is a video plugin for DamnVid that adds video downloading capabilities from Crunchyroll.""", # This is a longer description for your module. It will appear on your module's own configuration panel. This may span as many lines as you want, and may describe your module's preferences in greater detail.
        'url':'http://code.google.com/p/damnvid/wiki/Modules' # This is the URL of the page DamnVid will fetch to grab update information about your module. It is also the page where the user will be sent to if (s)he clicks your module's title. More on that later.
    },
    'sites':[ # This is an array of video websites that your module supports. Each item of the array is a dictionary containing information about a site. These sites show up in the "Add URL..." dialog, on the bottom-left pane.
        {
            'title':'Crunchyroll', # This is the title of the website.
            'icon':'crunchyroll.png', # This is its icon, 16x16, which will show up next to the title. Note: It is possible to reuse the same icons for multiple purposes, as done here.
            'url':'http://www.crunchyroll.com/anime' # This is the website's URL, where the user will be sent to if he clicks on the site's title. If the website has a "Videos" page or a "Browse" page, link to that page. Always link to the as-close-to-videos-as-possible page.
        } # This module supports only one website, so the array contains only one dictionary.
    ],
    'class':DamnModule_Crunchyroll, # This is the class that handles all the module's code and functionality. Note that there are no quotation marks; it's not the name of the class that's passed, it is the class itself.
    'preferences':{ # Your module is configurable! This is a dictionary that describes your module's preferences.
        'profile':{ # This is the description of the "profile" preference. Each key of the "preferences" dictionary is a preference name (that your user will never see).
            'name':'Default profile', # This is the user-friendly TITLE (yes, not name, sorry for the weird naming... titling? Argh) of the preference, the one that your user will see.
            'type':DV.preference_type_profile, # This may be called "type", it actually represents the location on the configuration panel where your preference will be placed. More on that later.
            'kind':'profile', # This is the preference kind, its type, its nature, whatever you wanna call it. More on that later as well.
            'strict':True, # This option can have different meanings, depending on the "kind". More on that later.
            'default':3 # This is the default value for this preference. Notice that this is a 3. More on that later as well.
        }, # End of preference!
        'outdir':{
            'name':'Output directory',
            'type':DV.preference_type_misc, # Notice that this is not the same as the other pref
            'kind':'dir', # Directory
            'strict':True,
            'default':'?DAMNVID_MY_VIDEOS?/DamnVid/Crunchyroll/' # Notice the "?DAMNVID_MY_VIDEOS?" alis, which always points to the user's My Videos (or Movies on OS X) folder.
        }
    },
    'preferences_order':['profile','outdir'], # This is the order in which the preferences will show up in the panel (optional).
    'register':{ # This is a dictionary of little resources that your module might need at runtime.
        'listicons':{ # This is a dictionary of icons to show in DamnVid's main video list when the user adds a video that this module can handle.
            'crunchyroll':'crunchyroll.png' # Each key is a meaningful name for the icon. Each value is the actual path to the icon. Once again, the same 16x16 icon has been used.
        }
    }
}) # Tada!
```
Whew, that was long. But it's not over yet. Let's go through the details now.
  * about/url: The URL of your module has to be both a user-friendly webpage and a DamnVid-friendly webpage (pleasing both humans and machines. It's never been easy). Basically, what that means is that this page must inform your user about the module, what it does, where to get it, etc; and it must inform DamnVid about it too. To do so, you must include some code that matches the following regex:
```
<tt>module_name_here</tt>.*?Latest\s+version\s*:\s*<tt>([^<>]+)</tt>.*?Available\s+at\s*:\s*<a href="([^"]+)"
```
> In practice, it comes down to including this line in your HTML code:
```
<tt>module_name_here</tt> Latest version: <tt>1.0</tt> Available at: <a href="http://mymodule.com/module_download_url_here.module.damnvid">http://mymodule.com/module_download_url_here.module.damnvid</a>
```
> That's it. Please note that you don't need to actually make that show up on the page. You can totally put that code between HTML comments `<!-- like so -->`, DamnVid will handle it just fine.
  * profile/type: This may be one of 4 values:
    * `DV.preference_type_video`
    * `DV.preference_type_audio`
    * `DV.preference_type_profile`
    * `DV.preference_type_misc`
> What is the point? Well, DamnVid's preferences panes are organized like so:
<table cellpadding='15' border='1' cellspacing='3'>
<tr><td align='center'>Video pane<br /><code>DV.preference_type_video</code></td><td align='center'>Audio pane<br /><code>DV.preference_type_audio</code></td></tr>
<tr><td align='center'>Profile pane<br /><code>DV.preference_type_profile</code></td></tr>
<tr><td align='center'>All the rest<br /><code>DV.preference_type_misc</code></td></tr>
</table>
> So, setting the type will locate your preference in one of these four panes. If you don't care, just put them all in misc.
  * profile/kind: This is one of the following values:
    * `'bool'`: A boolean, represented by a checkbox. Default may be `True` or `False`. Please note that when coding your class later, bool preferences are returning as strings, not actual booleans. Therefore, to do an `if` check, you'd need something like `if pref=='True':`. When putting boolean preferences, you also need to add the "align" key to that preference's dictionary. "align" is a boolean; if false, the checkbox will simply sit there against the left edge of its panel; otherwise, the label will sit on the right half of the horizontal space reserved to the checkbox, while the checkbox itself will be right-aligned on the left half of that horizontal space. It's easier to understand with a table, where `[x]` is a checkbox: <table cellpadding='2' border='1' cellspacing='0'><tr><td width='50%' align='right'>A preference:</td><td width='50%' align='left'><code>[ Textbox ]</code></td></tr><tr><td width='50%' align='right'><code>[x]</code></td><td width='50%' align='left'>A boolean preference with <code>align==True</code></td></tr><tr><td width='100%'><code>[x]</code> A boolean preference with <code>align==False</code></td></tr><tr><td width='50%' align='right'>Another preference:</td><td width='50%' align='left'><code>[ Textbox ]</code></td></tr></table>
    * `'text'`: Just a piece of text, represented by a textbox. Default may be any string.
    * `'int:0-24'`: An integer (here, between 0 and 24), represented by a slider. Default may be any integer between the accepted range. Once again, preferences are always returned as strings, so use `int(pref)` to grab the integer. The range part is optional; you can put `'int'` if you want. In this case, a textbox will be used rather than a slider.
    * `'intk:5-10'`: A kilo-int! This is actually a dropdown box from which the user may select one of the automatically generated options. These options are simply each power of two (here, from 2<sup>5</sup>=32 to 2<sup>10</sup>=1024) with a "k" afterwards (so, from 32k to 1024k in this case). Useful for selecting bitrates. Please note that these are always strings since they contain the letter "k". Default may be any accepted value (as a string, with a k afterwards, like so: `'128k'`). The `strict` parameter, if set to `False`, will let the user type any text in the dropdown box.
    * `'%256'`: A percentage. To the user, it is perceived as a percentage, but to the code, it is perceived as a floating-point number from 0 to 256 in this case. To get a real percentage, use `'%100'`.
    * `'dir'`: A directory. You don't have to handle the "Browse..." button or resolve directories, DamnVid does all the heavy lifting for you. Even when getting/setting the preference, you don't have to worry about aliases and stuff. The available alias is `?DAMNVID_MY_VIDEOS?`, which refers to "My Videos" on Windows XP or lower, "Videos" on Windows Vista, "~/Videos" on `*`nix, and "~/Movies" on OS X. Do not worry about path separators, DamnVid does that for you too (ain't it nice?). Default may be any path, which may include the `?DAMNVID_MY_VIDEOS?` alias. Default paths should always be written with slashes (`/`) as path separators.
    * `'profile`': An encoding profile (yeah, really). Please note that encoding profile are saved internally as integers, so the default value has to be a integer. Here are the default profiles (in bold are the profiles you're most likely to pick as default): **`-1`: "(Do not encode)"**; `0`: "DamnVid default"; `1`: "iPod-compatible"; `2`: "PSP-compatible"; **`3`: "Online video"**; `4`: "Ultra high quality"; **`5`: "High-definition (720p)"**; `6`: "All-free video"; `7`: "Flash video"; **`8`: "MP3 (audio only)"**.
    * `dictionary`: If you use a dictionary as `kind`, DamnVid will treat that as a dropdown box containing all the values of your dictionary. However, when getting/setting the preference, it's your dictionary's keys that will be used. With dictionaries, the `strict` key must be set in your preference's dictionary. If `True`, the user will have no choice but to pick one of the options from the menu. If `False`, the user will be able to type in any value. If that value correspond to one of your dictionary's values, the corresponding key will be returned when getting the preference's value. You also have to set the `order` key in your preference's dictionary. `order` is an array of strings; each string is one of your dictionary's keys. `order`, as the name implies, sets the order of the options in the dropdown box, just like `preference_order` in your module's metadata dictionary. Default may be any of your dictionary's keys, or any string if `strict` is `False`.
  * You can also set the `'noedit'` key in your preferences to hide it from your configuration panel. It is useful for preferences that only your module modifies internally, or for long-term storage.

That's it for the preferences and all metadata-related matters, now let's get coding.

## The module class ##
Let's take another look at the Crunchyroll class:
```
class DamnModule_Crunchyroll(DamnVideoModule):
    def __init__(self,uri):
        DamnVideoModule.__init__(self,uri)
        self.name='crunchyroll'
        self.regex={
            'url':re.compile('crunchyroll\.com/media-(\d+)/?',re.IGNORECASE),
            'title':re.compile('<title>[^-<>"]*-\s*([^"<>]+)</title>',re.IGNORECASE),
            'ticket':re.compile('crunchyroll.com%2Fgetitem%3Fvideoid%3D(\w+)%26amp%3Bmediaid%3D(\w+)%3C%2Ffile%3E',re.IGNORECASE)
        }
        self.valid=self.regex['url'].search(uri)
        if self.valid:
            self.id='cr:'+self.valid.group(1)
            self.link='http://www.crunchyroll.com/media-'+self.valid.group(1)+'/'
    def renewTicket(self):
        if self.ticket is not None:
            return
        html=urllib2.urlopen(self.link+'?h264=1')
        for i in html:
            res=self.regex['ticket'].search(i)
            if res:
                self.newTicket('http://www.crunchyroll.com/getitem?videoid='+res.group(1)+'&mediaid='+res.group(2))
```
So yeah, it's a [Python class](http://docs.python.org/tutorial/classes.html), alright. It is called `DamnModule_Crunchyroll`; please pseudo-namespace your classes with `DamnModule_`. The rest of the class name is up to you; here, it is not exactly the module name, as the C is capitalized. Doesn't matter much, just use your common sense and figure out a class name that won't collide with others.
You'll notice that this class inherits from the DamnVideoModule class. Indeed, our module is a video module, remember?
```
class DamnVideoModule: # The class!
    def __init__(self,uri): # The constructor. Always called with a "URI" parameter.
        self.name='generic' # This is your module's name. Since it is probably not "generic", you should first call DamnVideoModule.__init__ in your module's __init__, then override self.name later on in your module's __init__.
        self.uri=uri
        self.link=None # Define this in your module's __init__. A (unique) link to the video.
        self.id=None # Define this in your module's __init__. A unique string for your video. Most commonly, a two-letter-and-semicolon prefix'd ID, like so: "yt:WkKa4xfiYA4", which stands for http://www.youtube.com/watch?v=WkKa4xfiYA4
        self.valid=None # Define this in your module's __init__. A boolean-like object, True if your module can handle the provided URI.
        self.title=None # Define this in your module's getTitle. A unicode string, the video's title.
        self.ticket=None # Define this in (re)newTicket.
        self.ticketdate=0 # Same as the line above
        self.regex={ # This is a regex dictionary. Fill it like you want, but conventionally:
            # There's a 'url' regex here that matches all URLs that this module can handle
            'title':DV.generic_title_extract # A title regex
            # One or more 'ticket' regex(es) here that are used to grab a ticket.
        }
    def isUp(self): # Don't override this. Just a check.
        return True
    def validURI(self): # Determines whether the module can handle the provided URI.
        return not not self.valid # See, it returns self.valid as a boolean.
    def getLink(self): # Returns self.link, you shouldn't have to override this
        return self.link
    def getURI(self): # Returns self.uri, you shouldn't have to override this
        return self.uri
    def getID(self): # Returns self.id, you shouldn't have to override this
        return self.id
    def getStorage(self): # Returns a class-wide (not instance-wide!) shared dictionary object in which you can store whatever you want, it will be kept in memory until DamnVid is closed. For more permanent storage, use preferences, eventually with the noedit flag.
        return DV.modulesstorage[self.name]
    def getTitle(self): # This function returns the video title. If your title regex is defined and can grab the video title from the self.link page, you shouldn't have to override this unless you want to grab additional information from the page at the same time.
        if self.title is None: # If the title hasn't been figured out yet...
            html=urllib2.urlopen(self.link) # Open self.link, grab the page, store it in total
            total=''
            for i in html:
                total+=i
            res=self.regex['title'].search(total) # Find matches with the 'title' regex
            if res: # If there was a match
                self.title=DamnHtmlEntities(res.group(1)) # Set title
        if self.title is not None: # If title has been set
            return self.title # Return it
        return u'Unknown title' # Else return generic title
    def getIcon(self): # This returns the icon to use in the video list. Override if your module uses multiple icons, conditionally.
        return DamnGetListIcon(self.name) # Use the DamnGetListIcon function with the icon name you defined in the metadata to grab the icon ID associated to it.
    def pref(self,pref,value=None): # This is the preference manager function. You shouldn't override this.
    # Usage: self.pref('somepref') returns somepref
    # self.pref('somepref','somevalue') sets somepref to somevalue.
        if value is None:
            return DV.prefs.getm(self.name,pref)
        return DV.prefs.setm(self.name,pref,value)
    def newTicket(self,ticket): # When you've got a new ticket, call this function and it will store it for you.
        self.ticket=ticket
        self.ticketdate=time.time()
    def getProfile(self): # This returns the encoding profile to use for the video.
        return self.pref('profile') # Usually, there's only one profile, and it's stored in the 'profile' preference. Just return it.
        # If your module has multiple profiles (for instance, YouTube has a "normal" profile and an "HD" profile), override this.
    def getOutdir(self): # Same as above, but for the output directory, the directory where the video will be saved.
        return self.pref('outdir')
    def renewTicket(self): # Override this. In this function:
        if self.ticket is None: # First check if the ticket hasn't already been acquired, and if it's recent enough, in case it expires. If it's available, return.
            # Otherwise, grab a ticket using some obscure means and...
            self.newTicket(self.uri) # Call the newTicket function with your newly-acquired ticket.
    def getDownload(self): # This function returns the direct download URL.
        self.renewTicket() # At first, it tries to renew the ticket, is needed (renewTicket takes care of not wasting time if it's not necessary).
        return self.ticket # Then it returns the ticket (direct download URL).
        # You should override renewTicket rather than this method in order to store the final download URL.
    def getFFmpegArgs(self): # This returns an array of additional arguments for ffmpeg.
        return [] # For example, Revver needs a few additional stream mappings, so it adds -map 0:6, etc.
    def getDownloadGetter(self): # This returns the function that will be called to get the final, direct download URL. Usually, it's self.getDownload(), but sometimes you may want to pass arguments to it.
        return self.getDownload # No parentheses, remember? Return the function, not the result of the function.
    def addVid(self,parent): # This will be called by the DamnVideoLoader thread. Override this if you want to add more than one video.
        parent.addValid(self.getVidObject())
    def getVidObject(self): # Do not override this unless you know what you're doing. This is the video object passed to the DamnVideoLoader thread.
        return {'name':self.getTitle(),'profile':self.getProfile(),'profilemodified':False,'fromfile':self.getTitle(),'dirname':self.getLink(),'uri':self.getID(),'status':'Pending.','icon':self.getIcon(),'module':self,'downloadgetter':self.getDownloadGetter()}
```
Take a look again at the DamnModule\_Crunchyroll class and it should all make sense:
```
class DamnModule_Crunchyroll(DamnVideoModule):
    def __init__(self,uri):
        DamnVideoModule.__init__(self,uri) # First, let the DamnVideoModule's __init__ constructor kick in
        self.name='crunchyroll' # Override self.name
        self.regex={ # Override self.regex
            'url':re.compile('crunchyroll\.com/media-(\d+)/?',re.IGNORECASE), # A little url regex... You don't need to check if the URL is a valid HTTP address, DamnVid already checks that.
            'title':re.compile('<title>[^-<>"]*-\s*([^"<>]+)</title>',re.IGNORECASE), # A little title regex... To reuse the DamnVideoModule's title regex, you could just use: 'title':self.regex['title'],
            'ticket':re.compile('crunchyroll.com%2Fgetitem%3Fvideoid%3D(\w+)%26amp%3Bmediaid%3D(\w+)%3C%2Ffile%3E',re.IGNORECASE) # A little ticket regex.
        }
        self.valid=self.regex['url'].search(uri) # self.valid is actually a regex match result, but it acts as a boolean too:
        if self.valid: # See?
            self.id='cr:'+self.valid.group(1) # Set unique ID.
            self.link='http://www.crunchyroll.com/media-'+self.valid.group(1)+'/' # Set permalink
    def renewTicket(self): # renewTicket function, called by getDownload
        if self.ticket is not None: # If ticket has already been grabbed...
            return # Stop right there, no need to grab it again.
        html=urllib2.urlopen(self.link+'?h264=1') # Otherwise, grab this page...
        for i in html: # Go through it...
            res=self.regex['ticket'].search(i) # Search for matches with the ticket regex
            if res: # If there's a match
                self.newTicket('http://www.crunchyroll.com/getitem?videoid='+res.group(1)+'&mediaid='+res.group(2)) # Save the ticket!
```
As you can see, only two functions had to be overwritten. That's the beauty of inheritance.

DamnVid offers some handy functions available to use by modules:
  * `DamnHtmlEntities(html)`: Returns a unicode string with HTML entities decoded.
  * `DamnGetListIcon(icon)`: Returns the icon ID associated with the corresponding `icon`. Once you register an icon with the `register` metadata dictionary, use it here.
  * `DamnGetAlternateModule(uri)`: If your video site actually embeds video from other video websites, you can try this function with the URI of the embedded video. DamnVid will attempt to return an instance of another module class than can handle the provided URI, allowing you to work its magic inside your own module. (Hint: use the returned module's .getDownloader()() function, double parentheses, because you must execute the function returned from the execution of the getDownloader function!)
  * `DamnURLPicker(urls,urlonly=False)`: Returns the first valid URL from the array `urls`. (i.e. no HTTP error) If `urlonly` is `False`, returns a pipe object to that URL. If `urlonly` is `True`, returns the valid URL.
  * `DamnURLPickerBySize(urls,array=False)`: Fetches all URLs in the `urls` array, and sorts them by file-size using the Content-Length HTTP header. If `array` is `True`, returns the sorted array, from heaviest to lightest URL. If `array` is `False`, returns only the first element of the sorted array. If a URL doesn't provide Content-Length information, it is considered 0 and is put at the tail of the array. This function is useful if you have multiple download streams and want to pick the highest-quality one (even though better quality doesn't necessarily mean larger file), but use it with parsimony, as it is time-consuming to fetch all these URLs. If you can sort URLs by other means, do so without this function.
  * `DamnTempFile()`: Returns the path of a writable, guaranteed-not-to-exist temporary file.
  * `DamnCurry(func,*args,**kwargs)`: Returns a callable function with pre-set arguments. See http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/52549 for details.
You can use all of these functions into your code.
That's it for the module class.

## Other files ##

You may place any file your module may need in your module's directory. However, to reduce file size, do not forget to run your PNGs through [http://pmt.sourceforge.net/pngcrush/](pngcrush.md), with the following arguments: `pngcrush -rem gAMA -rem cHRM -rem iCCP -rem sRGB -brute icon1_tobecrushed.png icon1.png`.

# That's all folks #

Happy coding!