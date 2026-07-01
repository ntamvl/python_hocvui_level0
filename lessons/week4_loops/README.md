# Tuần 4: Vòng quay vô tận! 🔄

Máy tính có một siêu năng lực cực kỳ lợi hại: làm các việc lặp đi lặp lại hàng triệu lần mà không hề biết mệt mỏi hay than thở. Hôm nay, chúng ta sẽ học cách làm việc đó qua **Vòng lặp (Loops)**!

---

## 🌟 Mục tiêu cần đạt
* Hiểu cách bắt máy tính làm việc lặp lại.
* Biết sử dụng vòng lặp `for` để đếm số.
* Biết sử dụng vòng lặp `while` khi chờ một điều kiện nào đó xảy ra.

---

## 🔑 Khái niệm cốt lõi

### 1. Vòng lặp `for` (Đếm số lần lặp) 🏃
Khi bạn biết chắc mình muốn lặp lại bao nhiêu lần, hãy dùng `for`.
Ví dụ, bạn muốn vỗ tay 3 lần:
```python
for i in range(3):
    print("Bép! 👏")
```
> [!NOTE]
> * Hàm `range(3)` sẽ tạo ra một danh sách số bắt đầu từ `0` đến `2` (tổng cộng 3 số: 0, 1, 2).
> * Biến `i` sẽ nhận lần lượt các giá trị đó qua mỗi vòng chạy.

### 2. Vòng lặp `while` (Lặp đến khi nào dừng thì thôi) 🔁
Vòng lặp `while` sẽ tiếp tục chạy **khi điều kiện còn đúng**.
Ví dụ: "Trong khi bụng vẫn đói, tiếp tục ăn bánh!"
```python
con_doi = True
while con_doi:
    print("Ăn một cái bánh... măm măm 🥐")
    con_doi = False # Ăn xong cái này thì hết đói!
```

---

## 🚀 Dự án thực hành: Hỏa tiễn đếm ngược phóng vào vũ trụ!
Bên cột phải là một chương trình đếm ngược thời gian từ 5 về 1, sau đó kích hoạt động cơ tên lửa để bay vút lên trời!

### 💡 Thử thách cho bạn:
1. Hiện tại tên lửa đang đếm ngược từ 5. Bạn hãy sửa số `5` ở dòng 4 thành số `10` để đếm ngược lâu hơn nhé!
2. Chạy thử chương trình để xem khoảnh khắc hỏa tiễn cất cánh cực ngầu!
