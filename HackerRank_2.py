import os

os.system('cls')

print(' '*15,'SELAMAT DATANG',' '*15)
print("-"*46)
class Item():
    list_item = []
    def __init__(self,name : str , price : int) -> None:
            self.name = name.lower()
            self.price = price
            Item.list_item.append(self)
class ShoppingCart(Item):
    list_cart = []
    total_price = 0
    def __init__(self, name: str, price: int) -> None:
        super().__init__(name, price)
    @classmethod
    def cart(cls):
        item_add = input("\nAdd ").lower()
        item_quantity = int(input("Masukkan jumlah item yang Anda inginkan : "))
        list_cart_tambahan = []
        for i in range(len(Item.list_item)):
            if item_add == Item.list_item[i].name:
                list_cart_tambahan = Item.list_item[i]
                for x in range(item_quantity):
                    ShoppingCart.list_cart.append(list_cart_tambahan)
                ShoppingCart.total_price += Item.list_item[i].price * item_quantity
        if list_cart_tambahan == []:
            print("Maaf produk tidak ditemukan")
        

number_items = int(input("Banyak Item yang dijual : "))
for i in range(number_items):
    try :
        data_item = input("Masukkan nama dan harga : ").split()
        name = data_item[0]
        price = int(data_item [1])
        item= Item(name,price)
    except IndexError :
        print("Masukkan item yang dijual dengan format yang benar")
        print("(Nama_Item)<space>(Harga_Item)")
        print("Silahkan untuk mengulang input dari awak kembali")


print("\nSilahkan masukkan barang yang ingin anda beli ke dalam keranjang")

while True:
    ShoppingCart.cart()

    isContinue = input("Masih ingin berbelanja ? (y/n) ").lower()
    if isContinue == "n":
        break
    

banyak_item = len(ShoppingCart.list_cart)
print(f"\nBanyak item yang anda beli sebanyak {banyak_item} buah")
print(f"Total Belanja Anda adalah IDR {ShoppingCart.total_price}\n")

