# Dự án Tuần 5 (Level 2): Trạm Chế Tạo Siêu Robot ⚡

# Biến toàn cục (Global variable)
ten_tram = "Trạm Chế Tạo Robot Alpha"

# 1. Hàm có Tham số mặc định và *args
def che_tao_robot(ten_robot, loai="Chiến đấu", *trang_bi):
    # Biến cục bộ (Local variable)
    ma_so = "RB-" + str(len(ten_robot) * 100)
    
    print(f"\n🤖 [{ten_tram}] Vừa chế tạo thành công:")
    print(f"  • Mã số: {ma_so}")
    print(f"  • Tên Robot: {ten_robot}")
    print(f"  • Loại: {loai}")
    if trang_bi:
        print(f"  • Trang bị gắn kèm ({len(trang_bi)} món): {', '.join(trang_bi)}")
    else:
        print("  • Trang bị gắn kèm: Chưa có")

# 2. Sử dụng Hàm Lambda siêu gọn để tính điểm sát thương
tinh_sat_thuong = lambda suc_manh, he_so: suc_manh * he_so

# 3. Chạy thử nghiệm trạm chế tạo
che_tao_robot("IronBot") # Sử dụng tham số mặc định
che_tao_robot("ThunderBot", "Phòng thủ", "Khiên sắt", "Súng Laser", "Động cơ phản lực")

print("\n⚡ TÍNH TOÁN SỨC MẠNH (LAMBDA):")
d_sat_thuong = tinh_sat_thuong(50, 1.5)
print(f"-> Sức mạnh 50 x Hệ số 1.5 = {d_sat_thuong} sát thương!")
