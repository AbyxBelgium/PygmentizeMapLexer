# PygmentizeMapLexer
A simple Lexer for a very custom language I wrote that is designed to describe the structure of maps or dictionaries. The language is meant to be used in Latex-reports.
Map follows following BNF-specification (eps stands for epsilon, the empty string):

<root> ::= {<body>}
<body> ::= {<body>}|<rule>|<rule>,<whitespace><rule>
<rule> ::= <key><optional><whitespace>=><whitespace><value>
<key> ::= <character><key>|<character>
<value> ::= [<root>]|<root>|<type>
<type> ::= int|string|double|float|char
<optional> ::= ?|<eps>
<character> ::= a|b|...|z|A|B|...|Z|_|-|:
<whitespace> ::= <whitespace_character><whitespace>|<whitespace_character>
<whitespace_character> ::= <eps>| |\t|\n|\r
