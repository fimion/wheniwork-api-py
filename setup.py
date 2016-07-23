from distutils.core import setup
setup(
  name = 'wheniwork',
  packages = ['wheniwork'], # this must be the same as the name above
  version = '0.1',
  description = 'A library for interfacing with the WhenIWork.com API',
  author = 'Alex Riviere',
  author_email = 'fimion@gmail.com',
  url = 'https://github.com/fimion/wheniwork-api-py',
  download_url = 'https://github.com/fimion/wheniwork-api-py/tarball/0.1',
  keywords = ['wheniwork', 'api'],
  classifiers = [],
  install_requires = ['requests'],
)