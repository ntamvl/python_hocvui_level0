# Kế hoạch triển khai: Tô sáng cú pháp Python (Syntax Highlighting)

Dự án hiện tại sử dụng một ô `<textarea>` đơn giản không có màu sắc cú pháp cho code Python, và các khối code trong phần lý thuyết (cột bên trái) cũng chưa được tô màu. Điều này làm bé khó phân biệt các thành phần như từ khóa, chuỗi văn bản, số hay hàm số.

Tôi đề xuất triển khai tính năng tô sáng cú pháp (syntax highlighting) đồng bộ cho cả hai phần bằng giải pháp tự xây dựng siêu nhẹ (custom regex-based tokenizer) nhằm tránh các vấn đề xung đột phiên bản thư viện với React 19 và giữ ứng dụng hoạt động mượt mà.

---

## Các thay đổi đề xuất

### 1. [NEW] [pythonHighlighter.js](file:///Users/tamnguyen/Projects/giaoduc/laptrinh_python_canban_v1.2/frontend/src/utils/pythonHighlighter.js)
Tạo file tiện ích chứa hàm phân tích cú pháp Python bằng biểu thức chính quy (regular expressions). Hàm này sẽ:
* Nhận vào chuỗi code thô (raw Python code).
* Chuyển đổi và escape các ký tự đặc biệt HTML (`<`, `>`, `&`).
* Tìm và bọc các thành phần cú pháp Python (từ khóa, chuỗi, bình luận, số, boolean, hàm dựng sẵn) bằng các thẻ `<span>` với các lớp CSS tương ứng.

### 2. [MODIFY] [PracticeColumn.jsx](file:///Users/tamnguyen/Projects/giaoduc/laptrinh_python_canban_v1.2/frontend/src/components/PracticeColumn.jsx)
Cải tiến giao diện soạn thảo:
* Đè một phần tử `<pre><code>` chứa code đã được tô sáng ngay bên dưới `<textarea>` trong suốt.
* Đồng bộ hóa chính xác vị trí cuộn (scroll), cỡ chữ (font size), kiểu chữ (font family) và giãn dòng giữa `<textarea>` và `<pre><code>`.
* Sử dụng thuộc tính `pointer-events: none` trên lớp phủ tô sáng để mọi tương tác chuột (click, chọn văn bản, nhập liệu) vẫn đi thẳng vào `<textarea>`.

### 3. [MODIFY] [TheoryColumn.jsx](file:///Users/tamnguyen/Projects/giaoduc/laptrinh_python_canban_v1.2/frontend/src/components/TheoryColumn.jsx)
Cải tiến hiển thị lý thuyết:
* Định nghĩa một component tùy chỉnh cho phần tử `code` trong `ReactMarkdown`.
* Khi gặp khối code Python (`language-python`), chúng ta sẽ gọi hàm tô sáng cú pháp của chúng ta để hiển thị trực quan sinh động thay vì một khối chữ trắng đen nhàm chán.

### 4. [MODIFY] [index.css](file:///Users/tamnguyen/Projects/giaoduc/laptrinh_python_canban_v1.2/frontend/src/index.css)
* Thêm các quy tắc CSS định cấu trúc lớp phủ của trình soạn thảo.
* Định nghĩa hệ thống màu sắc tươi sáng, ngộ nghĩnh và dễ nhìn cho bé (ví dụ: bình luận màu xám nghiêng, từ khóa màu tím, chuỗi màu cam, hàm số màu xanh dương, số màu xanh lá...).

---

## Kế hoạch kiểm thử & xác minh (Verification Plan)

### Kiểm thử thủ công (Manual Verification)
1. Chạy ứng dụng bằng lệnh `npm run dev` trong thư mục `frontend`.
2. Kiểm tra cột lý thuyết bên trái: Các khối mã ví dụ Python có hiển thị màu sắc đầy đủ không.
3. Kiểm tra cột thực hành bên phải:
   * Khi gõ mã Python, cú pháp có tự động đổi màu theo thời gian thực không.
   * Chức năng cuộn (scroll) lên xuống có đồng bộ hoàn hảo giữa cột số dòng, mã hiển thị và con trỏ gõ chữ không.
   * Thử nghiệm gõ phím Tab, nút xóa, nút xuống dòng xem có khớp ký tự 1-1 giữa phần gõ chữ và phần tô màu không.
   * Nhấn nút chạy thử (Run Code) xem kết quả hiển thị có chính xác không.
