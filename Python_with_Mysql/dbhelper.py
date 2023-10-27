import mysql.connector 
class DBHelper:
    def __init__(self):
        self.con=mysql.connector.connect(host='localhost',
                                         port='3306',
                                         user='root', 
                                         password='root',
                                         database='pythontest')        
        query = 'create table if not exists book(bookId int primary key, bookName varchar(100),bookPrice int)'
        mycur=self.con.cursor()
        mycur.execute(query)
       # mycur.execute("create table")
        print("Created")

    #insert data
    def insert_book(self, bookid, bookname, bookprice):
        query = "insert into book(bookId, bookName, bookPrice) values ({},'{}',{})".format(bookid,bookname,bookprice)
        # print(query)
        mycur=self.con.cursor()
        mycur.execute(query)
        self.con.commit()
        print("user saved to table")

    #Fetch all data
    def fetch_all(self):
        query='select * from book'
        mycur=self.con.cursor()
        mycur.execute(query)
        for row in mycur:
            print("Book Id:",row[0])
            print("Book Name:",row[1])
            print("Book Price:",row[2])
            print()
            print()

    #Delete an Book
    def delete_book(self,bookid):
        query='delete from book where bookId={}'.format(bookid)
        # print(query)
        mycur=self.con.cursor()
        mycur.execute(query)
        self.con.commit()
        print("Data deleted")

    #update the book
    def update_book(self,bookid,newname,newprice):
        query="update book set bookName='{}', bookPrice={} where bookId={}".format(newname,newprice,bookid)
        mycur=self.con.cursor()
        # print(query)
        mycur.execute(query)
        self.con.commit()
        print("Data updated")