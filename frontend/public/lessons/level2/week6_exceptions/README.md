# Tuần 6 (Cấp 2): Khiên Bảo Vệ Chương Trình (Exception Handling) 🛡️

Trong khi chơi game hoặc viết code, đôi khi người dùng nhập nhầm chữ vào ô số, hoặc chia một số cho 0. Khi đó Python sẽ bị "bối rối" và gây ra lỗi sập chương trình. Tuần này, bạn sẽ trang bị **Khiên bảo vệ `try...except`** để giữ cho chương trình luôn chạy mượt mà!

---

## 🌟 Mục tiêu cần đạt
* Nhận biết các lỗi ngoại lệ (Exception) thường gặp: `ValueError`, `ZeroDivisionError`, `IndexError`, `KeyError`, `TypeError`.
* Nắm vững cú pháp `try`, `except`, `else`, `finally`.
* Hiển thị thông báo hướng dẫn sửa lỗi thân thiện thay vì những dòng lỗi đỏ khô khan.

---

## 🔑 Khái niệm cốt lõi

### 1. Cấu trúc Khiên Bảo Vệ `try...except`
```python
try:
    # Dòng code có thể gây ra lỗi (Ví dụ nhập dữ liệu)
    tuoi = int("mười") # Lỗi ValueError vì "mười" không đổi thành số được!
except ValueError:
    # Đoạn code xử lý khi gặp lỗi cụ thể
    print("Oops! Bạn phải nhập dạng số (như 10) cơ!")
```

### 2. Các thành phần mở rộng: `else` và `finally`
* `try`: Thử chạy đoạn code nguy hiểm.
* `except`: Kích hoạt NẾU có lỗi xảy ra.
* `else`: Kích hoạt NẾU KHÔNG có lỗi nào xảy ra.
* `finally`: LUÔN LUÔN kích hoạt dù có lỗi hay không (dùng để dọn dẹp, đóng ứng dụng).

### 3. Một số lỗi phổ biến cần ghi nhớ
* `ValueError`: Giá trị không đúng kiểu (vd: `int("abc")`).
* `ZeroDivisionError`: Chia một số cho `0` (vd: `10 / 0`).
* `IndexError`: Truy cập chỉ số nằm ngoài độ dài List (vd: List có 3 phần tử nhưng lấy `list[10]`).
* `KeyError`: Tra cứu một Key không tồn tại trong Dictionary.

---

## 🤖 Dự án thực hành: Game Khiên Phép Thuật Bảo Vệ!
Bên cột phải là chương trình nhận lệnh từ người chơi và xử lý an toàn các tình huống nhập dữ liệu sai.
Hãy nhấn **"Bấm để Chạy thử! 🚀"** để xem khiên bảo vệ hoạt động nhé!

### 💡 Thử thách cho bạn:
1. Thử thay đổi phép chia cho `0` trong `project.py` và xem khiên `ZeroDivisionError` bắt lỗi như thế nào.
2. Thử truy cập một vị trí phần tử không có thật trong danh sách và xem `IndexError` xuất hiện!
