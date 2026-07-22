# Tuần 6: Bản thiết kế quái thú nuôi ảo! 👾

Chúc mừng bạn đã đến với tuần học cuối cùng! Hôm nay chúng ta sẽ làm quen với một chủ đề siêu cao cấp nhưng cũng cực kỳ thú vị: **Lập trình hướng đối tượng (OOP)**, bao gồm **Lớp (Class)** và **Đối tượng (Object)**.

---

## 🌟 Mục tiêu cần đạt
* Hiểu thế nào là Lớp (Class) - Bản thiết kế.
* Hiểu thế nào là Đối tượng (Object) - Sản phẩm tạo ra từ bản thiết kế.
* Biết cách tự định nghĩa Class đơn giản đại diện cho một con vật cưng ảo.

---

## 🔑 Khái niệm cốt lõi

### 1. Lớp (Class) và Đối tượng (Object) là gì? 🗺️🤖
* **Lớp (Class)**: Giống như một **bản vẽ thiết kế** để chế tạo đồ chơi. Ví dụ: Bản thiết kế của một chú Robot thú cưng sẽ ghi rõ: Robot phải có một cái tên, có chỉ số năng lượng, biết ăn và biết kêu.
* **Đối tượng (Object)**: Là **chú Robot thực tế** được chế tạo ra từ bản vẽ đó. Bạn có thể dùng một bản thiết kế để tạo ra vô số chú Robot khác nhau: Robot A màu đỏ tên Bông, Robot B màu vàng tên Milu...

Trong Python, chúng ta tạo bản vẽ thiết kế bằng từ khóa `class`:
```python
class QuaiThu:
    def __init__(self, ten_nhap_vao):
        self.ten = ten_nhap_vao # Thuộc tính tên
        self.nang_luong = 10    # Năng lượng ban đầu
```

### 2. Thuộc tính (Properties) và Hành động (Methods) 🏷️🏃
* **Thuộc tính**: Những thông tin đặc trưng của đối tượng (như tên, màu sắc, tuổi).
* **Hành động**: Những việc đối tượng có thể làm (như ăn, ngủ, kêu). Trong Class, hành động thực chất là các hàm được định nghĩa bên trong Class.

---

## 🦖 Dự án thực hành: Nuôi thú ảo vui nhộn!
Bên cột phải là bản thiết kế của loài quái thú ảo tên là `Monster`. Chúng có thể ăn bánh để tăng năng lượng, đùa nghịch để tiêu hao năng lượng và gầm rú thật to!

### 💡 Thử thách cho bạn:
1. Hãy đổi tên chú quái thú của bạn ở dòng 23 từ `"Pikachu"` thành cái tên bạn thích (ví dụ: `"Godzilla"`).
2. Hãy cho chú quái thú ăn nhiều lần bằng cách viết thêm lệnh `thu_cung.cho_an()` hoặc cho chú đi chơi bằng cách viết thêm `thu_cung.vui_choi()`.
3. Bấm nút **"Bấm để Chạy thử! 🚀"** để xem các chỉ số năng lượng của chú thay đổi thế nào nhé!
