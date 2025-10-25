from django import forms
from stores.models import Booking
from django.forms import SelectDateWidget, ValidationError
from datetime import date

class BookingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        #self.fields['store'].queryset = Store.objects.all()

        # 手動設定'store'欄位的下拉選項

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
        
    
        self.fields['toast'].choices = toast_choices

        self.fields['sub_1'].choices = sub_choices
        self.fields['sub_2'].choices = sub_choices
        self.fields['sub_3'].choices = sub_choices

        # 手動設定'time'欄位的下拉選項
        # 第一個下拉選單包含數字1-24
        hour_choices = [(str(i), str(i)) for i in range(0, 24)]

        # 第二個下拉選單包含00到55每五分鐘一個的選項
        minute_choices = [(str(i).zfill(2), str(i).zfill(2)) for i in range(0, 60, 5)]

        num_choices = [(str(i), str(i)) for i in range(1, 100)]

        self.fields['hour'] = forms.ChoiceField(choices=list(hour_choices))

        self.fields['min'] = forms.ChoiceField(choices=list(minute_choices))

        self.fields['num'] = forms.ChoiceField(choices=list(num_choices))
    
        
    

    
    class Meta:
        model = Booking     # 對應的資料

        # fields = '__all__'  # 呈現所有欄位
        # 也可以用 list 來表達要呈現的欄位
        fields = ['cus','name','store', 'toast','sub_1', 'sub_2', 'sub_3','num' ,'date', 'hour', 'min', 'tel', 'address']

        widgets = {

            'cus': forms.Select(attrs={'readonly': 'readonly'}),

            
            'name': forms.Textarea(attrs={'class': 'form-control', 'rows': 1 }),
            # 'user': forms.TextInput(                
            #     attrs={'readonly': 'readonly'}),    # 文字框
            'store': forms.Select(),                # 下拉式選單
            'toast': forms.Select(),
            'sub_1': forms.Select(), 
            'sub_2': forms.Select(), 
            'sub_3': forms.Select(), 
            'num': forms.Select(),
            
            #'date': forms.DateInput(attrs={'type': 'date'}),   # 日期選單

            'date': SelectDateWidget(),
            'hour': forms.Select(),
            'min': forms.Select(),
            'tel': forms.Textarea(attrs={'class': 'form-control', 'rows': 1 }),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 1 }),                
        }
        #exclude = ['date']

        labels = {
            'cus':'帳號',
            'name': '姓名',   #user
            'store': '分店',  #court
            'toast': '吐司種類',
            'sub_1': '配料1',
            'sub_2': '配料2',
            'sub_3': '配料3',
            'date': '預訂日期',
            'time': '預訂時間',
            'tel': '電話',
            'address': '地址', #reason
        }

    
    
   