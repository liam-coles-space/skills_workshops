from lib.encrypt import *
#Part 1 tests
def test_basic_letter_to_number_cipher():
    encrypt = Encrypt('A')
    assert encrypt.letter_number_cipher('a',3) == 4
    assert encrypt.letter_number_cipher('a',10) == 11
    assert encrypt.letter_number_cipher('b',3) == 5
    assert encrypt.letter_number_cipher('abc',3) == 456
    assert encrypt.letter_number_cipher('a cab',3) == 43645

#Part 2 test
def test_basic_letter_to_number_cipher():
    encrypt = Encrypt()
    assert encrypt.letter_number_cipher('My name is Edward!', 3) == 4228317416831222334726421756
    assert encrypt.letter_number_cipher('My name is Edward!',7) == 4632721820127162673811308251160

#Part 3 test
def test_new_method():
    encrypt = Encrypt()
    assert encrypt.advanced_letter_number_cipher('       ', 20) == 21212121212121
    assert encrypt.advanced_letter_number_cipher('Look over there!', 2374) == 37141410981421041798190704170452
    assert encrypt.advanced_letter_number_cipher('Look over there!', 2473) == 37141410981421041798190704170452
    assert encrypt.advanced_letter_number_cipher('Look over there!', 2572) == 37141410981421041798190704170452
    assert encrypt.advanced_letter_number_cipher('Look over there!', 7) == 4239464649850896030864646461
    assert encrypt.advanced_letter_number_cipher("'\"' a double quote can be tricky, as can be \\ backslashes", 43) == 181918444544485965465649446165596449444745584446494464625347556922444563444745584446494420444645475563564563524963