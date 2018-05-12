# Notify-Me

Simple program to make timed notifications using `notify-send` on Linux.
`notify-send` comes pre-installed on Ubuntu. To install on other distros, type `sudo apt-get install notify-osd` in terminal and hit enter.

## Usage:-
- `python3 notify-me.py <heading> <message> <minutes>`
- Example - `python3 notify-me.py "Notification Heading" "Notification Message" 10.5` 
- Set shortcut alias in .bashrc to notify-me.py to run from anywhere easily. It should look like this - `alias ShortcutName="Path/to/notify-me.py"`
- and run like this - `ShortcutName "Important Notification" "Time to get ready" 60`
- Send this program to background using & symbol after command. Example - `ShortcutName "Alarm" "5 Minutes has passed!" 5 &`