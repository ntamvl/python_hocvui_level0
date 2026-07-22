# Dự án Tuần 4 (Level 3): Xưởng Sản Xuất & Quản Lý Robot 🛠️

print("🏭 XƯỞNG CHẾ TẠO ROBOT TỰ ĐỘNG PYTHON 🏭\n")

class Robot:
    # Biến cấp Lớp (Class Attribute): Dùng chung cho toàn bộ xưởng
    tong_so_robot = 0

    def __init__(self, ten, toc_do, pin):
        self.ten = ten
        self.toc_do = toc_do
        self.pin = pin
        # Mỗi khi tạo 1 Robot mới, tăng tổng số robot của Lớp
        Robot.tong_so_robot += 1

    # 1. INSTANCE METHOD: Phương thức riêng của từng Robot (dùng self)
    def bao_cao_trang_thai(self):
        print(f"🤖 Robot [{self.ten}] | Tốc độ: {self.toc_do} km/h | Pin: {self.pin}%")

    # 2. CLASS METHOD: Phương thức cấp Lớp (dùng @classmethod và cls)
    @classmethod
    def lay_tong_so_luong(cls):
        print(f"📊 [BÁO CÁO XƯỞNG] Tổng số Robot đang hoạt động: {cls.tong_so_robot} robot.")

    # Class Method làm Factory Method (Xưởng tạo nhanh mẫu Robot)
    @classmethod
    def tao_robot_sieu_toc(cls, ten):
        print(f"✨ Đang sản xuất phiên bản Siêu Tốc cho {ten}...")
        # Tạo đối tượng Robot mới với cấu hình mặc định siêu tốc
        return cls(ten=ten, toc_do=250, pin=100)

    # 3. STATIC METHOD: Phương thức tĩnh tiện ích (dùng @staticmethod, không cần self/cls)
    @staticmethod
    def tinh_thoi_gian_di_chuyen(quang_duong_km, toc_do_kmh):
        if toc_do_kmh <= 0:
            return 0
        thoi_gian_gio = quang_duong_km / toc_do_kmh
        return round(thoi_gian_gio * 60, 2) # Trả về số phút


print("--- 1. Kiểm tra số lượng robot ban đầu ---")
Robot.lay_tong_so_luong()

print("\n--- 2. Tạo robot bằng Instance Constructor thông thường ---")
r1 = Robot("Bumblebee", toc_do=80, pin=90)
r1.bao_cao_trang_thai()

print("\n--- 3. Tạo robot bằng Class Method (Factory Method) ---")
r2 = Robot.tao_robot_sieu_toc("Flash-Bot")
r2.bao_cao_trang_thai()

print("\n--- 4. Kiểm tra lại số lượng robot cấp Lớp ---")
Robot.lay_tong_so_luong()

print("\n--- 5. Sử dụng Static Method tiện ích tính thời gian ---")
quang_duong = 50 # km
phut_r1 = Robot.tinh_thoi_gian_di_chuyen(quang_duong, r1.toc_do)
phut_r2 = Robot.tinh_thoi_gian_di_chuyen(quang_duong, r2.toc_do)

print(f"⏱️ Quãng đường {quang_duong}km:")
print(f"  - {r1.ten} đi mất: {phut_r1} phút")
print(f"  - {r2.ten} đi mất: {phut_r2} phút")
