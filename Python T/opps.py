#task
#create a class about laptop with 10 instances
class Laptop:
    def __init__(self, brand, display, storage, ram, processor, battery):
        self.brand = brand
        self.display = display
        self.storage = storage
        self.ram = ram
        self.processor = processor
        self.battery = battery



    def about(self):
        return f"This is a {self.brand} laptop with {self.display} display, {self.storage} storage, {self.ram} RAM, {self.processor} processor and {self.battery} battery."


laptop1 = Laptop("HP", "15.6 inch", "512 GB", "16 GB", "Intel i7", "6000 mAh")
laptop2 = Laptop("Dell", "14 inch", "256 GB", "8 GB", "Intel i5", "4000 mAh")
laptop3 = Laptop("Lenovo", "15.6 inch", "1 TB", "32 GB", "AMD Ryzen 7", "7000 mAh")
laptop4 = Laptop("Asus", "17 inch", "2 TB", "64 GB", "Intel i9", "8000 mAh")
laptop5 = Laptop("Acer", "15.6 inch", "512 GB", "16 GB", "Intel i7", "6000 mAh")
laptop6 = Laptop("MSI", "15.6 inch", "1 TB", "32 GB", "AMD Ryzen 7", "7000 mAh")
laptop7 = Laptop("Razer", "17 inch", "2 TB", "64 GB", "Intel i9", "8000 mAh")
laptop8 = Laptop("Apple", "13 inch", "256 GB", "8 GB", "M1", "4000 mAh")
laptop9 = Laptop("Microsoft", "15 inch", "512 GB", "16 GB", "Intel i7", "6000 mAh")
laptop10 = Laptop("Toshiba", "14 inch", "256 GB", "8 GB", "Intel i5", "4000 mAh")

laptops = [laptop1, laptop2, laptop3, laptop4, laptop5, laptop6, laptop7, laptop8, laptop9, laptop10]
for laptop in laptops:
    print(laptop.about())
