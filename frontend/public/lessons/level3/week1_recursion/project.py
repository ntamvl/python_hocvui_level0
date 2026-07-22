# Dự án Tuần 1 (Level 3): Tháp Đếm Ngược Đệ Quy & Máy Tính Giai Thừa 🪆

print("🪆 CHÀO MỪNG ĐẾN VỚI THẾ GIỚI HÀM ĐỆ QUY! 🪆\n")

# 1. Hàm đệ quy đếm ngược thời gian phóng hỏa tiễn
def dem_nguoc(sec):
    # 🛑 Điểm dừng (Base Case)
    if sec == 0:
        print("🚀 Đã đến 0 giây! Phóng hỏa tiễn thôi nào! 🎉")
        return
    
    # In bước hiện tại
    print(f"⏱️ Đếm ngược: {sec}...")
    
    # 🔄 Lời gọi đệ quy (tiến gần hơn về 0)
    dem_nguoc(sec - 1)

print("--- 1. Thử nghiệm Đếm ngược đệ quy ---")
dem_nguoc(5)


# 2. Hàm đệ quy tính Giai thừa (n!) năng lượng
def tinh_giai_thua(n):
    # 🛑 Điểm dừng
    if n <= 1:
        return 1
    
    # 🔄 Recursive step
    return n * tinh_giai_thua(n - 1)

print("\n--- 2. Thử nghiệm Tính Giai thừa ---")
so_cap = 5
ket_qua = tinh_giai_thua(so_cap)
print(f"⚡ Năng lượng tích lũy của {so_cap}! là: {ket_qua}")

# 3. Hàm đệ quy tính tổng từ 1 đến n
def tinh_tong(n):
    if n <= 1:
        return 1
    return n + tinh_tong(n - 1)

print(f"📊 Tổng năng lượng từ 1 đến {so_cap} là: {tinh_tong(so_cap)}")
