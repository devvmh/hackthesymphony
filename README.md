1) Install Github app from https://mac.github.com

2) Intsall XCode developer tools in the App Store or in XCode, I forget which

4) Clone the git repository with the git app: https://github.com/devvmh/hackthesymphony

5) Open a terminal and type these commands, one to a line, hitting Enter after each one:

    cd ~/Github/hackthesymphony
    sudo -H easy_install pip
    ./install-requirements.command
    ./sync-database.command
    ./run-server.command

6) The terminal will show you error messages from the Python server, if any.

7) Use a text editor (I recommend http://www.sublimetext.com/2) to edit the Javascript/CSS/other files as needed
