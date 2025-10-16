from lib.artists import Artist
from lib.artworks import Artwork
from lib.sales import Sale

def main_menu():
    while True:
        print("\n🎨 ART GALLERY MANAGEMENT SYSTEM 🎨")
        print("1. Manage Artists")
        print("2. Manage Artworks")
        print("3. Manage Sales")
        print("4. Exit")

        choice = input("Select an option (1–4): ")

        if choice == "1":
            artist_menu()
        elif choice == "2":
            artwork_menu()
        elif choice == "3":
            sale_menu()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

def artist_menu():
    while True:
        print("\n--- Manage Artists ---")
        print("1. Add Artist")
        print("2. View All Artists")
        print("3. Back to Main Menu")

        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter artist name: ")
            nationality = input("Enter nationality: ")
            birth_year = int(input("Enter birth year: "))
            Artist.add_artist(name, nationality, birth_year)
        elif choice == "2":
            Artist.view_all_artists()
        elif choice == "3":
            break
        else:
            print("❌ Invalid choice.")

def artwork_menu():
    while True:
        print("\n--- Manage Artworks ---")
        print("1. Add Artwork")
        print("2. View All Artworks")
        print("3. Back to Main Menu")

        choice = input("Select an option: ")

        if choice == "1":
            title = input("Enter artwork title: ")
            medium = input("Enter medium: ")
            year_created = int(input("Enter year created: "))
            price = float(input("Enter price: "))
            artist_id = int(input("Enter artist ID: "))
            image_url = input("Enter image URL (optional): ") or None
            Artwork.add_artwork(title, medium, year_created, price, artist_id, image_url)
        elif choice == "2":
            Artwork.view_all_artworks()
        elif choice == "3":
            break
        else:
            print("❌ Invalid choice.")

def sale_menu():
    while True:
        print("\n--- Manage Sales ---")
        print("1. Add Sale")
        print("2. View All Sales")
        print("3. Back to Main Menu")

        choice = input("Select an option: ")

        if choice == "1":
            artwork_id = int(input("Enter artwork ID: "))
            buyer_name = input("Enter buyer name: ")
            sale_amount = float(input("Enter sale amount: "))
            sale_date = input("Enter sale date (YYYY-MM-DD): ")
            Sale.add_sale(artwork_id, buyer_name, sale_amount, sale_date)
        elif choice == "2":
            Sale.view_all_sales()
        elif choice == "3":
            break
        else:
            print("❌ Invalid choice.")
