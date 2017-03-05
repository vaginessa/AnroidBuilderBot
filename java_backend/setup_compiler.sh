
sudo apt-get install lib32ncurses5 lib32stdc++6 lib32z1

sudo apt-get install zip

curl -s "https://get.sdkman.io" | bash

source "$HOME/.sdkman/bin/sdkman-init.sh"

mkdir android && cd android
wget https://dl.google.com/android/repository/tools_r25.2.3-linux.zip
unzip tools_r25.2.3-linux.zip



git clone https://github.com/AndroidBuilderBotTeam/AnroidBuilderBot
