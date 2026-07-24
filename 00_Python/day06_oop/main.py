# Day 6: Object-Oriented Programming (OOP)
# 请在此编写第六天的练习代码

#   - **任务 1：银行账户系统**：
#     - 设计一个 `BankAccount` 类，包含 `owner` (开户人) 和 `__balance` (私有余额) 属性。
#     - 提供 `deposit()` (存款), `withdraw()` (取款) 和 `get_balance()` (查询余额) 方法。确保取款时余额不足会打印警告或报错。

class BankAccount:
    def __init__(self, name, balance = 0):
        self.owner = name
        self.__balance = balance

    def deposit(self, Amount):
        self.__balance += Amount

    def withdraw(self, Amount):
        if self.__balance >= Amount:
            self.__balance -= Amount
        else:
            print("余额不足")

    def get_balance(self):
        print(self.__balance)
        return self.__balance


#   - **任务 2：图书管理系统**：
#     - 设计 `Book` 类（包含书名、作者、状态）和 `Library` 类（包含书单列表，提供添加图书、借阅图书、归还图书的方法）。
class Book:
    def __init__(self,name,author):
        self.name = name
        self.author = author
        self.isfree = True

    def try_borrow(self):
        if self.isfree == False:
            print(f"---> 该图书--{self.name}--不在馆内，无法借阅")
            return False
        else:
            self.isfree = False
            print(f"---> 该图书--{self.name}--借阅成功")
            return True

    def try_return(self):
        if self.isfree == False:
            self.isfree = True
            print(f"---> 该图书--{self.name}--归还成功")
            return True
        else:
            print(f"---> 该图书--{self.name}--正在馆内，无法归还")
            return False


class Library:
    def __init__(self):
        self.__booklist = []
        
    def list_book(self):
        print("------> 图书列表:")
        for n,book in enumerate(self.__booklist):
            print(f"------> 序号：{n} --- {book.name} --- {book.author} --- 图书是否可借阅：{book.isfree}")

    def add_book(self,book,isfree=True):
        if not isinstance(book,Book) :
            print("---> 添加图书失败")
        else:
            if isfree:
                pass
            else:
                book.try_borrow()
            self.__booklist.append(book)


    def borrow_book(self):
        self.list_book()
        index_int = int(input("输入借阅的图书序号(int)："))
        self.__booklist[index_int].try_borrow()


    def return_book(self):
        self.list_book()
        index_int = int(input("输入归还的图书序号(int)："))
        self.__booklist[index_int].try_return()

if __name__ == "__main__":
    print("--- Day 6 OOP Practice ---")
    # 测试任务一
    # account = BankAccount("fire")
    # account.get_balance()
    # account.withdraw(100)
    # account.deposit(120)
    # account.get_balance()
    # account.withdraw(50)
    # account.get_balance()

    # 测试任务二
    book1 = Book("数学","lxy")
    book2 = Book("物理","lhy")
    book3 = Book("英语",'xhy')
    book4 = Book("语文",'zy')
    book5 = Book("语文",'fs')

    SunLib = Library()
    SunLib.add_book("老人与海")
    SunLib.add_book(book1)
    SunLib.add_book(book2,False)
    SunLib.add_book(book3)
    SunLib.add_book(book4)    
    SunLib.add_book(book5)
    
    SunLib.borrow_book()
    # SunLib.borrow_book()
    SunLib.return_book()
    # SunLib.return_book()
    SunLib.list_book()
