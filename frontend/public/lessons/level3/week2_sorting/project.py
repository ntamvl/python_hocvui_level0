# Dự án Tuần 2 (Level 3): Bảng Xếp Hạng Điểm Cao Game Arcade 📊

print("🏆 MÁY SẮP XẾP BẢNG XẾP HẠNG ĐIỂM GAME 🏆\n")

# Danh sách điểm số hỗn loạn của các game thủ
diem_so = [450, 120, 890, 320, 670, 950, 210]
ten_game_thu = ["Pikachu", "Mario", "Sonic", "Zelda", "Kirby", "Dragon", "Luigi"]

print(f"📋 Danh sách điểm ban đầu: {diem_so}\n")

# 1. Thuật toán Sắp xếp Nổi Bọt (Bubble Sort) - Sắp xếp GIẢM DẦN (Điểm cao đứng đầu)
def sap_xep_noi_bot_giam_dan(danh_sach):
    arr = danh_sach.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Nếu số đằng trước NHỎ HƠN số đằng sau -> Đổi chỗ để đưa số lớn lên trước
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 2. Thuật toán Sắp xếp Chọn (Selection Sort) - Sắp xếp TĂNG DẦN
def sap_xep_chon_tang_dan(danh_sach):
    arr = danh_sach.copy()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Thực thi sắp xếp
ket_qua_bubble = sap_xep_noi_bot_giam_dan(diem_so)
ket_qua_selection = sap_xep_chon_tang_dan(diem_so)

print("🥇 BẢNG XẾP HẠNG TOP ĐIỂM CAO (Bubble Sort - Giảm dần):")
for rank, score in enumerate(ket_qua_bubble, start=1):
    print(f"  Top {rank}: {score} điểm 🔥")

print("\n📈 DANH SÁCH ĐIỂM TĂNG DẦN (Selection Sort):")
print(f" -> {ket_qua_selection}")
