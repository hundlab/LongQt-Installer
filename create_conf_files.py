#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 16:54:44 2019

@author: grat05
"""

from shutil import copyfile
import argparse

parser = argparse.ArgumentParser(description='Produce xml config files for Qt Installer Creator')
parser.add_argument('--version', type=str)
parser.add_argument('--releaseDate', type=str)
parser.add_argument('--LQRoot', type=str)

args = parser.parse_args()
#version = '0.4'

#releaseDate = '2018-10-09'
#longqtRoot = '/home/dgratz/src/LongQt'

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

installerConf = PackageConfig('installer', './config', opts = {'version':args.version})
installerConf.writeConf()

longqtConf = PackageConfig('package', './packages/LongQt/meta', opts = {
 'name': 'LongQt',
 'description': 'LongQt Gui Tools',
 'version': args.version,
 'release_date': args.releaseDate,
 'license_name': 'License LongQt',
 'license_file': 'LICENSE-LongQt',
 'default': 'true' })
longqtConf.writeConf()
longqtConf.copyLicense(args.LQRoot)

#if __name__ == '__main__':
#    print('Files writen and copied successfully')
#    input('Press Enter to end program')
