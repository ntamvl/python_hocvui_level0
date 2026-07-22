# Tuần 2 (Cấp 2): Chiếc Balo Danh Sách (List) 🎒

Hãy tưởng tượng bạn có một chiếc balo thần kỳ có thể chứa rất nhiều món đồ chơi theo thứ tự ngăn nắp. Trong Python, "chiếc balo" đó được gọi là **List (Danh sách)**!

---

## 🌟 Mục tiêu cần đạt
* Biết cách khởi tạo một List trong Python với cặp dấu ngoặc vuông `[]`.
* Hiểu cách lấy món đồ ra bằng vị trí **Index** (bắt đầu từ số `0`).
* Nắm vững các phương thức: `append()`, `insert()`, `remove()`, `pop()`, `sort()`, `len()`.
* Sử dụng vòng lặp `for` để duyệt qua từng vật phẩm trong danh sách.

---

## 🔑 Khái niệm cốt lõi

### 1. Tạo List và lấy phần tử theo Index
```python
tui_do = ["Đèn pin", "Bản đồ", "Lương khô"]
```
* Phần tử đầu tiên ở vị trí **0**: `tui_do[0]` ➡️ `"Đèn pin"`
* Phần tử thứ hai ở vị trí **1**: `tui_do[1]` ➡️ `"Bản đồ"`
* Lấy phần tử cuối cùng: `tui_do[-1]` ➡️ `"Lương khô"`

### 2. Thêm và Xóa đồ vật trong List (Mutable)
List trong Python rất linh hoạt, bạn có thể sửa đổi nội dung của nó bất cứ lúc nào:
* `tui_do.append("Dây thừng")` ➡️ Thêm món đồ vào cuối balo.
* `tui_do.insert(1, "Nước uống")` ➡️ Chèn vào vị trí số 1.
* `tui_do.remove("Bản đồ")` ➡️ Xóa món đồ theo tên.
* `mon_do = tui_do.pop()` ➡️ Lấy và xóa món đồ cuối cùng ra khỏi balo.
* `tui_do.sort()` ➡️ Sắp xếp các món đồ theo thứ tự bảng chữ cái A-Z.

> [!IMPORTANT]
> **Nhớ kĩ nhé**: Trong thế giới lập trình, chúng ta đếm từ số **0** chứ không phải số **1** đâu nha!

---

## 🤖 Dự án thực hành: Quản lý Balo Thám Hiểm!
Bên cột phải là chương trình quản lý vật phẩm trong chuyến thám hiểm rừng xanh của bạn.
Hãy nhấn **"Bấm để Chạy thử! 🚀"** để xem kiểm kê balo nào!

### 💡 Thử thách cho bạn:
1. Thêm một món đồ mới vào balo bằng lệnh `.append("Kính thiên văn")`.
2. Sắp xếp lại balo bằng lệnh `.sort()` xem điều kỳ diệu gì xảy ra nhé!
