# Dự án Tuần 5 (Level 3): Túi Đồ Ma Thuật Dunder Methods 🪄

print("🎒 HỆ THỐNG TÚI ĐỒ MA THUẬT GAME ARCADE 🎒\n")

class VatPham:
    def __init__(self, ten, suc_manh):
        self.ten = ten
        self.suc_manh = suc_manh

    # 1. Dunder __str__: Tùy biến hiển thị khi print()
    def __str__(self):
        return f"[{self.ten} (+{self.suc_manh} SM)]"

    # 2. Dunder __eq__: So sánh 2 vật phẩm xem có giống hệt nhau không
    def __eq__(self, other):
        if not isinstance(other, VatPham):
            return False
        return self.ten == other.ten and self.suc_manh == other.suc_manh


class TuiDoMaThuat:
    def __init__(self, ten_chu_nhan):
        self.ten_chu_nhan = ten_chu_nhan
        self.vat_pham_list = []

    def them_vat_pham(self, item):
        self.vat_pham_list.append(item)

    # 3. Dunder __str__: In ra toàn bộ thông tin túi đồ
    def __str__(self):
        ds_str = ", ".join(str(item) for item in self.vat_pham_list) if self.vat_pham_list else "Trống"
        return f"🎒 Túi đồ của {self.ten_chu_nhan} (Chứa {len(self)} món): {ds_str}"

    # 4. Dunder __len__: Cho phép gọi len(tui_do) để đếm số vật phẩm
    def __len__(self):
        return len(self.vat_pham_list)

    # 5. Dunder __add__: Cho phép cộng 2 túi đồ tui1 + tui2 thành túi chung mới!
    def __add__(self, other):
        if not isinstance(other, TuiDoMaThuat):
            raise TypeError("Chỉ có thể cộng 2 Túi Đồ Ma Thuật với nhau!")
        
        tui_hop_nhat = TuiDoMaThuat(f"{self.ten_chu_nhan} & {other.ten_chu_nhan}")
        tui_hop_nhat.vat_pham_list = self.vat_pham_list + other.vat_pham_list
        return tui_hop_nhat


# --- CHẠY THỬ PHÉP THUẬT DUNDER ---

# Tạo các vật phẩm
kiem_bich = VatPham("Thánh Kiếm", 100)
khien_than = VatPham("Khiên Thần", 80)
binh_mau = VatPham("Bình Máu", 20)

print("--- 1. Thử nghiệm __str__ của VatPham ---")
print(f"-> Vật phẩm 1: {kiem_bich}")

# Tạo 2 túi đồ
tui_nam = TuiDoMaThuat("Nam")
tui_nam.them_vat_pham(kiem_bich)
tui_nam.them_vat_pham(binh_mau)

tui_an = TuiDoMaThuat("An")
tui_an.them_vat_pham(khien_than)

print("\n--- 2. Thử nghiệm __str__ và __len__ của TuiDoMaThuat ---")
print(tui_nam) # Gọi tự động __str__ và __len__
print(tui_an)

print("\n--- 3. Thử nghiệm __add__ (Cộng 2 túi đồ bằng dấu +) ---")
tui_dong_doi = tui_nam + tui_an # Phép thuật Dunder __add__
print(f"✨ Kết quả hợp nhất: {tui_dong_doi}")
print(f"📊 Số vật phẩm trong túi đồng đội: {len(tui_dong_doi)} món.")
