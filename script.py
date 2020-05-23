import utils
import sorts

bookshelf = utils.load_books('books_small.csv')
for book in bookshelf:
  print(book['title'])

def by_title_ascending(book_a, book_b):
  if book_a['title_lower'] > book_b['title_lower']:
    return True
  else:
    return False

def by_author_ascending(book_a, book_b):
  if book_a['author_lower'] > book_b['author_lower']:
    return True
  else:
    return False

def by_total_length(book_a, book_b):
  if len(book_a['title_lower']) + len(book_a['author_lower']) > len(book_b['title_lower']) + len(book_b['author_lower']):
    return True
  else:
    return False

bookshelf_v1 = bookshelf[:]
bookshelf_v2 = bookshelf[:]
long_bookshelf = utils.load_books('books_large.csv')

sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)
for book in sort_1:
  print(book['title'])

sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)
for book in sort_2:
  print(book['title'])

sort_3 = sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2)-1, by_author_ascending)
print(sort_3)

#sort_4 = sorts.bubble_sort(long_bookshelf, by_total_length)

sorts.quicksort(long_bookshelf, 0, len(long_bookshelf)-1, by_total_length)

for book in long_bookshelf:
  print(len(book['title_lower']) + len(book['author_lower']))