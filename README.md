# 2024F-CS466E-Gr.17

## 🚀 Giới thiệu dự án
Dự án **2024F-CS466E-Gr.17** bao gồm các file bài tập, slide, cùng với đồ án nhóm dự án web được triển khai với các công nghệ chính như **Flask** và **Django**.

## 📂 Cấu trúc thư mục
```
2024F-CS466E-Gr.17/
│
├── 2024F-CS466E-Gr.17-Baitap+Slide/
│   ├── 2024F-CS466E-Gr.17-Baitap3/    # Bài tập 3
│   │   └── UserManagementSystem/      # Ứng dụng Flask quản lý người dùng
│   │       ├── app.py                 # File chính chạy ứng dụng Flask
│   │       ├── models.py              # Định nghĩa model dữ liệu
│   │       ├── routes.py              # Định nghĩa các routes Flask
│   │       ├── requirements.txt       # File cài đặt thư viện cần thiết
│   │       ├── templates/             # Thư mục chứa các file HTML
│   │       └── static/                # Thư mục chứa các file CSS, JS
│   │
│   ├── 2024F-CS466E-Gr.17-Baitap4/    # Bài tập 4 về xử lý đa luồng và đơn luồng
│   │   ├── multi-Thread/              # Server đa luồng
│   │   └── single-threaded/           # Server đơn luồng
│   │
│   └── 2024F-CS466E-Gr.17-Slide/      # Tài liệu slide cho bài tập
│
├── 2024F-CS466E-Gr.17-Project/        # Folder đồ án nhóm
│   ├── báo cáo/
│   │   ├── Group_17_CS-466E.docx      # Báo cáo chi tiết đồ án nhóm
│   │   └── Group_17_CS-466E.pptx      # Slide thuyết trình đồ án nhóm
│   │
│   └── DJANGOPROJECT/                 # Ứng dụng Django
│       ├── manage.py                  # File khởi chạy chính của Django
│       ├── db.sqlite3                 # Database SQLite
│       ├── myBlog/                    # App chính của dự án Django
│       │   ├── blog/                  # Module quản lý nội dung blog
│       │   ├── users/                 # Module quản lý người dùng
│       ├── Scripts/                   # Các script cần thiết
│       └── venv/                      # Môi trường ảo Python
│
└── README.md                         # File mô tả
```

---

## 🖥️ User Management System
### **Giới thiệu**
Ứng dụng **User Management System** sử dụng **Flask** để:
- Quản lý người dùng: đăng ký, đăng nhập, chỉnh sửa thông tin.
- Xác thực 2 yếu tố.
- Phân quyền người dùng và quản lý quyền truy cập.
- Giao diện được chia thành phần **Admin Dashboard** và **User Dashboard**.
### **Công nghệ sử dụng**
- **Python + Flask**
- **Jinja2** (Template Engine)
- **SQLite**
- **HTML/CSS/JavaScript**

-------------------------

## 🌐 Django Project
### **Giới thiệu**
Ứng dụng **Django Project** được phát triển trên **Django Framework**, hỗ trợ:
- Quản lý người dùng (CRUD).
- Phân quyền và xác thực.
- Quản lý nội dung blog.

### **Công nghệ sử dụng**
- **Python + Django**
- **SQLite**
- **HTML/CSS**

-------------------------

## 🛠️ Cài đặt và khởi chạy
### **1. Khởi chạy User Management System (Flask):**
```bash
cd 2024F-CS466E-Gr.17-Baitap3/UserManagementSystem
pip install -r requirements.txt

# User Management System

## Yêu cầu cài đặt
1. Python 3.11 hoặc mới hơn.
2. MySQL Server (phiên bản 8.0 trở lên).
3. Các thư viện Python: Flask, SQLAlchemy, pymysql, cryptography.

#Khởi chạy ứng dụng:
-Tạo cơ sở dữ liệu và tài khoản:
   - Kết nối MySQL:
     ```bash
     mysql -u root -p
     ```
   - Thực hiện các lệnh SQL:
     ```sql
     CREATE DATABASE user_management;
     CREATE USER 'admin'@'localhost' IDENTIFIED BY 'admin_password';
     GRANT ALL PRIVILEGES ON user_management.* TO 'admin'@'localhost';
     FLUSH PRIVILEGES;
     ```

-Cấu hình kết nối:
   - Chỉnh sửa biến `SQLALCHEMY_DATABASE_URI` trong file `app.py`:
     ```python
     SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:admin_password@localhost/user_management'
     ```

-Cài đặt thư viện Python:
   ```bash
   pip install -r requirements.txt
python app.py
```

### **2. Khởi chạy Django Project:**
```bash
cd 2024F-CS466E-Gr.17-Project/DJANGOPROJECT
python -m venv env
.\env\Scripts\activate
pip install django
pip install crispy-forms
pip install crispy-bootstrap5
pip install django-tinymce
cd myBlog
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
-------------------------

## 📊 Báo cáo và Tài liệu
- **Group_17_CS-466E.docx**: Báo cáo chi tiết đồ án nhóm.
- **Group_17_CS-466E.pptx**: Slide trình bày đồ án nhóm.

-------------------------

## 👨‍💻 Thành viên nhóm
- **1.Đỗ Nguyễn Minh Quân - 27211248290**
- **2.Phạm Minh Thiện - 27211202495**

-------------------------

## 📞 Liên hệ
Mọi thắc mắc vui lòng liên hệ qua email: **minhthienp50@gmail.com**
