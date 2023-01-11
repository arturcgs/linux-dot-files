# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import subprocess
from libqtile import qtile, bar, layout, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from qtile_extras.popup.toolkit import PopupRelativeLayout, PopupImage, PopupText, PopupWidget
from qtile_extras import widget


#### OVERALL SETTINGS ####


# defining super key and terminal
mod = "mod4"
terminal = 'alacritty'

# Color theming
everforest = {  #271f2d
    "background":                    "#e9b5f9",
    "selection":                     "#28273a",
    "current_screen_border":         "#9c4b6d", # ORANGE
    "other_screen_border":           "#634e6a",
    "font_color":                    "#ffffff", # FG1  b8a3df
    "inactive_font_color":           "#8c7caa", # GREY
    "this_screen_border":            "#6c334b",

    "purple1": '#2D033B',
    "purple2": '#810CA8',
    "purple3": '#C147E9',
    "purple4": '#E5B8F4',




    "orange":                        "#ab5277",
    "grey":                          "#dbe3ff",
    "bg_blue":                       "#f0000d",
    "error":                         "#514045",
    "fg1":                           "#a07ccd",
    "red":                           "#E67E80",
    "yellow":                        "#DBBC7F",
    "green":                         "#A7C080",
    "aqua":                          "#83C092",
    "aqua1":                         "#648a6d",
    "aqua2":                         "#506e57",
    "blue":                          "#7FBBB3",
    "purple":                        "#D699B6",
    "greyblock":                     "#565e65",
    "greybg":                        "#3a4248",
    "black":                         "#1d2124"
}

'''
rosa bem levinho - c8a3d2#
'''

#### POPUP MENU ####


def show_power_menu(qtile):
    ''' This function creates a popup menu with options
    to lock, sleep and shutdown the system.'''
    controls = [
        PopupImage(
            filename="/home/arturcgs/Pictures/icons/lock.png",
            pos_x=0.15,
            pos_y=0.1,
            width=0.1,
            height=0.5,
            mouse_callbacks={
                "Button1": lazy.spawn("betterlockscreen -l")
            }
        ),
        PopupImage(
            filename="/home/arturcgs/Pictures/icons/sleep.png",
            pos_x=0.45,
            pos_y=0.1,
            width=0.1,
            height=0.5,
            mouse_callbacks={
                "Button1": lazy.spawn("/home/arturcgs/Scripts/qtile/sleep.sh")
            }
        ),
        PopupImage(
            filename="/home/arturcgs/Pictures/icons/shutdown.png",
            pos_x=0.75,
            pos_y=0.1,
            width=0.1,
            height=0.5,
            highlight="A00000",
            mouse_callbacks={
                "Button1": lazy.spawn("systemctl poweroff")
            }
        ),
        PopupText(
            text="Lock",
            pos_x=0.1,
            pos_y=0.7,
            width=0.2,
            height=0.2,
            h_align="center"
        ),
        PopupText(
            text="Sleep",
            pos_x=0.4,
            pos_y=0.7,
            width=0.2,
            height=0.2,
            h_align="center"
        ),
        PopupText(
            text="Shutdown",
            pos_x=0.7,
            pos_y=0.7,
            width=0.2,
            height=0.2,
            h_align="center"
        ),
    ]

    layout = PopupRelativeLayout(
        qtile,
        width=1000,
        height=200,
        controls=controls,
        background="00000060",
        initial_focus=None,
    )

    layout.show(centered=True)
    

#### KEY BINDINGS ####


keys = [
    
    ## DEFAULT ##
    
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "Tab", lazy.layout.next(), desc="Move window focus to other window"),
    
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Tab", lazy.layout.shuffle_up(), desc="Move window up"),
    
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Tab", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    
    # Toggle between different layouts as defined below
    Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    
    ## CUSTOM ##
    
    # brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +5%"), desc="Increses brightness"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-"), desc="Decreases brightness"),
    
    # volume
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -D pulse sset Master 5%+"), desc="Increses volume"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -D pulse sset Master 5%-"), desc="Decreases volume"),
   
    # print screen
    Key([], "Print", lazy.spawn("flameshot gui"), desc="Printscreens"),
        
    # menu for lock, sleep, reboot and turnoff
    Key([mod], "x", lazy.function(show_power_menu)),
	
	# screen lock
    Key([mod], "l", lazy.spawn("betterlockscreen -l")),

]



#### GROUP SETTINGS ####


groups = [
    Group("Blehh", layout="max"),
    Group("Bebuh", layout="max"),
    Group("Abubleh", layout="columns"),
    Group("Blomp", layout="max"),
    Group("Bimb", layout="max"),
    Group("666", layout="max")
]
group_hotkeys = "123456"

for g, k in zip(groups, group_hotkeys):
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                k,
                lazy.group[g.name].toscreen(),
                desc="Switch to group {}".format(g.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                k,
                lazy.window.togroup(g.name, switch_group=False),
                desc="Switch to & move focused window to group {}".format(g.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )


#### LAYOUT SETTINGS ####


layouts = [
    layout.Max(
        margin = 5
    ),
    layout.Columns(
        margin = 5,
        border_focus_stack=["#d75f5f", "#8f3d3d"],
        border_width=4
    ),
    layout.TreeTab(margin = 5),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]


#### WIDGET SETTINGS ####


# Widget Functions


def open_pavu():
    qtile.cmd_spawn("pavucontrol")
    
    
# General Settings
font_name = ''
widget_defaults = dict(
    font='OpenDyslexicMono NF',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

# Creating Widgets

def get_widgets(primary = False):

    # defining overall variable
    if primary:
        bar_sizes = {
            # GroupBox
            "group_font": 16,
            "group_spacing": 0,

            # Current Window Name
            "max_chars": 65,

            # Battery widget
            "battery_height": 10,
            "battery_width": 17,

            # General
            "widget_font": 12,
            "text_box": 26,
            "spacer": 6,
        }
    else:
        bar_sizes = {
            # GroupBox
            "group_font": 18,
            "group_spacing": 5,

            # Current Window Name
            "max_chars": 300,

            # Battery widget
            "battery_height": 12,
            "battery_width": 22,

            # General
            "widget_font": 14,
            "text_box": 24,
            "spacer": 10,
        }

    # creating widgets
    widgets = [

        #### LEFT WIDGETS ####



        # Current Layout
        widget.Spacer(
            length=4,
            background=everforest["purple1"],
        ),

        widget.CurrentLayoutIcon(
            background=everforest["purple1"],
            max_chars = 3,
            scale = 0.59,
            custom_icon_paths = [".config/qtile/icons/layout-icons"],
            use_mask = True,
            #foreground = everforest["font_color"]
        ),

        widget.TextBox(
            text="",
            padding=-1,
            fontsize=bar_sizes["text_box"],
            foreground=everforest["purple1"],
            background=everforest["purple2"],
        ),


        # GroupBox
        widget.Spacer(
            length = 2,
            background = everforest["purple2"],
        ),

        widget.GroupBox(
            highlight_method = "line",
            background = everforest["purple2"],
            fontsize = bar_sizes["group_font"],
            spacing = bar_sizes["group_spacing"],
            margin = 4,
            highlight_color = [everforest["selection"],everforest["selection"]],
            this_current_screen_border = everforest["current_screen_border"],
            other_screen_border = everforest["other_screen_border"],
            active = everforest["font_color"],
            inactive = everforest["inactive_font_color"],
            this_screen_border = everforest["this_screen_border"]
        ),

        widget.TextBox(
            text="",
            padding=-1,
            fontsize=bar_sizes["text_box"],
            foreground=everforest["purple2"],
            background=everforest["purple3"],
        ),



        # Prompt
        widget.Prompt(
            sont=font_name,
            background = everforest["purple3"],
            fontsize = bar_sizes["group_font"],
            foreground = everforest["font_color"]
        ),


        # Window Name Layout
        widget.WindowName(
            max_chars=bar_sizes["max_chars"],
            fontsize = bar_sizes["widget_font"],
            font = font_name,
            foreground = everforest["font_color"],
            background = everforest["background"]
        ),



        #### RIGHT WIDGETS ####



        # Utilities

        widget.TextBox(
            text="",
            padding=-1,
            fontsize=bar_sizes["text_box"],
            foreground=everforest["greyblock"],
            background=everforest["background"],
        ),

        widget.WidgetBox(
            widgets = [
                widget.Memory(
                    measure_mem='G',
                    format='Mem: {MemUsed: .1f}{mm}/{MemTotal: .1f}{mm}',
                    background=everforest["greyblock"],
                    foreground=everforest["font_color"],
                    fontsize=bar_sizes["widget_font"]
                ),
                widget.CPU(
                    format='CPU: {freq_current}GHz {load_percent}%',
                    background=everforest["greyblock"],
                    foreground=everforest["font_color"],
                    fontsize=bar_sizes["widget_font"]
                ),
                widget.ThermalSensor(
                    background=everforest["greyblock"],
                    foreground=everforest["font_color"],
                    fontsize=bar_sizes["widget_font"]
                )
            ],
            background = everforest["greyblock"],
            foreground = everforest["font_color"],
            text_closed = "PC Utilities",


        ),

        widget.TextBox(
            text="",
            padding=-1,
            fontsize=bar_sizes["text_box"],
            foreground=everforest["greyblock"],
            background=everforest["background"],
        ),

        widget.Spacer(
            length=bar_sizes["spacer"],
            background=everforest["background"],
        ),



        # Battery widget
        widget.TextBox(
            text ="",
            padding =-1,
            fontsize =bar_sizes["text_box"],
            foreground=everforest["greyblock"],
            background=everforest["background"],
        ),
                      
        widget.UPowerWidget(
            background=everforest["greyblock"],
            battery_height = bar_sizes["battery_height"],
            battery_width = bar_sizes["battery_width"]
        ),

        widget.Battery(
            font = font_name,
            update_delay = 5,
            foreground = everforest["font_color"],
            background = everforest["greyblock"],
            fontsize = bar_sizes["widget_font"],
            full_char = "",
            charge_char = "↑",
            discharge_char = "↓",
            format = " {char} {percent:2.0%}",
            notify_below = 15,
            ),

        widget.TextBox(
            text="",
            padding=-1,
            fontsize=bar_sizes["text_box"],
            foreground=everforest["greyblock"],
            background=everforest["background"],
        ),

        widget.Spacer(
            length = bar_sizes["spacer"],
            background = everforest["background"],
        ),



        # Backlight 
        widget.TextBox(
            text ="",
            padding =-1,
            fontsize=bar_sizes["text_box"],
            foreground=everforest["greybg"],
            background=everforest["background"],
        ),

        widget.Backlight(
            fmt = "盛  {}",
            font = font_name,
            backlight_name = "intel_backlight",
            brightness_file = "actual_brightness",
            change_command = "brightnessctl s {0}%",
            foreground = everforest["font_color"],
            background = everforest["greybg"],
            step = 5
        ),

        widget.Spacer(
            length = bar_sizes["spacer"],
            background = everforest["purple3"],
        ),



        # Volume 
        widget.TextBox(
            text ="",
            padding =-1,
            fontsize =bar_sizes["text_box"],
            foreground=everforest["purple2"],
            background=everforest["purple3"],
        ),

        widget.Volume(
            fmt = "🔊 {}",
            font = font_name,
            foreground = everforest["fg1"],
            background = everforest["purple2"],
            mouse_callbacks={'Button1': open_pavu},
            volume_app = "pavucontrol"
        ),

        widget.Spacer(
            length = bar_sizes["spacer"],
            background = everforest["purple2"],
        ),



        # Date and time
        widget.TextBox(
            text="",
            padding=0,
            fontsize=bar_sizes["text_box"],
            foreground=everforest["purple1"],
            background=everforest["purple2"],
        ),

        widget.Clock(
            format="%d-%m-%Y %a, %I:%M",
            font = font_name,
            foreground = everforest["fg1"],
            background = everforest["purple1"]
        ),





        # Shutdown
        widget.QuickExit(
            default_text='[X]',
            countdown_format='[{}s]',
            foreground=everforest["font_color"],
            background=everforest["background"],
        ),

    ]

    if primary:
        # Systray Widget
        widgets.insert(
            6,
            widget.TextBox(
                text = "",
                padding = -1,
                fontsize = bar_sizes["text_box"],
                foreground = everforest["greybg"],
                background = everforest["background"],
            )
        )

        widgets.insert(
            7,
            widget.Systray(
                background = everforest["greybg"],
                padding = 5,
                icon_size = 18
            )
        )

        widgets.insert(
            8,
            widget.TextBox(
                text = "",
                padding = -1,
                fontsize = bar_sizes["text_box"],
                foreground = everforest["greybg"],
                background = everforest["background"],
            )
        )

        widgets.insert(
            9,
            widget.Spacer(
                length = bar_sizes["spacer"],
                background = everforest["background"]
            )
        )
    return widgets




#### SCREEN SETTINGS ####




screens = [
    Screen(
        top=bar.Bar(
            get_widgets(primary = True),
            26,
            opacity = 1,
            margin = [4,4,0,4],
            #border_width=[0, 0, 2, 0],  # Draw top and bottom borders
            #border_color=["ff00ff", "000000", everforest["greybg"], "000000"]  # Borders are magenta
        ),
    ),
    Screen(
        top=bar.Bar(
            get_widgets(primary = False),
            28, opacity = 1, margin = [6,6,0,6]
            #border_width=[0, 0, 2, 0],  # Draw top and bottom borders
            #border_color=["ff00ff", "000000", everforest["greybg"], "000000"]  # Borders are magenta
        ),
    ),
]


#### MOUSE SETTINGS ####


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]





#### EXTRAS ####


dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


#### STARTUP CONFIG ####


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("/home/arturcgs/Scripts/qtile/autostart.sh")
    subprocess.run([home])
