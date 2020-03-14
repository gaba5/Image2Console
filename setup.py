from distutils.core import setup
setup(
  name = 'image2console',
  packages = ['image2console'],
  version = '0.2',
  license='MIT',
  description = 'A module to print (pixelated) jpg images in the python console',
  author = 'Sebastien Lorentz',
  author_email = 'sebastien8lorentz@gmail.com',
  url = 'https://github.com/gaba5/image2console',
  download_url = 'https://github.com/gaba5/image2console/archive/1.2.tar.gz',
  keywords = ['Image', 'Print', 'Image in console'],
  install_requires=[
          'colr',
          'Pillow',
          "numpy"
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)
