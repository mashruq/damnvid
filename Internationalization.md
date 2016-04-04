# Introduction #
DamnVid can be translated to other languages. Translating requires fluent language skills in the language you want to translate DamnVid in.

# Details #
Do you love DamnVid _AND_ have a few hours to spare _AND_ have good language skills? Let's get started.
  * First, contact Etienne (post a comment here) and ask. Specify the language you want to translate DamnVid to, and add contact info so that Etienne can get back to you.
  * Once you have received agreement, open `English.locale` in DamnVid's locale directory (`%DAMNVID%/locale`, where `%DAMNVID%` is DamnVid's installation directory) as a text file, with your favorite text editor. The file should look like this:
```
DV.languages['English']={
    'title':'English',
    'author':'Etienne Perot',
    'strings':{
        'locale:damnvid-profile-explanation':u'An encoding profile is a set of encoding preferences used to encode videos.'
        'Videos':'Videos',
        ...
    }
}
```
  * Edit the part where it first says `English` to the name of your language, in **ASCII characters only**. The `title` however can contain Unicode, but prepend a `u` before the string in this case. Same goes for the `author`.
  * Go through each string in the `'strings'` part. Each line is in this format:
```
        'string identifier':u'Translated string',
```
  * Replaced `Translated string` by the translation in your language. Be sure to keep the `u` in front of the string.
  * Escape apostrophes with `\`, like so:
```
        'I am fine':u'J\'vais bien',
```
  * Escape backslashes (`\`) with another backslash.
  * You can insert linebreaks with `\n`.
  * Make sure to preserve all parentheses and extra spaces on both sides of the string identifier. For example, for the string `'). The latest version is '`, do not forget the parenthesis and the space at the end.

Once you are done, save your locale file as `MyLanguageName.locale` in the same directory as `English.locale`. (Re-)Start DamnVid and your language should appear in the preferences. Select it and restart DamnVid (again). You should now be able to use DamnVid in your language. Test every corner of DamnVid and look for missing translations. Check `DamnVid.log` in DamnVid's preferences folder (`%APPDATA%\DamnVid` on Windows, `~/.damnvid` on Linux, `~/Library/Preferences/DamnVid` for Mac OS X) for any line containing "Locale warning" or "Locale error". DamnVid does _not_ warn you about them while it is running and quietly falls back to English whenever there is an error, so make sure you check that file even if everything seems fine.

When you are sure that there is nothing left to translate, send your `.locale` file to Etienne; he will add it to DamnVid's language list and your language will be available in the next DamnVid version! And thanks for translating DamnVid.