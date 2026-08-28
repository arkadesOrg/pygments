"""
    pygments.lexers.ascii
    ~~~~~~~~~~~~~~~~~~~~~~

    Lexer for ASCII art and text diagrams.

    :copyright: Copyright 2006-present by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from pygments.lexer import RegexLexer, words
from pygments.token import Text, Whitespace, Name, Operator, Punctuation, String, Generic


__all__ = ['AsciiArtLexer']


class AsciiArtLexer(RegexLexer):
    """
    Lexer for ASCII art and text diagrams.

    The initial lexer deliberately performs only lexical classification:
    words, whitespace, flowchart characters and other special characters.
    """

    name = 'ASCII Art'
    url = 'https://en.wikipedia.org/wiki/ASCII_art'
    aliases = ['ascii', 'ascii-art', 'asciiart']
    filenames = []
    mimetypes = ['text/x-ascii-art']
    version_added = '0.1'

    # Semantic words
    _warning_words = (
        'warning',
        'warn',
    )

    _error_words = (
        'error',
        'fatal',
    )

    # Flowchart arrows
    _flowchart_arrows = (
        r'-->|<--|->|<-|=>|<=|'
        r'↑|↓|←|→|'
        r'▲|▼|◀|▶'
    )

    # Box-drawing and flowchart geometry
    _flowchart_lines = (
        r'[|=\-─│]+'
    )

    _flowchart_corners = (
        r'[+┌┐└┘╭╮╰╯╒╕╘╛╓╖╙╜╔╗╚╝]'
    )
    
    tokens = {
        'root': [
            # Whitespace
            (r'\s+', Whitespace),

            # Semantic words
            (words(_warning_words, suffix=r'\b'), Generic.Emph),
            (words(_error_words, suffix=r'\b'), Generic.Error),

            # Flowchart arrows
            (_flowchart_arrows, Operator),

            # Flowchart lines
            (_flowchart_lines, Operator),
            
            # Flowchart corners and junctions
            (_flowchart_corners, Punctuation),

            # camelCase / PascalCase:
            # networkManager, Permapeople, NuttX, HTTPServer
            (r'[A-Z][a-z]+(?:[A-Z][a-z0-9]*)+',
             Name.Class),
            
            # ALL CAPS: CORE, ERROR, INSTRUMENTS
            (r'[A-Z][A-Z0-9_]', Name.Constant),
            
            # lowercase: services, network, federation
            (r'[a-z][a-z0-9_]*', Name),

            # Ordinary mixed/initial-capital words
            (r'[A-Z][a-z0-9_]*', String),

            # Other characters
            (r'.', Text),
        ],
    }
