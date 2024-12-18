COMMON_PASSWORD_BASES = [
    # Basic words
    'password', 'admin', 'welcome', 'test', 'user', 'qwerty', 'letmein', 
    'guest', 'default', 'pass', 'login', 'root', 'system',
    
    # Common patterns
    'abc', 'abcd', 'xyz', 'qwerty', 'asdf', 'zxcv', 'wasd', 'test', 'demo',
    'example', 'sample', 'temp', 'admin', 'root', 'user', 'guest',
    
    # Common words
    'love', 'hate', 'life', 'death', 'god', 'angel', 'devil',
    'heaven', 'hell', 'peace', 'war', 'sun', 'moon', 'star',
    
    # Common number sequences
    '123', '1234', '12345', '123456', '12345678', '1234567890',
    '321', '456', '567', '678', '789', '987', '654', '543',
    'abcdef', 'abcdefg',
]

KEYBOARD_PATTERNS = [
    # Horizontal rows (full and partial)
    'qwert', 'qwerty', 'qwertyui', 'qwertyuiop',
    'asdf', 'asdfg', 'asdfgh', 'asdfghjkl',
    'zxcv', 'zxcvb', 'zxcvbn', 'zxcvbnm',
    
    # Vertical patterns (top to bottom)
    'qaz', 'qazwsx', 'qazwsxedc',
    'wsx', 'wsxedc', 'wsxedcrfv',
    'edc', 'edcrfv', 'edcrfvtgb',
    'rfv', 'rfvtgb', 'rfvtgbyhn',
    'tgb', 'tgbyhn', 'tgbyhnujm',
    
    # Diagonal patterns
    'qweasd', 'wersdf', 'erdfgh',
    'asdzxc', 'sdfcvb', 'dfgvbn',
    
    # Common gaming keys
    'wasd', 'wqsd', 'werd',
    
    # Reverse patterns
    'poiuy', 'poiuyt', 'poiuytr',
    'lkjhg', 'lkjhgf', 'lkjhgfd',
    'mnbvc', 'mnbvcx', 'mnbvcxz',
    
    # Number row patterns
    '1234', '12345', '123456',
    '4321', '54321', '654321',
]

# L33t speak substitutions mapping
LEET_SUBSTITUTIONS = {
    'a': ['@', '4', '^'],
    'b': ['8', '6'],
    'e': ['3', '&'],
    'i': ['1', '!', '|'],
    'l': ['1', '|'],
    'o': ['0', '*'],
    's': ['$', '5', 'z'],
    't': ['7', '+'],
    'z': ['2'],
    'g': ['9', '6'],
    'h': ['#']
} 

MAX_PROFILE_PIC_UPLOAD_SIZE = 5 * 1024 * 1024