# Dự án Tuần 6 (Level 2): Khiên Phép Thuật Bảo Vệ Chương Trình 🛡️

print("🛡️ KÍCH HOẠT HỆ THỐNG KHIÊN BẢO VỆ PYTHON 🛡️\n")

def chia_qua(so_qua, so_ban):
    try:
        print(f"👉 Thử chia {so_qua} quả táo cho {so_ban} bạn...")
        ket_qua = so_qua / so_ban
    except ZeroDivisionError:
        print("❌ LỖI KHÔNG THỂ CHIA CHO 0: Không thể chia quà cho 0 bạn được!")
    except TypeError:
        print("❌ LỖI KIỂU DỮ LIỆU: Số quả và số bạn phải là chữ số nha!")
    else:
        print(f"✅ THÀNH CÔNG: Mỗi bạn nhận được {ket_qua:.1f} quả táo!")
    finally:
        print("🧹 [Khiên Hệ Thống]: Đã hoàn thành kiểm tra an toàn.")

# 1. Thử nghiệm trường hợp hợp lệ
chia_qua(10, 2)
print("-" * 40)

# 2. Thử nghiệm trường hợp chia cho 0
chia_qua(10, 0)
print("-" * 40)

# 3. Kiểm tra an toàn khi nhập chuỗi dữ liệu (ValueError)
du_lieu_nhap = "một trăm"
try:
    so_tuoi = int(du_lieu_nhap)
except ValueError:
    print(f"⚠️ [Cảnh báo khiên]: Dữ liệu '{du_lieu_nhap}' không phải số hợp lệ!")

print("\n🎉 Chúc mừng bạn đã hoàn thành xuất sắc toàn bộ CẤP ĐỘ 2!")
