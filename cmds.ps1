$QT_COMPILE_BIN = "C:\Qt\5.12.4\msvc2017_64\bin"
$QT_INSTALLER_FRAMEWORK_BIN = "C:\Qt\Tools\QtInstallerFramework\3.1\bin"
$PYTHON_EXE = "C:\Windows\py.exe"

&$PYTHON_EXE .\create_conf_files.py
&$PYTHON_EXE .\copy_files_to_package.py
&$QT_COMPILE_BIN\windeployqt.exe .\packages\LongQt\data\bin\LongQt.exe
&$QT_COMPILE_BIN\windeployqt.exe .\packages\LongQt\data\bin\LongQtGrapher.exe
&$QT_COMPILE_BIN\windeployqt.exe .\packages\LongQt\data\bin\LQGridEditor.exe
&$QT_INSTALLER_FRAMEWORK_BIN\binarycreator.exe -c .\config\config.xml -p .\packages\ LongQtInstaller.exe
