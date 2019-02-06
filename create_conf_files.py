#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 16:54:44 2019

@author: grat05
"""

from shutil import copyfile

version = '0.4'
try:
    import PyLongQt
    version = PyLongQt.version.replace('v','')
except:
    print('PyLongQt module not found, using version:',version)
releaseDate = '2018-10-09'
longqtRoot = 'U:/LongQt'
longqtModelRoot = 'U:/LongQt-model'
pylongqtRoot = 'U:/PyLongQt'

class PackageConfig:
    def __init__(self, ty, location, opts):
        self.ty = ty
        self.location = location
        self.opts = opts
    def writeConf(self):
        with open(str(self.ty)+'.txt') as file:
            txt = file.read()
        conf = txt.format(**self.opts)
        name = ''
        if self.ty == 'package':
            name = 'package.xml'
        elif self.ty == 'installer':
            name = 'config.xml'
        else:
            print('type unknown: ',self.ty)
        with open(self.location+'/'+name, 'w') as configFile:
            configFile.write(conf)
    def copyLicense(self, srcRoot):
        dest = self.location+'/'+self.opts['license_file']
        copyfile(srcRoot+'/LICENSE',dest)

installerConf = PackageConfig('installer', './config', opts = {'version': version})
installerConf.writeConf()

longqtConf = PackageConfig('package', './packages/LongQt/meta', opts = {
 'name': 'LongQt',
 'description': 'LongQt Gui Tools',
 'version': version,
 'release_date': releaseDate,
 'license_name': 'License LongQt',
 'license_file': 'LICENSE-LongQt',
 'default': 'true' })
longqtConf.writeConf()
longqtConf.copyLicense(longqtRoot)

longqtModelConf = PackageConfig('package', './packages/LongQtmodel/meta', opts = {
 'name': 'LongQt model',
 'description': 'LongQt model library',
 'version': version,
 'release_date': releaseDate,
 'license_name': 'License LongQt model',
 'license_file': 'LICENSE-LongQt-model',
 'default': 'false' })
longqtModelConf.writeConf()
longqtModelConf.copyLicense(longqtModelRoot)

pylongqtConf = PackageConfig('package', './packages/PyLongQt/meta', opts = {
 'name': 'PyLongQt',
 'description': 'Python bindings for LongQt-model',
 'version': version,
 'release_date': releaseDate,
 'license_name': 'License PyLongQt',
 'license_file': 'LICENSE-PyLongQt',
 'default': 'false' })
pylongqtConf.writeConf()
pylongqtConf.copyLicense(pylongqtRoot)

#if __name__ == '__main__':
#    print('Files writen and copied successfully')
#    input('Press Enter to end program')