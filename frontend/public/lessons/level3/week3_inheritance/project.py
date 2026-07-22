# Dự án Tuần 3 (Level 3): Biệt Đội Siêu Anh Hùng Kế Thừa (OOP Inheritance) 🦸‍♂️

print("⚡ HỆ THỐNG QUẢN LÝ BIỆT ĐỘI SIÊU ANH HÙNG ⚡\n")

# 1. LỚP CHA: AnhHung (Parent Class / Superclass)
class AnhHung:
    def __init__(self, ten, mau, suc_manh):
        self.ten = ten
        self.mau = mau
        self.suc_manh = suc_manh

    def gioi_thieu(self):
        print(f"🦸 Anh Hùng [{self.ten}] | Máu: {self.mau} HP | Sức mạnh: {self.suc_manh}")

    def tan_cong(self):
        print(f"💥 {self.ten} tấn công cơ bản! Gây {self.suc_manh} sát thương.")

# 2. LỚP CON 1: PhuThuy (Subclass kế thừa AnhHung)
class PhuThuy(AnhHung):
    def __init__(self, ten, mau, suc_manh, nang_luong_phep):
        # Dùng super() để tái sử dụng khởi tạo của AnhHung
        super().__init__(ten, mau, suc_manh)
        self.nang_luong_phep = nang_luong_phep

    # Ghi đè phương thức gioi_thieu (Method Overriding)
    def gioi_thieu(self):
        print(f"🧙 Phù Thủy [{self.ten}] | Máu: {self.mau} HP | Phép thuật: {self.nang_luong_phep} MP")

    # Tuyệt chiêu riêng của Phù thủy
    def ban_phep(self):
        sat_thuong_phep = self.suc_manh * 2 + self.nang_luong_phep
        print(f"✨ {self.ten} niệm phép 'Cầu Lửa'! Gây {sat_thuong_phep} sát thương phép thuật!")

# 3. LỚP CON 2: ChienSi (Subclass kế thừa AnhHung)
class ChienSi(AnhHung):
    def __init__(self, ten, mau, suc_manh, giap):
        super().__init__(ten, mau, suc_manh)
        self.giap = giap

    def gioi_thieu(self):
        print(f"🛡️ Chiến Sĩ [{self.ten}] | Máu: {self.mau} HP | Giáp sắt: {self.giap}")

    def vung_kiem(self):
        print(f"⚔️ {self.ten} vung Siêu Kiếm! Sức mạnh phòng thủ tăng +{self.giap}!")


# Khởi tạo các siêu anh hùng
phu_thuy_gandalf = PhuThuy("Gandalf", mau=100, suc_manh=25, nang_luong_phep=80)
chien_si_thor = ChienSi("Thor", mau=200, suc_manh=40, giap=50)

print("--- 📢 GIỚI THIỆU NHÂN VẬT ---")
phu_thuy_gandalf.gioi_thieu()
chien_si_thor.gioi_thieu()

print("\n--- ⚔️ HÀNH ĐỘNG CHIẾN ĐẤU ---")
phu_thuy_gandalf.tan_cong()   # Gọi phương thức từ Lớp Cha
phu_thuy_gandalf.ban_phep()   # Gọi phương thức riêng của Lớp Con

chien_si_thor.tan_cong()      # Gọi phương thức từ Lớp Cha
chien_si_thor.vung_kiem()     # Gọi phương thức riêng của Lớp Con
