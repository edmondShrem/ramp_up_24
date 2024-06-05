from fastapi import FastAPI
import uvicorn
app = FastAPI()

fakeDatabase = {}

@app.get("/books/")
def getBooks():
    return fakeDatabase

@app.get("/books/{id}")
def getBook(id:int):
    return fakeDatabase[id]

@app.post("/books/")
def addBook(id, title, author, year):
    fakeDatabase[id] = {"id":id, "Title":title, "author":author, "year": year}
    return fakeDatabase[id]

@app.put("/books/{id}")
def updtadeBook(id, title, author, year):
    if not fakeDatabase.keys().__contains__(id):
         return "that book doesn't exist, silly :P"
    fakeDatabase[id]["Title"] = title
    fakeDatabase[id]["author"] = author
    fakeDatabase[id]["year"] = year
    return fakeDatabase[id]

@app.delete("/books/{id}")
def deleteBook(id):
       del fakeDatabase[id]
