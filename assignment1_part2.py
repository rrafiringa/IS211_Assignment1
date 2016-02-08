#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Assignment 1 part 2 """


class Book(object):
    """ Book class"""
    def __init__(self, bauthor, btitle):
        """
        Constructor.
        Args:
            bauthor (String): Input book author.
            btitle (String): Input book title.
        Attributes:
            author (String): Book author.
            title (String): Book title
        Examples:
            >>> THEBOOK = Book('Bjarne Stroustrup', 'C++')

        """
        self.author = bauthor.strip().title()
        self.title = btitle.strip().title()

    def display(self):
        """
        Display book info.
        Args:
        Returns:
            String: Book information
        Examples:
            >>> MYBOOK = Book('Frank Herbert', ' dune')
            Dune by Frank Herbert
        """
        return '{}, written by {}'.format(self.title, self.author)


if __name__ == '__main__':
    MYBOOK = Book('Louis pergaud', ' the war of the buttons')
    print MYBOOK.display()