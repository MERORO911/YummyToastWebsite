from django.db import models
# User
from django.contrib.auth.models import User
from django.utils import timezone



# timezone
from datetime import date

class Store(models.Model):  
    STORE_TYPE = [     # 使用 list 來做列舉
        # 第一個 "bana" 表示真實儲存的資料，第二個表示呈現的字
        ("台北", "台北"),
        ("新北", "新北"),
        ("基隆", "基隆"),
        ("桃園", "桃園"),
        ("新竹", "新竹"),
        ("苗栗", "苗栗"),
        ("台中", "台中"),
        ("彰化", "彰化"),
        ("南投", "南投"),
        ("雲林", "雲林"),
        ("嘉義", "嘉義"),
        ("台南", "台南"),
        ("高雄", "高雄"),
        ("屏東", "屏東"),
        ("宜蘭", "宜蘭"),
        ("花蓮", "花蓮"),
        ("台東", "台東"),
        
        
    ]   
    storename = models.CharField(max_length=100)
    city = models.CharField(max_length=20, choices=STORE_TYPE)
    ''' 列舉型態用 choices = 來設定 '''
    address = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)



    def __str__(self):
        return f"{self.city} {self.storename}"  

'''
    預借場館的紀錄，包含誰借的，借哪一個場館及日期
'''

class Booking(models.Model):

    toast_choices = [
            ("蜂蜜麥片吐司", "蜂蜜麥片吐司 $45"),
            ("白吐司", "白吐司 $20"),
            ("全麥吐司", "全麥吐司 $40"),
            ("多穀吐司", "多穀吐司 $35"),
            ("法式麵包", "法式麵包 $30"),
            ("全素吐司", "全素吐司 $20"),
        ]

    sub_choices = [
            ("草莓","草莓 +15"),
            ("酪梨", "酪梨 +15"),
            ("起司", "起司 +10"),
            ("培根", "培根 +15"),
            ("雞肉", "雞肉 +15"),
            ("紅豆", "紅豆 +5"),
            ("抹茶", "抹茶 +5"),
            ("蛋", "蛋 +10"),
            ("半熟蛋", "半熟蛋 +10"),
            ("玉米", "玉米 +5"),
            ("火腿", "火腿 +15"),
            ("洋蔥", "洋蔥 +5"),
            ("番茄", "番茄 +5"),
            ("高麗菜", "高麗菜 +10"),
            ("鮪魚", "鮪魚 +5"),
            ("豬肉", "豬肉 +10"),
            ("牛肉", "牛肉 +25"),
            ("馬鈴薯沙拉", "馬鈴薯沙拉 +5"),
            ("香蕉", "香蕉 +5"),
            ("巧克力醬", "巧克力醬 +5"),
            ("草莓果醬", "草莓果醬 +5"),
            ("藍莓果醬", "藍莓果醬 +5"),
            ("棉花糖", "棉花糖 +10"),
            ("芋泥", "芋泥 +5"),
            ("蜂蜜", "蜂蜜 +5"),
            ("奶油", "奶油 +5"),
        ]
    hour_choices = [(str(i), str(i)) for i in range(0, 24)]

        # 第二個下拉選單包含00到55每五分鐘一個的選項
    minute_choices = [(str(i).zfill(2), str(i).zfill(2)) for i in range(0, 60, 5)]

    cus = models.ForeignKey(User, models.CASCADE)
    name = models.CharField(max_length=10, null=True)
    toast = models.CharField(max_length=255, choices=toast_choices, default='1')
    sub_1 = models.CharField(max_length=255, choices=sub_choices)
    sub_2 = models.CharField(max_length=255, choices=sub_choices)
    sub_3 = models.CharField(max_length=255, choices=sub_choices)
    num = models.CharField(max_length=10,blank=True )
    store = models.ForeignKey(Store, models.CASCADE)
    date = models.DateField(default=timezone.now)
    hour = models.CharField(max_length=255, choices=hour_choices)
    min = models.CharField(max_length=255, choices=minute_choices)
    tel = models.IntegerField(null=True)
    address = models.CharField(max_length=100)
    
    
    
    
    

    

    

    def __str__(self):
        return f"{self.cus}, {self.store}, {self.date}"
