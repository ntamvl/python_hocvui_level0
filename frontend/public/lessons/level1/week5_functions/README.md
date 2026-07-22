# Tuần 5: Chiếc máy làm bánh ma thuật! 🍞

Khi viết code, có những việc chúng ta cần làm đi làm lại ở nhiều nơi. Thay vì viết lại tất cả các dòng code đó, chúng ta có thể gom chúng vào một chiếc máy đa năng gọi là **Hàm (Functions)**!

---

## 🌟 Mục tiêu cần đạt
* Hiểu hàm giống như một "chiếc máy" làm việc tự động.
* Biết cách tự định nghĩa một hàm bằng từ khóa `def`.
* Biết cách gửi nguyên liệu vào hàm (tham số) và nhận kết quả ra (`return`).

---

## 🔑 Khái niệm cốt lõi

### Hàm là gì? 🔮
Hãy tưởng tượng bạn chế tạo một chiếc máy làm bánh.
1. Bạn cho bột và đường vào máy (đây là **Tham số đầu vào**).
2. Máy tự động nhào bột, nướng bánh (đây là **Phần thân hàm**).
3. Máy đẩy ra một chiếc bánh thơm ngon (đây là **Kết quả trả về - `return`**).

Kể từ khi có chiếc máy này, bạn chỉ cần bấm nút và cung cấp bột, không cần phải tự tay nhào bột và canh lò nướng nữa!

### 📝 Cách khai báo hàm trong Python:
* Dùng từ khóa `def` (viết tắt của define - nghĩa là định nghĩa).
* Đặt tên cho hàm (viết thường, ngăn cách bằng dấu gạch dưới).
* Đặt các tham số (nguyên liệu) trong ngoặc đơn `()`.
* Dùng từ khóa `return` ở cuối để xuất ra kết quả.

```python
# Định nghĩa chiếc máy nhân đôi niềm vui
def nhan_doi_niem_vui(mon_do):
    ket_qua = mon_do + " và " + mon_do
    return ket_qua

# Sử dụng máy:
hop_qua = nhan_doi_niem_vui("Kẹo")
print(hop_qua) # Sẽ in ra: Kẹo và Kẹo
```

---

## 🦸 Dự án thực hành: Máy tạo biệt danh siêu anh hùng!
Bên cột phải là một chiếc máy ma thuật giúp bạn ghép màu sắc yêu thích và con vật yêu thích để tạo nên một biệt danh siêu anh hùng cực kỳ ngầu!

### 💡 Thử thách cho bạn:
1. Hãy sửa màu sắc ở dòng 12 thành màu bạn thích (ví dụ: `"Đỏ"`, `"Bóng Đêm"`).
2. Sửa con vật ở dòng 13 thành con vật bạn thích (ví dụ: `"Rồng"`, `"Hổ"`, `"Phượng Hoàng"`).
3. Chạy thử chương trình để xem biệt danh siêu anh hùng của bạn là gì nhé!
