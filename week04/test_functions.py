from helper_functions import transform_name, get_lyricspages

# # transform_name

# def test_uppercase():
#     assert transform_name('Mariah Carey') == 'mariah-carey'

# def test_lowercase():
#     assert transform_name('mariah carey') == 'mariah-carey'

# def test_single_word():
#     assert transform_name('lizzo') == 'lizzo'

# get_lyricspages

# def test_valid_name():
#     assert get_lyricspages('princess nokia') == ['https://www.metrolyrics.com/princess-nokia-alpage-1.html']

def test_invalid_name():
    assert get_lyricspages('somethingsnotright') == None