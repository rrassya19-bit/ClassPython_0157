class PersegiPanjang:
    def __init__(self, panjang, lebar):
        if panjang == 0 or lebar == 0:
            raise ValueError("panjang dan lebar tidak boleh 0")
        self.panjang = panjang
        self.lebar = lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)

    def luas(self):
        return self.panjang * self.lebar

    def __str__(self):
        return "persegi panjang dengan panjang " + str(self.panjang) + " cm dan lebar " + str(self.lebar) + " cm"

