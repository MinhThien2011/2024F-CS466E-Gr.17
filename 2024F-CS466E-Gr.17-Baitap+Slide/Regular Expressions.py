import re

# Tìm tất cả số điện thoại hợp lệ
text = "Call me at (123) 456-7890 or 123-456-7890."
pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'

phones = re.findall(pattern, text)
print(phones)


# Bài 2: Kiểm tra địa chỉ email
# Yêu cầu: Xác định xem một chuỗi có phải là email hợp lệ không.

def is_valid_email(email):
    pattern = r'^\w+@\w+\.\w+$'
    return bool(re.match(pattern, email))

print(is_valid_email("user@example.com"))
print(is_valid_email("user.example.com"))  

# Bài 3: Tách từ trong chuỗi
# Yêu cầu: Tách các từ trong chuỗi có chứa dấu câu.

text = "Hello, world! Welcome to Python."
words = re.findall(r'\b\w+\b', text)
print(words)
    
