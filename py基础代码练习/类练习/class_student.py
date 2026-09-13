


class student:
    def __init__(self,name,chinese,math,english):

        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

# 输出格式为:“姓名:张三|语文:85|数学:90|英语:88|总分:263”
    def __str__(self):
        return f"姓名:{self.name}|语文:{self.chinese}|数学:{self.math}|英语:{self.english}|总分:{self.chinese+self.math+self.english}"

    #修改学生成绩
    def update(self, chinese=None, math=None, english=None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
             self.english = english

if __name__ == "__main__":
    s = student("小明", 11, 22, 33)
    print(s)
