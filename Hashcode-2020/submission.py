from math import *
books = []
libraries = []

bookid_to_books = {}
library_id_to_library = {}

remaining_days = 0

def get_ints():
	return [int(i)for i in input().split()] 

def get_books_score(books):
	return [book.score for book in books]

def get_book_by_id(id):
	return bookid_to_books[id]

# def get_library_books(library):
#   return [get_book_by_id(book_id) for book_id in library.books]

def top_n(books, remaining_days):
	return books[:remaining_days]

def ratio_max_sign_up(library):
	return sum(get_books_score(library.books))/library.sign_up_days

def ratio_possible_max_sign_up(library):
	global remaining_days
	# return sum(get_books_score(library.books))/   library.sign_up_days
	try:
		return library.num_of_books/sum(get_books_score(top_n(library.books,remaining_days*library.ship_per_day)))
	except ZeroDivisionError:
		return 100000000000000000000

def ratio_ship_per_day_sign_up(library):
	return library.ship_per_day/library.sign_up_days

def shortest_sign_up(library):
	return library.sign_up_days

def biggest_ship_per_day(library):
	return library.ship_per_day

def ratio_max_score_ship_per_day(library):
	return get_books_score(library.books)/library.ship_per_day

def max_scored(library):
	return sum(get_books_score(library.books))

class Book:

	def __init__(self,score,bid):
		self.score = score
		self.bid = bid
		self.selected = 0
		bookid_to_books[self.bid] = self

	def __str__(self):
		return f"Book: {self.bid}"

	def __repr__(self):
		return self.__str__()

class Library:

	def __init__(self,num_of_books,sign_up_days,ship_per_day,lid):
		self.num_of_books = num_of_books
		self.sign_up_days = sign_up_days
		self.ship_per_day = ship_per_day
		self.books = []
		self.lid = lid
		self.to_send = 0

	def load_books(self,books):
		self.books = books

	def __str__(self):
		return f"Library: {self.lid}"

	def __repr__(self):
		return self.__str__()

B,L,D = get_ints()
remaining_days = D

for book_id,book_score in enumerate(get_ints()):
	new_book = Book(book_score, book_id)
	books.append(new_book)

for library_id in range(L):

	num_of_books, sign_up_days, ship_per_day = get_ints()
	new_library = Library(num_of_books, sign_up_days, ship_per_day, library_id)
	new_library.load_books([get_book_by_id(bid)for bid in get_ints()])

	libraries.append(new_library)
# sorted_libraries = sorted(libraries, key = ratio_max_sign_up)
# sorted_libraries = sorted(libraries, key = shortest_sign_up)

sorted_libraries = sorted(libraries, key = shortest_sign_up)


selected_books = []
selected_from = []
selected_books_dict = {}
for library in sorted_libraries:
	# print("Library:",library)
	# print("Library Sign Up Days:",library.sign_up_days)
	lib_books = library.books
	sorted_lib_books = sorted(lib_books,key = lambda book:book.score, reverse=True)
	# print("Sorted Books:",sorted_lib_books)
	# print("Sorted Books Score:",get_books_score(sorted_lib_books))
	# print("Remaining Days:",remaining_days)
	# print("Remaining Days After Signup:",remaining_days-library.sign_up_days)
	current_selected_books = []
	selected_books_dict[library.lid] = []
	for book in sorted_lib_books:
		if book.selected:
			continue
		if ceil(len(current_selected_books)/library.ship_per_day) < remaining_days-library.sign_up_days:
			current_selected_books.append(book)
			selected_books_dict[library.lid].append(book)
			book.selected = 1
			library.to_send += 1
			if not library in selected_from:
				selected_from.append(library)

	remaining_days -= library.sign_up_days
	selected_books += current_selected_books
	# sorted_libraries.remove(library)
	# sorted_libraries = sorted(libraries, key = ratio_possible_max_sign_up)
	# print("Selected Books:",selected_books)
	# sorted_libraries.remove(library)
	# sorted_libraries = sorted(libraries, key = ratio_possible_max_sign_up)
#   print("Selected Books Score:",get_books_score(selected_books))
#   print("Selected Books Score Sum:",sum(get_books_score(selected_books)))
#   print()
# print("Selected From:",selected_from)

print(len(selected_from))
for library in selected_from:
	print(library.lid, library.to_send)
	# print(selected_books)
	for book in selected_books_dict[library.lid]:
		# print(library.books)
		if book in library.books:
			print(book.bid,end=" ")
	print()

