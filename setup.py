from setuptools import setup, find_packages

setup (
    name='maplexer',
    packages=find_packages(),
    entry_points =
    """
    [pygments.lexers]
    maplexer = pygments_map.lexer:MapLexer
    """,
)
