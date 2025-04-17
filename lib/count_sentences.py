#!/usr/bin/env python3
import re

class MyString:
  def __init__(self, value = ''):
    self.value = value

  @property
  def value(self):
    """return value property"""
    return self._value
  
  @value.setter
  def value(self, value):
    if isinstance(value, str):
      self._value = value
    else:
      print('The value must be a string.')

  def is_sentence(self):
    if self.value[len(self.value) - 1] == '.':
      return True
    else: return False

  def is_question(self):
    if self.value[len(self.value) - 1] == '?':
      return True
    else: return False

  def is_exclamation(self):
    if self.value[len(self.value) - 1] == '!':
      return True
    else: return False

  def count_sentences(self):
    self.str_replace = self.value
    for i in range(len(self.value)):
      if self.value[i] in '?.!' and self.value[i] == self.value[i - 1]:
        self.str_replace.replace(self.str_replace[i], ',', 1)
    str_list = [s for s in re.split(r'[.?!]', self.str_replace) if s]
    return len(str_list)
