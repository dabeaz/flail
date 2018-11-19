try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name = "flail",
            description="Flail - The Ball and Chain Decorator",
            long_description = """
Decorators with more injuries
""",
            license="""MIT""",
            version = "0.0",
            author = "David Beazley",
            author_email = "dave@dabeaz.com",
            maintainer = "David Beazley",
            maintainer_email = "dave@dabeaz.com",
            url = "https://github.com/dabeaz/flail",
            packages = ['flail'],
            classifiers = [
              'Programming Language :: Python :: 3',
              ]
            )
