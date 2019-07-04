'''
Author:Chris Moran
Contact:chris@equalreality.com
Date:2019/06/28
Licence: GPLv3
Version:0.1
How Do You Feel - Terminal application test
This script tests the funtions of the HDYF application
'''

import os
import json
from os import remove as delete_file
from hdyf import input_checker
from hdyf import file_to_string
from hdyf import file_to_dict

def test_input_checker():
    TEST1 = 'SHOULD BE LOWER'
    TEST2 = 134
    
    assert input_checker(TEST1) == 'should be lower'
    assert input_checker(TEST2) == None

def test_file_to_string():
    TEST1 = 'This is a quote'
    TEST2 = 'Something else'
    FILENAME = 'test-emotion-dict.txt'
    with open(FILENAME, 'x+') as file:
        file.write(TEST1)
    
    assert file_to_string(FILENAME) == TEST1
    assert file_to_string(FILENAME) != TEST2
    delete_file(FILENAME)

def test_file_to_dict():
    CHECK = {'key': 'value'}
    CHECK2 = {'key1': 'value1'}
    TEST = json.dumps({'key': 'value'})
    #TEST1 = json.dumps({'key1': 'value1'})
    FILENAME = 'test-emotion-dict.json'
    with open(FILENAME, 'x+') as file:
        file.write(TEST)
    
    assert file_to_dict(FILENAME) == CHECK
    assert file_to_dict(FILENAME)!= CHECK2
    delete_file(FILENAME)
