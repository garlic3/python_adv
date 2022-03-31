import sys  # 하드웨어 접근 모듈
from PyQt5.QtWidgets import * # 파이큐티 관련 모듈
from PyQt5.QtCore import * # 타이머 관련 모듈 
from PyQt5 import uic  # ui 관련 모듈
import pybithumb

tickers = ["BTC","ETH","XRP","ADA"]
form_class = uic.loadUiType("day4.ui")[0]  # 파이큐티로 만든 폼 불러오기

class MyWindow(QMainWindow, form_class):   # MyWindow 클래스를 상속받음 
    def __init__(self):                 # 생성자로 창 생성
        super().__init__()              # 부모의 생성자를 이용
        self.setupUi(self)              # ui 창 생성     
        timer = QTimer(self)
        timer.start(1000)
        timer.timeout.connect(self.timeout)


    def timeout(self):
        for i, ticker in enumerate(tickers):
            item = QTableWidgetItem(ticker)
            self.tableWidget.setItem(i,0, item)
            price = QTableWidgetItem(str(pybithumb.get_current_price(ticker)))
            self.tableWidget.setItem(i,1, price)

        
            

app = QApplication(sys.argv)    # 파이썬은 원래 인터프리터로 한줄씩 실행후 창이 꺼져야 정상
window = MyWindow()             # 윈도우 클래스로 객체 생성
window.show()                   # 생성한 객체를 통해 창을 보여주기 
app.exec_()                     # 윈도우 창이 열린 상태로 계속 대기 유지 
