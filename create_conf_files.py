#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 16:54:44 2019

@author: grat05
"""

from shutil import copyfile, copytree
import argparse
import sys

parser = argparse.ArgumentParser(description='Produce xml config files for Qt Installer Creator')
parser.add_argument('--version', type=str)
parser.add_argument('--releaseDate', type=str)
parser.add_argument('--LQRoot', type=str)

args = parser.parse_args()

class PackageConfig:
    def __init__(self, ty, destination, build_location, opts):
        self.ty = ty
        self.location = destination
        self.build_location = build_location
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
    def copyLicenseFile(self, src_root=None):
        if src_root is None:
            src_root = self.build_location+'/share/info/'
        dest = self.location+'/'+self.opts['license_file']
        copyfile(srcRoot+'/LICENSE',dest)
    def copyBuiltFiles(self, build_root=None):
        if build_root is None:
            build_root = self.build_location
            if sys.platform.startswith(('linux','win')):
                build_root += '/bin/'
            elif sys.platform.startswith('darwin'):
                build_root += '/bundle/'
        dest = self.location+'/'
        copytree(build_root, dest, dirs_exist_ok=True)


installerConf = PackageConfig('installer', './config', opts = {'version':args.version})
installerConf.writeConf()

longqtConf = PackageConfig('package', './packages/LongQt/meta', args.LQRoot, opts = {
 'name': 'LongQt',
 'description': 'LongQt Gui Tools',
 'version': args.version,
 'release_date': args.releaseDate,
 'license_name': 'License LongQt',
 'license_file': 'LICENSE-LongQt',
 'default': 'true' })
longqtConf.writeConf()
longqtConf.copyLicense()
longqtConf.copyBuiltFiles()

#if __name__ == '__main__':
#    print('Files writen and copied successfully')
#    input('Press Enter to end program')
