# -*- coding: utf-8 -*-
"""
Synopsis:
Parse the title and release date of movies, series... 

Steps:
- Ask user for the number of pages to parse
- Use a function to parse the number of websites
Imput:
- if we inspect the elements of the web we can see that class clearfix holds all info we want
- user select number of pages
Output:
- Print the releases on each page

Disclamer: The only intent of this script is to illustrate an example
of how to parse a website and how to work with regular expressions.
This is for Use at your own risk!

"""
from ParseWeb import ParseWeb

def main():
    numPages = input('Enter number of pages:')
    num = 1
    while num <= int(numPages):
        ParseWeb(num)
        num += 1
        
main()
if __name__ == '__name__':
    main()




