movies = []

def menu():
    print("\nWELCOME IN THE MOVIE SYSTEM!!")
    print("\n1 : To add movie")
    print("2 : To see all movies")
    print("3 : To search movie")
    print("4 : To delete movie")
    print("0 : To exit")
    
def add_movie():
    movie_name = input("\nEnter the name of movie to add : ")
    hero = input("Enter the name of hero : ")
    release_date = input("Enter the release date[dd/mm/yyyy] : ")
    seats = input("Enter the no of seats : ")
    
    movies.append({"Movie Name":movie_name , "Hero":hero , "Release Date":release_date, "Seats":seats})
    print("\n",movie_name," added successfully!! \n")
    
def all_movie():
    print("\n*********** Total MOVIESs*************")
    for m in movies:
       print('\nName : ', m["Movie Name"],'\nHero : ', m["Hero"],'\nRelease Date : ', m["Release Date"],'\nSeats : ', m["Seats"])

def search_movie():
    name = input("\nEnter Movie name to be searched : ")
    found = False
    for m in movies:
        if m["Movie Name"].lower() == name.lower():
            found = True
            print('\nName : ', m["Movie Name"],'\nHero : ', m["Hero"],'\nRelease Date : ', m["Release Date"],'\nSeats : ', m["Seats"])
            break
    if not found:
        print(name," not found!!")

def delete_movie():
    name = input("\nEnter Movie name to be deleted : ")
    found = False
    for m in movies:
        if m["Movie Name"].lower() == name.lower():
            movies.remove(m)
            found = True
            print('\n',name,' deleted successfully')
            break
    if not found:
        print(name," not found!!")

def main():
    menu()
    while True:
        choice = int(input("\nPlease Enter your choice[0-4] : "))
        if choice == 1:
            add_movie()
        elif choice == 2:
            all_movie()
        elif choice == 3:
            search_movie()
        elif choice == 4:
            delete_movie()
        elif choice == 0:
            print("\nEXITING THE MOVIE SYSTEM!!\n")
            break
        else:
            print("\nInvalid Choice!!")
            print("Please try again")
            
if __name__ == "__main__":
    main()
