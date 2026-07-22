# Dự án Tuần 5: Máy tạo biệt danh siêu anh hùng
# Hãy thay đổi màu sắc và con vật ưa thích của bạn dưới đây!

# Định nghĩa hàm tạo biệt danh siêu anh hùng
def tao_biet_danh(mau_sac, con_vat):
    # Biệt danh sẽ là sự kết hợp siêu ngầu!
    biet_danh = "Chiến binh " + mau_sac + " " + con_vat
    return biet_danh

# Hãy thay đổi 2 dòng này nhé:
mau_yeu_thich = "Xanh Lá"
con_vat_yeu_thich = "Khủng Long"

# Gọi hàm để lấy biệt danh siêu anh hùng
ten_anh_hung = tao_biet_danh(mau_yeu_thich, con_vat_yeu_thich)

print("⚡--- MÁY TẠO TÊN SIÊU ANH HÙNG ACTIVATED ---⚡")
print("Màu yêu thích:", mau_yeu_thich)
print("Con vật yêu thích:", con_vat_yeu_thich)
print("Biệt danh siêu anh hùng của bạn là:")
print("👉", ten_anh_hung, "👈")
print("Hãy dùng sức mạnh này để bảo vệ vũ trụ nhé! 🪐")
