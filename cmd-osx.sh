#!/bin/sh
QT_INSTALLER_FRAMEWORK_BIN="/Applications/Qt/Tools/QtInstallerFramework/3.0/bin"

$QT_INSTALLER_FRAMEWORK_BIN/binarycreator -c ./config/config.xml -p ./packages/ LongQtInstaler.dmg
