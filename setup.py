from distutils.core import setup

setup(
    name='pywkpdf',
    version='0.1dev',
    packages=['pywkpdf',],
    package_data={'pywkpdf': ['bin/wkhtmltopdf-linux', 'bin/wkhtmltopdf.app/*']},
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.txt').read(),
    # test_suite='nose2.collector.collector',
)