"""
setup.py file for reverse chirp example pycbc waveform plugin package
"""

from setuptools import Extension, setup, Command
from setuptools import find_packages

VERSION = '0.0.dev0'

setup (
    name = 'pycbc-wave',
    version = VERSION,
    author = 'The PyCBC team',
    author_email = 'alex.nitz@gmail.org',
    url = 'http://www.pycbc.org/',
    download_url = 'https://github.com/gwastro/revchirp/tarball/v%s' % VERSION,
    keywords = ['pycbc', 'signal processing', 'gravitational waves'],
    install_requires = ['pycbc'],
    py_modules = ['mywave'],
    entry_points = {"pycbc.waveform.fd_sequence":"taperf2 = mywave:fd_sequence",
                    "pycbc.waveform.fd":"taperf2 = mywave:fd"},
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Scientific/Engineering :: Physics',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    ],
)
