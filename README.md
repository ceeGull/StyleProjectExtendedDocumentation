# Style Project Configuration (Complete)
This is a project that attempts to replicate current and previous macOS versions' window decorations and application style, in the projects documentation though not everything is there, this project is a way to include all information

If you want to try this window decoration go [here](https://sourceforge.net/projects/styleproject/)
_Note: Some code in this project does some of the source code from that project here_
_[settings.h](https://sourceforge.net/p/styleproject/code/ci/master/tree/config/settings.h)_
_[settings.cpp](https://sourceforge.net/p/styleproject/code/ci/master/tree/config/settings.cpp)_

## General Options

### opacity=100
_Integer_  
Opacity for UNO parts, *NOT* enabled atm due to problems with Qt5  

### blacklist="smplayer"
_String_  
Blacklist of apps that should not get opacity if set, mostly media players should be here  

### removetitlebars=false
_Boolean_  
Hack for removing titlebars from windows in order to get the look of Mac Os Yosemite  

### titlepos=1
_Integer_  
Position of the title in the toolbar (if room for it at all), 0 = Left, 1 = Center, 2 = Right  

### hackdialogs=false
_Boolean_  
Hack for making the dialogs act more like they do in Mac Os, appearing under the titlebar or toolbar of the parent window, also shapes away the titlebar of the dialog  

### compactmenu=false
_Boolean_  
Hides the menubar and adds a button in the toolbar to popup the menu, if there is a toolbar to add it to  

### splitterext=false
_Boolean_  
Splitters are small in this style (1px height/width), this adds an invisible area outside the splitter temporarily when you hover a splitter  

### maxarrowsize=9
_Integer_  
Maximum allowed size in pixels for any arrows thats drawn  

### simplearrows=true
_Boolean_  
Use, simple triangles as arrows.  

### balloontips=false
_Boolean_  
Draw tooltips as comic a like balloons  

### palette=QString()
_String (Qt Based)_  
Palette to be used (filename, no suffix), this should only be used in presets, not directly in dsp.conf  

### animatestack=false
_Boolean_  
Animate when the topmost widget in a stack changes, ie: when the active tab changes  

### animatescroll=false
_Boolean_  
Smooth scrolling globally, known to cause trouble in certain cases, mainly dolphin  

### lockdocks=false
_Boolean_  
Locks the docks, removes the titlebar from them, cant float or close. Toggles with Ctrl+Alt+D  

### differentinactive=false
_Boolean_  
Makes the UNO part of inactive windows shaded, a'la Mac Os, also, if the toolbuttons are set to Yosemite shadow style, this changes the toolbutton appearance for inactive windows slightly  

### icontheme=QString()
_String (Qt Based)_  
Icontheme to use, must exist in one of the icontheme pats and must have a index.theme file in it, only read for presets, not global dsp.conf.  

### iconpaths=QStringList()
_String List_  
Extra paths where to look for icons, ~ means $HOME, stringlist.  

### framernd=8
_Integer_  
Roundness for frames in general, groupboxes, sunken frames... raised frames etc.  

## deco Options

### deco.buttons=0
_Integer_  
Style of the Min|Max|Close buttons, Sunken = 0, Etched = 1, Raised = 2, Yosemite = 3, Carved = 4, Rect = 5  

### deco.icon=true
_Boolean_  
Wheter or not the deco client should paint an icon in the titlebar  

### deco.shadowsize=32
_Integer_  
Size of the windowshadow for active window, inactive windows will have a smaller  

### deco.shadowrnd=5
_Integer_  
Roundness applied to the shadow  

### deco.framesize=0
_Integer_  
Size of borders for the decoration, not yet implemented in the kde5 deco  

### deco.embedded=false
_Boolean_  
CSD-a-like bullshit that embeds crap in the title area, will cause trouble, do not use  

### deco.mincolor="#FFC05E"
_Color_  
Color of minimize button #RRGGBB  

### deco.maxcolor="#88EB51"
_Color_  
Color of maximize button #RRGGBB  

### deco.closecolor="#F98862"
_Color_  
Color of close button #RRGGBB  

## pushbtn Options

### pushbtn.rnd=8
_Integer_  
Roundness of normal pushbuttons  

### pushbtn.shadow=3
_Integer_  
Shadow of normal pushbuttons  

### pushbtn.gradient="0.0:5, 1.0:-5"
_Gradient_  
Gradient of normal pushbuttons  
Check [here](https://sourceforge.net/p/styleproject/wiki/gradient/) to see how gradients work in StyleProject

### pushbtn.tinthue="-1:0"
_Gradient_  
Hue to tint normal pushbuttons with  
Check [here](https://sourceforge.net/p/styleproject/wiki/gradient/) to see how gradients work in StyleProject

## toolbtn Options

### toolbtn.rnd=8
_Integer_  
Roundness of toolbuttons  

### toolbtn.shadow=3
_Integer_  
Shadow of toolbuttons  

### toolbtn.gradient="0.0:5, 1.0:-5"
_Gradient_  
Gradient of toolbuttons  
Check [here](https://sourceforge.net/p/styleproject/wiki/gradient/) to see how gradients work in StyleProject

### toolbtn.activegradient="0.0:-5, 1.0:5"
_Gradient_  
Gradient on active/selected toolbuttons  
Check [here](https://sourceforge.net/p/styleproject/wiki/gradient/) to see how gradients work in StyleProject

### toolbtn.tinthue="-1:0"
_Gradient_  
Hue to tint toolbuttons with  
Check [here](https://sourceforge.net/p/styleproject/wiki/gradient/) to see how gradients work in StyleProject

### toolbtn.followcolors=false
_Boolean_  
If the icons on toolbuttons should be manipulated to be monochromatic and follow the palette (highly experimental and does not always produce nice results)  

### toolbtn.invertactive=false
_Boolean_  
Whether the active/checked toolbuttons should have inverted foreground/background colors a'la Mac Os  

### toolbtn.flat=false
_Boolean_  
Windows alike toolbuttons thats just icons and/or text  

### toolbtn.morph=true
_Boolean_  
When toolbtn.folcol=true, morph the icon back into its original colors on hover  

### toolbtn.normal=false
_Boolean_  
Draw all toolbuttons as normal buttons, not just those inside toolbars  

### toolbtn.mask=true
_Boolean_  
Draw toolbutton mask as a normal button, default true  

## input Options

### input.rnd=8
_Integer_  
Roundness of input boxes, lineedits and spinboxes and such  

### input.inunornd=8
_Integer_  
Roundness of inputs inside UNO  

### input.shadow=3
_Integer_  
Shadow of input boxes, lineedits and spinboxes and such  

### input.gradient="0.0:-5, 1.0:5"
_Gradient_  
Gradient of input boxes, lineedits and spinboxes and such  
Check [here](https://sourceforge.net/p/styleproject/wiki/gradient/) to see how gradients work in StyleProject

### input.tinthue="-1:0"
_Gradient_  
Hue to tint input boxes, lineedits and spinboxes and such with  
Check [here](https://sourceforge.net/p/styleproject/wiki/gradient/) to see how gradients work in StyleProject

## tabs Options

### tabs.docstyle=0
_Integer_  
Style / shape of document mode tabbar tabs, 0 = Chrome, 1 = Simple  

### tabs.selectors=true
_Boolean_  
Use selectors instead of tabs on tabwidgets  

### tabs.safari=true
_Boolean_  
Integrate the tabbars under toolbars like the Safari web browser from Mac Os does  

### tabs.rnd=4
_Integer_  
Roundness of tabs  

### tabs.shadow=3
_Integer_  
Shadow of tabs  

### tabs.gradient="0.0:5, 1.0:-5"
_Gradient_  
Gradient of tabs  
Check [here](https://sourceforge.net/p/styleproject/wiki/gradient/) to see how gradients work in StyleProject

### tabs.bargrad="0.0:-5, 1.0:5"
_Gradient_  
Gradient on document mode tabbars  
Check [here](https://sourceforge.net/p/styleproject/wiki/gradient/) to see how gradients work in StyleProject

### tabs.safrnd=4
_Integer_  
Roundness of tabs in a safari-like tabbar. Max roundness allowed 8  
safaritabs roundness capped at 8 atm, might change in the future if needed  

### tabs.closebuttonside=0
_Integer_  
Side of the tab the close button should be on, 0 = Left, 1 = Right  

### tabs.closerrnd=16
_Integer_  
Roundness of tab close button  

### tabs.docwidth=0
_Integer_  
Width/height of document mode tabbar tabs, leave blank or set to 0 for default content based size.  

### tabs.invertdocumode=false
_Boolean_  
Invert (upside down) document mode tabs like safari tabs.  

### tabs.invertdocucolor=false
_Boolean_  
Invert color of inactive document mode tabs  

## uno Options

### uno=true
_Boolean_  
If the head of the window should be integrated into one area a'la Mac Os  

### uno.gradient="0.0:5, 1.0:-5"
_Gradient_  
Gradient of the UNO area  
Check [here](https://sourceforge.net/p/styleproject/wiki/gradient/) to see how gradients work in StyleProject

### uno.tinthue="-1:0"
_Gradient_  
Hue to tint the UNO area with  
Check [here](https://sourceforge.net/p/styleproject/wiki/gradient/) to see how gradients work in StyleProject

### uno.noisefactor=5
_Integer_  
How much noise the UNO area should have  

### uno.noisefile=QString()
_String (Qt Based)_  
Filename to use, files are loaded from ~/.local/share/data/dsp/, so a place a file with the name filename.png and set this to filename.png and set uno.noisestyle to -1. Image must be tileable and smaller then 0.5 megapixel.  

### uno.noisestyle=0
_Integer_  
Style of the noise on the UNO area, 0 = Generic, 1 = Brushed Metal  

### uno.horizontal=false
_Boolean_  
Whether the UNO area gradient should be horizontal instead of Vertical  

### uno.contentaware=QStringList()
_String List_  
Yosemite alike content aware toolbars, *very* experimental and expensive, veeery fast cpus/gfx cards should be fine  

### uno.contentopacity=10
_Integer_  
Opacity of the content painted in the toolbar  

### uno.contentblurradius=2
_Integer_  
Amount of blur applied to the content in the toolbar  

### uno.overlay=0
_Integer_  
Use overlays on the frames so we get 1px frame frames always for layouts w/ 0 spacing.  

## menues Options

### menues.icons=false
_Boolean_  
Show icons in menues  

### menues.gradient="0:5, 1:-5"
_Gradient_  
Gradient on menues  
Check [here](https://sourceforge.net/p/styleproject/wiki/gradient/) to see how gradients work in StyleProject

### menues.itemgradient="0.0:5, 1.0:-5"
_Gradient_  
Gradient on menuitems  
Check [here](https://sourceforge.net/p/styleproject/wiki/gradient/) to see how gradients work in StyleProject

### menues.itemshadow=0
_Integer_  
Shadow on menuitems  

## sliders Options

### sliders.size=16
_Integer_  
Size of sliders  

### sliders.dot=true
_Boolean_  
Paint a dot in the middle of the slider handles, like Mac Os pre Yosemite  

### sliders.metallic=false
_Boolean_  
the infinitely popular conical slidergradient that makes it look like metal  

### sliders.slidergradient="0.0:5, 1.0:-5"
_Gradient_  
Gradient of sliderhandles  
Check [here](https://sourceforge.net/p/styleproject/wiki/gradient/) to see how gradients work in StyleProject

### sliders.groovegradient="0.0:-5, 1.0:5"
_Gradient_  
Gradient of slidergrooves  
Check [here](https://sourceforge.net/p/styleproject/wiki/gradient/) to see how gradients work in StyleProject

### sliders.grooveshadow=0
_Integer_  
Shadow of slidergrooves  

### sliders.fillgroove=false
_Boolean_  
Fill up the groove like a progressbar to where the slider is with the highight color  

### sliders.groovestyle=0
_Integer_  
How to fill groove section of a slider, 0 = Window colored, 1 = Blend of WindowText and Window color, 2 = WindowText color  

## scrollers Options

### scrollers.size=12
_Integer_  
Size of scrollbars  

### scrollers.style=0
_Integer_  
Style of scrollbars, 0 = Yosemite alike, 1 = Pre Yosemite alike  

### scrollers.slidergradient="0.0:5, 1.0:-5"
_Gradient_  
Gradient of the slider in scrollbars  
Check [here](https://sourceforge.net/p/styleproject/wiki/gradient/) to see how gradients work in StyleProject

### scrollers.groovegradient="0.0:5, 0.5:-5, 1.0:5"
_Gradient_  
Gradient of the groove part of scrollbars, only read if style of scrollbars set to 1 (Pre Yosemite alike)  
Check [here](https://sourceforge.net/p/styleproject/wiki/gradient/) to see how gradients work in StyleProject

### scrollers.groovestyle=0
_Integer_  
How to fill groove section of a scrollbar, 0 = Window colored, 1 = Blend of WindowText and Window color, 2 = WindowText color  

### scrollers.grooveshadow=0
_Integer_  
Shadow for the groove in scrollbars to be used, only read if style of scrollbars set to 1 (Pre Yosemite alike)  

### scrollers.separator=true
_Boolean_  
Draw a separator line between the view and the scrollbar when using scrollers.style=0  

## views Options

### views.treelines=true
_Boolean_  
Draw the branches in the treeviews  

### views.itemgradient="0:5, 1:-5"
_Gradient_  
Gradient on viewitems  
Check [here](https://sourceforge.net/p/styleproject/wiki/gradient/) to see how gradients work in StyleProject

### views.itemshadow=0
_Integer_  
Shadow on viewitems  

### views.itemrnd=6
_Integer_  
Roundness of viewitems  

### views.headergradient="0:5, 1:-5"
_Gradient_  
Gradient on headers in views  
Check [here](https://sourceforge.net/p/styleproject/wiki/gradient/) to see how gradients work in StyleProject

### views.headershadow=Sunken
_Shadow Enumerator_  
Shadow for the header items if views.traditional is set  
Please refer to Shadow Options for your choices that you can make

### views.headerrnd=4
_Integer_  
Roundness of header items if views.traditional is set  

### views.opacity=0xff
_Hex_  
Opacity of views, leave at 255  

### views.traditional=false
_Boolean_  
Traditional views, no honky-ponky, just how you'd expect the views to work, you can set roundness and shadow...  

### views.rnd=4
_Integer_  
Roundness of views if views.traditional is set.  

### views.shadow=0
_Integer_  
Shadows of views if views.traditional is set.  

## progressbars Options

### progressbars.shadow=3
_Integer_  
Shadows for progressbars  

### progressbars.rnd=4
_Integer_  
Roundness for progressbars  

### progressbars.textonlyonhover=false
_Boolean_  
Text only on hover for progressbars  

### progressbars.textpos=0
_Integer_  
Text position for progressbars, 0 = Center (default), 1 = Left of progressbarcontents, 2 = Right of progressbarcontents  

### progressbars.gradient="0:5, 1:-5"
_Gradient_  
Gradient on progressbars  
Check [here](https://sourceforge.net/p/styleproject/wiki/gradient/) to see how gradients work in StyleProject

### progressbars.stripesize=32
_Integer_  
Size of stripes on progressbars  

## windows Options

### windows.gradient="0.0:-10, 0.5:10, 1.0:-10"
_Gradient_  
Gradient for windows  
Check [here](https://sourceforge.net/p/styleproject/wiki/gradient/) to see how gradients work in StyleProject

### windows.noisefactor=0
_Integer_  
How much noise to use on the window background  

### windows.noisefile=QString()
_String (Qt Based)_  
Filename to use, files are loaded from ~/.local/share/data/dsp/, so place a file with the name filename.png and set this to filename.png and set windows.noisestyle to -1. Image must be tileable  

### windows.noisestyle=0
_Integer_  
Style of the noise painted on the window background, 0 = Generic, 1 = Brushed Metal  

### windows.horizontal=true
_Boolean_  
Whether the gradient set on windows should be horizontal instead of vertical  

## shadows Options

### shadows.opacity=33
_Integer_  
Opacity of the shadows painted on widgets  

### shadows.illuminationopacity=33
_Integer_  
Opacity of the illuminated(light) parts of the shadows  

### shadows.darkraisededges=false
_Boolean_  
Whether widgets with a raised shadow should be darker around the left/right edges  

### shadows.ontextopacity=50
_Integer_  
Opacity of the textshadow/textbevel, 0 to disable (faster)  

## Shadow Options

### 0=Sunken
_Enum_  
A shadow intended to make the control look as if below window surface."  

### 1=Etched
_Enum_  
A shadow intended to look etched into the window."  

### 2=Raised
_Enum_  
A shadow intended to make the control look raised above the window."  

### 3=Yosemite
_Enum_  
A 'shadow' (more like a rectangle) to loosely mimic the look of the mac os yosemite 'shadows' - unrecommended, looks dull and bland."  

### 4=Carved
_Enum_  
A shadow 'inspired' the the ever popular 'rhino' style for mac os",    
rhino like  

### 5=Rect
_Enum_  
A simple rectangle, mostly internally used.",      
simple rounded rectangle, no honky-ponky  

### 6=ElCapitan
_Enum_  
A 'shadow' (more like rectangle) to loosely mimic the look of the mac os elcapitan 'shadows' - unrecommended, looks dull and bland."  

### 7=SemiCarved
_Enum_  
Same as carved but less margins.  

