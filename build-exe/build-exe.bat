@echo Packaging DamnVid for win32.
@echo ----------------------------
@cd ..
@echo Trying to delete old setup, if any.
@del /q DamnVid-setup*
@echo Building list of required files.
@python build-any/build-required-files.py
@echo Creating /package/ directory.
@mkdir package
@echo Switching to /package/ directory.
@cd package
@echo Compyling DamnVid.
@python ..\build-exe\py2exe-win32.py py2exe --package encodings
@echo Running UPX --brute on compyled executable.
@upx --brute dist\DamnVid.exe
@echo Switching to /package/dist/ directory.
@cd dist
@echo Packaging with NSIS.
@python ..\..\build-exe\build-nsi.py
@"C:\Program Files\NSIS\makensis.exe" -V4 -NOCD ..\..\NSIS-win32.nsi
@echo Switching back to root directory.
@cd ..\..
@echo DamnVid packaged. Cleaning up.
@rmdir package /s /q
@del /q NSIS-win32.nsi
@del /q required-files.txt
@echo Renaming setup.
@set /p version= < version.damnvid
@ren DamnVid-setup.exe DamnVid-setup-%version%.exe
@python build-any/cleanup.py
@echo All done.
@pause