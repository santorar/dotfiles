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

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os
import subprocess

mod = "mod4"
terminal = "kitty"
browser = "brave"
explorer = "nemo"
POWERLINE_SYMBOL = "\ue0ba"

COLORS = {
        "black": "#17070a",
        "white": "#D9E0EE",
        "purple": "#F28FAD",
        "yellow": "#FAE3B0",
        "pink": "#96CDFB",
        }


keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h",
        lazy.layout.left(),
        desc="Move focus to left"
        ),
    Key([mod], "l",
        lazy.layout.right(),
        desc="Move focus to right"
        ),
    Key([mod], "j",
        lazy.layout.down(),
        desc="Move focus down"
        ),
    Key([mod], "k",
        lazy.layout.up(),
        desc="Move focus up"
        ),
    Key([mod, "shift"], "space",
        lazy.layout.next(),
        desc="Move window focus to other window"
        ),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left"
        ),
    Key([mod, "shift"], "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right"
        ),
    Key([mod, "shift"], "j",
        lazy.layout.shuffle_down(),
        desc="Move window down"
        ),
    Key([mod, "shift"], "k",
        lazy.layout.shuffle_up(),
        desc="Move window up"
        ),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        desc="Grow window to the left"
        ),
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        desc="Grow window to the right"
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        desc="Grow window down"
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        desc="Grow window up"
        ),
    Key([mod], "n",
        lazy.layout.normalize(),
        desc="Reset all window sizes"
        ),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
        ),
    Key([mod], "Return",
        lazy.spawn(terminal),
        desc="Launch terminal"
        ),
    # Toggle between different layouts as defined below
    Key([mod], "Tab",
        lazy.next_layout(),
        desc="Toggle between layouts"
        ),
    Key([mod], "q",
        lazy.window.kill(),
        desc="Kill focused window"
        ),
    Key([mod, "control"], "r",
        lazy.reload_config(),
        desc="Reload the config"
        ),
    Key([mod, "control"], "q",
        lazy.shutdown(),
        desc="Shutdown Qtile"
        ),
    Key([mod], "r",
        lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"
        ),
    Key([mod], "b",
        lazy.spawn(browser),
        desc="Launch browser"
        ),
    Key([mod], "e",
        lazy.spawn(explorer),
        desc="Launch explorer"
        ),
    Key([mod], "space",
        lazy.spawn("rofi -show drun"),
        desc="Launch rofi"
        ),
    Key([mod], "c",
        lazy.spawn("gnome-calculator"),
        desc="Launch a calculator"
        ),
    Key([mod, "shift", "control"], "l",
        lazy.spawn("i3lock-fancy"),
        desc="Locks the screen"
        ),
    # Volume
    Key([], "XF86AudioLowerVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"),
        desc="-5% of volume"),
    Key([], "XF86AudioRaiseVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"),
        desc="5% of volume",
        ),
    Key([], "XF86AudioMute",
        lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"),
        desc="mute the audio"
        ),
    # Brightness
    Key([], "XF86MonBrightnessUp",
        lazy.spawn("brightnessctl set +10%"),
        desc="10% brightness"
        ),
    Key([], "XF86MonBrightnessDown",
        lazy.spawn("brightnessctl set 10%-"),
        desc="-10% brightness"
        ),

    # switch monitors
    Key([mod], "period",
        lazy.next_screen(),
        desc="Move focus to next monitor"
        ),
    Key([mod], "comma",
        lazy.prev_screen(),
        desc="Move focus to previous monitor"
        ),

    # fullscreen and float windows
    Key([mod, "shift"], "f",
        lazy.window.toggle_floating(),
        desc="toggle floating on a window"
        ),
    Key([mod], "f",
        lazy.window.toggle_fullscreen(),
        desc="toggle fullscreen on a window"
        ),
    # take a fullscreen screenshot
    Key([mod], "a",
        lazy.spawn("flameshot full"),
        desc="take a fullscreen screenshot",
        ),
    # take a selection screenshot
    Key([mod, "shift"], "a",
        lazy.spawn("flameshot gui"),
        desc="launch the interface for take a screenshot",
        ),
]

# groups = [Group(i) for i in "123456789"]


def longNameParse(text):
    for string in ["NVIM", "Brave", "Google Chrome", "Firefox"]:
        if string in text:
            text = string
        else:
            text = text
    return text


groups = [
        Group(name, **kwargs)
        for name, kwargs in [
            ("일", {"matches": [Match(wm_class=["firefox"])]}),
            ("이", {}),
            ("삼", {}),
            ("사", {}),
            ("오", {}),
            ("육", {"matches": [Match(wm_class=["spotify"])]}),
            ("칠", {"matches": [Match(wm_class=["mpv"])]}),
            ("팔", {"matches": [Match(wm_class=["discord"])]}),
            ]
        ]

for i, group in enumerate(groups, 1):
    keys.extend(
        [
            # Switch between workspaces
            Key(
                [mod],
                str(i if i != 10 else 0),
                lazy.group[group.name].toscreen(toggle=False),
                desc=f"Switch to group {group.name}",
            ),
            # Move focused window to workspace
            Key(
                [mod, "shift"],
                str(i if i != 10 else 0),
                lazy.window.togroup(group.name),
                desc=f"Move focused window to group {group.name}",
            ),
        ]
    )

layouts = [
    layout.Bsp(
        border_width=2,
        margin=3,
        margin_on_single=False,
        border_focus=COLORS["pink"],
        ),
    # layout.Columns(border_focus_stack=[, border_width=2,margin = 3),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),pink
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
]
widget_defaults = dict(
    font='Iosevka Fixed Semibold',
    fontsize=13,
    padding=0,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar([
            widget.Spacer(length=5),
            widget.GroupBox(
                font="Ubuntu Mono",
                highlight_method='text',
                highlight_color=COLORS["black"],
                active=COLORS["white"],
                this_current_screen_border=COLORS["yellow"],
                other_screen_border=COLORS["pink"],
                padding=5,
                fontsize=13,
            ),
            widget.TextBox(
                text=POWERLINE_SYMBOL,
                foreground=COLORS["white"],
                background=COLORS["black"],
                fontsize=30,
            ),
            widget.WindowName(
                foreground=COLORS["black"],
                parse_text=longNameParse,
                padding=5,
                background=COLORS["white"],
                ),
            widget.TextBox(
                text=POWERLINE_SYMBOL,
                foreground=COLORS["black"],
                background=COLORS["white"],
                fontsize=30,
            ),
            widget.Systray(
                icon_size=15,
                padding=4,
            ),
            widget.TextBox(
                text=POWERLINE_SYMBOL,
                foreground=COLORS["white"],
                background=COLORS["black"],
                fontsize=30,
            ),
            widget.Memory(
                background=COLORS["white"],
                foreground=COLORS["black"],
                format='Ram: {MemUsed: .0f}{mm}',
                ),
            widget.TextBox(
                text=POWERLINE_SYMBOL,
                foreground=COLORS["pink"],
                background=COLORS["white"],
                fontsize=30,
            ),
            widget.ThermalSensor(
                fmt='Thermal:  {}',
                background=COLORS["pink"],
                foreground=COLORS["black"],
                fontsize=13,
                padding=5,
                ),
            widget.TextBox(
                text=POWERLINE_SYMBOL,
                foreground=COLORS["purple"],
                background=COLORS["pink"],
                fontsize=30,
            ),
            widget.CPU(
                format="CPU {load_percent}%",
                background=COLORS["purple"],
                foreground=COLORS["black"],
                padding=3,
            ),
            widget.TextBox(
                text=POWERLINE_SYMBOL,
                foreground=COLORS["yellow"],
                background=COLORS["purple"],
                fontsize=30,
            ),
            widget.Clock(
                format="%b %d - %I:%M %p",
                foreground=COLORS["black"],
                background=COLORS["yellow"],
                padding=8
            ),
            ],
            32,
            background=COLORS["black"],
            # border_width=[3, 2, 3, 2],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]
            # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod], "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
        ),
    Drag(
        [mod], "Button3",
        lazy.window.set_size_floating(),
        start=lazy.window.get_size(),
        ),
    Click(
        [mod], "Button2",
        lazy.window.bring_to_front(),
        ),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see
        # the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="gnome-calculator"),  # calculator
        Match(wm_class="solanum"),  # pomodoro timer
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(title="gnome-calculator"),  # gnome calculator
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('/home/santorar/.config/qtile/autostart.sh')
    subprocess.run([home])


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
