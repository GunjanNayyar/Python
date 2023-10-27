from dbhelper import DBHelper
def main():
    db=DBHelper()
    while True:
        print("**********WELCOME*************")
        print()
        print("Press 1. To insert the Book data")
        print("Press 2. To display all the Books")
        print("Press 3. To delete the Book data")
        print("Press 4. To update the Book data")
        print("Press 5. To exit the program")
        print()
        try:
            choice=int(input())
            if(choice==1):
                #insert book
                bid=int(input("Enter Book Id:"))
                bname=input("Enter Book Name:")
                bprice=int(input("Enter Book Price:"))
                db.insert_book(bid,bname,bprice)
            elif(choice==2):
                #display book
                db.fetch_all()
            elif(choice==3):
                #delete book
                bid=int(input("Enter Book Id which you want to delete:"))
                db.delete_book(bid)
            elif(choice==4):
                #update book
                bid=int(input("Enter Book Id you want to update:"))
                bname=input("Enter New Book Name:")
                bprice=int(input("Enter New Book Price:"))
                db.update_book(bid,bname,bprice)
            elif(choice==5):
                pass
                break
            else:
                print("Invalid input!!! Try again")
        except Exception as e:
            print(e)
            print("Invalid detail!! Try again")

    
if __name__=="__main__":
    main()


#main coding
# helper = DBHelper()
# # helper.insert_book(102,"The psychology of moon", 300)
# # helper.insert_book(103,"If tomorrow comes", 180)
# # helper.insert_book(104,"A stranger in the mirror", 450)
# #helper.delete_all(103)
# helper.update_book(102,"Sydney Sheldon",700)
# helper.fetch_all()




