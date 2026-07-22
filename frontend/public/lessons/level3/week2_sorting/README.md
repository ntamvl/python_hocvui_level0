# Tuần 2 (Cấp 3): Thợ May Xếp Hàng 📊 (Thuật Toán Sắp Xếp - Sorting Algorithms)

Trong lập trình, việc sắp xếp dữ liệu theo thứ tự (tăng dần hoặc giảm dần) là một tác vụ cực kỳ phổ biến: từ bảng xếp hạng điểm game, danh sách tên theo thứ tự ABC cho đến danh sách giá tiền từ thấp đến cao. Tuần này, bạn sẽ tự tay xây dựng các **Thuật toán Sắp xếp (Sorting Algorithms)** huyền thoại!

---

## 🌟 Mục tiêu cần đạt
* Hiểu tư duy và tầm quan trọng của bài toán sắp xếp dữ liệu.
* Tự cài đặt được thuật toán **Sắp xếp Nổi bọt (Bubble Sort)** và **Sắp xếp Chọn (Selection Sort)**.
* Thành thạo kỹ thuật **Hoán đổi giá trị (Swapping)** hai phần tử trong Python: `a, b = b, a`.
* Hiểu cách hoạt động của vòng lặp lồng nhau (Nested Loops) áp dụng trong thuật toán.

---

## 🔑 Khái niệm cốt lõi

### 1. Kỹ thuật Hoán đổi giá trị (Swapping)
Trong Python, việc đổi chỗ giá trị của 2 biến siêu đơn giản:
```python
x = 5
y = 10
x, y = y, x  # Sau dòng này: x = 10, y = 5
```

### 2. Thuật toán Sắp xếp Nổi bọt (Bubble Sort) 🫧
* **Ý tưởng**: Giống như các bong bóng nước nhẹ hơn sẽ nổi lên trên. Ta so sánh từng cặp 2 phần tử đứng cạnh nhau, nếu phần tử đằng trước lớn hơn phần tử đằng sau thì đổi chỗ chúng.
* **Cơ chế**: Qua mỗi lượt duyệt, phần tử lớn nhất sẽ "nổi" về cuối danh sách.
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # Đổi chỗ
    return arr
```

### 3. Thuật toán Sắp xếp Chọn (Selection Sort) 🎯
* **Ý tưởng**: Đi tìm phần tử nhỏ nhất trong danh sách chưa sắp xếp, sau đó đổi chỗ nó về vị trí đầu tiên. lặp lại quá trình với phần còn lại.
```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i] # Đưa số nhỏ nhất về vị trí i
    return arr
```

> [!NOTE]
> **Mẹo so sánh**:
> * **Bubble Sort**: So sánh các cặp liền kề và đổi chỗ liên tục.
> * **Selection Sort**: Tìm vị trí nhỏ nhất trước rồi chỉ đổi chỗ đúng 1 lần cho mỗi lượt.

---

## 🤖 Dự án thực hành: Bảng Xếp Hạng Game Arcade!
Bên cột phải là chương trình tự động sắp xếp điểm số của các game thủ từ cao xuống thấp bằng các thuật toán bạn vừa học.
Hãy nhấn nút **"Bấm để Chạy thử! 🚀"** để xem các con số tự động nhảy về đúng vị trí nhé!

### 💡 Thử thách cho bạn:
1. Thử thay đổi danh sách điểm `scores = [450, 120, 890, 320, 670]` thành các điểm số ngẫu nhiên của riêng bạn.
2. Thử sửa điều kiện so sánh trong `bubble_sort` để danh sách sắp xếp tăng dần thay vì giảm dần!
