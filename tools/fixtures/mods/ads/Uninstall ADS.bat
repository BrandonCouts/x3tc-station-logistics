@echo off
cls
color 0C  
echo   ================================================================
echo   == [SCRIPT] ANARKIS DEFENSE SYSTEM - UNINSTALLER              ==
echo   ================================================================
echo   ==                                                            ==
echo   == This will delete all anarkis defense system files          ==
echo   == Press a key to continue or close this window to cancel.    ==
echo   ==                                                            ==
echo   ================================================================
echo   ==                       Serial Kicked / [Anarkis Federation] ==
echo   ================================================================
echo.
pause>nul
cls
echo   ================================================================
echo   == [SCRIPT] ANARKIS DEFENSE SYSTEM - UNINSTALLER              ==
echo   ================================================================
echo.
echo      - Deleting Script Files
del .\scripts\anarkis.acc.*.* >nul
del .\scripts\anarkis.ads.*.* >nul
del .\scripts\setup.anarkis.acc.xml >nul
del .\scripts\al.plugin.sk.ecs.xml >nul
echo      - Deleting Language Files
del .\t\8510-L*.xml >nul
echo      - Deleting Readme
del .\ads.readme.txt >nul
echo.
echo.
echo ADS has been succesfully removed from your computer !
echo.
echo.
pause