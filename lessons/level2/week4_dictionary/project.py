# Dự án Tuần 4 (Level 2): Quản Lý Hồ Sơ Siêu Anh Hùng 📖

# 1. Tạo từ điển hồ sơ nhân vật
ho_so_hero = {
    "bi_danh": "Chiến Binh Ánh Sáng",
    "ten_that": "Nguyễn Văn Nam",
    "cap_do": 85,
    "ky_nang": ["Chiếu sáng", "Tạo giáp năng lượng", "Tăng tốc"],
    "trang_thai": "Đang hoạt động"
}

print("📋 HỒ SƠ SIÊU ANH HÙNG (BAN ĐẦU):")
for khoa, gia_tri in ho_so_hero.items():
    print(f"  • {khoa.upper()}: {gia_tri}")

# 2. Thêm thông tin vũ khí và nâng cấp cấp độ
print("\n⚡ Tiến hành nâng cấp Siêu Anh Hùng...")
ho_so_hero["vu_khi"] = "Gậy Ánh Sáng"
ho_so_hero["cap_do"] = 99
ho_so_hero["ky_nang"].append("Bay lượn")

# 3. Kiểm tra xem thông tin có tồn tại không bằng từ khóa 'in'
if "vu_khi" in ho_so_hero:
    print(f"⚔️ Vũ khí đã trang bị: {ho_so_hero['vu_khi']}")

# 4. In lại toàn bộ thông tin sau nâng cấp
print("\n✨ HỒ SƠ SIÊU ANH HÙNG SAU KHI NÂNG CẤP:")
print(f"- Biệt danh: {ho_so_hero['bi_danh']}")
print(f"- Cấp độ mới: {ho_so_hero['cap_do']}")
print(f"- Các kỹ năng: {', '.join(ho_so_hero['ky_nang'])}")
