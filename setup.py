import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(name='jobfuscator',

    version='1.0.4',

    description='JObfuscator is a source code obfuscator for the Java programming language. Obfuscate and protect your Java source code and algorithms from hacking, cracking, reverse engineering, decompilation, and technology theft. JObfuscator provides advanced Java source code parsing based on AST trees, multiple advanced obfuscation strategies are available.',
    long_description=long_description,
    long_description_content_type="text/markdown",

    keywords="java jar war class source obfuscator obfuscation obfuscate decompile decompiler decompilation",

    url='https://www.pelock.com',

    author='Bartosz Wójcik',
    author_email='support@pelock.com',

    license='Apache-2.0',

    packages=['jobfuscator'],

    install_requires=[
              'requests',
    ],

    zip_safe=False,

    classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Topic :: Security",
          "Natural Language :: English",
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Programming Language :: Java"
      ],
)