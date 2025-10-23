class BankAccout:
    def __init__(self, so_du):
        self.so_du = so_du

    def gui_tien(self, so_tien):
        self.so_du += so_tien

    def rut_tien(self, so_tien):
        if (self.so_du < so_tien):
            print(f"Có {self.so_du}, rút {so_tien}")
        else:
            print(f"Rút {so_tien}, còn {self.so_du-so_tien}")

nnt = BankAccout(1000)
nnt.gui_tien(500)
nnt.rut_tien(2000)
