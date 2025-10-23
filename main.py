class CPU:
    def __init__(self, model, core, clock_speed):
        self.model = model
        self.core = core
        self.clock_speed = clock_speed

    def calculate_performance_score(self):
        return self.core * self.clock_speed * 10

    def __str__(self):
        return f'CPU: {self.model}, {self.cores} lõi, {self.clock_speed} GHz'
class RAM:
    def __init__(self, capacity_gb, ram_type):
        self.capacity_gb = capacity_gb
        self.ram_type = ram_type

    def __str__(self):
        return f'RAM: {self.capacity_gb}GB {self.ram_type}'

    @classmethod
    def create_standard_ram(cls, capacity_gb):
        cls.capacity_gb = capacity_gb
        cls.type = 'DDR4'

class Computer:
    def __init__(self, name, gpu, ram):
        self.name = name
        self.gpu = gpu
        self.ram = ram

    def is_compatible_os(os_name):
        if os_name == 'Windows' or os_name == 'Linux':
            return True
        return False

    def get_system_info(self):
        return f'Name: {self.name} + {self.GPU} + {self.RAM}'


print("=== A. KHỞI TẠO CÁC THÀNH PHẦN ===")

# 1. Tạo đối tượng CPU
high_end_cpu = CPU(model="Intel i9-14900K", core=24, clock_speed=6.0)
mid_range_cpu = CPU(model="AMD Ryzen 5 7600", core=6, clock_speed=5.1)

# 2. Tạo đối tượng RAM

# Sử dụng constructor mặc định (__init__)
ddr5_ram = RAM(capacity_gb=32, ram_type='DDR5')
print(f"Tạo RAM mặc định: {ddr5_ram}")

# Sử dụng Class Method (@classmethod)
standard_ram = RAM.create_standard_ram(capacity_gb=16)
print(f"Tạo RAM tiêu chuẩn (@classmethod): {standard_ram}")

print("\n=== B. COMPOSITION VÀ KIỂM TRA MÁY TÍNH ===")

# 1. Khởi tạo Máy tính (Composition)
gaming_pc = Computer(
    name="Gaming Rig V1",
    cpu=high_end_cpu,
    ram=ddr5_ram
)

office_pc = Computer(
    name="Office Workstation",
    cpu=mid_range_cpu,
    ram=standard_ram
)

# 2. Kiểm tra thông tin hệ thống
gaming_pc.get_system_info()
office_pc.get_system_info()

# 3. Kiểm tra Phương thức Tĩnh và Hiệu năng
print("\n--- KIỂM TRA PHƯƠNG THỨC TĨNH VÀ HIỆU NĂNG ---")

# Kiểm tra OS (gọi is_compatible_os từ đối tượng)
print(f"MacOS tương thích: {Computer.is_compatible_os('MacOS')}")

# Chạy thử nghiệm trên Gaming PC
gaming_pc.run_test(os_name="Windows")

# Chạy thử nghiệm trên Office PC
office_pc.run_test(os_name="Ubuntu")