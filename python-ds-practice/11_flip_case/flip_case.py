def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    swapper = swapper.lower()
    out_phrase = ""

    for ltr in phrase:
        if ltr.lower() == swaper:
            ltr = ltr.swapcase()
        out_phrase += ltr

    return out_phrase
