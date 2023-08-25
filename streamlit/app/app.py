import streamlit as st
import pandas as pd
import numpy as np
import requests as rq
import json
import os
import subprocess

st.title('Make your own Roman Number Encoder!!!')
st.markdown('Your task is the code a function in Python that takes an integer (0 <= n= <= 4999) as input and return its corresponding Roman number in string')
st.markdown('Test cases will only be integer ranging from 0 to 4999')
st.markdown('Guide line about Roman numerals notation can be found here https://en.wikipedia.org/wiki/Roman_numerals')
st.image('https://images.fineartamerica.com/images-medium-large-5/roman-numerals-carved-in-stone-staci-bigelow.jpg')

if st.button('Reveal Solution'):       
    exercice_solution = '''class Solution:
        def __init__(self, input : int):
            self.input = input
            self.output = self.solution(self.input)
            
        def solution(self, input):
            roman = {1:'I', 4: 'IV', 5:'V', 9:'IX', 10:'X', 40:'XL', 50: 'L', 90:'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
            output = ''
            while input != 0:    
                val = max([i for i in list(roman.keys()) if i <= input])
                input -= val
                output += roman[val] 
            return output'''
    st.code(exercice_solution, language="python")

code = st.text_area('Complete the code above and clic the submit button', 
'''class Solution:
    def __init__(self, input : int):
        self.input = input
        self.output = self.solution(self.input)
        
    def solution(self, input):
        return
    ''')


if st.button('Submit'):
    file_name = "exercice.py"

    # Open the file in write mode and write the string content
    with open(file_name, "w") as file:
        file.write(code)
        
    # Define the command you want to run
    command = "pytest > test_results.txt"

    # Run the command in the terminal
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check if the command was successful
    if result.returncode == 0:
        print("Command executed successfully!")
        print("Output:")
        print(result.stdout)
    else:
        print("Command failed with error:")
        print(result.stderr)
    
    file_path = "test_results.txt"

    try:
        with open(file_path, "r") as file:
            # Read the entire content of the file
            content = file.read()

        # Do something with the content
        print(content)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    st.markdown(content)
    
    if '14 passed' in content:
        st.image('https://i.guim.co.uk/img/media/384faecfbbc32859bc269b915a3f1fdeaa60a266/154_360_2795_1677/master/2795.jpg?width=1300&dpr=2&s=none')   
    
