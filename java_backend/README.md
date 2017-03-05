#API

    POST hostname/repo
    body: url={github url}

#http://www.androidcentral.com/installing-android-sdk-windows-mac-and-linux-tutorial
#repo
https://dl.google.com/android/repository/tools_r25.2.3-linux.zip
mkdir android
#sdknam
curl -s "https://get.sdkman.io" | bash

http://www.androidcentral.com/installing-android-sdk-windows-mac-and-linux-tutorial

source ~/.bashrc

export PATH="$ANDROID_HOME/tools:$PATH"
export PATH="$ANDROID_HOME/platform-tools:$PATH"

Sandroid update sdk --no-ui --all


