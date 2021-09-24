# LongQt Installer Creator

This repository is for building the executable installer for LongQt. It requires that
LongQt is already built, if you have not yet built LongQt see the developer instructions
on [github.com/hundlab/LongQt](https://github.com/hundlab/LongQt). If you are looking
for the pre-built executable installers see our website [hundlab.org](http://hundlab.org/).

## Usage

In addition to the requirements needed for building LongQt, the installer needs
Qt Installer Framework to be installed (version 4) and python version 3.

The last set of instrutions in the Development Build setions of LongQt's README, specifies
how to setup the install directive for LongQt to copy the executables over to LongQt Installer.
Follow those instructions first before continuing. After completing those instructions
ensure that the `LongQt-Installer/packages/LongQt` directory has been created and
the executables have been copied in there (on windows there will also be other dependancies
copied in there as well). Finally run the python script (`create_conf_files.py`)
providing the version number,
the release date (can be the current date) and the root directory of LongQt install.

```
python create_conf_files.py \
   --version <LongQt version> \
   --releaseDate <release date or current date> \
   --LQRoot ./install/LongQt
```

Finally, from the root directory of LongQt-Installer run the Qt Installer Framework binary
creator. This will be in the Qt install
directory usually `/Qt/Tools/QtInstallerFramework/4.1/bin/binarycreator`.

```
<Installer Framework path>/binarycreator \
   -c ./config/config.xml \
   -p ./packages/ \
   LongQtInstaller
```

This should produce a LongQtInstaller executable, which can be run to install LongQt on
the system.
