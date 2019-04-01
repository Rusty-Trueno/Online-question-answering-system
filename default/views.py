#coding=utf-8
from django.contrib.auth import  authenticate,login,logout
from django.shortcuts import render,render_to_response,HttpResponse
from django.contrib.auth.models import User
from question.models import ques
from hotlist.models import hotques
from answer.models import answer
from information.models import info
from reply.models import reply
from follow.models import follow
from django.contrib import auth
# Create your views here.
def mylogin(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        # 获取的表单数据与数据库进行比较
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return render(request, 'welcome.html',{'username':username})
            else:
                return render(request,'login.html',{'tip1':"用户不匹配"})
        else:
            return render(request,'login.html',{'tip2':"密码不匹配"})
    elif request.method == "GET":
        logout(request);
        return render(request,'login.html')

def regist(request):
    if request.method=="GET":
        return render(request,'regist.html')
    elif request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        email1=request.POST['mail']
        tele=request.POST['phone']
        name=request.POST['name']
        u = User.objects.filter(username=username)
        if u:
            return render(request, 'regist.html', {'tip': "已存在"})
        elif len(u) == 0:
            user = User.objects.create_user(username,email1,password)
            inform=info(user=user,name=name,tel=tele)
            inform.save()
            user.save()
            return render(request,'login.html')

def List(request):
    start=request.GET['start']
    end = request.GET['end']
    u=request.user
    queslist = ques.objects.all().order_by('-id').filter(id__range=[start,end])
    quest=ques.objects.all()
    return render(request,'list.html',{'queslist':quest,'user':u,'id':end})

def hotlist(request):
    hotqueslist = hotques.objects.all().order_by('-hotid')[0:10]
    return render(request, 'hotlist.html',{'hotqueslist': hotqueslist})

def questionlist(request):
    quename=request.GET['questionID']
    que=ques.objects.get(quename=quename)
    u=que.user
    List = map(str, range(0))
    List=list(List)
    answerlist = map(str, range(0))
    answerlist=list(answerlist)
    responselist = map(str, range(0))
    responselist=list(responselist)
    list1=answer.objects.filter(question=que).order_by('id','useraname')
    for i in range(len(list1)):
        if(list1[i].userbname==u.username):
            answerlist.append(list1[i])
    list2 = answer.objects.filter(question=que).order_by('id','userbname')
    for i in range(len(list2)):
        if(list2[i].useraname==u.username):
            responselist.append(list2[i])
    maxlen=len(answerlist)
    if(len(answerlist)>maxlen):
        maxlen=len(answerlist)
    for i in range( maxlen):
        if(i<len(answerlist)):
            List.append(answerlist[i])
        if(i<len(responselist)):
            List.append(responselist[i])
    #answerlist1 = answer.objects.filter(question=que)
    return render(request,'questionlist.html',{'answerlist':List,'que':que,'user':request.user})

def toresponse(request):
    quename=request.GET['questionID']
    que=ques.objects.get(quename=quename)
    u=que.user
    List = map(str, range(0))
    List = list(List)
    answerlist = map(str, range(0))
    answerlist = list(answerlist)
    responselist = map(str, range(0))
    responselist = list(responselist)
    list1=answer.objects.filter(question=que).order_by('id','useraname')
    for i in range(len(list1)):
        if(list1[i].userbname==u.username):
            answerlist.append(list1[i])
    list2 = answer.objects.filter(question=que).order_by('id','userbname')
    for i in range(len(list2)):
        if(list2[i].useraname==u.username):
            responselist.append(list2[i])
    maxlen=len(answerlist)
    if(len(responselist)>maxlen):
        maxlen=len(responselist)
    for i in range( maxlen):
        if(i<len(answerlist)):
            List.append(answerlist[i])
        if(i<len(responselist)):
            List.append(responselist[i])

    return render(request,'toresponse.html',{'answerlist':List,'que':que,'user':request.user})


def selfhomepage(request):
    u=request.user
    myanswer1 = answer.objects.filter(useraname=u.username).order_by('-id')
    myquestion=ques.objects.filter(user=u).order_by('-id')
    myfollow=follow.objects.filter(follower=u.username).order_by('-id')
    List = map(str, range(0))
    List=list(List)
    lista=map(str, range(0))
    lista=list(lista)
    listb=map(str, range(0))
    listb=list(listb)
    for que in myquestion:
        list1=answer.objects.filter(question=que)
        for l in list1:
            if l.userbname==u.username:
                lista.append(l)
        for l in list1:
            if l.useraname==u.username:
                listb.append(l)
        if len(lista)>len(listb):
            List.append(que)
    return  render(request,'myhomepage.html',{'myquestion':myquestion,'myanswer':myanswer1,'needresponseque':List,'myfollow':myfollow})

def selfinfor(request):
    if request.method=="POST":
        user=request.POST['user']
        nam=request.POST['name']
        te=request.POST['tel']
        u=User.objects.get(username=user)
        infor=info.objects.get(user=u)
        infor.tel=te
        infor.name=nam
        infor.user=u
        infor.save()
        queslist = ques.objects.all()
        return render(request, 'list.html', {'queslist': queslist,'user':u})
    elif request.method=="GET":
        user=request.GET['user']
        u=User.objects.get(username=user)
        infor=info.objects.get(user=u)
        return  render(request,'selfinfor.html',{'user':u,'infor':infor})

def publish(request):
    if request.method=="GET":
        return render(request,'publish.html')
    elif request.method=="POST":
        name=request.POST['firstname']
        content=request.POST['question']
        u=request.user
        que = ques(user=u, content=content, quename=name)
        que.save()
        hotq=hotques(user=u,content=content, quename=name,hotid=0)
        hotqueslist=hotques.objects.all().order_by('-hotid')
        if len(hotqueslist)==20:
            hotqueslist[19].delete()
            hotq.save()
        else:
            hotq.save()
        return render(request, 'publish.html')

def homepage(request):
    username = request.GET['queuser']
    I=request.GET['user']
    me=User.objects.get(username=I)
    u = User.objects.get(username=username)
    yourquestion = ques.objects.filter(user=u)
    youranswer = answer.objects.filter(useraname=u.username)
    return render(request, 'homepage.html', {'yourquestion': yourquestion,'youranswer': youranswer,'user':u,'me':me})

def answerlist(request):
    if request.method=="POST":
        content=request.POST['answer']
        quename=request.POST['questionID']
        question=ques.objects.get(quename=quename)
        u=question.user
        ans=answer(useraname=request.user.username,userbname=u.username,question=question,content=content)

        hotq = hotques(user=question.user, content=question.content, quename=question.quename,hotid=0)
        hotqueslist = hotques.objects.all().order_by('-hotid')
        q = hotques.objects.filter(quename=question.quename)
        if len(q) == 0:
            if len(hotqueslist) == 20:
                hotqueslist[19].delete()
                hotq.save()
            else:
                hotq.save()
        else:
            for i in range(len(hotqueslist)):
                if hotqueslist[i].quename==quename:
                    hotq.hotid =hotqueslist[i].hotid+1
                    hotqueslist[i].delete()
                    hotq.save()
                    break
        ans.save()
        return render(request,'answer.html',{'quename':quename,'user':request.user})
    elif request.method=="GET":
        quename=request.GET['question']
        return  render(request,'answer.html',{'quename':quename,'user':request.user})


def response(request):
    if request.method=="POST":
        ansusername=request.POST['user']
        content=request.POST['response']
        quename=request.POST['questionID']
        question=ques.objects.get(quename=quename)
        u=question.user
        ans=answer(useraname=request.user.username,userbname=ansusername,question=question,content=content)
        ans.save()
        return render(request,'response.html',{'quename':quename,'user':request.user})
    elif request.method=="GET":
        quename=request.GET['quename']
        ansusername=request.GET['ansusername']
        user=User.objects.get(username=ansusername)
        return  render(request,'response.html',{'quename':quename,'user':user})

def Reply(request):
    if request.method=="POST":
        user=request.POST['user']
        username=request.POST['username']
        quename=request.POST['quename']
        content=request.POST['reply']
        que=ques.objects.get(quename=quename)

        hotq = hotques(user=que.user, content=que.content, quename=que.quename)
        hotqueslist = hotques.objects.all()
        q = hotques.objects.filter(user=que.user, content=que.content, quename=que.quename)
        if len(q) == 0:
            if len(hotqueslist) == 2:
                hotqueslist.pop(0)
                hotq.save()
            else:
                hotq.save()
        else:
            hotques.objects.filter(user=que.user, content=que.content, quename=que.quename).delete()
            hotq.save()
        ans=answer.objects.filter(question=que)
        u=User.objects.get(username=user)
        anscur=ans.get(user=u)
        I=User.objects.get(username=username)
        rep=reply(user=I,answer=anscur,content=content)
        rep.save()
        replycur=reply.objects.filter(answer=anscur)
        queslist = ques.objects.all()
        return render(request,'list.html',{'replylist':replycur,'queslist':queslist})
    elif request.method=="GET":
        username=request.GET['user']
        quename=request.GET['quename']
        usercur=request.GET['username']
        u=User.objects.get(username=username)
        return render(request, 'reply.html', {'user':u, 'quename':quename, 'usercur':usercur})

def Reply1(request):
    if request.method=="POST":
        user=request.POST['user']
        username=request.POST['username']
        quename=request.POST['quename']
        content=request.POST['reply']
        que=ques.objects.get(quename=quename)

        hotq = hotques(user=que.user, content=que.content, quename=que.quename)
        hotqueslist = hotques.objects.all()
        q=hotques.objects.filter(user=que.user, content=que.content, quename=que.quename)
        if len(q)==0:
            if len(hotqueslist) == 20:
                hotqueslist.pop(0)
                hotq.save()
            else:
                 hotq.save()
        else:
            hotques.objects.filter(user=que.user, content=que.content, quename=que.quename).delete()
            hotq.save()

        ans=answer.objects.filter(question=que)
        u=User.objects.get(username=user)
        anscur=ans.get(user=u)
        I=User.objects.get(username=username)
        rep=reply(user=I,answer=anscur,content=content)
        rep.save()
        replycur=reply.objects.filter(answer=anscur)
        return render(request,'hotlist.html',{'replylist':replycur,'hotqueslist':hotqueslist})
    elif request.method=="GET":
        username=request.GET['user']
        quename=request.GET['quename']
        usercur=request.GET['username']
        u=User.objects.get(username=username)
        return render(request,'reply1.html',{'user':u,'quename':quename,'usercur':usercur})

def Follow(request):
    if request.method=="POST":
        user=request.POST['user']
        me=request.POST['me']
        u=User.objects.get(username=me)
        fo=follow(user=user,follower=me)
        fo.save()
        queslist = ques.objects.all()
        return render(request, 'list.html', {'queslist': queslist,'user':u})
    elif request.method=="GET":
        user=request.GET['user']
        u = User.objects.get(username=user)
        myanswer1 = answer.objects.filter(useraname=u.username)
        myquestion = ques.objects.filter(user=u)
        fo=follow.objects.filter(user=u.username)
        return render(request, 'myhomepage.html', {'myquestion': myquestion, 'myanswer': myanswer1,'follower':fo})
import time
def upload_image(request):
        if request.method == 'POST':
            callback = request.GET.get('CKEditorFuncNum')
            try:
                path = "media/upload/" + time.strftime("%Y%m%d%H%M%S", time.localtime())
                f = request.FILES["upload"]
                file_name = path + "_" + f.name
                des_origin_f = open(file_name, "wb+")
                for chunk in f:
                    des_origin_f.write(chunk)
                des_origin_f.close()
            except Exception as e:
                print
                'error:没找到文件或找文件失败'
            res = "<script>window.parent.CKEDITOR.tools.callFunction(" + callback + ",'/" + file_name + "', '');</script>"
            return HttpResponse(res)
        else:
            return HttpResponse("ERROR")