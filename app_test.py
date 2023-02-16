import pytest
import pandas as pd
from pandas.testing import assert_frame_equal
from baby_names import BabyNamesProject

file_name = 'data/yob2002.txt'

bn = BabyNamesProject(file_name=file_name, separator=',')

def test_row_cols_count():
    assert bn.number_rows_cols() == (30568, 3,)

def test_total_babies_born():
    assert bn.total_babies_born() == 3737470

def test_total_babies_born_by_sex():
    assert bn.total_babies_born_by_sex() == (1941037, 1796433,)

def test_if_name_in_data():
    assert bn.check_name('emily') == True
    assert bn.check_name('Emily') == True
    assert bn.check_name('eMILY') == True
    assert bn.check_name('EmIlY') == True

def test_if_not_name_in_data():
    assert bn.check_name('Tope') == False
    assert bn.check_name('tope') == False
    assert bn.check_name('hsytsjasa') == False
    assert bn.check_name('HYtrE4c') == False
    assert bn.check_name('1233456') == False

def test_if_name_is_empty():
    with pytest.raises(ValueError) as e:
        assert bn.check_name('') == e

def test_if_not_string_value():
    with pytest.raises(TypeError) as e:
        assert bn.check_name(1) == e

def test_percentage_sex_group():
    assert bn.percentage_boys_girls() == (51.93, 48.07,)

def test_top_names_by_sex():
    table = {'Top Boys Names': ['Jacob', 'Michael', 'Joshua', 'Matthew', 'Ethan'], 
             'Top Girls Names': ['Emily', 'Madison', 'Hannah', 'Emma', 'Alexis']}
    assert_frame_equal(bn.top_names(), pd.DataFrame(table))