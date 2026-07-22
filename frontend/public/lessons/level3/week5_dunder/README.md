# Tuần 5 (Cấp 3): Phép Thuật Python 🪄 (Phương Thức Kỳ Diệu - Dunder Methods)

Bạn có bao giờ tự hỏi làm thế nào lệnh `print(danh_sach)` có thể in ra đẹp mắt dạng `[1, 2, 3]`, hay hàm `len("Hello")` lại biết đếm số ký tự chưa? Bí mật nằm ở các **Dunder Methods** (viết tắt của **Double Underscore** - hai dấu gạch dưới ở 2 đầu `__tên__`)!

---

## 🌟 Mục tiêu cần đạt
* Hiểu khái niệm **Dunder Methods** (hay Magic Methods) trong Python.
* Cài đặt được các phương thức kỳ diệu phổ biến: `__init__`, `__str__`, `__len__`, `__eq__`, `__add__`.
* Tùy biến cách đối tượng in ra màn hình khi gọi lệnh `print()`.
* Nạp chồng toán tử (Operator Overloading): Giúp các đối tượng của bạn có thể cộng `+` hoặc so sánh `==` như số thực thụ!

---

## 🔑 Khái niệm cốt lõi

### 1. Dunder Method là gì?
Là các phương thức đặc biệt được Python tự động gọi ngầm khi bạn thực hiện các thao tác tiêu chuẩn (như `print`, `len`, `+`, `==`).

### 2. Các Dunder Method phổ biến nhất

#### 🪄 `__str__(self)`: Định dạng chuỗi hiển thị
Được gọi khi bạn dùng `print(obj)` hoặc `str(obj)`:
```python
class VatPham:
    def __init__(self, ten, gia):
        self.ten = ten
        self.gia = gia

    def __str__(self):
        return f"⚔️ Vật phẩm: {self.ten} (Giá: {self.gia} vàng)"
```

#### 📏 `__len__(self)`: Đo độ dài
Được gọi khi bạn dùng `len(obj)`:
```python
class Tuido:
    def __init__(self):
        self.danh_sach = []

    def __len__(self):
        return len(self.danh_sach) # Trả về số lượng item trong túi
```

#### ⚖️ `__eq__(self, other)`: So sánh bằng (`==`)
Được gọi khi bạn so sánh `obj1 == obj2`:
```python
def __eq__(self, other):
    return self.ten == other.ten and self.gia == other.gia
```

#### ➕ `__add__(self, other)`: Nạp chồng phép cộng (`+`)
Được gọi khi bạn thực hiện `obj1 + obj2`:
```python
def __add__(self, other):
    # Gộp 2 túi đồ thành 1 túi đồ mới!
    tui_moi = Tuido()
    tui_moi.danh_sach = self.danh_sach + other.danh_sach
    return tui_moi
```

---

## 🤖 Dự án thực hành: Túi Đồ Ma Thuật Trong Game!
Bên cột phải là hệ thống Túi Đồ Ma Thuật (Inventory) cho phép in ra danh sách vật phẩm đẹp mắt, đo số lượng vật phẩm và hợp nhất 2 túi đồ bằng toán tử `+`!
Hãy nhấn nút **"Bấm để Chạy thử! 🚀"** để xem phép thuật Dunder hoạt động nhé!

### 💡 Thử thách cho bạn:
1. Viết thêm dunder method `__gt__(self, other)` (Greater Than - So sánh lớn hơn `>`) cho lớp `Tuido` để so sánh túi nào có nhiều vật phẩm hơn!
2. Thử nghiệm so sánh `tui_1 > tui_2` xem kết quả đúng hay sai.
