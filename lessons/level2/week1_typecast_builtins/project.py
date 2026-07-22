# Dự án Tuần 1 (Level 2): Máy Phân Tích Chỉ Số Siêu Anh Hùng ⚡

print("⚡ CHÀO MỪNG ĐẾN VỚI MÁY ĐO NĂNG LƯỢNG SIÊU ANH HÙNG ⚡")

# Giả lập dữ liệu nhập từ bàn phím (kiểu chuỗi chữ str)
dieu_khiên_luong = "85"
suc_manh_co_bap = "92"
toc_do_di_chuyen = "78.6"

# 1. Thực hiện ép kiểu dữ liệu sang int và float
chi_so_1 = int(dieu_khiên_luong)
chi_so_2 = int(suc_manh_co_bap)
chi_so_3 = float(toc_do_di_chuyen)

print(f"-> Chỉ số điều khiển năng lượng: {chi_so_1} (Kiểu: {type(chi_so_1).__name__})")
print(f"-> Chỉ số sức mạnh cơ bắp: {chi_so_2} (Kiểu: {type(chi_so_2).__name__})")
print(f"-> Chỉ số tốc độ: {chi_so_3} (Kiểu: {type(chi_so_3).__name__})")

# 2. Sử dụng các hàm Built-in thần kỳ
tong_chi_so = chi_so_1 + chi_so_2 + chi_so_3
trung_binh = tong_chi_so / 3
max_val = max(chi_so_1, chi_so_2, chi_so_3)
min_val = min(chi_so_1, chi_so_2, chi_so_3)

print("\n📊 KẾT QUẢ PHÂN TÍCH:")
print(f"- Tổng chỉ số sức mạnh: {tong_chi_so}")
print(f"- Sức mạnh trung bình (làm tròn): {round(trung_binh, 2)}")
print(f"- Chỉ số cao nhất: {max_val}")
print(f"- Chỉ số thấp nhất: {min_val}")

print("\n🎉 Siêu Anh Hùng của bạn đã sẵn sàng xuất kích!")
