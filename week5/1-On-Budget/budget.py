def on_budget(books, budget):
    books = sorted(books)
    book_counter = 0
    loan = 0
    
    for book in books:
        budget -= book
        if budget >= 0:
            book_counter += 1
    if budget < 0:
            loan = -(budget)
    arr = {
        "books_on_budget": book_counter,
        "loan": loan
        }
    
    return arr
        
        
print(on_budget([0, 10, 100, 5, 3, 8, 25],35))
