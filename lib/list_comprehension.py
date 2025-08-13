#!/usr/bin/env python3

def return_evens(sequence):
    # Return only even numbers using a list comprehension
    return [n for n in sequence if n % 2 == 0]

def make_exclamation(sentences):
    # Append "!" to each sentence using a list comprehension
    return [sentence + "!" for sentence in sentences]
