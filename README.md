# Python Học Vui - Lập trình Python Căn Bản cho Trẻ Em

Chào mừng bạn đến với **Python Học Vui**, một nền tảng học lập trình Python trực quan, sinh động và tương tác cao được thiết kế dành riêng cho trẻ em từ 12 tuổi trở lên. Dự án này giúp các bé làm quen với các khái niệm lập trình cơ bản thông qua giao diện kéo/thả, viết code và chạy trực tiếp ngay trên trình duyệt web.

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
*   **Lộ trình bài giảng 6 tuần đầy đủ:**
    *   Từ các lệnh xuất nhập cơ bản cho đến biến, rẽ nhánh logic, vòng lặp, hàm và lập trình hướng đối tượng (OOP).
    *   Mỗi tuần học đều đi kèm một dự án thực hành nhỏ thú vị (như Vẽ Robot, Game đoán số, Máy tạo biệt danh...).

---

## 📂 Cấu trúc thư mục dự án

```text
python_hocvui_level0/
├── frontend/               # Mã nguồn ứng dụng Web React + Vite
│   ├── public/             # Tài nguyên tĩnh
│   │   └── lessons/        # Bản sao các bài học phục vụ fetch API
│   ├── src/                # Source code React (Component, Styles, Utils)
│   │   ├── components/     # Các cột giao diện (Theory, Practice, Sidebar)
│   │   ├── utils/          # Bộ tô sáng cú pháp code Python
│   │   ├── App.jsx         # Component gốc quản lý trạng thái bài học
│   │   └── index.css       # File cấu hình giao diện & CSS tùy chỉnh phong cách trẻ em
│   ├── package.json        # Danh sách thư viện và tập lệnh frontend
│   └── vite.config.js      # Cấu hình Vite bundler
├── lessons/                # Thư mục gốc chứa nội dung 6 tuần học của bé
│   ├── week1_intro/        # Tuần 1: Lệnh print() & dự án Vẽ Robot
│   ├── week2_variables/    # Tuần 2: Biến & dự án Hộp quà sinh nhật
│   ├── week3_conditions/   # Tuần 3: Câu điều kiện if-else & Game đoán số
│   ├── week4_loops/        # Tuần 4: Vòng lặp & dự án Đếm sao
│   ├── week5_functions/    # Tuần 5: Hàm & Máy tạo tên biệt danh
│   └── week6_classes/      # Tuần 6: Lớp và Đối tượng & Siêu anh hùng
└── tasks/                  # Ghi chú các tác vụ phát triển hệ thống
```

> [!NOTE]
> Thư mục `lessons/` ở gốc và thư mục `frontend/public/lessons/` có cấu trúc nội dung giống nhau. Ứng dụng React trong thư mục `frontend` sẽ thực hiện tải động (`fetch`) lý thuyết từ đường dẫn `/lessons/` trên môi trường web.

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

Tập lệnh này sẽ tải tất cả các thư viện cần thiết bao gồm:
*   `react` & `react-dom` (v19)
*   `vite` (v8)
*   `bootstrap` (v5)
*   `react-markdown` (để kết xuất bài giảng từ file Markdown)
*   `canvas-confetti` (hiệu ứng pháo hoa)
*   `lucide-react` (bộ icon đẹp mắt)

### Bước 3: Khởi chạy môi trường phát triển (Development)
Chạy lệnh sau trong thư mục `frontend` để khởi động máy chủ thử nghiệm cục bộ:
```bash
npm run dev
```

Sau khi chạy thành công, terminal sẽ hiển thị địa chỉ truy cập cục bộ (thường là `http://localhost:5173`). Bạn chỉ cần copy và dán liên kết này vào trình duyệt để trải nghiệm website!

### Bước 4: Kiểm tra mã lỗi (Linting)
Bạn có thể kiểm tra lỗi code và định dạng bằng thư viện `oxlint` cực nhanh đã được cấu hình sẵn:
```bash
npm run lint
```

### Bước 5: Biên dịch dự án cho Production (Optional)
Khi dự án đã sẵn sàng để triển khai thực tế, bạn tiến hành đóng gói tối ưu mã nguồn:
```bash
npm run build
```

Các file sau khi biên dịch sẽ nằm trong thư mục `frontend/dist/`. Bạn có thể chạy thử bản build này bằng lệnh:
```bash
npm run preview
```

---

## 📘 Chi tiết Chương trình học 6 tuần của bé

1.  **Tuần 1: Chào bạn, mình là Python! 🐍**
    *   **Khái niệm:** Giới thiệu lập trình là gì, cú pháp và cách hoạt động của lệnh in dữ liệu `print()`.
    *   **Dự án:** Bé tự viết code vẽ chú Robot dễ thương trên màn hình terminal và thay đổi lời chào của Robot.
2.  **Tuần 2: Chiếc hộp kỳ diệu 📦**
    *   **Khái niệm:** Biến số là gì (khái niệm chiếc hộp chứa đồ), cách đặt tên biến, gán giá trị và các kiểu dữ liệu cơ bản (Số, Chữ, Đúng/Sai).
    *   **Dự án:** Tạo ứng dụng đếm tuổi của bé và tính xem bé sẽ bao nhiêu tuổi vào năm 2030.
3.  **Tuần 3: Ngã rẽ quyết định 🚦**
    *   **Khái niệm:** Cách đưa ra quyết định trong lập trình thông qua câu lệnh điều kiện `if`, `elif`, `else` và các phép so sánh toán học.
    *   **Dự án:** Lập trình trò chơi đoán số bí mật từ 1 đến 10, đưa ra gợi ý "lớn quá" hoặc "nhỏ quá" cho người chơi.
4.  **Tuần 4: Vòng lặp vui vẻ 🔁**
    *   **Khái niệm:** Tiết kiệm sức lao động bằng vòng lặp `for` và `while` để thực hiện lặp đi lặp lại các công việc giống nhau.
    *   **Dự án:** Vẽ một bầu trời đầy sao lấp lánh và in ra bảng cửu chương chỉ bằng vài dòng lệnh ngắn gọn.
5.  **Tuần 5: Nhà máy phép thuật 🏭**
    *   **Khái niệm:** Cách định nghĩa hàm (`def`), tham số truyền vào hàm và giá trị trả về (`return`) để tái sử dụng mã nguồn.
    *   **Dự án:** Xây dựng một "Máy chế tạo biệt danh siêu ngầu" tự động ghép tên của bé với các tính từ siêu anh hùng.
6.  **Tuần 6: Bản thiết kế siêu anh hùng 🦸**
    *   **Khái niệm:** Nhập môn Lập trình Hướng đối tượng (OOP) thông qua hình ảnh Lớp (`class`) như bản thiết kế và Đối tượng (`object`) là thực thể ngoài đời thực.
    *   **Dự án:** Bé tạo ra các siêu anh hùng khác nhau với tên gọi, siêu năng lực riêng và cho họ so tài sức mạnh với nhau.

---

## 🎨 Giao diện & Trải nghiệm Người dùng (UX/UI)

Giao diện trang web được tối ưu hóa cho trẻ em với:
*   Phông chữ **Outfit** hiện đại kết hợp với **Nunito** bo tròn, dễ đọc và vui nhộn.
*   Bảng màu tươi sáng, trẻ trung sử dụng các nút bấm kiểu 3D (phong cách Duolingo) phản hồi hiệu ứng ấn nổi bật.
*   Trang trí bằng nhiều biểu tượng cảm xúc (emoji) trực quan giúp bài giảng bớt khô khan và kích thích trí tò mò của trẻ.
