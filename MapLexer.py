from pygments.lexer import RegexLexer, bygroups
from pygments.token import *


class MapLexer(RegexLexer):
    name = "Map"
    aliases = ['Map']
    filenames = ['*.map']

    tokens = {
        'root': [
            (r'({)(\s*)', bygroups(Punctuation, Text), 'rule_start'),
            (r'(\s*)(})', bygroups(Text, Punctuation))
        ],
        'rule_start': [
            (r'([a-zA-Z\-_:<>?]*)(\s*)(=>)(\s*)', bygroups(Name.Variable, Text, Operator, Text), 'rule_end'),
            (r'', Text, "#pop")
        ],
        'rule_end': [
            (r'(int|string|double|float|char)(,)(\s*)', bygroups(Keyword.Type, Punctuation, Text), '#pop'),
            (r'(int|string|double|float|char)(\s*)', bygroups(Keyword.Type, Text), '#pop'),
            (r'({)(\s*)', bygroups(Punctuation, Text), 'rule_start'),
            (r'(\s*)(})', bygroups(Text, Punctuation), '#pop'),
            (r'(\[)(\s*)', bygroups(Punctuation, Text), 'array_start'),
            (r'(\s*)(\])', bygroups(Text, Punctuation), '#pop')
        ],
        'array_start': [
            (r'({)(\s*)', bygroups(Punctuation, Text), 'rule_start'),
            (r'(\s*)(})', bygroups(Text, Punctuation), '#pop')
        ]
    }
