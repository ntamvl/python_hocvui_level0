# Tuần 5 (Cấp 2): Xưởng Nâng Cấp Hàm (Advanced Functions) ⚡

Ở Cấp độ 1, bạn đã biết cách viết một hàm đơn giản bằng `def`. Tuần này, chúng ta sẽ mở khóa các kỹ thuật nâng cao: **Phạm vi biến**, **Tham số mặc định**, **Truyền nhiều tham số (`*args`)** và **Hàm Lambda siêu tốc**!

---

## 🌟 Mục tiêu cần đạt
* Hiểu sự khác biệt giữa biến Toàn cục (**Global**) và biến Cục bộ (**Local**).
* Biết tạo hàm với **Tham số mặc định** (Default Parameters).
* Biết truyền số lượng tham số không giới hạn bằng `*args`.
* Viết hàm 1 dòng cực gọn bằng **Lambda**.

---

## 🔑 Khái niệm cốt lõi

### 1. Scope: Biến Toàn cục vs Cục bộ
* **Biến Cục bộ (Local)**: Biến tạo bên trong hàm, chỉ sống bên trong hàm đó.
* **Biến Toàn cục (Global)**: Biến tạo bên ngoài, cả chương trình đều nhìn thấy.

### 2. Tham số mặc định (Default Parameters)
Nếu người dùng không truyền giá trị vào, hàm sẽ tự động lấy giá trị mặc định có sẵn:
```python
def tao_nhan_vat(ten, mau="Xanh", cap_do=1):
    print(f"{ten} - Màu: {mau} - Cấp: {cap_do}")

tao_nhan_vat("Robot A")                 # Lấy màu Xanh, cấp 1
tao_nhan_vat("Robot B", mau="Đỏ", cap_do=5) # Thay đổi màu và cấp
```

### 3. Biến linh hoạt `*args`
Cho phép truyền bao nhiêu tham số vào hàm cũng được (Python gộp chúng thành 1 Tuple):
```python
def tinh_tong_diem(*diem_so):
    return sum(diem_so)

print(tinh_tong_diem(10, 20, 30, 40)) # Trả về 100
```

### 4. Hàm Lambda (Hàm 1 dòng siêu gọn)
```python
gấp_đôi = lambda x: x * 2
print(gấp_đôi(5)) # Trả về 10
```

---

## 🤖 Dự án thực hành: Trạm Chế Tạo Siêu Robot!
Bên cột phải là hệ thống lắp ráp Robot tùy chỉnh với các tham số linh hoạt và tính năng tính điểm chiến đấu.
Hãy nhấn **"Bấm để Chạy thử! 🚀"** để chế tạo Robot nào!

### 💡 Thử thách cho bạn:
1. Thử gọi hàm `che_tao_robot()` chỉ với tên Robot xem các tham số mặc định xuất hiện như thế nào.
2. Dùng hàm lambda để tạo một phép tính nhân 3 sức mạnh!
