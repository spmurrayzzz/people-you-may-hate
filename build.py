#!/usr/bin/env python

import os
import json
from zipfile import ZipFile


def build_package():
    """Package the source for distribution (zip)"""
    pkgname = 'pymh-%s.zip' % MANIFEST['version']
    pkgpath = 'build/%s' % pkgname
    files = [
        'manifest.json',
        'icons/icon128.png',
        'icons/icon48.png',
        'icons/icon19.png',
        'icons/icon16.png',
        'src/inject/inject.css',
        'src/inject/inject.js',
    ]
    if os.path.isfile(pkgpath):
        os.remove(pkgpath)
    with ZipFile(pkgpath, 'w') as pkg:
        for file in files:
            pkg.write(file)


def setup_env():
    """Prepare build path"""
    if not os.path.exists('build'):
        os.mkdir('build')


def load_manifest():
    """Parse extension manifest"""
    with open('manifest.json', 'r') as f:
        manifest = json.load(f)
    return manifest

if __name__ == '__main__':
    MANIFEST = load_manifest()
    setup_env()
    build_package()
