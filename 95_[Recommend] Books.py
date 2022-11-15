"""Books"""
import math
def main():
    """Books"""
    book = int(input())
    page = int(input())
    xxx = int(input())
    yyy = int(input())
    day = 0
    read_book = 0
    read_page = 0
    book_day = 0
    while True:
        if read_book == book:
            break
        read_page = read_page + math.ceil(((xxx+day)/(yyy+day))*page)
        day += 1
        book_day += 1
        if read_page >= page:
            if book_day == 1:
                day = day + (book-read_book) - 1
                return print(day)
            read_book += 1
            read_page = 0
            book_day = 0
    print(day)
main()
