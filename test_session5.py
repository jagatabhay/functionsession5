import pytest , session5 , re , inspect , os

README_CONTENT_CHECK_FOR = ['temp_convertor']



#1 Inavlid Temperature Type Check
def test_invalidtemperature():
    with pytest.raises(NotImplementedError):
        session5.temp_converter(temp = 32 , temp_given_in = 'x')


#2 README Exists
def test_readmeexist():
    assert os.path.isfile("README.md") , 'README File is missing'


#5 identation check
def test_identation():
    lines = inspect.getsource(session5)
    spaces = re.findall('\n +.',lines)
    for space in spaces:
        assert re.search('[a-zA-Z#@\'\"]', space) , 'Your code identation does not follow PEP8 guidelines'
        assert len(re.sub(r'[a-zA-Z#@\n\"\']', '', space)) % 4 == 0 , 'Your code doesnot follow PEP8 guidelines'


#4 Out of Range Polygon check.
def test_notvalidpolygon():
    with pytest.raises(NotImplementedError):
        session5.polygon_area(side_length = 5 , side = 10)


#5 README formatting
def test_readme_for_formatting():
    readme = open('README.md','r')
    content = readme.read()
    readme.close()
    assert content.count('#') >= 5 , "Kindly format the README.md"


#6 speed_converter  negative check
def test_speed_negative_check():
    with pytest.raises(ValueError):
        session5.speed_converter(speed = -10 , dist = 'km' , time = 'ms' )



#7 Ploygon side length negative
def test_negative_side_length():
    with pytest.raises(ValueError):
        session5.polygon_area( side_length = -3 , side = 9)



#8 speed_converter  dist valid check
def test_valid_dist_check():
    with pytest.raises(ValueError):
        session5.speed_converter(speed = 10 , dist = 0 , time = 'ms')


#9 speed_converter Time valid check
def test_valid_time_check():
    with pytest.raises(ValueError):
        session5.speed_converter(speed = -100 , dist = 'KM' , time = 0)


#10 speed_converter wrong combination arguments.
def test_wrong_combination_input():
    with pytest.raises(ValueError):
        session5.speed_converter(speed = 200 , dist = 'KM' , time = 'lightyear')


#11 Function name had caps letter
def test_funcation_had_cap_letter():
    functions = inspect.getmembers(session5, inspect.isfunction )
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"



#12 temp_converter Negative temperature check
def test_negative_temp_check():
    with pytest.raises(ValueError):
        session5.temp_converter(temp = -1 , temp_given_in = 'c')



#13 squared_power_list negative number check
def test_negative_power_number():
    with pytest.raises(ValueError):
        session5.squared_power_list( number = -5 )



#14 squared_power_list inavlid start and end 
def test_invalid_start_end():
    with pytest.raises(ValueError):
        session5.squared_power_list( number = 10 , start = 10 , end = 2)



#15 squared_power_list wrong combination
def test_wrong_square_power_combo():
    with pytest.raises(ValueError):
        session5.squared_power_list( number = 10 , start = 'xyz' , end = 4 )



#16 squared_power_list invalid number pass
def test_string_number_check():
    with pytest.raises(ValueError):
        session5.squared_power_list( number = 'Hola' , start = 'xyz'  , end = 7 )



#17 Return Type Check squared_power_list
def test_square_power_return_number():
    a = session5.squared_power_list( number = 2 , start = 1 , end = 4 )
    assert type(a) == list , "Invalid Return Type"



#18 temperature return type check
def test_temp_return_type_check():
    a = session5.temp_converter( 15 , temp_given_in = 'C')
    assert type(a) == float or type(a) == int , "How How temperature can be in String"



#19 Square Power Check
def test_squared_power_list():
    q1=session5.squared_power_list(2 , start=0, end=5 )
    assert q1 == [1, 2, 4, 8, 16, 32] ,'Wrong Result'



#20 print check
def test_print_function():
    a=print(1, 2, 3, sep='-', end= ' ***\n')
    assert bool(a) == False


# 21 ReadMe Words Count
def test_readme_words_counts():
    readme = open('README.md','r')
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 100 , "Kindly define README properly"



#22 Read Proper Description
def test_readme_proper_desscription():
    READMELOOKSGOOD = True
    readme = open('README.md','r')
    readme_words = readme.read().split()
    readme.close()
    for words in README_CONTENT_CHECK_FOR:
        if words not in readme_words:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True , "You have not defined all functions/classes in README.md"
