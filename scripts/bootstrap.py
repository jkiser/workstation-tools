#!/usr/bin/env python
import os
import shutil

HOME_DIRS = ('bin', 'etc', 'lib', 'scripts', 'tmp', 'data', 'log', 'sql', '.vim.backup')

def configure_home():
    """
    Very basic layout of home dir.
    """
    created = []
    for d in HOME_DIRS:
        d = os.path.expanduser(
                os.path.join('~', d)
                )
        if not os.path.exists(d):
            try:
                os.mkdir(d)
                created.append(d)
            except:
                pass
        else:
            print('Skipping %s' % d)
    return created

