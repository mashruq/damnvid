@echo Packaging DamnVid for win32.
@echo ----------------------------
@echo Trying to delete old setup, if any.
@del /q ..\DamnVid-setup*
@echo Switching to /package/dist/ directory.
@cd ..\package\dist
@echo Packaging with NSIS.
@%python%\python -OO ..\..\build-exe\build-nsi.py
@makensis -V4 -NOCD ..\..\NSIS-win32.nsi
@echo Switching back to root directory.
@cd ..\..
@echo DamnVid packaged.
@echo Renaming setup.
@set /p version= < version.d
@ren DamnVid-setup.exe DamnVid-setup-%version%.exe
@echo Cleaning up.
@%python%\python -OO build-any/cleanup.py
@cd build-exe
@echo All done.
@pause
