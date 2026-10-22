errors = []

def check(condition, message):
    if not condition:
        errors.append(message)

def lex(text, label):
    tokens = []
    i = 0
    while i < len(text):
        c = text[i]
        if c.isspace() or c == '\ufeff':
            i += 1
        elif c == '#':
            end = text.find('\n', i)
            i = len(text) if end < 0 else end + 1
        elif c == '"':
            start = i
            i += 1
            while i < len(text) and text[i] != '"':
                i += 2 if text[i] == '\\' else 1
            check(i < len(text), f'{label}: unterminated string')
            tokens.append(text[start:i+1])
            i += 1
        elif c in '{}=<>!':
            token = c
            i += 1
            if i < len(text) and text[i] == '=' and c in '<>!=':
                token += '='
                i += 1
            tokens.append(token)
        else:
            start = i
            while i < len(text) and not text[i].isspace() and text[i] not in '#{}=<>!"':
                i += 1
            tokens.append(text[start:i])
    return tokens

def parse(text, label):
    tokens = lex(text, label)
    pos = 0
    def block(nested=False):
        nonlocal pos
        entries = []
        while pos < len(tokens):
            if tokens[pos] == '{':
                pos += 1
                entries.append((None, None, block(True)))
                continue
            if tokens[pos] == '}':
                check(nested, f'{label}: unexpected closing brace')
                pos += 1
                return entries
            key = tokens[pos]
            pos += 1
            if pos < len(tokens) and tokens[pos] in ('=', '<', '>', '<=', '>=', '!=', '=='):
                op = tokens[pos]
                pos += 1
                if pos < len(tokens) and tokens[pos] == '{':
                    pos += 1
                    value = block(True)
                elif pos < len(tokens):
                    value = tokens[pos].strip('"')
                    pos += 1
                else:
                    errors.append(f'{label}: missing value for {key}')
                    value = ''
                entries.append((key.strip('"'), op, value))
            else:
                entries.append((None, None, key.strip('"')))
        check(not nested, f'{label}: unclosed block')
        return entries
    return block()

def walk(tree):
    for key, op, value in tree:
        yield key, op, value
        if isinstance(value, list):
            yield from walk(value)

def values(tree, key):
    return [v for k, _, v in tree if k == key]

def first(tree, key, default=None):
    return next((v for k, _, v in tree if k == key), default)
