# Tuần 1 (Cấp 2): Ép kiểu & Siêu công cụ Python 🧰

Chào mừng bạn đến với **Cấp độ 2**! Ở cấp độ này, chúng ta sẽ mở khóa những siêu năng lực mạnh mẽ hơn của Python. Tuần đầu tiên, bạn sẽ học cách biến đổi các kiểu dữ liệu (Ép kiểu) và sử dụng các "siêu công cụ" có sẵn!

---

## 🌟 Mục tiêu cần đạt
* Biết cách chuyển đổi qua lại giữa các kiểu dữ liệu (`int()`, `float()`, `str()`, `bool()`).
* Nắm vững các hàm có sẵn hữu ích nhất: `len()`, `sum()`, `max()`, `min()`, `abs()`, `round()`, `type()`.
* Viết được chương trình tính toán và chuẩn hóa dữ liệu đầu vào.

---

## 🔑 Khái niệm cốt lõi

### 1. Ép kiểu dữ liệu (Type Casting) là gì?
Đôi khi Python nhận dữ liệu ở dạng chuỗi chữ `"100"` nhưng bạn lại muốn thực hiện phép cộng số `100`. Đó là lúc ta dùng **Ép kiểu** (chuyển dạng này sang dạng khác):
* `int("100")` ➡️ Chuyển chuỗi thành Số nguyên (`100`).
* `str(50)` ➡️ Chuyển số thành Chuỗi chữ (`"50"`).
* `float("3.14")` ➡️ Chuyển thành Số thực (`3.14`).
* `bool(1)` ➡️ Chuyển thành Đúng/Sai (`True`).

### 2. Các hàm có sẵn thần kỳ (Built-in Functions)
Python đã trang bị sẵn rất nhiều "vũ khí" cực xịn mà bạn không cần tự viết:
* `len("Python")` ➡️ Đếm số ký tự (Trả về `6`).
* `max(5, 12, 8)` ➡️ Tìm số lớn nhất (Trả về `12`).
* `min(5, 12, 8)` ➡️ Tìm số nhỏ nhất (Trả về `5`).
* `sum([10, 20, 30])` ➡️ Tính tổng danh sách (Trả về `60`).
* `abs(-15)` ➡️ Trị tuyệt đối (Trả về `15`).
* `round(3.14159, 2)` ➡️ Làm tròn 2 chữ số thập phân (Trả về `3.14`).
* `type(100)` ➡️ Kiểm tra kiểu dữ liệu của biến.

> [!NOTE]
> **Mẹo nhỏ**: Hàm `input()` luôn trả về kiểu Chuỗi (`str`). Muốn tính toán toán học, bạn nhớ ép kiểu thành `int()` hoặc `float()` nhé!

---

## 🤖 Dự án thực hành: Máy đo chỉ số Siêu Anh Hùng!
Bên cột phải là ứng dụng đo và phân tích các chỉ số sức mạnh của 3 Siêu Anh Hùng.
Hãy nhấn **"Bấm để Chạy thử! 🚀"** để xem phân tích nhé!

### 💡 Thử thách cho bạn:
1. Thử thay đổi các chỉ số sức mạnh `power1`, `power2`, `power3` thành các số thực (ví dụ `88.5`, `92.4`) và xem kết quả làm tròn bằng `round()`.
2. Dùng lệnh `max()` và `min()` để tìm ra chỉ số mạnh nhất và yếu nhất!
