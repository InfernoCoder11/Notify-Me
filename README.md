# Notify-Me

Simple program to make timed notifications using `notify-send` on Linux and PyQt5 on Windows.
`notify-send` comes pre-installed on Ubuntu. To install on other linux distros, type `sudo apt-get install notify-osd` in terminal and hit enter.

## Usage:-
- `python3 notify-me.py <heading> <message> [-m MINUTES , -a]`
- Use `-a` if you want to use PyQt notification.
- By default, MINUTES is 60 minutes.
- Example - `python3 notify-me.py "Notification Heading" "Notification Message" -m 10.5 - a` 
- Set shortcut alias in .bashrc or in .bash_aliases to notify-me.py to run from anywhere easily. It should look like this - `alias ShortcutName="Path/to/notify-me.py"`
- and run like this - `ShortcutName "Important Notification" "Time to get ready" -m 60`
- Send this program to background using & symbol after command. Example - `ShortcutName "Alarm" "5 Minutes has passed!" -m 5 &`
