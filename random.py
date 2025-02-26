users = []

def sign_up():
    name = input("Enter your name: ")
    email = input("Enter your email ID: ")
    password = input("Enter your password: ")

    if any(user['Email'] == email for user in users):
        print("Email ID already exists. Please try logging in.")
        return

    users.append({"Name": name, "Email": email, "Password": password})
    print("Sign-up successful!")

def login():
    email = input("Enter your email ID: ")
    password = input("Enter your password: ")

    if any(user['Email'] == email and user['Password'] == password for user in users):
        print("Login successful.")
    else:
        print("Login failed. Invalid email ID or password.")

def display_users():
    if users:
        print("\n{:<20} {:<30} {:<15}".format("Name", "Email", "Password"))
        print("-" * 65)
        for user in users:
            print("{:<20} {:<30} {:<15}".format(user['Name'], user['Email'], user['Password']))
    else:
        print("No users found.")

def delete_user():
    email = input("Enter the email ID of the user to delete: ")

    for user in users:
        if user['Email'] == email:
            users.remove(user)
            print("User deleted successfully.")
            return

    print("User not found.")

def main():
    while True:
        print("\n1. Sign-up\n2. Login\n3. Display all users\n4. Delete a user\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            sign_up()
        elif choice == '2':
            login()
        elif choice == '3':
            display_users()
        elif choice == '4':
            delete_user()
        elif choice == '5':
            if users:
                print("\nAll registered users:\n")
                print("{:<20} {:<30} {:<15}".format("Name", "Email", "Password"))
                print("-" * 65)
                for user in users:
                    print("{:<20} {:<30} {:<15}".format(user['Name'], user['Email'], user['Password']))
            else:
                print("\nNo users registered.\n")
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()