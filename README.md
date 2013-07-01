krawall
=======

Experimental Wallpaper Changer that works with most desktops.

#### Supported:
  * KDE 3
  * KDE 4
  * Gnome 2
  * gnome 3
  * i3 and xmonad
  * XFCE
  * Enlightenment

#### Required:
  * find, cat, cp, rm, shuffle, mkdir, touch, convert, awk, sed, identify

#### Requirement depends on Desktop Environment:
  * kdialog, feh, gsettings, dcop, enlightenment_remote, edje_cc

#### Usage: ./krawall [arguments]
      -p (--prev)           Show previous Wallpaper
      -n (--next)           Show next Wallpaper
      -s (--rescan)         Rescan Wallpaper directories
      -r (--resort)         Randomize Wallpaper list
      -z (--random)         Rescan and Randomize Wallpaper directories

      --xfce                Setup for the XFCE4-Desktop
      --hacker              Setup for the i3 or xmonad Desktop
      --gnome2              Setup for the GNOME2-Desktop
      --gnome3              Setup for the GNOME3-Desktop
      --kde3                Setup for the KDE3-Desktop
      --kde4                Setup for the KDE4-Desktop (experimental)
      --edesk               Setup for the Enlightenment Desktop

##### XFCE Example:
      ./krawall --xfce -p # should return the previous wallpaper in the stack
      ./krawall --xfce -n # should return the next wallpaper in the stack

#### HowTo:
 Add a new GlobalHotkeys to your preferred _buttons_ and run *krawall* as required.
 There are other ways to invoke this script: Button and Keypresses, Plasmoids, Events..
 You can use the tools given by your Desktop Environment to invoke this script.

#### Caveat
For KDE4 you currently have to set your wallpaper manually per desktop to:
    $WALLPAPER_PATH/krawall/$DESKTOP_NUMBER


#### TODO:
     [ ] Rewrite the kde4 part in cpp and use of the API
     [ ] Get --prev --next working with reliable history (rewrite to use sqlite)
     [x] Switch to different Wallpaper on each Virtual-Desktop (Only for e17 atm).
     [x] Get the call_enlightenment function to work for the Enlightenment Desktop.
     [x] Get the call_kde4 function for KDE4 to work without a restart of the plasma desktop. run some ./qt_cpp maybe?
     [x] I think I should cache the result of $WALLPAPER for faster switching of wallpapers.
