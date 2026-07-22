# Tuần 3: Ngã rẽ quyết định! 🧭

Hôm nay, chúng ta sẽ học cách làm cho chương trình trở nên thông minh hơn bằng cách giúp nó tự đưa ra quyết định dựa trên các tình huống khác nhau. Đó chính là **Cấu trúc điều kiện If-Else**!

---

## 🌟 Mục tiêu cần đạt
* Hiểu cách chương trình đưa ra quyết định.
* Biết cách sử dụng cấu trúc `if`, `elif` và `else`.
* Biết cách so sánh các giá trị (lớn hơn, nhỏ hơn, bằng).

---

## 🔑 Khái niệm cốt lõi

### Quyết định dựa trên điều kiện là gì? 🤔
Trong cuộc sống, bạn luôn đưa ra lựa chọn dựa trên điều kiện:
* **NẾU** trời mưa: Bạn sẽ mang theo ô (dù).
* **NẾU KHÔNG THÌ** (trời nắng): Bạn sẽ đeo kính râm.

Trong Python, chúng ta sử dụng các từ khóa sau để diễn đạt:
1. `if` (Nếu): Kiểm tra điều kiện đầu tiên.
2. `elif` (viết tắt của else if - Nếu không thì nếu): Kiểm tra thêm một điều kiện phụ khác nếu điều kiện trên bị sai.
3. `else` (Nếu không): Trường hợp cuối cùng, khi tất cả các điều kiện trên đều không đúng.

### 📝 Cách viết điều kiện trong Python:
```python
thoi_tiet = "mưa"

if thoi_tiet == "mưa":
    print("Mang theo ô nhé!")
else:
    print("Hãy đeo kính râm!")
```

> [!IMPORTANT]
> **Chú ý quan trọng**: 
> * Sử dụng hai dấu bằng `==` để kiểm tra xem hai thứ có bằng nhau không (khác với một dấu gán `=` cất đồ vào hộp nhé!).
> * Cuối câu lệnh `if`, `elif`, `else` phải có **dấu hai chấm `:`**.
> * Các lệnh nằm bên trong khối điều kiện phải được **lùi vào lề** (nhấn phím Tab hoặc 4 dấu cách) để Python hiểu nó thuộc về khối lệnh đó.

---

## 🔮 Dự án thực hành: Gương thần dự báo thời tiết!
Bên cột phải là một "Gương thần" biết đọc thời tiết và khuyên bạn nên làm gì.

### 💡 Thử thách cho bạn:
1. Hãy thay đổi giá trị của biến `thoi_tiet` (ở dòng 4) từ `"nắng"` sang `"mưa"`, `"lạnh"`, hoặc bất kỳ từ nào khác (ví dụ: `"bão"`).
2. Chạy thử chương trình để xem Gương thần khuyên bạn thế nào nhé!
