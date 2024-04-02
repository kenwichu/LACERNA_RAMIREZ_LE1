game_library = {
    "Donkey Kong" : { "Quantity" : 3, "Cost" : 2},
    "Super Mario Bros" : { "Quantity" : 5, "Cost" : 3 },
    "Tetris" : { "Quantity" : 2, "Cost" : 1}
}
user_account = {}
admin_username = "admin" 
admin_password = "adminpass"

def display_available_games():
    print(f"Available Games: {game_library}")

def sign_up():
    while True:
        balance = 0
        points = 0
        username = str(input("Enter your username: "))
        if not username: 
            main()
        if username in user_account:
            print("User already exist.")
    while True: 
        try:
            password = str(input("Enter your password: "))
            if len(password) < 8:
                print("Password must have atleast 8 characters.")
                continue
            if len(password) > 8:
                print("Sign up successful!")
                main()
            else:
                print("Invalid output.")
                continue
        except ValueError as e:
            print(e)
            sign_up()

def return_item():
    print("Item to return")
    item_to_return = str(input("Enter the game you want to return: "))
    quantity_of_the_game = input("Enter the amount of the game you want to return: ")
    game_library[item_to_return]["Quantity"] += quantity_of_the_game
    print(f"Successfully returned {quantity_of_the_game} copies of {item_to_return}.")
    rentalmain(username)

def sign_in():
    print("Sign in")
    while True:
        try:
            username = str(input("Enter your username: "))
            if not username:
                main()
            password = str(input("Enter your password:"))
            if user_account.get(username) and user_account[username]['Password']:
                print("Login Successful")
                rentalmain(username)
            else:
                print("Invalid username or password")
        except ValueError as e:
            print(e)
            sign_up()

def rent(username):
    print("Rent a game:")
    print(game_library)
    game_name = input("Select a game you would like to rent: ")
    quantity_of_the_game = input(f"How many copies of {game_name} would you like to rent: ")
    if not game_name:
        main()
    if game_library[game_name]['Quantity'] <= 0:
        print("Game is not available.")
    if game_library[game_name]['Quantity'] <= quantity_of_the_game:
        print("1. Pay using balance.")
        print("2. Pay using points")
        pay = int(input("Choose your payment method: "))
        if pay == 1:
            if user_account[username]['Balance'] <= 0:
                print("Insufficient balance.") 
            else:
                user_account[username]['Balance'] -= game_library
                print("Purchase success!")
        if pay == 2:
            if user_account[username]['Points'] <= 0:
                print("Insufficient points.") 
            else:
                user_account[username]['Points'] -= game_library
                print("Purchase success!")
        else:
            print("Invalid Output")

def rentalmain(username):
    print("Welcome to the Rental Game System")
    print("1. Rent a game")
    print("2. Return a game")
    print("3. Top up account")
    print("4. Display inventory")
    print("5. Redeem free game rental")
    print("6. Check points")
    print("7. Logout")

    choice = input("Enter your choice: ")

    while True:
        if choice == 1:
            rent(username)
        if choice == 2:
            return_item(username)
        if choice == 3:
            top_up()
        if choice == 4:
            display_available_games()
        if choice == 5:
            redeem_game()
        if choice == 6:
            check_points()
        if choice == 7:
            print("Logged Out.")
            break

def redeem_game():
    pass

def admin_login():
    print("Admin Login")
    username = input("Enter username: ")
    if not username:
        main()
    if username == admin_username:
        password = input("Enter password: ")
        if password == admin_password:
            print("Login Successful")
            admin_menu()
        else:
            print("Invalid username or password")
    else:
        print("Try again")
        admin_login()

def admin_menu():
    while True:
        try:
            print("Welcome, Admin")
            print("1. Add Quantity")
            print("2.")
            print("3.")
            print("4.")
        except ValueError as e:
            print(e)

def check_points():
    print(f"Available Balance: {user_account[username]['Balance']}")
    print(f"Available Points: {user_account[username]['Points']}")
             

def top_up(username):
    print("Top Up")
    print(f"Username: {username}")
    top_up_amount = float(input("Enter amount: "))
    user_account[username]['Balance'] += top_up_amount
    print("Top up successful")
    print(f"Username: {username}, New balance: {user_account[username]['Balance']}")
    rentalmain(username)

def logged_in_main():
    pass

def main():
    print("Welcome to the Game Rental System")
    print("1. Display Available Games")
    print("2. Reigster User")
    print("3.Log in")
    print("4. Admin Login")
    print("5. Exit")

    choice = input("Enter your choice: ")
    while True:
        if choice == 1:
            display_available_games()
        if choice == 2:
            sign_up()
        if choice == 3:
            sign_in()
        if choice == 4:
            admin_login()
        if choice == 5:
            print("Exited...")
            break
