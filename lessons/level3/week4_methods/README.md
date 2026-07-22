# Tuần 4 (Cấp 3): Tuyệt Chiêu Của Class 🛠️ (Các Loại Phương Thức - Methods)

Trong Lập trình hướng đối tượng với Python, không phải tất cả phương thức trong một Lớp đều hoạt động giống nhau! Có 3 loại "tuyệt chiêu" (phương thức) mà mỗi chuyên gia Python đều cần làm chủ. Tuần này chúng ta sẽ cùng khám phá chúng!

---

## 🌟 Mục tiêu cần đạt
* Phân biệt rõ ràng 3 loại phương thức: **Instance Method**, **Class Method** và **Static Method**.
* Nắm vững cú pháp sử dụng **Decorator `@classmethod`** (với tham số `cls`) và **Decorator `@staticmethod`**.
* Biết cách dùng Class Method làm *Factory Method* (xưởng tạo đối tượng linh hoạt) hoặc quản lý trạng thái chung.
* Sử dụng Static Method cho các hàm tiện ích tính toán không phụ thuộc vào trạng thái đối tượng.

---

## 🔑 Khái niệm cốt lõi

### 1. Instance Method (Phương thức Đối Tượng) 👤
* Là phương thức quen thuộc nhất mà bạn đã học.
* **Tham số đầu tiên**: Bắt buộc là `self` (đại diện cho chính đối tượng đó).
* **Công dụng**: Đọc và thay đổi dữ liệu riêng của từng đối tượng.
```python
def gioi_thieu(self):
    print(f"Tôi là Robot {self.ten}")
```

### 2. Class Method (Phương thức Cấp Lớp) 🏭
* Được đánh dấu bằng ký hiệu `@classmethod`.
* **Tham số đầu tiên**: Bắt buộc là `cls` (đại diện cho toàn bộ Lớp, chứ không phải một đối tượng riêng lẻ).
* **Công dụng**: Tác động lên các biến cấp Lớp (Class attributes) hoặc dùng làm xưởng sản xuất đối tượng (Factory Method).
```python
class Robot:
    so_luong_robot = 0 # Biến cấp Lớp (dùng chung cho tất cả Robot)

    @classmethod
    def dem_so_luong(cls):
        print(f"🏭 Tổng số Robot đã xuất xưởng: {cls.so_luong_robot}")

    @classmethod
    def tao_robot_sieu_toc(cls, ten):
        # Factory method: tạo và trả về một robot mới với tốc độ tối đa
        robot = cls(ten, toc_do=100)
        return robot
```

### 3. Static Method (Phương thức Tĩnh) 🧮
* Được đánh dấu bằng ký hiệu `@staticmethod`.
* **Tham số**: **KHÔNG cần `self` cũng KHÔNG cần `cls`**.
* **Công dụng**: Đóng vai trò như một hàm tiện ích độc lập nằm bên trong Lớp để gom nhóm mã nguồn gọn gàng.
```python
class Robot:
    @staticmethod
    def doi_km_sang_m(km):
        return km * 1000 # Hàm tính toán tiện ích thuần túy
```

> [!TIP]
> **Bảng tóm tắt nhanh**:
> | Loại phương thức | Decorator | Tham số đầu | Tác động lên |
> | :--- | :--- | :--- | :--- |
> | **Instance Method** | *(Không có)* | `self` | Thuộc tính riêng của đối tượng |
> | **Class Method** | `@classmethod` | `cls` | Biến chung của Lớp / Tạo đối tượng mới |
> | **Static Method** | `@staticmethod` | *(Không có)* | Hàm tiện ích độc lập |

---

## 🤖 Dự án thực hành: Xưởng Sản Xuất Robot Tự Động!
Bên cột phải là ứng dụng Xưởng Robot áp dụng đủ 3 loại phương thức để đếm số lượng xuất xưởng, tạo nhanh Robot mẫu và đổi đơn vị đo.
Hãy nhấn nút **"Bấm để Chạy thử! 🚀"** để xem xưởng vận hành nhé!

### 💡 Thử thách cho bạn:
1. Tạo thêm một Class Method tên `tao_robot_khong_lo(cls, ten)` cài đặt sẵn máu `1000 HP` và sức mạnh `200`.
2. Tạo thử một Robot khổng lồ từ phương thức trên và kiểm tra chỉ số!
