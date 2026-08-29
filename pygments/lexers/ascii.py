"""
    pygments.lexers.ascii
    ~~~~~~~~~~~~~~~~~~~~~~

    Lexer for ASCII art and text diagrams.

    :copyright: Copyright 2006-present by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from pygments.lexer import RegexLexer, words
from pygments.token import Text, Whitespace, Name, Operator, Punctuation, String, Keyword, Generic


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
            (_flowchart_arrows, Keyword),

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


# ---------------------------------------------------------------------------
# Pygments token types useful for ASCII-art highlighting
#
# The color names below refer to the Pygments "colorful" style.
# Where several Pygments token types use the same color, only one
# representative token is listed here.
#
# Token                       Color             Likely use
#
# Name                        default           ordinary words
# Name.Class                  magenta           CamelCase / PascalCase words
# Name.Constant               dark blue         UPPERCASE words
# Name.Function               blue              functions / actions
# Name.Builtin                green             special vocabulary / built-ins
# Name.Namespace              cyan-blue         namespaces / qualified concepts
# Name.Variable               brown             variables
# Name.Label                  ochre              labels
# Name.Entity                 dark red          entities / resources
# Name.Attribute              blue              properties / attributes
# Name.Tag                    green             tags / categories
#
# Operator                    dark gray         flowchart geometry
# Operator.Word               black             word-based operators
#
# Keyword                     green             reserved / special words
# Keyword.Pseudo              dark blue         pseudo-keywords
# Keyword.Type                indigo            type-like vocabulary
#
# Generic.Heading             navy blue         diagram headings
# Generic.Subheading          purple            secondary headings
# Generic.Error               red               errors / failures
# Generic.Deleted             dark red          deprecated / removed
# Generic.Inserted            green             added / new
# Generic.Prompt              orange-brown      prompts / interaction
# Generic.Output              gray              output / status text
# Generic.Traceback           blue              diagnostic text
#
# Error                       red + light red   severe errors
#
# Literal.String.Char         blue              character literals
# Literal.String.Doc          red-orange        documentation text
# Literal.String.Escape       gray              escape sequences
# Literal.String.Regex        black + light pink regex-like text
# Literal.String.Symbol       orange-brown      symbolic strings
#
# Literal.Number              violet            numeric values
# Literal.Number.Integer      blue              integer values
# Literal.Number.Hex          dark cyan         hexadecimal values
# Literal.Number.Oct           violet-blue       octal values
#
# Note:
#   Pygments token styles are hierarchical. A token not explicitly styled
#   by a style may inherit the style of one of its parent token types.
#
#   This list is intended as a practical guide when selecting existing
#   Pygments token types for the ASCII-art lexer. If the lexer eventually
#   requires semantic categories which cannot be represented cleanly by the
#   existing hierarchy, a dedicated Token.ASCII.* hierarchy can be
#   introduced later.
# ---------------------------------------------------------------------------
