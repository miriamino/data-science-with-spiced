from helper_functions import transform_name, get_lyricspages, get_urls, get_lyrics, transform_answer

# transform_name

def test_uppercase():
    assert transform_name('Mariah Carey') == 'mariah-carey'

def test_lowercase():
    assert transform_name('mariah carey') == 'mariah-carey'

def test_single_word():
    assert transform_name('lizzo') == 'lizzo'

# transform_answer
def test_y():
    assert transform_answer('y') == 1

def test_yes():
    assert transform_answer('yes') == 1

def test_n():
    assert transform_answer('n') == 0

def test_bla():
    assert transform_answer('bla') == None


# # get_lyricspages

# def test_valid_name():
#     assert get_lyricspages('princess nokia') == ['https://www.metrolyrics.com/princess-nokia-alpage-1.html']

# def test_invalid_name():
#     assert get_lyricspages('somethingsnotright') == None

# def test_number_of_pages():
#     assert len(get_lyricspages('mariah carey')) == 6

# def test_number_of_pages_one():
#     assert len(get_lyricspages('princess nokia')) == 1

# # get_urls

# def test_get_url():
#     assert len(get_urls('princess-nokia',['https://www.metrolyrics.com/princess-nokia-alpage-1.html'])) == 29


# # get_lyrics

# def test_site_with_lyrics():
#     assert get_lyrics('https://www.metrolyrics.com/saggy-denim-lyrics-princess-nokia.html') == ('Saggy Denim', 'Princess Nokia', "\nSaggy denim, 1995\nI be all in 'em, L.L on the side\nIn my Tommy boxers or my Calvin Klein\nOoh baby, ooh baby, I love to get fly\n\nGotta get 'em Ralph Lauren denim\nPatches on that ass, my ass a good fitting\n1995, I'ma listen to Sublime\nDrink that 40oz. to Freedom to the day that I die\nGonna listen me Selena, drink a 40 a cry\nGonna roll me up a Beamer, I'ma go and get high\nWhile it's 1995, getting fly to pass the time\nI'ma slip up from behind while he go and buy that wine\nWe ain't looking at the time, don't nobody got a phone\nWe gon' kick it in the park and we ain't never going home\nCuly Culkin, Home Alone, while I'm smoking on a bone\nNew York City is my throne and I love to call it home\n\nSaggy denim, 1995\nI be all in 'em, L.L on the side\nIn my Tommy boxers or my Calvin Klein\nOoh baby, ooh baby, I love to get fly\n\nI speak that Gualla Gualla, that peso, pound, and dollar\nThat oocjie walla walla polo rican mama mama\nCome holla at ya Gualla, they hootin and they holla\nThat platano banana, roll my weed in my fanta\nI speak that Gualla Gualla\nThat Spanish hoochie mama\nThat Puerto Rican drama\nThat fuck you, pay me, nana\nI care about my comma\nI got a code of honor\nI smoke the bestest weed\nShout out my plug and farmer\nI speak that mira mira\nThat mira, oye linda\nThat vien aqui mi'jita\nTu eres mi chiquita\nI grew up in the projects with nasty stairs and halls\nThe ghetto has no censor and I done seen it all\n\nThat's why I see your cause\nAnd I see your flaws\nBut I see that you a G, and yeah, you be a boss\nGood chick with some rad tricks\n main chick\nSo I'ma leave alone\nIce cream and the cone\n L-O-V-E, baggy jeans is on\nAnd you know me, I be  sneakers on\n slow\nDestiny rides by me blowin\nSex in the sky to the extent that we high\nBorn in the same place, took a minute to find ya\nI'm tryin but you tryin to say my time's up\nAnd I've lied enough\nI haven't tried enough\nSo I gotta say some shit before this rhyme is up\nDes, my love\nMy thug, my drug\nWhen I gon' make my mind up\n\nSaggy denim, 1995\nI be all in 'em, L.L on the side\nWith my Tommy boxers or my Calvin Klein\nOoh baby, ooh baby, I love to get fly\nThe red and blue, yellow and white too\n1992, campus, we row crew\nWindbreakers with my 40 acres\nChillin like the quakers I roll through with mad flavors\nWent from philly dutches papers")

# def test_site_without_lyrics():
#     assert get_lyrics('https://www.metrolyrics.com/balenciaga-lyrics-princess-nokia.html') == None

