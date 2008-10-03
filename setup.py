import os
from setuptools import setup

def find_files(directory, suffix_list):
    for root, dirs, files in os.walk(directory):
        relative_root = root[len(directory)+1:]
        for f in files:
            for suffix in suffix_list:
                if f.endswith(suffix):
                    yield os.path.join(relative_root, f)

package_data = list(find_files('blog', ['.po', '.mo', '.html']))

kwargs = {
    'name' : 'basic',
    'version' : '0.6',
    'description' : 'Basic Apps for my weblog',
    'packages' : ['basic',
                  'basic.blog',
                  'basic.blog.templatetags',
                  'basic.inlines',
                  'basic.inlines.templatetags'],
    'package_data': { 'basic.blog': package_data},
    'zip_safe': False,
    'classifiers' : ['Development Status :: 4 - Beta',
                     'Environment :: Web Environment',
                     'Intended Audience :: Developers',
                     'License :: OSI Approved :: BSD License',
                     'Operating System :: OS Independent',
                     'Programming Language :: Python',
                     'Topic :: Utilities'],
}

setup(**kwargs)
