from lib.artists import Artist
from lib.artworks import Artwork
from lib.sales import Sale


def manage_artists():
    while True:
        print("\n🎭 MANAGE ARTISTS")
        print("1. Add Artist")
        print("2. View All Artists")
        print("3. Update Artist")
        print("4. Delete Artist")
        print("5. Back to Main Menu")
        choice = input("Select an option (1–5): ")

        if choice == "1":
            name = input("Enter artist name: ")
            nationality = input("Enter artist nationality: ")
            birth_year = input("Enter birth year: ")
            Artist.add_artist(name, nationality, birth_year)
        elif choice == "2":
            Artist.view_all_artists()
        elif choice == "3":
            artist_id = int(input("Enter artist ID to update: "))
            name = input("New name (press Enter to skip): ") or None
            nationality = input("New nationality (press Enter to skip): ") or None
            birth_year = input("New birth year (press Enter to skip): ") or None
            Artist.update_artist(artist_id, name=name, nationality=nationality, birth_year=birth_year)
        elif choice == "4":
            artist_id = int(input("Enter artist ID to delete: "))
            Artist.delete_artist(artist_id)
        elif choice == "5":
            break
        else:
            print("❌ Invalid choice. Try again.")


def manage_artworks():
    while True:
        print("\n🖼️ MANAGE ARTWORKS")
        print("1. Add Artwork")
        print("2. View All Artworks")
        print("3. Update Artwork")
        print("4. Delete Artwork")
        print("5. Back to Main Menu")
        choice = input("Select an option (1–5): ")

        if choice == "1":
            title = input("Enter artwork title: ")
            medium = input("Enter medium: ")
            year_created = input("Enter year created: ")
            price = input("Enter price: ")
            artist_id = input("Enter artist ID: ")
            image_url = input("Enter image URL (optional): ") or None
            Artwork.add_artwork(title, medium, year_created, price, artist_id, image_url)
        elif choice == "2":
            Artwork.view_all_artworks()
        elif choice == "3":
            artwork_id = int(input("Enter artwork ID to update: "))
            title = input("New title (press Enter to skip): ") or None
            medium = input("New medium (press Enter to skip): ") or None
            price = input("New price (press Enter to skip): ") or None
            status = input("New status (available/sold) (press Enter to skip): ") or None
            image_url = input("New image URL (press Enter to skip): ") or None
            Artwork.update_artwork(artwork_id, title=title, medium=medium, price=price, status=status, image_url=image_url)
        elif choice == "4":
            artwork_id = int(input("Enter artwork ID to delete: "))
            Artwork.delete_artwork(artwork_id)
        elif choice == "5":
            break
        else:
            print("❌ Invalid choice. Try again.")


def manage_sales():
    while True:
        print("\n💰 MANAGE SALES")
        print("1. Add Sale")
        print("2. View All Sales")
        print("3. Update Sale")
        print("4. Delete Sale")
        print("5. Back to Main Menu")
        choice = input("Select an option (1–5): ")

        if choice == "1":
            artwork_id = input("Enter artwork ID: ")
            buyer_name = input("Enter buyer name: ")
            amount = input("Enter sale amount: ")
            sale_date = input("Enter sale date (YYYY-MM-DD): ")
            Sale.add_sale(artwork_id, buyer_name, amount, sale_date)
        elif choice == "2":
            Sale.view_all_sales()
        elif choice == "3":
            sale_id = int(input("Enter sale ID to update: "))
            buyer_name = input("New buyer name (press Enter to skip): ") or None
            amount = input("New amount (press Enter to skip): ") or None
            sale_date = input("New sale date (YYYY-MM-DD) (press Enter to skip): ") or None
            Sale.update_sale(sale_id, buyer_name=buyer_name, amount=amount, sale_date=sale_date)
        elif choice == "4":
            sale_id = int(input("Enter sale ID to delete: "))
            Sale.delete_sale(sale_id)
        elif choice == "5":
            break
        else:
            print("❌ Invalid choice. Try again.")


def main():
    while True:
        print("\n🎨 ART GALLERY MANAGEMENT SYSTEM 🎨")
        print("1. Manage Artists")
        print("2. Manage Artworks")
        print("3. Manage Sales")
        print("4. Exit")

        choice = input("Select an option (1–4): ")

        if choice == "1":
            manage_artists()
        elif choice == "2":
            manage_artworks()
        elif choice == "3":
            manage_sales()
        elif choice == "4":
            print("👋 Exiting Art Gallery Management System. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
 