from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from . import models
from . import forms
import pymysql
import hashlib
import json
# Create your views here.

def hash_code(s, salt='mysite'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()
def homepage(request):

    return redirect("/news/")
def homepage_staff(request):
    return redirect("/news_staff/")

def homepage_manager(request):
    return redirect("/news/")

def apply(request):

    return  render(request,'club.html')

def register(request):

    return render(request,'register.html')



def login(request):
    if request.session.get('is_login', None):  #已经在线了

        return redirect("/homepage/")
    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        message = "Please check the content you have written！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            position = login_form.cleaned_data['position']
            try:
                user = models.Staff.objects.get(sname=username)
                if user.password == hash_code(password):  # 哈希值和数据库内的值进行比对
                    request.session['is_login'] = True
                    request.session['user_id'] = user.sid
                    request.session['user_name'] = user.sname
                    request.session['user_position'] = position
                  #  return redirect('homepage.html')
                    if position == '职工':
                        return redirect("/homepage_staff/")
                    else:
                        return redirect("/homepage_manager/")
                else:
                    message = "Wrong Password！"
            except:
                message = "Not Exist Client！"
    login_form = forms.UserForm()
    return render(request, 'log.html', locals())



def register_staff(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/homepage/")
    if request.method == "POST":
        registerform_staff = forms.RegisterForm_staff(request.POST)
        message = "请检查输入内容是否正确"
        if registerform_staff.is_valid():  # 获取数据
            id = registerform_staff.cleaned_data['id']
            username = registerform_staff.cleaned_data['username']
            password1 = registerform_staff.cleaned_data['password1']
            password2 = registerform_staff.cleaned_data['password2']
            age = registerform_staff.cleaned_data['age']
            gender = registerform_staff.cleaned_data['gender']

            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入密码不一致!"
                return render(request, 'register_staff.html', locals())
            else:
                same_id_user = models.Staff.objects.filter(sid= id)
                if same_id_user:  # 用户名唯一
                    message = '职工编号已存在，请更换职工编号再次输入!'
                    return render(request, 'register_staff.html', locals())

                # 当一切都OK的情况下，创建新用户

                new_user = models.Staff()
                new_user.sid = id
                new_user.sname = username
                new_user.password = hash_code(password1)  # 使用加密密码
                new_user.age = age
                new_user.gender = gender
                new_user.save()

                return redirect('/login/')  # 自动跳转到登录页面
    registerform_staff = forms.RegisterForm_staff()
    return render(request, 'register_staff.html', locals())

def register_club(request):
    if request.method == "POST":
        registerform_club = forms.RegisterForm_club(request.POST)
        message = "请检查输入内容是否正确"
        if registerform_club.is_valid():  # 获取数据
            id = registerform_club.cleaned_data['id']
            clubname = registerform_club.cleaned_data['clubname']
            manager = registerform_club.cleaned_data['manager']
            location = registerform_club.cleaned_data['location']

            dt = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='newclub',charset='utf8')
            cur = dt.cursor()
            cur.execute("select 姓名 from staff_staff where 姓名='%s'"%(manager))
            name_manager = cur.fetchall()


            same_name_club = models.Club.objects.filter(cname = clubname)
            same_id_club = models.Club.objects.filter(cid=id)
            if same_id_club:  # 用户名唯一
                message = '社团编号已存在，请更换社团编号!'
                return render(request, 'register_club.html', locals())
            elif same_name_club:
                    message = '社团名称已被使用，请更换名称'
                    return render(request, 'register_club.html', locals())
            elif len(name_manager) == 0:
                    message = '社团负责人必须为已注册的职工'
                    return render(request,'register_club.html',locals())
               # 当一切都OK的情况下，创建新用户

            new_club = models.Club()
            new_club.cid = id
            new_club.cname = clubname
            new_club.manager = manager
            new_club.location = location
            new_club.save()
            cur.close()
            dt.commit()
            dt.close()
            return redirect('/login/')  # 自动跳转到登录页面
    registerform_club = forms.RegisterForm_club()

    return render(request, 'register_club.html', locals())

def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/login/")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/login/")


def club(request):
    if not request.session.get('is_login', None):
        return redirect("/login/")
    position = request.session['user_position']
    if request.session['user_position'] == '职工':
        dt = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='newclub', charset='utf8')
        cur=dt.cursor()
        cur.execute("select 编号,名称 from staff_club ")
        cur.close()
        dt.close()
        data=cur.fetchall()
        return render(request,'club_staff.html',{'data':json.dumps(data),'position':position})
    else:
        dt = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='newclub', charset='utf8')
        cur=dt.cursor()
        manager = request.session['user_name']
        cur.execute("select 编号,名称 from staff_club where 负责人 = '%s'"%(manager))
        cur.close()
        dt.close()
        data=cur.fetchall()
        return render(request,'club_manager.html',{'data':json.dumps(data),'position':position})

@csrf_exempt
def StockTrading(request):
    if not request.session.get('is_login', None):
        return redirect("/login/")
    position = request.session['user_position']
    if request.session['user_position'] == '职工':
        sname = request.session['user_name']
        sid = request.session['user_id']
        error_msg=""
        q=request.GET.get("code")
        if not q:
            pass
        else:
            dt = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='newclub', charset='utf8')

            cur2 = dt.cursor()
            cur2.execute("select 名称 from staff_club where 编号='%s'"%(q))
            c_name = cur2.fetchall()

            new_apply = models.Apply()
            new_apply.staffname = sname
            new_apply.staffid = sid
            new_apply.clubname = c_name[0][0]
            new_apply.clubid = q
            new_apply.status = '待审核'
            new_apply.save()

            dt.commit()
            cur = dt.cursor()
            cur.execute("select 社团编号,申请社团,申请时间,状态 from staff_apply where 申请人编号='%s'"%(sid))
            data = cur.fetchall()
            cur.close()
            cur2.close()
            dt.close()

            trandata = []
            for item in data:
                dictdata = {}
                dictdata['cid']=item[0]
                dictdata['cname'] = item[1]
                dictdata['a_time'] = item[2]
                dictdata['status'] = item[3]
                trandata.append(dictdata)

            return render(request,'result_staff.html',{'error_msg':error_msg,'trandata':trandata,'position':position})
    else:
        sname = request.session['user_name']
        sid = request.session['user_id']
        error_msg=""
        q=request.GET.get("code")
        if not q:
            pass
        else:
            dt = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='newclub', charset='utf8')
            #cur = dt.cursor()
            cur2 = dt.cursor()
            cur2.execute("select 申请人,申请人编号,申请时间 from staff_apply where 社团编号 = %s and 状态 = '待审核'"%(q))
            data = cur2.fetchall()
            trandata = []
            for item in data:
                dictdata = {}
                dictdata['sname']=item[0]
                dictdata['sid'] = item[1]
                dictdata['a_time'] = item[2]
                trandata.append(dictdata)
            dt.close()
            post_list = models.Club.objects.filter(cid__iexact=q)
            if (len(post_list) != 0):
                cname = post_list[0].cname
                cid = post_list[0].cid
                return render(request, 'result_manager.html',{'error_msg': error_msg, 'cname': cname, 'cid': cid,'trandata':trandata,'position':position})

def agree(request):
    dt = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='newclub', charset='utf8')

    cid = request.POST.get("cid")

    for item in models.Apply.objects.all():

        choose = request.POST.get(item.staffid)

        if item.clubid == cid:   #所申请社团
            if choose == '1':    #同意申请
                cur = dt.cursor()
                cur.execute("update staff_apply set 状态='已通过' where 申请人编号= %s and 社团编号 = %s"%(item.staffid,cid))
                dt.commit()
                cur.close()
            elif choose == '2':
                cur = dt.cursor()
                cur.execute("update staff_apply set 状态='未通过' where 申请人编号= %s and 社团编号 = %s"%(item.staffid,cid))
                dt.commit()
                cur.close()
    return redirect("/club/")

def activity(request):
    pass

def create_activity(request):
    if not request.session.get('is_login', None):

        return redirect("/login/")
    if request.method == "POST":
        activity_form = forms.ActivityForm(request.POST)

        message = "请检查输入内容是否正确"
        if activity_form.is_valid():  # 获取数据
            id = activity_form.cleaned_data['id']
            a_name = activity_form.cleaned_data['aname']
            c_name = activity_form.cleaned_data['cname']
            m_anager = activity_form.cleaned_data['manager']
            l_ocation = activity_form.cleaned_data['location']
            d_ate = activity_form.cleaned_data['date']
            n_ump = activity_form.cleaned_data['nump']

            dt = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='newclub',charset='utf8')
            cur = dt.cursor()
            cur.execute("select 姓名 from staff_staff where 姓名='%s'"%(m_anager))
            name_manager = cur.fetchall()

            cur2 = dt.cursor()
            cur2.execute("select 名称 from staff_club where 名称='%s'"%(c_name))
            name_club = cur2.fetchall()


            same_name_activity = models.Activity.objects.filter(aname = a_name)
            same_id_activity = models.Activity.objects.filter(aid=id)

            if same_id_activity:  # 用户名唯一
                message = '活动编号已存在，请更换活动编号!'
                return render(request, 'create_activity.html', locals())
            elif same_name_activity:
                    message = '活动名称已被使用，请更换名称'
                    return render(request, 'create_activity.html', locals())
            elif len(name_manager) == 0:
                    message = '活动负责人必须为已注册的职工'
                    return render(request,'create_activity.html',locals())
            elif len(name_club) == 0:
                message = '未找到相关社团，请重新输入社团'
                return render(request,'create_activity.html',locals())
               # 当一切都OK的情况下，创建新活动

            new_activity = models.Activity()
            new_activity.aid = id
            new_activity.aname = a_name
            new_activity.cname = c_name
            new_activity.manager = m_anager
            new_activity.location = l_ocation
            new_activity.date = d_ate
            new_activity.nump = n_ump
            new_activity.save()
            cur.close()
            dt.commit()
            dt.close()
            return redirect('/homepage_manager/')  # 自动跳转到登录页面
    activity_form = forms.ActivityForm()

    return render(request, 'create_activity.html', locals())


def show_club(request):
    dt = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='newclub', charset='utf8')
    cur = dt.cursor()
    manager = request.session['user_name']
    cur.execute("select 编号,名称 from staff_club where 负责人 = '%s'" % (manager))
    cur.close()
    dt.close()
    data = cur.fetchall()
    trandata = []
    for item in data:
        dictdata = {}
        dictdata['cid'] = item[0]
        dictdata['cname'] = item[1]
       # dictdata['a_time'] = item[2]
        trandata.append(dictdata)
    return render(request, 'manager_club.html', {'trandata':trandata})

def activity_mag(request):

    dt = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='newclub', charset='utf8')
    # cur2 = dt.cursor()
    # cur2.execute("select 名称 from staff_club where 负责人='%s'"%(manager))
    # cname = cur2.fetchall()
    for item in models.Club.objects.all():
        p_val = request.POST.get(item.cname)
        if p_val == '1':
            cur = dt.cursor()
            cur.execute("select 编号,名称,负责人,活动时间,活动地点 from staff_activity where  社团= '%s'" % (item.cname))

            data = cur.fetchall()
            cur.close()
            dt.close()

            trandata = []
            for item in data:
                dictdata = {}
                dictdata['aid'] = item[0]
                dictdata['aname'] = item[1]
                dictdata['manager'] = item[2]
                dictdata['date'] = item[3]
                dictdata['location'] = item[4]
                trandata.append(dictdata)

            return render(request, 'activity_mag.html', {'trandata': trandata})


def delete_activity(request):
    dt = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='newclub', charset='utf8')
    for item in models.Activity.objects.all():
        p_val = request.POST.get(item.aid)
        if p_val == '2':
            cur = dt.cursor()
            cur.execute("delete from staff_activity where 编号='%s'" % (item.aid))
            dt.commit()
            cur.close()
            dt.close()
    return redirect("/show_club/")

def show_all_act(request):
    dt = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='newclub', charset='utf8')
    cur = dt.cursor()
    cur.execute("select * from staff_activity")
    data = cur.fetchall()
    cur.close()
    dt.close()

    trandata = []
    for item in data:
        dictdata = {}
        dictdata['aid'] = item[0]
        dictdata['aname'] = item[1]
        dictdata['manager'] = item[2]
        dictdata['location'] = item[3]
        dictdata['date'] = item[4]
        dictdata['max_pp'] = item[5]
        dictdata['cname'] = item[6]
        trandata.append(dictdata)
    return render(request, 'join.html', {'trandata': trandata})

def join(request):
    dt = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='newclub', charset='utf8')

    for item in models.Activity.objects.all():
        choose = request.POST.get(item.aid)
        if choose == '1':
            s_id = models.Staff.objects.get(sid=request.session['user_id'])
            a_id = models.Activity.objects.get(aid=item.aid)
            models.Join.objects.create(sid=s_id,aid=a_id)
    return redirect("/join_mag/")

def join_mag(request):
    dt = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='newclub', charset='utf8')
    cur = dt.cursor()
    cur.execute("select * from staff_join where 职工号='%s'"%(request.session['user_id']))
    data = cur.fetchall()
    cur.close()


    trandata = []
    for item in data:
        cur = dt.cursor()
        cur.execute("select * from staff_activity where 编号='%s'" % (item[2]))
        data2 = cur.fetchall()
        trandata2 = []
        for item2 in data2:
            dictdata = {}
            dictdata['aid'] = item2[0]
            dictdata['aname'] = item2[1]
            dictdata['manager'] = item2[2]
            dictdata['location'] = item2[3]
            dictdata['date'] = item2[4]
            dictdata['max_pp'] = item2[5]
            dictdata['cname'] = item2[6]
            trandata2.append(dictdata)
        trandata.append(trandata2)
    return render(request, 'join_mag.html', {'trandata': trandata})

def club_img(request):
    dt = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='newclub', charset='utf8')
    sid = request.session['user_id']
    cur = dt.cursor()
    cur.execute("select 社团编号,申请社团,申请时间,状态 from staff_apply where 申请人编号='%s'" % (sid))
    data = cur.fetchall()
    cur.close()
    dt.close()

    trandata = []
    for item in data:
        dictdata = {}
        dictdata['cid'] = item[0]
        dictdata['cname'] = item[1]
        dictdata['a_time'] = item[2]
        dictdata['status'] = item[3]
        trandata.append(dictdata)

    return render(request, 'club_img.html', {'trandata': trandata})


def club_sum(request):
    dt = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='newclub', charset='utf8')
    manager = request.session['user_name']

    cur = dt.cursor()
    cur.execute("select 编号,名称,活动地点 from staff_club where 负责人 = '%s'" % (manager))
    data = cur.fetchall()


    trandata = []
    for item in data:
        cur2 = dt.cursor()
        cur2.execute("select distinct 申请人编号,申请社团 from staff_apply where 状态='已通过' and 社团编号='%s'"%(item[0]))
        data2 = cur2.fetchall()

        num_member = len(data2)
        dictdata = {}
        dictdata['cid'] = item[0]
        dictdata['cname'] = item[1]
        dictdata['num_member'] = num_member
        dictdata['location'] = item[2]
        trandata.append(dictdata)
        cur2.close()

    return render(request, 'club_sum.html', {'trandata':trandata})

def search(request):
    q = request.GET.get('q')
    error_msg = ''
    if not q:
        error_msg = 'Please enter a key word'
        return render(request, 'search_activity.html', {'error_msg': error_msg})

    post_list = models.Activity.objects.filter(aname__icontains=q)   #名称中包含 "abc"，且abc不区分大小写

    trandata=[]
    if(len(post_list)!=0):
        for a in post_list:
            dictdata={}
            dictdata['aid']=a.aid
            dictdata['aname'] = a.aname
            dictdata['cname'] = a.cname
            dictdata['manager'] = a.manager
            dictdata['max_pp'] = a.nump
            dictdata['date'] = a.date
            dictdata['location'] = a.location
            trandata.append(dictdata)
    else:
        error_msg = '没有此活动'
    return render(request, 'search_activity.html',{'error_msg': error_msg,'trandata':trandata})


def fabu_activity(request):
    dt = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='newclub', charset='utf8')
    for item in models.Activity.objects.all():
        p_val = request.POST.get(item.aid)
        if p_val == '1':
            #
            # cur2 = dt.cursor()
            # cur2.execute("select 名称,社团,活动时间 from staff_activity where 编号 ='%s'"%(item.aid))
            # data = cur2.fetchall()
            # cur2.close()
            # print(data)
            cur = dt.cursor()
            cur.execute("insert into staff_news(活动名称, 社团, 活动时间) values ('%s','%s','%s')" % (item.aname,item.cname,item.date))
            dt.commit()
            cur.close()
            dt.close()

    return redirect("/news/")


def news(request):
    dt = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='newclub', charset='utf8')

    cur = dt.cursor()
    cur.execute("select * from staff_news")
    data = cur.fetchall()
    cur.close()
    dt.close()

    trandata = []
    for item in data:
        dictdata = {}
        dictdata['aname'] = item[1]
        dictdata['cname'] = item[2]
        dictdata['date'] = item[3]
        trandata.append(dictdata)
    return render(request, 'homepage_manager.html', {'trandata': trandata})



def news_staff(request):
    dt = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='newclub', charset='utf8')

    cur = dt.cursor()
    cur.execute("select * from staff_news")
    data = cur.fetchall()
    cur.close()
    dt.close()

    trandata = []
    for item in data:
        dictdata = {}
        dictdata['aname'] = item[1]
        dictdata['cname'] = item[2]
        dictdata['date'] = item[3]
        trandata.append(dictdata)
    return render(request, 'homepage_staff.html', {'trandata': trandata})