# Dự án Tuần 3 (Level 2): Bộ Sưu Tập Huy Hiệu & Tọa Độ Kho Báu 🧭

# 1. Tọa độ kho báu bí mật (Sử dụng Tuple - Bất biến)
toa_do_kho_bau = (10.7769, 106.7009)
print(f"📍 Tọa độ kho báu bí mật (Tuple): Kinh độ {toa_do_kho_bau[0]}, Vĩ độ {toa_do_kho_bau[1]}")

# 2. Bộ sưu tập Huy hiệu của Người chơi 1 và Người chơi 2 (Sử dụng Set - Không trùng)
huy_hieu_p1 = {"Dũng cảm", "Nhanh nhẹn", "Trí tuệ", "Dũng cảm"} # "Dũng cảm" trùng lặp
huy_hieu_p2 = {"Trí tuệ", "Siêu sức mạnh", "Bay cao"}

print(f"\n🏆 Huy hiệu P1 (đã tự động lọc trùng): {huy_hieu_p1}")
print(f"🏆 Huy hiệu P2: {huy_hieu_p2}")

# 3. Phép toán tập hợp với Set
tat_ca_huy_hieu = huy_hieu_p1 | huy_hieu_p2  # Hợp (Union)
huy_hieu_chung = huy_hieu_p1 & huy_hieu_p2   # Giao (Intersection)
huy_hieu_rieng_p1 = huy_hieu_p1 - huy_hieu_p2 # Hiệu (Difference)

print("\n📊 PHÂN TÍCH BỘ SƯU TẬP:")
print(f"- Tổng tất cả các loại huy hiệu độc nhất: {tat_ca_huy_hieu}")
print(f"- Huy hiệu mà CẢ HAI đều sở hữu: {huy_hieu_chung}")
print(f"- Huy hiệu CHỈ P1 sở hữu: {huy_hieu_rieng_p1}")
