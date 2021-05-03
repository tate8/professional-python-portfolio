codes = {
    'a' : '●⁃',
    'b' : '⁃●●●',
    'c' : '●⁃●⁃',
    'd' : '⁃●●',
    'e' : '●',
    'f' : '●●⁃●',
    'g' : '⁃⁃●',
    'h' : '●●●●',
    'i' : '●●',
    'j' : '●⁃⁃⁃',
    'k' : '⁃●⁃',
    'l' : '●⁃●●',
    'm' : '⁃⁃',
    'n' : '⁃●',
    'o' : '⁃⁃⁃',
    'p' : '●⁃⁃●',
    'q' : '⁃⁃●⁃',
    'r' : '●⁃●',
    's' : '●●●',
    't' : '⁃',
    'u' : '●●⁃',
    'v' : '●●●⁃',
    'w' : '●⁃⁃',
    'x' : '⁃●●⁃',
    'y' : '⁃●⁃⁃',
    'z' : '⁃⁃●●'
}
converted_text = []

def split(word):
    return [char for char in word]


text_to_convert = input('Enter text to convert: ')
l_text_to_convert = text_to_convert.lower()
split_string = split(l_text_to_convert)
for key in codes:
    for letter in split_string:
        if key == letter:
            converted_text.append(codes[key])
print(' '.join(converted_text))