class Employee:
    def __init__(self, ten, ma_so):
        self.ten = ten
        self.ma_so = ma_so

    def tinh_luong_thang(self):
        return 0

class FullTimeEmployee(Employee):
    def __init__(self, ten, ma_so, luong_co_dinh):
        super().__init__(ten, ma_so)
        self.luong_co_dinh = luong_co_dinh

    def tinh_luong_thang(self):
        return super().tinh_luong_thang() + self.luong_co_dinh

class HourlyEmployee(Employee):
    def __init__(self, ten, ma_so, so_gio_lam, luong_theo_gio):
        super().__init__(ten, ma_so)
        self.so_gio_lam = so_gio_lam
        self.luong_theo_gio = luong_theo_gio

    def tinh_luong_thang(self):
        return super().tinh_luong_thang() + self.luong_theo_gio * self.so_gio_lam

nnt1 = FullTimeEmployee('nnt1', 1, 100000)
print(nnt1.tinh_luong_thang())
nnt2 = HourlyEmployee('nnt', 2, 20, 5000)
print(nnt2.tinh_luong_thang())