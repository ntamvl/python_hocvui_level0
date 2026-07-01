# Kế hoạch xây dựng Trang web học Python cho trẻ em 12+

Dự án này nhằm xây dựng một ứng dụng web học lập trình Python cơ bản được thiết kế riêng cho trẻ em từ 12 tuổi trở lên. Giao diện sẽ tươi sáng, bắt mắt (tương tự Duolingo/Scratch), thân thiện, chia làm 2 cột: lý thuyết sinh động bên trái và trình thực hành code tương tác (chạy Python trực tiếp trên trình duyệt bằng Pyodide) bên phải.

---

## Lộ trình giảng dạy 6 tuần (Curriculum)

Ngôn ngữ diễn đạt sẽ cực kỳ gần gũi, sử dụng các ví dụ thực tế như thế giới game, siêu anh hùng, quái thú nuôi ảo, tránh tối đa các thuật ngữ học thuật khô khan.

1. **Tuần 1: Làm quen với người bạn Python! (Giới thiệu & Lệnh Print)**
   - **Mục tiêu**: Hiểu cách máy tính giao tiếp và viết câu lệnh đầu tiên.
   - **Khái niệm**: Lệnh `print()`, chuỗi văn bản (String), cách máy tính chạy từng dòng code.
   - **Dự án thực hành**: *Robot chào hỏi đáng yêu* - Vẽ chú robot bằng các ký tự đặc biệt (ASCII art) và gửi lời chào cá nhân hóa.
2. **Tuần 2: Chiếc hộp thần kỳ chứa đồ chơi (Biến và Phép toán cơ bản)**
   - **Mục tiêu**: Hiểu khái niệm lưu trữ thông tin và tính toán cơ bản.
   - **Khái niệm**: Biến (variable), kiểu dữ liệu (Số, Chữ), các phép toán `+`, `-`, `*`, `/`.
   - **Dự án thực hành**: *Máy tính tuổi thú cưng siêu cấp* - Nhập tuổi của cún/mèo và tính xem quy đổi sang tuổi con người là bao nhiêu.
3. **Tuần 3: Ngã rẽ quyết định (Cấu trúc điều kiện If-Else)**
   - **Mục tiêu**: Giúp chương trình biết suy nghĩ và đưa ra lựa chọn.
   - **Khái niệm**: Lệnh rẽ nhánh `if`, `elif`, `else`, các phép so sánh `>`, `<`, `==`.
   - **Dự án thực hành**: *Gương thần dự báo thời tiết* - Nhập thời tiết hiện tại và nhận lời khuyên chọn trang phục đi chơi dí dỏm.
4. **Tuần 4: Vòng quay vô tận (Vòng lặp For và While)**
   - **Mục tiêu**: Biết cách bắt máy tính làm các công việc lặp đi lặp lại một cách tự động.
   - **Khái niệm**: Vòng lặp `for`, vòng lặp `while`, hàm tạo khoảng số `range()`.
   - **Dự án thực hành**: *Hỏa tiễn đếm ngược phóng vào vũ trụ* - In ra đồng hồ đếm ngược từ 10 về 1 và bắn tên lửa kèm theo các hiệu ứng bay lượn sinh động.
5. **Tuần 5: Chiếc máy làm bánh ma thuật (Hàm - Functions)**
   - **Mục tiêu**: Gom các dòng lệnh vào một "cỗ máy" có tên để tái sử dụng dễ dàng.
   - **Khái niệm**: Định nghĩa hàm `def`, tham số truyền vào (parameters), giá trị trả về (`return`).
   - **Dự án thực hành**: *Máy tạo biệt danh siêu anh hùng* - Hàm nhận vào màu sắc và con vật bé yêu thích để ghép thành tên siêu anh hùng cực ngầu.
6. **Tuần 6: Bản thiết kế quái thú nuôi ảo (Lớp và Đối tượng - OOP cơ bản)**
   - **Mục tiêu**: Hiểu khái niệm hướng đối tượng thông qua trò chơi nuôi thú cưng ảo.
   - **Khái niệm**: Lớp (Class), Đối tượng (Object), thuộc tính (properties), hành động (methods).
   - **Dự án thực hành**: *Vườn thú ảo vui nhộn* - Tạo lớp Quái Thú (Monster) có tên, năng lượng; viết hàm cho ăn, đùa nghịch và phát tiếng kêu của quái thú.

---

## Kiến trúc kỹ thuật & Công nghệ

### 1. Cấu trúc thư mục đề xuất
Để đáp ứng yêu cầu lưu trữ rõ ràng và dễ quản lý:
- `/lessons/`: Thư mục gốc chứa các tài liệu giảng dạy gốc bằng Markdown và file code mẫu Python.
- `/frontend/`: Thư mục chứa mã nguồn React + Vite + Bootstrap.
  - Sử dụng **Pyodide** (Wasm) để chạy Python trực tiếp tại client-side giúp phản hồi tức thì, không cần kết nối internet hay gửi code lên server, cực kỳ an toàn và ổn định.
  - Sử dụng **Bootstrap** cho hệ thống Grid và Layout cơ bản, kết hợp Custom CSS tươi sáng, bo tròn góc, hoạt hình (giao diện giống Scratch/Duolingo).
  - Sử dụng thư viện **React Markdown** để hiển thị lý thuyết sinh động từ các file Markdown.
  - Sử dụng hiệu ứng **Confetti** (pháo hoa giấy) khi trẻ chạy code dự án thành công.

```
/Users/tamnguyen/Projects/giaoduc/laptrinh_python_canban_v1.2/
├── lessons/                     # Bài giảng & code mẫu gốc
│   ├── week1_intro/
│   │   ├── README.md
│   │   └── project.py
│   ├── ...
│   └── week6_classes/
│       ├── README.md
│       └── project.py
├── frontend/                    # Ứng dụng React (Vite)
│   ├── public/
│   │   └── lessons/             # Được đồng bộ từ thư mục gốc /lessons để frontend fetch
│   ├── src/
│   │   ├── components/
│   │   │   ├── Sidebar.jsx      # Danh sách bài học/tuần
│   │   │   ├── TheoryColumn.jsx # Cột lý thuyết (Render Markdown)
│   │   │   ├── CodeEditor.jsx   # Cột soạn thảo code (với syntax highlight & Pyodide runner)
│   │   │   └── Achievement.jsx  # Hiệu ứng pháo hoa chúc mừng
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css            # Custom CSS tươi tắn, hoạt họa
│   ├── package.json
│   └── vite.config.js
```

---

## Thiết kế giao diện (UI/UX)

- **Màu sắc chủ đạo**: Tone màu vui nhộn, pastel năng động.
  - Xanh lá cây nhạt (Duolingo style), Cam tươi, Xanh dương da trời, Vàng năng lượng.
- **Font chữ**: Sử dụng Google Font như **Nunito** hoặc **Outfit** (tròn trịa, dễ đọc, rất thân thiện với trẻ em).
- **Layout 2 cột chính**:
  - **Cột Trái (Lý thuyết)**: Rộng 45%, hiển thị bài học với các hộp ghi chú đầy màu sắc: `💡 Mẹo nhỏ`, `⚠️ Chú ý`, `🌟 Thử thách cho bé`.
  - **Cột Phải (Code thực hành)**: Rộng 55%.
    - Phía trên: Code Editor (có đánh số dòng, tô màu cú pháp nhẹ nhàng, thiết kế bắt mắt). Có nút bấm khổng lồ: **"Bấm để Chạy thử! 🚀"**.
    - Phía dưới: Màn hình console kết quả (Terminal màu đen mượt mà với chữ xanh lá/trắng, hiển thị kết quả của lệnh `print` hoặc lỗi Python được viết lại một cách dễ thương).

---

## Các bước triển khai chi tiết

### Bước 1: Tạo tài liệu bài học và code mẫu gốc (Markdown & Python)
- Viết 6 bài học markdown chi tiết, sử dụng định dạng phong phú (in đậm, blockquote, danh sách) và ngôn ngữ đáng yêu.
- Viết 6 file code Python mẫu tương ứng với dự án của mỗi tuần.

### Bước 2: Khởi tạo và thiết lập Frontend React
- Sử dụng Vite để khởi tạo project React trong `/frontend/`.
- Cài đặt Bootstrap, React Markdown, Lucide React (icons), Canvas Confetti.
- Tải cấu hình Pyodide từ CDN trong file `index.html` để khởi tạo trình chạy Python.

### Bước 3: Phát triển các Component React
- **Sidebar**: Hiển thị tiến trình 6 tuần dưới dạng các hòn đảo học tập hoặc bản đồ kho báu.
- **TheoryColumn**: Fetch file markdown tương ứng của tuần và hiển thị nó một cách đẹp mắt.
- **CodeEditor + CodeRunner**:
  - Tích hợp trình soạn thảo code đơn giản.
  - Sử dụng Pyodide để nạp và chạy code, bắt sự kiện `stdout` để ghi vào màn hình kết quả ảo.
  - Thêm tính năng chạy code mẫu (nút "Xem code mẫu" để tự động điền code mẫu vào editor).
- **Achievement/Confetti**: Khi code chạy không lỗi và cho ra kết quả, kích hoạt bắn pháo hoa ăn mừng.

### Bước 4: Thiết kế CSS tươi tắn
- Thiết kế các nút bấm dạng 3D đáng yêu (nhấn xuống có hiệu ứng lún nút).
- Bo tròn góc (`border-radius: 16px` trở lên).
- Thêm các hiệu ứng hover mượt mà.

---

## Kế hoạch kiểm thử & Xác minh (Verification Plan)

### Kiểm thử thủ công
1. **Kiểm tra hiển thị**: Xem giao diện trên màn hình máy tính có cân đối không, có đúng tỷ lệ 2 cột không.
2. **Kiểm tra Pyodide**: Viết thử các lệnh Python từ cơ bản (`print('Hello')`) đến nâng cao (vòng lặp, hàm, định nghĩa class) trong editor xem có chạy và hiển thị đúng kết quả ở terminal ảo không.
3. **Kiểm tra tải bài học**: Click qua lại giữa các tuần 1 - 6 để xem lý thuyết và code mẫu tương ứng có được cập nhật đúng và mượt mà không.
4. **Kiểm tra hiệu ứng**: Chạy thành công dự án tuần xem pháo hoa giấy (confetti) có hoạt động không.

---

## Ý kiến cần người dùng xác nhận
> [!IMPORTANT]
> **Về việc cài đặt Pyodide**: Chúng ta sẽ sử dụng Pyodide thông qua CDN trong file `index.html` của React để chạy Python trực tiếp tại client-side. Điều này giúp hệ thống **không cần backend FastAPI** mà vẫn chạy code Python cực kỳ mượt mà ngay trên trình duyệt của trẻ.
> Bạn có đồng ý với phương án chạy Python trực tiếp client-side này không, hay bạn muốn xây dựng thêm một FastAPI backend riêng để giao tiếp? (Phương án client-side thông qua Pyodide được khuyến khích vì tính tương tác cao và dễ triển khai).
