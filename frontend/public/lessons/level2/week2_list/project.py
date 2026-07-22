# Dự án Tuần 2 (Level 2): Quản Lý Balo Thám Hiểm 🎒

# 1. Tạo danh sách vật phẩm ban đầu
balo = ["Đèn pin", "Bản đồ", "Lương khô", "Hộp y tế"]

print(f"🎒 Balo ban đầu có {len(balo)} món đồ:")
for i, item in enumerate(balo, start=1):
    print(f"  {i}. {item}")

# 2. Thêm vật phẩm mới
print("\n🔍 Bạn vừa tìm thấy một 'Dây thừng' và 'Kính thiên văn'!")
balo.append("Dây thừng")
balo.append("Kính thiên văn")

# 3. Sử dụng món đồ Lương khô
print("\n🍴 Bạn cảm thấy đói và đã ăn hết 'Lương khô'...")
balo.remove("Lương khô")

# 4. Sắp xếp balo gọn gàng theo bảng chữ cái A-Z
balo.sort()

# 5. In kết quả balo hoàn chỉnh
print(f"\n✨ Balo sau khi sắp xếp gọn gàng ({len(balo)} món):")
for index, mon_do in enumerate(balo):
    print(f"  -> Ngăn [{index}]: {mon_do}")

print("\n🎉 Bạn đã sẵn sàng tiếp tục hành trình thám hiểm!")
