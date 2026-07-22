# Tuần 4 (Cấp 2): Cuốn Từ Điển Thần Kỳ (Dictionary) 📖

Trong đời thực, khi tra từ điển, bạn tìm **Từ cần tra (Key)** để xem **Ý nghĩa của từ (Value)**. Trong Python, **Dictionary (Từ điển)** là cấu trúc dữ liệu cực kỳ mạnh mẽ giúp lưu trữ thông tin dưới dạng cặp **Khóa - Giá trị (`Key: Value`)**!

---

## 🌟 Mục tiêu cần đạt
* Biết cách tạo một Dictionary với cặp dấu ngoặc nhọn `{}` và dấu hai chấm `:`.
* Tra cứu thông tin cực nhanh bằng `Khóa (Key)`.
* Biết cách thêm thông tin mới, cập nhật giá trị và xóa thông tin.
* Sử dụng vòng lặp duyệt qua `.keys()`, `.values()` và `.items()`.

---

## 🔑 Khái niệm cốt lõi

### 1. Cấu trúc Dictionary
```python
sieu_nhan = {
    "ten": "Iron Man",
    "tuoi": 35,
    "suc_manh": "Bộ giáp công nghệ",
    "cap_do": 99
}
```
* **Khóa (Key)**: `"ten"`, `"tuoi"`, `"suc_manh"` (thường là Chuỗi chữ, phải là duy nhất).
* **Giá trị (Value)**: `"Iron Man"`, `35`, `"Bộ giáp công nghệ"` (có thể là bất kỳ kiểu dữ liệu nào!).

### 2. Các thao tác cơ bản với Dictionary
* Tra cứu giá trị: `sieu_nhan["ten"]` ➡️ Trả về `"Iron Man"`.
* Thêm thông tin mới: `sieu_nhan["dong_doi"]` = "Spider-Man".
* Cập nhật giá trị: `sieu_nhan["cap_do"]` = 100.
* Xóa thông tin: `del sieu_nhan["tuoi"]`.

### 3. Duyệt Dictionary bằng vòng lặp
```python
for key, value in sieu_nhan.items():
    print(f"{key}: {value}")
```

> [!NOTE]
> **Điểm mạnh của Dictionary**: Tra cứu cực nhanh! Dù từ điển có 1.000.000 phần tử, Python tìm theo Key chỉ mất chớp mắt!

---

## 🤖 Dự án thực hành: Hồ Sơ Siêu Anh Hùng!
Bên cột phải là ứng dụng lưu trữ và quản lý Hồ sơ bí mật của các Siêu Anh Hùng.
Hãy nhấn **"Bấm để Chạy thử! 🚀"** để xem hồ sơ nào!

### 💡 Thử thách cho bạn:
1. Thêm một thuộc tính mới cho Siêu Anh Hùng, ví dụ: `hoso["vu_khi"] = "Khiên Vibranium"`.
2. Thay đổi `hoso["suc_manh"]` lên số `100` và in lại hồ sơ!
