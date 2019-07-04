'''
Author:Chris Moran
Contact:chris@equalreality.com
Date:2019/06/28
Licence: GPLv3
Version:0.1
How Do You Feel - Terminal application test
This script tests the funtions of the HDYF application
'''

import json
from os import remove as delete_file
from hdyf import input_checker
from hdyf import file_to_string
from hdyf import file_to_dict

def test_input_checker():
    test1 = 'SHOULD BE LOWER'
    test2 = 134
    assert input_checker(test1) == test1.lower()
    assert input_checker(test2) is None

def test_file_to_string():
    test1 = 'This is a quote'
    test2 = 'Something else'
    filename = 'test-emotion-dict.txt'
    with open(filename, 'x+') as file:
        file.write(test1)
    assert file_to_string(filename) == test1
    assert file_to_string(filename) != test2
    delete_file(filename)

def test_file_to_dict():
    check = {'key': 'value'}
    check2 = {'key1': 'value1'}
    test = json.dumps({'key': 'value'})
    filename = 'test-emotion-dict.json'
    with open(filename, 'x+') as file:
        file.write(test)
    assert file_to_dict(filename) == check
    assert file_to_dict(filename) != check2
    delete_file(filename)
