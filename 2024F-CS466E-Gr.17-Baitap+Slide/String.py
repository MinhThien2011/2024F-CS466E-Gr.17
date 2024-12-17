# Bài Tập Đếm Nguyên Âm và Phụ Âm
# input: Tôi yêu lập trình Python
# output: ?
# - nguyên âm:
# - phụ âm: 
user_input = input("Nhập một câu: ").lower()
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"

vowel_count = sum(1 for char in user_input if char in vowels)
consonant_count = sum(1 for char in user_input if char in consonants)

print(f"Số nguyên âm: {vowel_count}")
print(f"Số phụ âm: {consonant_count}")