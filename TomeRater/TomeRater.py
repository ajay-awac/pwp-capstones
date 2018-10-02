class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email 
        self.books = {}

    def get_email(self):
        return(self.email)

    def change_email(self, new_email):
        self.email = new_email
        print('The email address for the user: ' + self.name + ' has been updated.')

    def __repr__(self):
        return('User ' + self.name + ', email: ' + self.email + ', books read: ' + str(len(self.books)))

    def __eq__(self, other_user):
        return (type(other_user) == User and self.name == other_user.name and self.email == other_user.email)
        
    def read_book(self, book, rating=None):
        self.books[book] = rating
    
    def get_average_rating(self):
        sum = 0
        count = 0
        for book in self.books.keys():
            if self.books[book] != None:
                sum += self.books[book]
                count += 1
        
        return(sum/count)
        
    
class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn 
        self.ratings = []

    def get_title(self):
        return(self.title)

    def get_isbn(self):
        return(self.isbn)
    
    def set_isbn(self, isbn):
        self.isbn = isbn
        print('The ISBN for the book with title: ' + self.title + ' has been updated.')
        
    def add_rating(self, rating):
        if rating == None:
            return
        if rating >= 0 and rating <= 4: 
            self.ratings.append(rating)
        else:
            print('Invalid Rating')    

    def __eq__(self, other_book):
        return (self.title == other_user.title and self.isbn == other_user.isbn)

    def __repr__ (self):
        return('{title} with ISBN: {isbn}'.format(title = self.title, isbn = str(self.isbn)))
        
    def __hash__(self):
        return hash((self.title, self.isbn))    
        
    def get_average_rating(self):
        sum = 0
        count = 0
        for rating in self.ratings:
            if rating != None:
                sum += rating
                count += 1
        return(sum/count)    


class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author
    
    def get_author(self):
        return(self.author)
    
    def __repr__ (self):
        return('{title} by {author}'.format(title = self.title, author = self.author))


class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level
        
    def get_subject(self):
        return(self.subject)    
        
    def get_level(self):
        return(self.level)        

    def __repr__(self):
        return('{title}, a {level} manual on {subject}'.format(title = self.title, level = self.level, subject = self.subject))


class TomeRater:
    
    def __init__(self):
        self.users = {}
        self.books = {}

    def Book_ISBN_Exists(self, isbn):
        for book in self.books:
            if book.get_isbn() == isbn:
                print("Book with ISBN: {isbn} already exists !!".format(isbn = isbn))
                return(True)
        return(False)

    def create_book(self, title, isbn):
        #Make sure that books all have unique ISBNs
        if self.Book_ISBN_Exists(isbn) == False:
            return (Book(title, isbn))

    def create_novel(self, title, author, isbn):
        #Make sure that books all have unique ISBNs
        if self.Book_ISBN_Exists(isbn) == False:
            return (Fiction(title, author, isbn))
        
    def create_non_fiction(self, title, subject, level, isbn):
        #Make sure that books all have unique ISBNs
        if self.Book_ISBN_Exists(isbn) == False:
            return (Non_Fiction(title, subject, level, isbn))

    def add_book_to_user(self, book, email, rating=None):
        # find out the user from self.users
        if self.users.get(email) == None:
            print("No user with email {email}!".format(email = email))
        else:    
            user = self.users.get(email)
            user.read_book(book, rating)
            book.add_rating(rating)
            if (self.books.get(book, None) == None):
                self.books[book] = 1
            else:
                self.books[book] += 1
            
    def add_user(self, name, email, user_books=None):
        
        #If someone tries to add a user with an email that already
        #exists in TomeRater , print out a message telling them that
        #this user already exists
        
        if self.users.get(email) != None:
            print("User already exists !! Email: {email}".format(email = email))
        elif self.validate_email(email) == True:
            user = User(name, email)
            self.users[email] = user
            if (user_books != None):
                for book in user_books:
                    self.add_book_to_user(book, email)
                
    def print_catalog(self):
        for book in self.books:
            print(book)
            
    def print_users(self):
        for user in self.users:
            print(self.users[user])    
            
    def get_most_read_book (self):
        books = list(self.books)
        no_of_reads = list(self.books.values())
        
        max = 0
        max_index = 0
        for idx in range(0, len(no_of_reads)):
            if no_of_reads[idx] > max:
                max = no_of_reads[idx]
                max_index = idx
        return(books[max_index])
        
    def highest_rated_book(self):
        books = list(self.books)
        ratings = [k.get_average_rating() for k in self.books.keys()]
        
        max = 0
        max_index = 0
        for idx in range(0, len(ratings)):
            if ratings[idx] > max:
                max = ratings[idx]
                max_index = idx
        return(books[max_index])

    def most_positive_user (self):
        max = 0
        for user in self.users:
            if self.users[user].get_average_rating() > max:
                key = user
                max = self.users[user].get_average_rating()
        return (self.users[key])

    def validate_email(self, email):
        # email should have one and only one @ symbol
        if email.count("@") != 1:        
            print ("Invalid Email: {email} ".format(email = email))
            return (False)
            
        #Make sure that an email address is valid by checking if it
        #has an @ character and either .com , .edu , .org
        if (email[-4:].upper() != ".COM" and
           email[-4:].upper() != ".EDU" and
           email[-4:].upper() != ".ORG"):
           print ("Invalid Email: {email} ".format(email = email))
           return (False)
        
        return (True)    

    