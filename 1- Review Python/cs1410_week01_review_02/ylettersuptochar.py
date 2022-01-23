def letters_up_to_char(long_word,char):
    count=0
    new=""
    for letter in long_word:
        if letter!=char:
            new+=letter
        else:
            break
    return new
