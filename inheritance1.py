class Buah(object):
    def __init__(self, m, d, a):
        self.mangga = m
        self.durian = d
        self.alpukat = a
    def cetakData(self):
        print("mangga\t: ", self.mangga)
        print("durian\t: ", self.durian)
        print("alpukat\t: ", self.alpukat)
# mendefinisikan kelas turunan (subclass)
class Buahjeruk(Buah):
    def __init__(self, m, d, a, j):
        self.mangga = m
        self.durian = d
        self.alpukat = a
        self.jeruk = j
    def cetakData(self):
        print("mangga\t: ", self.mangga)
        print("durian\t: ", self.durian)
        print("alpukat\t: ", self.alpukat)
        print("jeruk\t: ", self.jeruk)
def main():
    # membuat objek Buahjeruk
    Buahjeruk1 = Buahjeruk(1, 2, 3, "4")
    # menggunakan objek
    Buahjeruk1.cetakData()
if __name__ == "__main__":
    main()
