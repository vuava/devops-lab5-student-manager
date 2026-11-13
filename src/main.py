# Query: main
# ContextLines: 1

1 result - 1 file

D:\devops-lab5-student-manager\src\student.py:
  31  # --- Test nhanh ---
  32: if __name__ == "__main__":
  33      s1 = Student("SV001", "Nguyen Van A", 20, "K20")
"""
Student Manager — DevOps Lab 5
Module: Main Application
"""
from student import Student


def main():
    """Hàm chính của ứng dụng."""
    print("=" * 50)
    print("STUDENT MANAGER — DevOps Lab 5")
    print("=" * 50)

    # Tạo danh sách sinh viên mẫu
    students = [
        Student("SV001", "Nguyen Van A", 20, "K20"),
        Student("SV002", "Tran Thi B", 21, "K20"),
        Student("SV003", "Le Van C", 19, "K21"),
    ]

    # Hiển thị danh sách
    for student in students:
        print(f"  {student}")

    print(f"\nTotal: {len(students)} students")

    def add_student():
    """Thêm sinh viên mới (tính năng add-student)"""
    print("Chức năng thêm sinh viên đang được thực thi...")

    def search_student():
    """Tìm kiếm sinh viên (tính năng search-student)"""
    print("Chức năng tìm kiếm sinh viên đang được thực thi...")


if __name__ == "__main__":
    main()
    # Sửa đổi từ nhánh conflict-test