class TastManager:
    def __init__(self):
        self.list = []

    def them_nhiem_vu(self, nhiem_vu):
        self.list.append(nhiem_vu)

    def hien_thi(self):
        for nhiem_vu in self.list:
            print(nhiem_vu)

task = TastManager()
task.them_nhiem_vu("an")
task.hien_thi()
task.them_nhiem_vu("ngu")
task.hien_thi()