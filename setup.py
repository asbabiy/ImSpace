from setuptools import setup

setup(
    name="imspace",
    version='0.1',
    py_modules=['rgb'],
    install_requires=[
        'Click', 'plotly', 'pandas', 'Pillow'
    ],
    entry_points='''
        [console_scripts]
        imspace=space:rgb
    ''',
)
