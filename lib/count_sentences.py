#!/usr/bin/env python3

import re

class MyString:
    def __init__(self, value=''):
        self._value = ''
        self.value = value  

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
     if isinstance(val, str):
        self._value = val
     else:
      print("The value must be a string.")


    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        
        parts = re.split(r'[.!?]+', self.value)

        sentences = [s.strip() for s in parts if s.strip()]
        return len(sentences)



string = MyString("This is a string! It has three sentences. Right?")
print("Sentence count:", string.count_sentences())  

string.value = "Hello."
print("Is sentence:", string.is_sentence())  

string.value = "What?"
print("Is question:", string.is_question())  

string.value = "Wow!"
print("Is exclamation:", string.is_exclamation())  

string.value = "Wait... What?! Really!! No way?"
print("Complex sentence count:", string.count_sentences())  

