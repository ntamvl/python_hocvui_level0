# Tuần 3 (Cấp 2): Huy Hiệu Độc Nhất & Tọa Độ Bí Mật (Tuple & Set) 🧭

Tuần này chúng ta sẽ khám phá 2 cấu trúc dữ liệu cực kỳ thú vị: **Tuple** (Chiếc hộp khóa chặt không thể sửa đổi) và **Set** (Tập hợp các món đồ duy nhất không bao giờ trùng lặp)!

---

## 🌟 Mục tiêu cần đạt
* Phân biệt được khi nào nên dùng Tuple và khi nào nên dùng Set.
* Hiểu tính chất **Immutable (không thể thay đổi)** của Tuple.
* Hiểu tính chất **Unique (độc nhất, tự động xóa phần tử trùng)** của Set.
* Thực hiện các phép toán tập hợp thần kỳ với Set: Hợp (gộp lại), Giao (món đồ chung), Hiệu (món đồ riêng).

---

## 🔑 Khái niệm cốt lõi

### 1. Tuple - Bộ giá trị cố định `()`
Tuple được tạo bằng dấu ngoặc đơn `()`. Một khi đã tạo ra Tuple, bạn **không thể** thêm, xóa hay thay đổi giá trị bên trong (giống như đúc thành khuôn kim loại):
```python
toa_do_can_cu = (105.85, 21.02) # Tọa độ kinh độ, vĩ độ
ngay_sinh = (15, 8, 2012)
```
* Rất an toàn, dùng để lưu những dữ liệu cố định như tọa độ GPS, ngày tháng năm sinh...

### 2. Set - Tập hợp độc nhất `{}`
Set được tạo bằng dấu ngoặc nhọn `{}`. Set có 2 tính năng tuyệt vời:
1. **Tự động loại bỏ trùng lặp**: Nếu bạn cho `{"Táo", "Táo", "Cam"}`, Set sẽ tự lọc chỉ còn `{"Táo", "Cam"}`!
2. **Các phép toán tập hợp**:
   * `set1 | set2` (Hợp): Gộp tất cả vật phẩm của cả 2 tập hợp.
   * `set1 & set2` (Giao): Tìm những vật phẩm mà CẢ HAI đều có.
   * `set1 - set2` (Hiệu): Những vật phẩm CHỈ set1 có mà set2 không có.

> [!TIP]
> **Bí kíp nhanh**: Muốn lọc bỏ tất cả phần tử trùng lặp trong một List, bạn chỉ cần ép kiểu List đó sang Set bằng `set(my_list)`!

---

## 🤖 Dự án thực hành: Bộ Sưu Tập Huy Hiệu & Tọa Độ Kho Báu!
Bên cột phải là hệ thống kiểm tra danh hiệu Siêu Anh Hùng và xác định tọa độ căn cứ bí mật.
Hãy nhấn **"Bấm để Chạy thử! 🚀"** để xem hệ thống hoạt động!

### 💡 Thử thách cho bạn:
1. Thử thêm danh hiệu bị trùng vào tập hợp `huy_hieu_p1` và xem Set có tự động lọc bỏ không nhé!
2. Thử thay đổi tọa độ `toa_do[0] = 999` để thấy Python báo lỗi bảo vệ Tuple tuyệt vời như thế nào!
