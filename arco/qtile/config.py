# ~/.config/qtile
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
# all copies or substantial portions of the Softwaree.
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
# https://icolorpalette.com/410179_8530d1_a25ce0_a473ce_a669db

color_theme = {
    "font_color": "#ffffff",
    "background": "#a460e0",
    "selection1": "#361453",
    "selection2": "#7825b4",
    "current_screen_border": "#9c4b6d",
    "other_screen_border": "#725f7b",
    "inactive_font_color": "#919191",
    "this_screen_border": "#9c4b6d",
    "unfocused_window": "#404040",

    # purple palette
    "purple1": "#250d39",
    "purple2": "#4a1b73",
    "purple3": "#6f29ac",
    "purple4": "#934ad3",
    "purple5": "#b583e1",
    "purple6": "#c6a0e8",

    # "purple1": "#250b3b",
    # "purple2": "#4a1677",
    # "purple3": "#6f22b3",
    # "purple4": "#9342db",
    # "purple5": "#a460e0",
    # "purple6": "#b57ee6",

    # "purple1": "#260046",
    # "purple2": "#4c018d",
    # "purple3": "#7201d4",
    # "purple4": "#9620fd",
    # "purple5": "#b767fd",
    # "purple6": "#c88afe",

}

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
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod, "shift"], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "space", lazy.spawn("rofi -show drun"), desc="Open rofi"),

    ## CUSTOM ##

    # brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +5%"), desc="Increses brightness"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-"), desc="Decreases brightness"),

    # volume
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -D pulse sset Master 5%+"), desc="Increses volume"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -D pulse sset Master 5%-"), desc="Decreases volume"),
    Key([], "XF86AudioMute", lazy.spawn("amixer sset Master 1+ toggle"), desc="Mute/Unmute Volume"),

    # print screen
    Key([], "Print", lazy.spawn("flameshot gui"), desc="Printscreens"),

    # music controller
    # if it pauses/plays the wrong thing sometimes, add the payerctl daemon to the autostart file.
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc="Play/Pause player"),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Skip to next"),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="Skip to previous"),

    # menu for lock, sleep, reboot and turnoff
    Key([mod], "x", lazy.spawn("archlinux-logout")),

    # screen lock and sleep
    Key([mod], "p", lazy.spawn("betterlockscreen -l")),
    Key([mod, "shift"], "p", lazy.spawn("systemctl suspend")),

    # toggle floating
    Key([mod], "f", lazy.window.toggle_floating())

]

#### GROUP SETTINGS ####

'''Cool NerdFont Icons:
https://www.nerdfonts.com/cheat-sheet

ﭓ
  ﱦ
 bacteria

 


ﬨ
 


ﳝ




 ﰬ ﰭ ﰮ 
ﰵ   
'''

groups = [
    Group("1", label="", layout="max"),
    Group("2", label="", layout="max"),
    Group("3", label="", layout="columns"),
    Group("4", label="殺", layout="columns"),
    Group("5", label="異", layout="columns"),
    Group("6", label="", layout="columns"),
    Group("7", label="", layout="columns"),
    Group("8", label="", layout="columns"),
    Group("9", label="", layout="columns"),

]

# add group hotkeys for numbers
group_hotkeys = "123456789"

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

# add group hotkeys for numpad numbers
group_numpad_hotkeys = ["KP_End", "KP_Down", "KP_Next", "KP_Left", "KP_Begin", "KP_Right", "KP_Home","KP_Up", "KP_Prior"]

for g, k in zip(groups, group_numpad_hotkeys):
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
        margin=5
    ),
    layout.Columns(
        margin=5,
        border_focus=color_theme["purple5"],
        border_normal=color_theme["unfocused_window"],
        border_width=2,
        border_normal_stack=color_theme["font_color"],
        insert_position=1,
    ),
    layout.TreeTab(margin=5),
    layout.Floating(border_focus=color_theme["purple5"], ),
    # layout.Stack(num_stacks=3),
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
widget_defaults = dict(
    font='SpaceMono Nerd Font Mono',
    style='Bold',
    padding=3,
)
extension_defaults = widget_defaults.copy()


# Creating Widgets

def get_widgets(primary=False):
    # defining overall variable
    if primary:
        bar_sizes = {
            # GroupBox
            "group_font": 22,
            "group_spacing": 0,

            # Current Window Name
            "max_chars": 65,

            # Battery widget
            "battery_height": 10,
            "battery_width": 17,

            # General
            "widget_font": 13,
            "text_box": 26,
            "spacer": 6,

            # Final widget background color
            "final_widget_bg_color": color_theme["purple4"]
        }
    else:
        bar_sizes = {
            # GroupBox
            "group_font": 30,
            "group_spacing": 5,

            # Current Window Name
            "max_chars": 300,

            # Battery widget
            "battery_height": 12,
            "battery_width": 22,

            # General
            "widget_font": 16,
            "text_box": 24,
            "spacer": 10,

            # Final widget background color
            "final_widget_bg_color": color_theme["background"]
        }

    # creating widgets
    widgets = [

        #### LEFT WIDGETS ####

        # Current Layout
        widget.Spacer(
            length=4,
            background=color_theme["purple1"],
        ),

        widget.CurrentLayoutIcon(
            background=color_theme["purple1"],
            max_chars=3,
            scale=0.59,
        ),

        widget.TextBox(
            text="",
            padding=-1,
            fontsize=bar_sizes["text_box"],
            foreground=color_theme["purple1"],
            background=color_theme["purple2"],
        ),

        # GroupBox
        widget.Spacer(
            length=0,
            background=color_theme["purple2"],
        ),

        widget.GroupBox(
            highlight_method="line",
            background=color_theme["purple2"],
            fontsize=bar_sizes["group_font"],
            spacing=bar_sizes["group_spacing"],
            margin=4,
            highlight_color=[color_theme["selection1"], color_theme["selection2"]],
            this_current_screen_border=color_theme["current_screen_border"],
            other_screen_border=color_theme["other_screen_border"],
            active=color_theme["font_color"],
            inactive=color_theme["inactive_font_color"],
            this_screen_border=color_theme["this_screen_border"]
        ),

        widget.TextBox(
            text="",
            padding=-1,
            fontsize=bar_sizes["text_box"],
            foreground=color_theme["purple2"],
            background=color_theme["background"],
        ),

        # Prompt
        widget.Prompt(
            background=color_theme["background"],
            fontsize=bar_sizes["group_font"],
            foreground=color_theme["font_color"]
        ),

        # Window Name Layout
        widget.WindowName(
            max_chars=bar_sizes["max_chars"],
            fontsize=bar_sizes["widget_font"],
            foreground=color_theme["font_color"],
            background=color_theme["background"]
        ),

        #### RIGHT WIDGETS ####

        # Utilities

        widget.TextBox(
            text="",
            padding=-1,
            fontsize=bar_sizes["text_box"],
            foreground=color_theme["purple3"],
            background=bar_sizes["final_widget_bg_color"],
        ),

        widget.WidgetBox(
            widgets=[
                widget.Memory(
                    measure_mem='G',
                    format='Mem: {MemUsed:.1f}{mm}/{MemTotal:.1f}{mm} |',
                    background=color_theme["purple3"],
                    foreground=color_theme["font_color"],
                    fontsize=bar_sizes["widget_font"]
                ),
                widget.CPU(
                    format='CPU: {freq_current}GHz/{load_percent}% |',
                    background=color_theme["purple3"],
                    foreground=color_theme["font_color"],
                    fontsize=bar_sizes["widget_font"]
                ),
                widget.ThermalSensor(
                    background=color_theme["purple3"],
                    foreground=color_theme["font_color"],
                    fontsize=bar_sizes["widget_font"]
                )
            ],
            background=color_theme["purple3"],
            foreground=color_theme["font_color"],
            fontsize=bar_sizes["widget_font"],
            text_closed="PC Utilities",
            close_button_location="right"

        ),

        widget.Spacer(
            length=bar_sizes["spacer"],
            background=color_theme["purple3"],
        ),

        # Battery widget
        widget.TextBox(
            text="",
            padding=-1,
            fontsize=bar_sizes["text_box"],
            foreground=color_theme["purple2"],
            background=color_theme["purple3"],
        ),

        widget.UPowerWidget(
            background=color_theme["purple2"],
            battery_height=bar_sizes["battery_height"],
            battery_width=bar_sizes["battery_width"],
            fontsize=bar_sizes["widget_font"]
        ),

        widget.Battery(
            update_delay=5,
            foreground=color_theme["font_color"],
            background=color_theme["purple2"],
            fontsize=bar_sizes["widget_font"],
            full_char="",
            charge_char="",
            discharge_char="",
            format="{char} {percent:2.0%}",
            notify_below=15,
            unknown_char=""
        ),

        widget.Spacer(
            length=bar_sizes["spacer"],
            background=color_theme["purple2"],
        ),

        # Backlight
        widget.Backlight(
            fmt="盛  {}",
            font="SpaceMono Nerd Font",
            backlight_name="intel_backlight",
            brightness_file="actual_brightness",
            change_command="brightnessctl s {0}%",
            foreground=color_theme["font_color"],
            background=color_theme["purple2"],
            fontsize=bar_sizes["widget_font"],
            step=5
        ),

        widget.Spacer(
            length=bar_sizes["spacer"],
            background=color_theme["purple2"],
        ),

        # Volume
        widget.Volume(
            fmt="墳  {}",
            font="SpaceMono Nerd Font",
            foreground=color_theme["font_color"],
            background=color_theme["purple2"],
            fontsize=bar_sizes["widget_font"],
            mouse_callbacks={'Button1': open_pavu},
            volume_app="pavucontrol"
        ),

        widget.Spacer(
            length=bar_sizes["spacer"],
            background=color_theme["purple2"],
        ),

        # Date and time
        widget.TextBox(
            text="",
            padding=-1,
            fontsize=bar_sizes["text_box"],
            foreground=color_theme["purple1"],
            background=color_theme["purple2"],
        ),

        widget.Clock(
            format="%d-%m-%Y %a, %H:%M ",
            foreground=color_theme["font_color"],
            background=color_theme["purple1"],
            fontsize=bar_sizes["widget_font"],
        ),
    ]

    if primary:
        # Systray Widget
        widgets.insert(
            8,
            widget.TextBox(
                text="",
                padding=-1,
                fontsize=bar_sizes["text_box"],
                foreground=color_theme["purple4"],
                background=color_theme["background"],
            )
        )

        widgets.insert(
            9,
            widget.Systray(
                background=color_theme["purple4"],
                padding=5,
                icon_size=18
            )
        )

        widgets.insert(
            10,
            widget.Spacer(
                length=bar_sizes["spacer"],
                background=color_theme["purple4"]
            )
        )
    return widgets


#### SCREEN SETTINGS ####


screens = [
    Screen(
        top=bar.Bar(
            get_widgets(primary=True),
            26,
            opacity=1,
            margin=[4, 4, 0, 4],
            # border_width=[0, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", color_theme["greybg"], "000000"]  # Borders are magenta
        ),
    ),
    Screen(
        top=bar.Bar(
            get_widgets(primary=False),
            34,
            opacity=1,
            margin=[6, 6, 0, 6]
            # border_width=[0, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", color_theme["greybg"], "000000"]  # Borders are magenta
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
    ],
    border_focus=color_theme["purple5"]
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
