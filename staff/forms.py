from django import forms



class UserForm(forms.Form):
    positions = (('职工','职工'),('社团负责人','社团负责人'))
    username = forms.CharField(label="Username", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Password", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    position = forms.ChoiceField(label="Position", choices = positions)

class RegisterForm_staff(forms.Form):
    genders = (
        ('男', "男"),
        ('女', "女"),
    )
    id = forms.CharField(label="Id",max_length=32, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label="Username", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Password", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Repeat Password", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}));
    #email = forms.EmailField(label="E-mail", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(label="Age",widget=forms.NumberInput(attrs={'class':'form-control'}))
    gender = forms.ChoiceField(label='Gender', choices=genders)

class RegisterForm_club(forms.Form):

    id = forms.CharField(label="Id",max_length=32, widget=forms.TextInput(attrs={'class': 'form-control'}))
    clubname = forms.CharField(label="Clubname", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    manager = forms.CharField(label='Manager',max_length=32,widget=forms.TextInput(attrs={'class':'form-control'}))
    location = forms.CharField(label='Location',max_length=128,widget=forms.TextInput(attrs={'class':'form-control'}))

class ActivityForm(forms.Form):
    id = forms.CharField(label="活动编号",max_length=32,widget=forms.TextInput(attrs={'class':'form-control'}))
    aname = forms.CharField(label="活动名称",max_length=64,widget=forms.TextInput(attrs={'class':'form-control'}))
    cname = forms.CharField(label="社团",max_length=128,widget=forms.TextInput(attrs={'class':'form-control'}))
    manager = forms.CharField(label="负责人",max_length=64,widget=forms.TextInput(attrs={'class':'form-control'}))
    location = forms.CharField(label='活动地点',max_length=128,widget=forms.TextInput(attrs={'class':'form-control'}))
    date = forms.DateTimeField(label='活动时间',widget=forms.DateTimeInput(attrs={'class':'form-control'}))
    nump = forms.IntegerField(label='人数',widget=forms.NumberInput(attrs={'class':'form-control'}))

    # aid = models.CharField(db_column='编号',max_length=32, primary_key=True)
    # aname = models.CharField(db_column='名称',max_length=64)
    # cname = models.ForeignKey('Club',on_delete=models.DO_NOTHING,db_column='社团')
    # manager = models.CharField(db_column='负责人',max_length=64)
    # location = models.CharField(db_column='活动地点',max_length=128)
    # date = models.CharField(db_column='活动时间',max_length=32)
    # nump = models.IntegerField(db_column='人数')