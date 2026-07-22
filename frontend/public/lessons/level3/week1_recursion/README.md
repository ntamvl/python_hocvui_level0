# Tuần 1 (Cấp 3): Búp bê Nga Matryoshka 🪆 (Hàm Đệ Quy - Recursion)

Chào mừng bạn đến với **Cấp độ 3: Chuyên Gia**! Ở cấp độ này, chúng ta sẽ chinh phục các tư duy thuật toán và lập trình hướng đối tượng nâng cao. Bài học mở đầu sẽ đưa bạn khám phá bí mật của **Hàm Đệ Quy** — một trong những khái niệm thú vị nhất trong lập trình!

---

## 🌟 Mục tiêu cần đạt
* Hiểu bản chất Đệ quy (Recursion) là gì: Hàm tự gọi lại chính nó để giải quyết bài toán nhỏ hơn.
* Nhận diện và thiết lập đúng 2 thành phần bắt buộc của đệ quy: **Điểm dừng (Base Case)** và **Lời gọi đệ quy (Recursive Step)**.
* Viết được chương trình đệ quy để giải bài toán đếm ngược và tính giai thừa (`n!`).
* Nhận biết lỗi tràn ngăn xếp (`RecursionError`) và biết cách khắc phục.

---

## 🔑 Khái niệm cốt lõi

### 1. Hàm Đệ Quy (Recursion) là gì?
Hãy tưởng tượng bộ búp bê Nga Matryoshka: bên trong con búp bê to chứa một con búp bê nhỏ hơn, bên trong con nhỏ hơn lại chứa một con nhỏ hơn nữa... cho đến khi đến con nhỏ nhất không thể mở ra được nữa!

Trong Python, **Hàm đệ quy** là hàm tự gọi lại chính nó trong quá trình thực thi:
```python
def mo_bup_be(kich_thuoc):
    if kich_thuoc == 1: # 🛑 Điểm dừng (Base Case)
        print("Đã tới con búp bê nhỏ nhất rồi! 🎉")
    else:
        print(f"Đang mở búp bê kích thước {kich_thuoc}...")
        mo_bup_be(kich_thuoc - 1) # 🔄 Lời gọi đệ quy (gọi lại chính nó)
```

### 2. Hai quy tắc vàng của Đệ quy 📜
Mỗi hàm đệ quy **BẮT BUỘC** phải có:
1. **Điểm dừng (Base Case)**: Điều kiện để hàm dừng lại, không gọi tiếp nữa. Nếu thiếu điểm dừng, chương trình sẽ chạy vô tận và bị lỗi `RecursionError` (Stack Overflow)!
2. **Bước đệ quy (Recursive Step)**: Gọi lại chính hàm đó nhưng với dữ liệu nhỏ hơn (tiến dần về Điểm dừng).

### 3. Ví dụ tính Giai thừa ($n!$) bằng Đệ quy
Toán học: $5! = 5 \times 4 \times 3 \times 2 \times 1 = 5 \times 4!$
```python
def giai_thua(n):
    if n == 1:
        return 1
    return n * giai_thua(n - 1)
```

> [!IMPORTANT]
> **Mẹo ghi nhớ**: Luôn hỏi bản thân 2 câu hỏi trước khi viết đệ quy:
> 1. *"Khi nào thì dừng lại?"* ➡️ Điểm dừng (`if`).
> 2. *"Làm sao để bài toán nhỏ đi một chút?"* ➡️ Lời gọi đệ quy (`else`).

---

## 🤖 Dự án thực hành: Tháp Đếm Ngược & Năng Lượng Robot!
Bên cột phải là chương trình kích hoạt Robot đếm ngược bằng đệ quy và tính toán năng lượng tiêu thụ.
Hãy nhấn nút **"Bấm để Chạy thử! 🚀"** để quan sát đệ quy hoạt động từng bước nhé!

### 💡 Thử thách cho bạn:
1. Thử thay đổi số giây đếm ngược `countdown(5)` thành `countdown(10)` và xem kết quả.
2. Thử viết thêm hàm đệ quy `tinh_tong(n)` để tính tổng từ `1` đến `n` (Ví dụ `tinh_tong(5)` trả về `15`).
