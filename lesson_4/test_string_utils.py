from string_utils import StringUtils
import pytest 

str = StringUtils()

@pytest.mark.parametrize( 'input, output', 
[('putest', 'Putest'), 
 ('my putest', 'My putest'), 
 ('1234', '1234')
] )
def test_pos_capitalize(input, output):
    assert str.capitalize(input) == output

@pytest.mark.xfail
@pytest.mark.parametrize( 'input, output', 
[(None, None),
 ('', ''), # проходит, но не должен
(' ', ' ') # проходит, но не должен
] )
def test_neg_capitalize(input, output):
  assert str.capitalize(input) == output


@pytest.mark.parametrize( 'input, output', 
[(' putest', 'putest'), 
 (' my putest ', 'my putest ')
] )
def test_pos_trim(input, output):
    assert str.trim(input) == output

@pytest.mark.xfail
@pytest.mark.parametrize( 'input, output', 
[(None, None),
 ('', ''), 
(' ', ' '), # проходит, но не должен
('  test  ', '  test  '),
(1234, '1234')
] )
def test_neg_trim(input, output):
  assert str.trim(input) == output


@pytest.mark.parametrize( 'input, delimeter, output', 
[('me,ui,to,luv', ",", ["me", "ui", "to", "luv"]), 
 ("1233:567:890", ":", ["1233","567","890"]),
 ('me me,ui ui,to to,luv luv', ",", ["me me", "ui ui", "to to", "luv luv"])
] )
def test_pos_to_list(input, delimeter, output):
    assert str.to_list(input, delimeter) == output

@pytest.mark.xfail
@pytest.mark.parametrize( 'input, delimeter, output', 
[(None, ",", None),
 ('', ",", ''), 
(' ', ",", ' '), 
('me,ui,to,luv', ",", 'me,ui,to,luv'),
("1233, 567,890", None, ["1233","567","890"]),
("", None, []) # проходит, но не должен
] )
def test_neg_to_list(input, delimeter, output):
  assert str.to_list(input, delimeter) == output


@pytest.mark.parametrize( 'input, symbol, output', 
[('Test', "e", True),
 ('Тест', "с", True),
 ('Test testing', "t", True),
 ('12345', "3", True),
 ('$$%&*()', "*", True),
 ('super-cooling', "-", True)
] )
def test_pos_contains(input, symbol, output):
    assert str.contains(input, symbol) == output

@pytest.mark.xfail
@pytest.mark.parametrize( 'input, symbol, output', 
[('Тест', "E" , True), #eng E
 ('Test', "E", True), 
 ('Test', "р", True),
 ('', "E", True),
 (' ', "E", True),
 ('', "", True), # проходит, но не должен
 (None, "E", True),
 (None, None, True),
] )
def test_neg_contains(input, symbol, output):
  assert str.contains(input, symbol) == output


@pytest.mark.parametrize( 'input, symbol, output', 
[('Test', "e", "Tst"),
 ('Тест', "с", "Тет"),
 ('Test testing', "t", "Tes esing"),
 ('12345', "3", "1245"),
 ('$$%&*()', "*", "$$%&()"),
 ('super-cooling', "super-", "cooling"),
 ("it is", "it is", ""),
 ('12345', "", "12345"),
 ('', "", "")
] )
def test_pos_delete_symbol(input, symbol, output):
    assert str.delete_symbol(input, symbol) == output

@pytest.mark.xfail
@pytest.mark.parametrize( 'input, symbol, output', 
[('Тест', "E" , "Тст"), 
 ('Test', "E", "Tst"), 
 ('Test', "р", "Test"), # проходит, но не должен
 ('', "E", ""), # проходит, но не должен
 (' ', "E", ' '), # проходит, но не должен
 (None, "E", None),
 (None, None, None),
] )
def test_neg_delete_symbol(input, symbol, output):
  assert str.delete_symbol(input, symbol) == output


@pytest.mark.parametrize( 'input, symbol, output', 
[('Test', "T", True),
 ('Тест', "Т", True),
 ('Test testing', "T", True),
 ('12345', "1", True),
 ('$$%&*()', "$", True),
 ('super-cooling', "s", True),
 (" test", "", True)
] )
def test_pos_starts_with(input, symbol, output):
    assert str.starts_with(input, symbol) == output

@pytest.mark.xfail
@pytest.mark.parametrize( 'input, symbol, output', 
[('Тест', "E" , True), 
 ('Test', "E", True), 
 ('Test', "t", True),
 ("Test", "k", True),
 ("Test", "Te", True), # проходит, но не должен
 ('', "", True), # проходит, но не должен
 (' ', " ", True), # проходит, но не должен
 ('', "k", True), 
 (None, "E", True),
 (None, None, True)
] )
def test_neg_starts_with(input, symbol, output):
  assert str.starts_with(input, symbol) == output


@pytest.mark.parametrize( 'input, symbol, output', 
[('Test', "t", True),
 ('Тест', "т", True),
 ('Test testing', "g", True),
 ('12345', "5", True),
 ('$$%&*()', ")", True),
 ('super-cooling', "g", True),
 ("test ", "", True)
] )
def test_pos_ends_with(input, symbol, output):
    assert str.end_with(input, symbol) == output

@pytest.mark.xfail
@pytest.mark.parametrize( 'input, symbol, output', 
[('Тест', "Т" , True), 
 ('Test', "T", True), 
 ('Test', "s", True),
 ("Test", "k", True),
 ("Test", "st", True), # проходит, но не должен
 ('', "", True), # проходит, но не должен
 (' ', " ", True), # проходит, но не должен
 ('', "k", True), 
 (None, "E", True),
 (None, None, True)
] )
def test_neg_ends_with(input, symbol, output):
  assert str.end_with(input, symbol) == output


@pytest.mark.parametrize( 'input, output', 
[('', True),
 (' ', True),
 ('         ', True)
] )
def test_pos_is_empty(input, output):
    assert str.is_empty(input) == output

@pytest.mark.xfail
@pytest.mark.parametrize( 'input, output', 
[('Тест', True),
 ('Test', True), 
 (' Test ', True),
 (None, True)
] )
def test_neg_is_empty(input, output):
  assert str.is_empty(input) == output


@pytest.mark.parametrize( 'lst, joiner, output', 
[(['Test'], ", ", "Test"),
 (['Test', 'testing'], ", ", "Test, testing"),
 (['Нкси', 'Нкси'], ", ", "Нкси, Нкси"),
 ([1,2,3,4], ", ", "1, 2, 3, 4"),
 ([1456,25,399,4250], ", ", "1456, 25, 399, 4250"),
 (["I", "am", "here"], " ", "I am here"),
 (["I", "am", "here"], "", "Iamhere")
] )
def test_pos_list_to_string(lst, joiner, output):
    assert str.list_to_string(lst, joiner) == output

@pytest.mark.xfail
@pytest.mark.parametrize( 'lst, joiner, output', 
[(['Test'], ", ", ["Test"]),
 ([], ", ", []),
 ('Test', ", ", "Test"),
 ([''], ", ", ""), # проходит, но не должен
 ([' '], ", ", " "), # проходит, но не должен
 (None, ", ", None),
 (['Test', 1], "-", "Test, 1")
] )
def test_neg_list_to_string(lst, joiner, output):
  assert str.list_to_string(lst, joiner) == output