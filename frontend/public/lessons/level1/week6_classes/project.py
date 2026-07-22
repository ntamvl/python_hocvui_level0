# Dự án Tuần 6: Nuôi thú ảo vui nhộn!
# Hãy tạo quái thú của riêng bạn và chơi đùa cùng nó!

class Monster:
    # Hàm khởi tạo (bản thiết kế lúc mới tạo quái thú)
    def __init__(self, ten):
        self.ten = ten
        self.nang_luong = 50
        print("👾 Quái thú", self.ten, "đã xuất hiện chào thế giới!")

    # Hành động: Gầm rú
    def gam_ru(self):
        print("🔊", self.ten, "gầm rú: GRRRRRRR! HÙ!!!")

    # Hành động: Cho ăn
    def cho_an(self):
        self.nang_luong = self.nang_luong + 20
        print("🍖 Bạn cho", self.ten, "ăn đùi gà. Năng lượng hiện tại:", self.nang_luong)

    # Hành động: Vui chơi
    def vui_choi(self):
        self.nang_luong = self.nang_luong - 15
        print("⚽ Bạn cho", self.ten, "đá bóng. Năng lượng hiện tại:", self.nang_luong)

# --- BẮT ĐẦU CHƠI NUÔI THÚ ---

# Tạo ra chú quái thú ảo
thu_cung = Monster("Pikachu")

# Chơi với thú cưng
thu_cung.gam_ru()
thu_cung.cho_an()
thu_cung.vui_choi()
thu_cung.vui_choi()

print("🏁 Trò chơi kết thúc! Hãy thử viết thêm lệnh để chăm sóc bé quái thú của bạn nhé!")
