from exercice import Solution
import pytest
    
test_cases = {0: '',
    1: 'I',
    2: 'II',
    4: 'IV',
    44: 'XLIV',
    66: 'LXVI',
    89: 'LXXXIX',
    99: 'XCIX',
    149: 'CXLIX',
    271: 'CCLXXI',
    1026: 'MXXVI',
    2999: 'MMCMXCIX',
    3725: 'MMMDCCXXV',
    4999: 'MMMMCMXCIX'}

@pytest.mark.parametrize("input_val, expected_output", test_cases.items())
def test_solution(input_val, expected_output):
    assert Solution(input_val).output == expected_output
    

    
    
    