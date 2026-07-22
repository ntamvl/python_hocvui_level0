# Dự án Tuần 6 (Level 3): Đấu Trường Võ Thuật Quái Thú Python 🏆

print("🏆 CHÀO MỪNG ĐẾN VỚI ĐẤU TRƯỜNG HUYỀN THOẠI LEVEL 3 🏆\n")

# 1. LỚP CHA: QuaiThuy (Sử dụng Kế thừa & Dunder Methods)
class QuaiThuy:
    tong_so_quai_thuy = 0

    def __init__(self, ten, mau, suc_manh):
        self.ten = ten
        self.mau = mau
        self.suc_manh = suc_manh
        QuaiThuy.tong_so_quai_thuy += 1

    # Dunder __str__: In thông tin nhân vật
    def __str__(self):
        return f"👾 [{self.ten}] | Máu: {self.mau} HP | Sức mạnh: {self.suc_manh}"

    # Dunder __gt__: So sánh sức mạnh giữa 2 quái thú (gt = Greater Than)
    def __gt__(self, other):
        return self.suc_manh > other.suc_manh

    # Static Method: Hàm tính toán tiện ích
    @staticmethod
    def tinh_sat_thuong_chi_mang(dame_co_ban):
        return dame_co_ban * 2

# 2. LỚP CON 1: QuaiThuyRong (Inheritance)
class QuaiThuyRong(QuaiThuy):
    def __init__(self, ten, mau, suc_manh, suyen_long):
        super().__init__(ten, mau, suc_manh)
        self.suyen_long = suyen_long

    def __str__(self):
        return f"🐉 [Rồng {self.ten}] | Máu: {self.mau} HP | Sức mạnh: {self.suc_manh} | Phun Lửa: {self.suyen_long}"

# 3. LỚP CON 2: QuaiThuyNuoc (Inheritance)
class QuaiThuyNuoc(QuaiThuy):
    def __init__(self, ten, mau, suc_manh, hoi_mau):
        super().__init__(ten, mau, suc_manh)
        self.hoi_mau = hoi_mau

    def __str__(self):
        return f"🌊 [Thủy Thần {self.ten}] | Máu: {self.mau} HP | Sức mạnh: {self.suc_manh} | Hồi Máu: {self.hoi_mau}"

# 4. RECURSION (Đệ quy): Tính năng lượng tích lũy của nhà vô địch
def tinh_nang_luong_vo_dich(cap_do):
    if cap_do <= 1:
        return 100
    return cap_do * 50 + tinh_nang_luong_vo_dich(cap_do - 1)

# 5. SORTING ALGORITHM (Bubble Sort): Sắp xếp bảng xếp hạng quái thú theo sức mạnh giảm dần
def sap_xep_quai_thuy(ds_quai_thuy):
    arr = ds_quai_thuy.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Dùng Dunder __gt__ (toán tử >) để so sánh 2 quái thú
            if not (arr[j] > arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# --- KHỞI CHẠY GIẢI ĐẤU ---

q1 = QuaiThuyRong("Infernus", mau=500, suc_manh=150, suyen_long=80)
q2 = QuaiThuyNuoc("Leviathan", mau=600, suc_manh=120, hoi_mau=50)
q3 = QuaiThuy("Goblin Vương", mau=300, suc_manh=90)
q4 = QuaiThuyRong("Bahamut", mau=700, suc_manh=200, suyen_long=120)

danh_sach_chiên_dau = [q1, q2, q3, q4]

print(f"📊 Tổng số Quái thú đăng ký: {QuaiThuy.tong_so_quai_thuy} chiến binh!\n")

print("⚔️ ĐANG DIỄN RA CÁC TRẬN ĐẤU KỊCH TÍNH...\n")

# Sắp xếp bảng xếp hạng
bang_xep_hang = sap_xep_quai_thuy(danh_sach_chiên_dau)

print("🥇 BẢNG XẾP HẠNG CHUNG CUỘC (Đã dùng Thuật toán Sắp xếp & Dunder __gt__):")
for idx, qt in enumerate(bang_xep_hang, start=1):
    print(f"  Hạng {idx}: {qt}")

# Nhà vô địch
vo_dich = bang_xep_hang[0]
print(f"\n🎉 NHÀ VÔ ĐỊCH GIẢI ĐẤU LÀ: {vo_dich.ten} 🎉")

# Tính năng lượng vô địch bằng đệ quy
nl_thu_duoc = tinh_nang_luong_vo_dich(5)
print(f"⚡ Năng lượng Đệ quy tích lũy cấp 5 nhận được: {nl_thu_duoc} MP!")
print("🌟 BẠN ĐÃ HOÀN THÀNH TOÀN BỘ CẤP ĐỘ 3! XIN CHÚC MỪNG CHUYÊN GIA PYTHON! 🎉")
