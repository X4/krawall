#!/usr/bin/env python
import os, sys, datetime
from dbus import SessionBus
from PyKDE4.kdecore import KConfig, KConfigGroup
from PyKDE4.kdeui import KGlobalSettings
kGlobalSettings = KGlobalSettings.self()
# tell all KDE apps to recreate their styles to apply the setitngs
kGlobalSettings.emitChange(KGlobalSettings.StyleChanged)
kGlobalSettings.emitChange(KGlobalSettings.SettingsChanged)
kGlobalSettings.emitChange(KGlobalSettings.ToolbarStyleChanged)
kGlobalSettings.emitChange(KGlobalSettings.PaletteChanged)
kGlobalSettings.emitChange(KGlobalSettings.FontChanged)
kGlobalSettings.emitChange(KGlobalSettings.IconChanged)
kGlobalSettings.emitChange(KGlobalSettings.CursorChanged)

print 'Telling Kwin to reload its config'
os.system("dbus-send --dest=org.kde.kwin /KWin org.kde.KWin.reloadConfig")

print 'Telling plasma to reload its config'
plasma = SessionBus().get_object('org.kde.plasma-desktop','/MainApplication')
plasma.reparseConfiguration()