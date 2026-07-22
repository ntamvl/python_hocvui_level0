# Tuần 3 (Cấp 3): Gia Đình Siêu Anh Hùng 🦸‍♂️ (Kế Thừa Trong OOP - Inheritance)

Ở Cấp độ 1, bạn đã biết tạo **Lớp (Class)** và **Đối tượng (Object)**. Tuần này, chúng ta sẽ mở khóa một tính năng cực kỳ mạnh mẽ của Lập trình hướng đối tượng (OOP): **Tính Kế Thừa (Inheritance)**!

---

## 🌟 Mục tiêu cần đạt
* Hiểu khái niệm Kế thừa: Lớp con nhận lại tất cả thuộc tính và phương thức từ Lớp cha mà không cần viết lại mã nguồn.
* Biết cách khai báo Lớp Con kế thừa từ Lớp Cha: `class LopCon(LopCha):`.
* Sử dụng hàm `super()` để gọi phương thức khởi tạo (`__init__`) của Lớp cha.
* Thực hiện **Ghi đè phương thức (Method Overriding)** để lớp con có những tuyệt chiêu độc nhất!

---

## 🔑 Khái niệm cốt lõi

### 1. Kế Thừa (Inheritance) là gì?
Hãy tưởng tượng:
* Siêu anh hùng nào cũng có `ten` (tên) và `mau` (lượng máu), và đều biết `tan_cong()` (tấn công). Đó là **Lớp Cha (AnhHung)**.
* **Phù Thủy** hay **Chiến Sĩ** đều là Siêu anh hùng nhưng Phù Thủy có thêm `phep_thuat` và tuyệt chiêu `ban_phep()`. Đó là **Lớp Con (PhuThuy, ChienSi)**.

Thay vì viết lại `ten` và `mau` cho từng loại nhân vật, Lớp con chỉ cần **Kế thừa** từ Lớp cha!

### 2. Cú pháp Kế thừa & Hàm `super()`
```python
# 🦸 1. LỚP CHA (Superclass)
class AnhHung:
    def __init__(self, ten, mau):
        self.ten = ten
        self.mau = mau
    
    def gioi_thieu(self):
        print(f"🦸 Tôi là {self.ten}, máu: {self.mau} HP")

# 🧙 2. LỚP CON (Subclass) kế thừa từ AnhHung
class PhuThuy(AnhHung):
    def __init__(self, ten, mau, nang_luong):
        # Gọi constructor của Lớp cha bằng super()
        super().__init__(ten, mau)
        self.nang_luong = nang_luong # Thuộc tính riêng của Phù thủy

    # Ghi đè phương thức (Method Overriding)
    def gioi_thieu(self):
        print(f"🧙 Tôi là Phù thủy {self.ten}, Năng lượng phép: {self.nang_luong} MP!")
```

### 3. Ghi đè phương thức (Method Overriding)
Khi lớp con viết lại một phương thức đã có ở lớp cha với tên giống hệt, phương thức mới của lớp con sẽ được ưu tiên chạy. Đây gọi là **Method Overriding**.

> [!IMPORTANT]
> **Lợi ích lớn nhất của Kế thừa**: Tiết kiệm thời gian, tránh viết lặp lại mã nguồn (DRY - Don't Repeat Yourself) và dễ dàng mở rộng dự án game!

---

## 🤖 Dự án thực hành: Biệt Đội Siêu Anh Hùng!
Bên cột phải là hệ thống nhân vật Game gồm Chiến sĩ, Phù thủy và Xạ thủ cùng kế thừa từ Lớp Hero gốc.
Hãy nhấn nút **"Bấm để Chạy thử! 🚀"** để xem các nhân vật trổ tài nhé!

### 💡 Thử thách cho bạn:
1. Thử tạo thêm một Lớp con mới tên là `SieuNhanNhanhNhen` kế thừa từ `AnhHung` có thêm thuộc tính `toc_do`.
2. Tạo đối tượng `flash` từ lớp mới và cho Flash cất lời chào!
