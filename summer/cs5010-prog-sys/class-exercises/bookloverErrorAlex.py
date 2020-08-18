# Module 5 Live Session Exercise: Testing Activity
# Alex Stern
# acs4wq



class BookLover:
    # initialize fields
    def __init__(self, name, email,
                 favGenre, numBooks=None, bookLst=None):
        self.name = name
        self.email = email
        self.favGenre = favGenre
        if numBooks is None:
            self.numBooks = 0
        else:
            self.numBooks = numBooks 
        if bookLst is None:
            self.bookLst = []
        else:
            self.bookLst = bookLst 
    
    # print(BookLover)
    def __str__(self):
        return 'Name: '+self.name+'\n Book List: '+str(self.bookLst)
    
    # add a book to book list, increment numBook 1
    def addBook(self, bookName, rating):
        # check if book has already been read
        if self.hasRead(bookName):
            return False 
        # add book
        self.bookLst.append((bookName, rating))
        return True  
    
    # look for bookName in book list
    def hasRead(self, bookName):
        if self.numBooks > 0:
            for i in range(self.numBooks):
                # do any books in the book list match 'bookName'?
                if self.bookLst[i][0] == bookName:
                    return True 
    
    # return numBooks
    def numBooksRead(self):
        return self.numBooks
    
    # look for all books w/ rating > 3
    def favBooks(self):
        fav = []
        for i in range(self.numBooks):
            if self.bookLst[i][1] >= 3:
                fav.append(self.bookLst[i][0])
        return fav 
    