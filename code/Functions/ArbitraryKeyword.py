# write a function  book detail at takes title of book as positional arguments any number of keyword arguments for additional book information publisider,
#book details

#Book Name:
#auther =

def book_detail(title, **detail):
    print("Book Details")
    print(f"Book Name: {title}")
    for key, value in detail.items():
        print(f"{key.capitalize()}: {value}")

book_detail("Aadujeevitham",author="Benyamin",publisher="DC Books", year=2008, genre="Novel")


# Create a function product details product name as positional argument quantity as default argument any number of keyword argument with additional product details

def product_details(Name, quantity=1, **details):
    print("Product Details")
    print(f"Product: {Name}")
    print(f"Quantity: {quantity}")
    for key, value in details.items():
        print(f"{key.capitalize()}: {value}")


product_details(
    Name="Laptop",
    brand="Dell",
    price="$1200",
    warranty="2 years",
    processor="Intel i7",
    ram="16GB",
    storage="512GB SSD"
)
