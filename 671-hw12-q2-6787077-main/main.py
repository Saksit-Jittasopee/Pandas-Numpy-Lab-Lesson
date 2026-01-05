# YOUR CODE HERE
input_text = input()      #work
position_text = input()   #prefix
extra_text = input()      #home

def combine_words(word, **kwargs):
    position = kwargs.get('position')
    extra = kwargs.get('extra')
    if position == 'prefix':
        return extra + word
    elif position == 'suffix':
        return word + extra
    else:
        return word

print(combine_words(input_text, position = position_text, extra=extra_text)) #homework


