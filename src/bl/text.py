def add(D, name, content):
    text = D.texts.new(name)
    text.from_string(content)
    text.cursor_set(0)
    return text
