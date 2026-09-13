from class_student import student
# 采用面向对象的编程思想,完成教务管理系统的开发。教务管理系统可以管理在校学生的成绩信息,通过控制台菜单与用户交互,具体的功能如下:

class jiaowu:
    def __init__(self):
        self.students = []
# 1. 添加学生成绩:根据输入的学生姓名、语文成绩、数学成绩、英语成绩,记录在系统中
# 1.1 输入学生姓名、语文成绩、数学成绩、英语成绩
# 1.2 检查学生姓名是否已存在,如果学生不存在,再添加(存在则,不添加)
# 1.3 验证成绩范围(0-100分)
# 1.4 创建学生对象并添加到系统

    def add_student(self):
            name = input("请输入学生姓名:")
            for s in self.students:
                if s.name == name:
                    print("学生已存在")
                    return
            while True:
                chinese = int(input("请输入语文成绩:"))
                math = int(input("请输入数学成绩:"))
                english = int(input("请输入英语成绩:"))
                if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                    s = student(name, chinese, math, english)
                    self.students.append(s)
                    print("添加成功")
                    break
                else:
                    print("成绩范围错误,请重新输入")

# 2. 修改学生成绩:根据输入的学生姓名,修改对应的学生成绩
# 2.1 输入要修改的学生姓名
# 2.2 根据姓名查找该学生,显示该生当前成绩信息
 # 2.3 输入新的语文、数学、英语成绩
# 2.4 更新学生成绩数据
    def update_student(self):
        while True:
            name = input("请输入学生姓名:")
            for s in self.students:
                if s.name == name:
                    print(f"姓名: {s.name}|语文: {s.chinese}|数学: {s.math}|英语: {s.english}|总分: {s.total}")
                    while True:
                        chinese = int(input("请输入新的语文成绩:"))
                        math = int(input("请输入新的数学成绩:"))
                        english = int(input("请输入新的英语成绩:"))
                        if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                            s.chinese = chinese
                            s.math = math
                            s.english = english
                            print("修改成功")
                            return
                        else:
                            print("成绩范围错误,请重新输入")
            else:
                print("学生不存在")

# 3. 删除学生成绩:根据输入的学生姓名,删除对应的学生成绩
# 3.1 输入要删除的学生姓名
# 3.2 根据姓名查找该学生,显示该生当前成绩信息
# 3.3 确认删除
# 3.4 从系统中删除该学生
    def delete_student(self):
        while True:
            name=input("请输入学生姓名:")
            for s in self.students:
                if s.name == name:
                    print(f"姓名: {s.name}|语文: {s.chinese}|数学: {s.math}|英语: {s.english}|总分: {s.total}")
                    x=input("是否确认删除?(yes/no)")
                    if x=="yes":
                        self.students.remove(s)
                        print("删除成功")
                        return
                    else:
                        print("已取消删除")
                        return
            else:
                print("学生不存在")

# 4. 查询指定学生成绩:根据输入的学生姓名,查找对应的学生成绩,并输出
# 4.1 输出格式为:“姓名:张三|语文:85|数学:90|英语:88|总分:263”
    def look(self):
        name = input("请输入学生姓名:")
        for s in self.students:
            if s.name == name:
                print(f"姓名: {s.name}|语文: {s.chinese}|数学: {s.math}|英语: {s.english}|总分: {s.chinese + s.math + s.english}")
                return
        else:
            print("学生不存在")


# 5. 展示全部学生成绩:展示出系统中所有学生的成绩
    def show_all(self):
        for s in self.students:
            print(f"姓名: {s.name}|语文: {s.chinese}|数学: {s.math}|英语: {s.english}|总分: {s.chinese + s.math + s.english}")


if __name__=="__main__":
    j = jiaowu()
    while True:
        print("1. 添加学生成绩")
        print("2. 修改学生成绩")
        print("3. 删除学生成绩")
        print("4. 查询学生成绩")
        print("5. 展示全部学生成绩")
        print("6. 退出系统")

        choice = input("请输入你的选择:")
        if choice == "1":
            j.add_student()
        elif choice == "2":
            j.update_student()
        elif choice == "3":
            j.delete_student()
        elif choice == "4":
            j.look()
        elif choice == "5":
            j.show_all()
        elif choice == "6":
            print("退出系统")
            break
        else:
            print("输入错误,请重新输入")
