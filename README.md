# Python Học Vui - Lập trình Python Căn Bản cho Trẻ Em

Chào mừng bạn đến với **Python Học Vui**, một nền tảng học lập trình Python trực quan, sinh động và tương tác cao được thiết kế dành riêng cho trẻ em từ 12 tuổi trở lên. Dự án này giúp các bé làm quen với các khái niệm lập trình từ căn bản đến nâng cao thông qua giao diện kéo/thả, viết code và chạy trực tiếp ngay trên trình duyệt web.

---

## 🌟 Tính năng nổi bật

*   **Học và Thực hành song song (Hai cột thông minh):**
    *   **Cột bên trái:** Lý thuyết được trình bày bằng ngôn ngữ dễ hiểu, gần gũi, không quá nặng thuật ngữ, hỗ trợ hiển thị Markdown với sơ đồ trực quan và tô sáng cú pháp Python.
    *   **Cột bên phải:** Sân chơi lập trình thực tế với trình soạn thảo mã nguồn hỗ trợ phím `Tab` lùi lề tự động (4 khoảng trắng), tô sáng mã màu Python thời gian thực.
*   **Chạy code trực tiếp trên trình duyệt (WebAssembly):**
    *   Tích hợp **Pyodide**, cho phép chạy code Python trực tiếp dưới client-side mà không cần máy chủ (backend) hay cài đặt môi trường Python phức tạp trên máy tính của bé.
    *   Màn hình kết quả mô phỏng Terminal chuyên nghiệp nhưng gần gũi, giúp bé dễ dàng quan sát đầu ra (`print`).
*   **Phản hồi thân thiện & Khích lệ:**
    *   **Thông báo lỗi Việt hóa:** Thay vì hiển thị những dòng thông báo lỗi tiếng Anh khô khan, hệ thống sẽ dịch và đưa ra gợi ý sửa lỗi vô cùng dễ thương (Ví dụ: lỗi lùi lề `IndentationError`, lỗi viết hoa, quên dấu ngoặc...).
    *   **Bắn pháo hoa ăn mừng 🎉:** Khi bé chạy code chính xác và hoàn thành bài tập, hiệu ứng pháo hoa giấy (confetti) sẽ bung tỏa để khích lệ tinh thần bé.
*   **Chương trình học đa cấp độ (Level 1, Level 2 & Level 3 - Tổng cộng 18 bài học):**
    *   **Cấp độ 1 (Level 1 - Nền tảng):** Lệnh print, biến, rẽ nhánh logic, vòng lặp, hàm và OOP cơ bản.
    *   **Cấp độ 2 (Level 2 - Thám hiểm):** Ép kiểu, Built-in Functions, List, Tuple, Set, Dictionary, Hàm nâng cao, Lambda & Exception Handling.
    *   **Cấp độ 3 (Level 3 - Chuyên gia):** Hàm đệ quy (Recursion), Thuật toán sắp xếp (Sorting Algorithms), Kế thừa OOP (Inheritance), Phân loại phương thức (Methods) & Dunder Methods.

---

## 📂 Cấu trúc thư mục dự án

```text
python_hocvui_level0/
├── frontend/               # Mã nguồn ứng dụng Web React + Vite
│   ├── public/             # Tài nguyên tĩnh
│   │   └── lessons/        # Bản sao các bài học phục vụ fetch API (level1, level2, level3)
│   ├── src/                # Source code React (Component, Styles, Utils)
│   │   ├── components/     # Các cột giao diện (Theory, Practice, Sidebar)
│   │   ├── utils/          # Bộ tô sáng cú pháp code Python
│   │   ├── App.jsx         # Component gốc quản lý trạng thái bài học
│   │   └── index.css       # File cấu hình giao diện & CSS tùy chỉnh phong cách trẻ em
│   ├── package.json        # Danh sách thư viện và tập lệnh frontend
│   └── vite.config.js      # Cấu hình Vite bundler
├── lessons/                # Thư mục gốc chứa nội dung bài giảng
│   ├── level1/             # Cấp độ 1: Căn bản (6 tuần học)
│   │   ├── week1_intro/
│   │   ├── week2_variables/
│   │   ├── week3_conditions/
│   │   ├── week4_loops/
│   │   ├── week5_functions/
│   │   └── week6_classes/
│   ├── level2/             # Cấp độ 2: Thám hiểm & Nâng cao (6 tuần học)
│   │   ├── week1_typecast_builtins/
│   │   ├── week2_list/
│   │   ├── week3_tuple_set/
│   │   ├── week4_dictionary/
│   │   ├── week5_functions_advanced/
│   │   └── week6_exceptions/
│   └── level3/             # Cấp độ 3: Chuyên gia (6 tuần học)
│       ├── week1_recursion/
│       ├── week2_sorting/
│       ├── week3_inheritance/
│       ├── week4_methods/
│       ├── week5_dunder/
│       └── week6_synthesis/
└── tasks/                  # Ghi chú các tác vụ phát triển hệ thống
```

> [!NOTE]
> Thư mục `lessons/` ở gốc và thư mục `frontend/public/lessons/` có cấu trúc nội dung giống nhau. Ứng dụng React trong thư mục `frontend` sẽ thực hiện tải động (`fetch`) lý thuyết từ đường dẫn `/lessons/levelX/...` trên môi trường web.

---

## 🛠️ Yêu cầu hệ thống

Trước khi bắt đầu, hãy đảm bảo máy tính của bạn đã cài đặt:
*   [Node.js](https://nodejs.org/) (Khuyến nghị phiên bản **LTS v18** trở lên)
*   Trình duyệt web hiện đại (Chrome, Edge, Firefox, Safari) hỗ trợ WebAssembly và đã bật kết nối Internet để tải thư viện Pyodide từ CDN.

---

## 🚀 Hướng dẫn cài đặt và Chạy dự án

Thực hiện theo các bước dưới đây để thiết lập dự án trên máy cục bộ của bạn:

### Bước 1: Mở thư mục dự án
Mở terminal của bạn và di chuyển vào thư mục dự án:
```bash
git clone git@github.com:ntamvl/python_hocvui_level0.git
cd python_hocvui_level0
```

### Bước 2: Di chuyển vào thư mục frontend và cài đặt thư viện
Di chuyển vào thư mục `frontend` nơi chứa mã nguồn giao diện React:
```bash
cd frontend
npm install
```

### Bước 3: Khởi chạy môi trường phát triển (Development)
Chạy lệnh sau trong thư mục `frontend` để khởi động máy chủ thử nghiệm cục bộ:
```bash
npm run dev
```

---

## 📘 Chi tiết Chương trình học theo Cấp độ

### 🟢 CẤP ĐỘ 1: CĂN BẢN (LEVEL 1)
1. **Tuần 1: Chào bạn, mình là Python!** - Lệnh `print()` & Dự án Robot chào hỏi.
2. **Tuần 2: Chiếc hộp kỳ diệu 📦** - Biến số, kiểu dữ liệu cơ bản & Dự án tính tuổi.
3. **Tuần 3: Ngã rẽ quyết định 🚦** - Điều kiện `if-elif-else` & Game đoán số.
4. **Tuần 4: Vòng lặp vui vẻ 🔁** - Vòng lặp `for`/`while` & Dự án bầu trời sao.
5. **Tuần 5: Nhà máy phép thuật 🏭** - Định nghĩa Hàm (`def`) & Máy tạo biệt danh.
6. **Tuần 6: Bản thiết kế siêu anh hùng 🦸** - Nhập môn Lớp (`class`) và Đối tượng (`object`).

### 🔵 CẤP ĐỘ 2: THÁM HIỂM (LEVEL 2)
1. **Tuần 1: Siêu công cụ 🧰** - Ép kiểu dữ liệu (`int`, `str`, `float`) & Hàm Built-in (`len`, `max`, `min`, `sum`, `round`).
2. **Tuần 2: Balo danh sách 🎒** - Cấu trúc dữ liệu `List`, chỉ số Index, phương thức `append`, `pop`, `remove`, `sort`.
3. **Tuần 3: Huy hiệu & Tọa độ 🧭** - `Tuple` (bộ cố định bất biến) & `Set` (tập hợp độc nhất không trùng).
4. **Tuần 4: Từ điển thông minh 📖** - `Dictionary` với cặp `Key: Value`, tra cứu siêu tốc, `.items()`, `.keys()`.
5. **Tuần 5: Xưởng nâng cấp ⚡** - Biến Global/Local, Tham số mặc định, `*args` linh hoạt & Biểu thức `lambda`.
6. **Tuần 6: Khiên bảo vệ 🛡️** - Bắt lỗi & Xử lý ngoại lệ (`try...except...finally`), phòng tránh crash ứng dụng.

### 🔴 CẤP ĐỘ 3: CHUYÊN GIA (LEVEL 3)
1. **Tuần 1: Búp bê Nga Matryoshka 🪆** - Hàm Đệ quy (`Recursion`), Điểm dừng (`Base Case`) & Ngăn xếp lời gọi hàm.
2. **Tuần 2: Thợ may xếp hàng 📊** - Thuật toán Sắp xếp (`Sorting Algorithms`: Bubble Sort, Selection Sort) & Hoán đổi (`Swapping`).
3. **Tuần 3: Gia đình Siêu anh hùng 🦸‍♂️** - Kế thừa trong OOP (`Inheritance`), Lớp Cha/Con, hàm `super()` & Ghi đè phương thức.
4. **Tuần 4: Tuyệt chiêu của Class 🛠️** - Phân loại phương thức (`Instance Method`, `@classmethod`, `@staticmethod`) & Decorator.
5. **Tuần 5: Phép thuật Python 🪄** - Phương thức kỳ diệu Dunder (`__init__`, `__str__`, `__len__`, `__eq__`, `__add__`) & Nạp chồng toán tử.
6. **Tuần 6: Đấu trường Huyền thoại 🏆** - Dự án Tổng hợp Level 3 (Đấu trường Quái thú Python).

---

## 🎨 Giao diện & Trải nghiệm Người dùng (UX/UI)

Giao diện trang web được tối ưu hóa cho trẻ em với:
*   Phông chữ **Outfit** hiện đại kết hợp với **Nunito** bo tròn, dễ đọc và vui nhộn.
*   Bảng màu tươi sáng, trẻ trung sử dụng các nút bấm kiểu 3D (phong cách Duolingo) phản hồi hiệu ứng ấn nổi bật.
*   Trang trí bằng nhiều biểu tượng cảm xúc (emoji) trực quan giúp bài giảng bớt khô khan và kích thích trí tò mò của trẻ.
