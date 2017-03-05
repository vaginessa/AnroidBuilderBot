#API

    POST hostname/repo
    body: url={github url}

#Curl test
    curl --progress-bar -m 900 -X POST -F 'url=https://github.com/daniel-kashin/BatyaMessagingApp' 188.226.133.72:8080/repo > ke423k.apk
    

http://www.androidcentral.com/installing-android-sdk-windows-mac-and-linux-tutorial
#repo
    https://dl.google.com/android/repository/tools_r25.2.3-linux.zip
    mkdir android

#sdknam
    curl -s "https://get.sdkman.io" | bash
    http://www.androidcentral.com/installing-android-sdk-windows-mac-and-linux-tutorial

    source ~/.bashrc

    export PATH="$ANDROID_HOME/tools:$PATH"
    export PATH="$ANDROID_HOME/platform-tools:$PATH"

    android update sdk --no-ui --all

    url --progress-bar -m 900 -X POST -F 'url=https://github.com/daniel-kashin/BatyaMessagingApp' 188.226.133.72:8080/repo > ke423k.apk

