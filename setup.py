"""Netstring encoder / decoder module

Encodes and decodes netstring streams, or files."""

classifiers = """\
Development Status :: 5 - Production/Stable
Intended Audience :: Developers
Programming Language :: Python
License :: Public Domain
Operating System :: OS Independent
Topic :: Internet
"""

from distutils.core import setup
from netstring import __version__

doclines = __doc__.split("\n")

setup( name='netstring',
       version = __version__,       
       author = 'Will McGugan',
       author_email = 'will@willmcgugan.com',
       license = "public domain",
       url = 'http://code.google.com/p/netstring/',
       download_url = 'http://code.google.com/p/netstring/downloads/list',
       platforms = ['any'],
       description = doclines[0],
       long_description = '\n'.join(doclines[2:]),
       py_modules = ['netstring'],
       classifiers = classifiers.splitlines(),
       )
