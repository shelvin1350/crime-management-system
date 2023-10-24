
from datetime import date
import os
import MySQLdb
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
con=MySQLdb.connect("localhost","root","","crime")
c=con.cursor()

# Create your views here.
def home(request):
    return render(request,'commonhome.html')
def adminhome(request):
    return render(request,'adminhome.html')
def userhome(request):
    return render(request,'userhome.html')
def dgphome(request):
    return render(request,'dgphome.html')
def stationhome(request):
    return render(request,'stationhome.html')
def userreg(request):
    if(request.POST):
        na=request.POST.get("name")
        addr=request.POST.get("addr")
        dob=request.POST.get("dob")
        gen=request.POST.get("rad")
        dis=request.POST.get("dis")
        email=request.POST.get("email")
        phno=request.POST.get("phno")
        uname=request.POST.get("uname")
        password=request.POST.get("pass")
        
        tr="insert into cusreg(name,addr,dob,gender,dis,email,phno,username) values('"+str(na)+"','"+str(addr)+"','"+str(dob)+"','"+str(gen)+"','"+str(dis)+"','"+str(email)+"','"+str(phno)+"','"+str(uname)+"')"
        c.execute(tr)
        print(tr)
        type="customer"
        st="not approved"
        tv="insert into login(username,password,type,status) values('"+str(uname)+"','"+str(password)+"','"+str(type)+"','"+str(st)+"')"
        c.execute(tv)
        con.commit()
       
    return render(request,'userregistration.html')
def complaint(request):
    p="select sid,name from station"
    c.execute(p)
    data=c.fetchall()
    print(data)
    if 'compsub' in request.POST:
    
        station=request.POST.get("station")
        comp=request.POST.get("comp")
        desc=request.POST.get("desc")
        
        uid=request.session["cid"]
        if request.FILES.get("f1"):
            
            myfile=request.FILES.get("f1")
            fs=FileSystemStorage()
            filename=fs.save(myfile.name , myfile)
            uploaded_file_url = fs.url(filename)
            st="not approved"
            d1=date.today()
            tv="insert into complaint(comptitle,stationid,description,file,status,date,cusid) values('"+str(comp)+"','"+str(station)+"','"+str(desc)+"','"+str(uploaded_file_url)+"','"+str(st)+"','"+str(d1)+"','"+str(uid)+"')"
            c.execute(tv)
            con.commit()
    return render(request,'customeraddcomplaints.html',{'data':data})

def login(request):
    msg=""
    if(request.POST):
        try:
            uname=request.POST.get("uname")
            pswd=request.POST.get("pswd")              
            v="select type from login where username='"+str(uname)+"' and password='"+str(pswd)+"'"
            c.execute(v)
            da=c.fetchone()
            print(v)        
            request.session["un"]=uname
            if da[0]=="admin":
                    return HttpResponseRedirect("/adminhome/")
            
            if da[0]=="customer":
                    c.execute("select name,cusid from cusreg where username='"+str(uname)+"'")
                    cc=c.fetchall()
                    request.session["name"]=cc[0][0]
                    request.session["cid"]=cc[0][1]
                    return HttpResponseRedirect("/userhome")
            if da[0]=="station":
                    c.execute("select name,sid from station where username='"+str(uname)+"'")
                    cc=c.fetchall()
                    request.session["name"]=cc[0][0]
                    request.session["cid"]=cc[0][1]
                    return HttpResponseRedirect("/stationhome")
            if da[0]=="DGP":
                    
                    request.session["name"]=uname
                    
                    return HttpResponseRedirect("/dgphome")
            con.commit()  
        except:
            msg="Invalid Username Or Password"
    return render(request,'login.html',{"msg":msg})

def stationviewcomplaint(request):
        st="pending"
        st1="not approved"
        p="select cusreg.*,complaint.* from complaint inner join cusreg on cusreg.cusid=complaint.cusid where complaint.status='"+str(st)+"' or complaint.status='"+str(st1)+"'"
        c.execute(p)
        print(p)
        data=c.fetchall()
        return render(request,'stationviewcomplaints.html',{'data':data})
def stationaddcomplaintresponse(request):
        compid=request.GET.get("id")
        st="not approved"
        p="select * from complaint  where compid='"+str(compid)+"'"
        c.execute(p)
        data=c.fetchall()
        if 'complaintsolved' in request.POST:
        
            station=request.POST.get("ctype")
            des1=request.POST.get("ipc")
            st="solved"
            vb="update complaint set status='"+str(st)+"',reply='"+str(des1)+"' where compid='"+str(station)+"'"
            c.execute(vb)
            con.commit()
            return HttpResponseRedirect("/stationviewcomplaint")

        if 'complaintpending' in request.POST:
            
            station=request.POST.get("ctype")
            des1=request.POST.get("ipc")
            st="pending"
            vb="update complaint set status='"+str(st)+"',reply='"+str(des1)+"' where compid='"+str(station)+"'"
            c.execute(vb)
            con.commit()
            return HttpResponseRedirect("/stationviewcomplaint")

        if 'complaintreject' in request.POST:
            
            station=request.POST.get("ctype")
            des1=request.POST.get("ipc")
            st="rejected"
            vb="update complaint set status='"+str(st)+"',reply='"+str(des1)+"' where compid='"+str(station)+"'"
            c.execute(vb)
            con.commit()
            return HttpResponseRedirect("/stationviewcomplaint")

        return render(request,'stationaddcomplaintstatus.html',{'data':data})
def adminapprovecomp(request):
        id=request.GET.get("id")
        
        st="Processing"
        p="update complaint set status='"+str(st)+"' where compid='"+str(id)+"'"
        c.execute(p)
        data=c.fetchall()
        return render(request,'adminviewcomplaints.html',{'data':data})

def adminviewprocessing(request):
        st="processing"
        p="select cusreg.*,complaint.* from complaint on cusreg.cusid=complaint.cusid where status='"+str(st)+"'"
        c.execute(p)
        data=c.fetchall()
        return render(request,'stationupdatecomplaint.html',{'data':data})
def adminviewfeedback(request):   
        p="select * from feedback"
        c.execute(p)
        data=c.fetchall()
        return render(request,'adminviewfeedback.html',{'data':data})

def stationreg(request):
    if(request.POST):
        na=request.POST.get("name")
        sc=request.POST.get("sc")
        addr=request.POST.get("addr")

        dis=request.POST.get("dis")
        email=request.POST.get("email")
        phno=request.POST.get("phno")
        uname=request.POST.get("uname")
        password=request.POST.get("pass")
        
        tr="insert into station(name,stationcharge,addr,district,email,phno,username) values('"+str(na)+"','"+str(sc)+"','"+str(addr)+"','"+str(dis)+"','"+str(email)+"','"+str(phno)+"','"+str(uname)+"')"
        c.execute(tr)
        print(tr)
        type="station"
        st="approved"
        tv="insert into login(username,password,type,status) values('"+str(uname)+"','"+str(password)+"','"+str(type)+"','"+str(st)+"')"
        c.execute(tv)
        con.commit()
       
    return render(request,'adminaddstation.html')
def addfeedback(request):
    p="select sid,name from station"
    c.execute(p)
    data=c.fetchall()

    return render(request,'useraddfeedback.html',{'data':data})
def userviewcomplaintstatus(request):
    cid=request.session["cid"]
    p="select * from complaint where cusid='"+str(cid)+"'"
    c.execute(p)
    data=c.fetchall()

    return render(request,'userviewcomplaintstatus.html',{'data':data})
def userviewmissingstatus(request):
    cid=request.session["cid"]
    p="select * from missingitem where cid='"+str(cid)+"'"
    c.execute(p)
    data=c.fetchall()

    return render(request,'userviewmissingstatus.html',{'data':data})
def useraddmissingitem(request):
    p="select sid,name from station"
    c.execute(p)
    data=c.fetchall()
    if(request.POST):
        na=request.POST.get("mitem")
        sc=request.POST.get("mdate")
        addr=request.POST.get("mdesc")

        dis=request.POST.get("phno")
        
        uid=request.session["cid"]
        st="not approved"
        d1=date.today()
        tv="insert into missingitem(itemname,missingdate,description,phno,cdate,cid,status) values('"+str(na)+"','"+str(sc)+"','"+str(addr)+"','"+str(dis)+"','"+str(d1)+"','"+str(uid)+"','"+str(st)+"')"
        c.execute(tv)
        con.commit()
    return render(request,'useraddmissingitem.html',{'data':data})
def stationaddcrimedetails(request):
   
    if(request.POST):
        na=request.POST.get("ctype")
        cdesc=request.POST.get("cdesc")
        date1=request.POST.get("date1")

        cloc=request.POST.get("cloc")
        ipc=request.POST.get("ipc")
        vname=request.POST.get("vname")
        sname=request.POST.get("sname")
        cloc=request.POST.get("ipc")
        uid=request.session["cid"]
        if request.FILES.get("f1"):
                
            myfile=request.FILES.get("f1")
            fs=FileSystemStorage()
            filename=fs.save(myfile.name , myfile)
            uploaded_file_url = fs.url(filename)
            #st="not approved"
            d1=date.today()
            tv="insert into crimedetails(type,description,date,location,ipc,victimname,suspectname,f1,stationid) values('"+str(na)+"','"+str(cdesc)+"','"+str(date1)+"','"+str(cloc)+"','"+str(ipc)+"','"+str(vname)+"','"+str(sname)+"','"+str(uploaded_file_url)+"','"+str(uid)+"')"
            c.execute(tv)
            con.commit()
    return render(request,'stationaddcrime.html')

def stationaddcriminaldetails(request):
       
    if(request.POST):
        na=request.POST.get("name")
        cdesc=request.POST.get("age")
        date1=request.POST.get("height")

        cloc=request.POST.get("weight")
        ipc=request.POST.get("r1")
        vname=request.POST.get("addr")
        sname=request.POST.get("phno")
        cloc=request.POST.get("nickname")
        comp=request.POST.get("complex")
        ctype=request.POST.get("crimetype")
        mo=request.POST.get("mode")
        idmark=request.POST.get("idmark")
        lang=request.POST.get("langknwn")
        crimeno=request.POST.get("crimeno")
        uid=request.session["cid"]
        if request.FILES.get("f1"):
                
            myfile=request.FILES.get("f1")
            fs=FileSystemStorage()
            filename=fs.save(myfile.name , myfile)
            uploaded_file_url = fs.url(filename)
            myfile1=request.FILES.get("f11")
            fs1=FileSystemStorage()
            filename1=fs1.save(myfile1.name , myfile)
            uploaded_file_url1 = fs1.url(filename1)
            #st="not approved"
            #d1=date.today()
            tv="insert into criminaldetails(name,age,height,weight,gender,addr,phno,nickname,complexion,crimetype,moperation,identification,photo,thumb,languages,nocrime,stationid) values('"+str(na)+"','"+str(cdesc)+"','"+str(date1)+"','"+str(cloc)+"','"+str(ipc)+"','"+str(vname)+"','"+str(sname)+"','"+str(cloc)+"','"+str(comp)+"','"+str(ctype)+"','"+str(mo)+"','"+str(idmark)+"','"+str(uploaded_file_url)+"','"+str(uploaded_file_url1)+"','"+str(lang)+"','"+str(crimeno)+"','"+str(uid)+"')"
            c.execute(tv)
            con.commit()
            os.startfile("C:\Program Files (x86)\BioEnable\BioDesk\\BioDesk.exe")
    return render(request,'stationaddcriminal.html')

def stationviewmissingitem(request):
        st="pending"
        stid=request.session["cid"]
        st1="not approved"
        p="select cusreg.*,missingitem.* from missingitem inner join cusreg on cusreg.cusid=missingitem.cid where missingitem.sid='"+str(stid)+"' and missingitem.status='"+str(st)+"' or missingitem.status='"+str(st1)+"'"
        c.execute(p)
        print(p)
        data=c.fetchall()
        return render(request,'stationviewmissingdetails.html',{'data':data})

def adminsendfilestation(request):
        
        # stid=request.session["cid"]
        # st1="not approved"
    p="select sid,name from station"
    c.execute(p)
    print(p)
    data=c.fetchall()
    if 'subfile' in request.POST:
        st=request.POST.get("dis")
        sub=request.POST.get("sub")
        da=date.today()
        if request.FILES.get("f1"):
                
            myfile=request.FILES.get("f1")
            fs=FileSystemStorage()
            filename=fs.save(myfile.name , myfile)
            uploaded_file_url = fs.url(filename)
            fu="admin"
            tv="insert into filesendstation(fromuser,touser,sub,file,date) values('"+str(fu)+"','"+str(st)+"','"+str(sub)+"','"+str(uploaded_file_url)+"','"+str(da)+"')"
            c.execute(tv)
            con.commit()
            return HttpResponseRedirect("/adminsendfilestation/")

    return render(request,'adminstationsendfile.html ',{'data':data})

def stationsendfilestation(request):
        
        # stid=request.session["cid"]
        # st1="not approved"
    p="select sid,name from station"
    c.execute(p)
    print(p)
    sid=request.session["cid"]
    data=c.fetchall()
    if 'subfile' in request.POST:
        st=request.POST.get("dis")
        sub=request.POST.get("sub")
        da=date.today()
        if request.FILES.get("f1"):
                
            myfile=request.FILES.get("f1")
            fs=FileSystemStorage()
            filename=fs.save(myfile.name , myfile)
            uploaded_file_url = fs.url(filename)
            tv="insert into filesendstation(fromuser,touser,sub,file,date) values('"+str(sid)+"','"+str(st)+"','"+str(sub)+"','"+str(uploaded_file_url)+"','"+str(da)+"')"
            c.execute(tv)
            con.commit()
            return HttpResponseRedirect("/stationsendfilestation/")

    return render(request,'stationsendfilestation.html ',{'data':data})

def adminviewfiles(request):
        
        # stid=request.session["cid"]
        # st1="not approved"
    ad="admin"
    p="select filesendstation.*,station.name from station inner join filesendstation on filesendstation.fromuser=station.sid where filesendstation.touser='"+str(ad)+"'"
    c.execute(p)
    print(p)
    data=c.fetchall()
    
    return render(request,'adminviewreceivedfile.html ',{'data':data})

def stationviewfiles(request):
        
        # stid=request.session["cid"]
        # st1="not approved"
    ad=request.session["cid"]
    p="select filesendstation.*,station.name from station inner join filesendstation on filesendstation.fromuser=station.sid where filesendstation.touser='"+str(ad)+"'"
    c.execute(p)
    print(p)
    data=c.fetchall()
    
    return render(request,'stationviewreceivedfile.html ',{'data':data})

def dgpviewcriminal(request):
    if 'searchcr' in request.POST:   
        cr=request.POST.get("search")
        # ad=request.session["cid"]
        
        p="select * from criminaldetails where name='"+str(cr)+"' or nickname='"+str(cr)+"' or moperation='"+str(cr)+"' or identification='"+str(cr)+"'"
        c.execute(p)
        print(p)
        data=c.fetchall()
        return render(request,'dgpsearchcriminal.html ',{'data':data})
    return render(request,'dgpsearchcriminal.html ')

def dgpviewcrime(request):
    
    # cr=request.POST.get("search")
    # ad=request.session["cid"]
    
    p="select * from crimedetails"
    c.execute(p)
    print(p)
    data=c.fetchall()
    
    return render(request,'dgpsearchcrime.html ',{'data':data})

def dgpsendfilestation(request):
        
        # stid=request.session["cid"]
        # st1="not approved"
    p="select sid,name from station"
    c.execute(p)
    print(p)
    data=c.fetchall()
    if 'subfile' in request.POST:
        st=request.POST.get("dis")
        sub=request.POST.get("sub")
        da=date.today()
        if request.FILES.get("f1"):
                
            myfile=request.FILES.get("f1")
            fs=FileSystemStorage()
            filename=fs.save(myfile.name , myfile)
            uploaded_file_url = fs.url(filename)
            fu=request.session["cid"]
            tv="insert into filesendstation(fromuser,touser,sub,file,date) values('"+str(fu)+"','"+str(st)+"','"+str(sub)+"','"+str(uploaded_file_url)+"','"+str(da)+"')"
            c.execute(tv)
            con.commit()
            return HttpResponseRedirect("/dgpsendfilestation/")

    return render(request,'dgpsendfile.html ',{'data':data})

def stationaddwantedlist(request):
        
        # stid=request.session["cid"]
        # st1="not approved"
    p="select criminalid,name from criminaldetails"
    c.execute(p)
    print(p)
    data=c.fetchall()
    print(data)
    if 'subf' in request.POST:
        st=request.POST.get("dis")
        sub=request.POST.get("descr")
        fu=request.session["cid"]
        tv="insert into wantedlist(criminalid,description,stationid) values('"+str(st)+"','"+str(sub)+"','"+str(fu)+"')"
        c.execute(tv)
        con.commit()
        return HttpResponseRedirect("/stationaddwantedlist/")

    return render(request,'stationaddwantedlist.html ',{'data':data})

def stationviewcrime(request):
    
    # cr=request.POST.get("search")
    # ad=request.session["cid"]
    
    p="select * from crimedetails"
    c.execute(p)
    print(p)
    data=c.fetchall()
    
    return render(request,'stationviewcrime.html ',{'data':data})

def stationviewcriminal(request):
    if 'searchcr' in request.POST:   
        cr=request.POST.get("search")
        # ad=request.session["cid"]
        
        p="select * from criminaldetails where name='"+str(cr)+"' or nickname='"+str(cr)+"' or moperation='"+str(cr)+"' or identification='"+str(cr)+"'"
        c.execute(p)
        print(p)
        data=c.fetchall()
        return render(request,'stationviewcriminal.html ',{'data':data})
    return render(request,'stationviewcriminal.html ')

def userviewwantedlist(request):
    
    # cr=request.POST.get("search")
    # ad=request.session["cid"]
    
    p="select criminaldetails.*,wantedlist.* from criminaldetails inner join wantedlist on criminaldetails.criminalid=wantedlist.criminalid"
    c.execute(p)
    print(p)
    data=c.fetchall()
    
    return render(request,'userviewwantedlist.html ',{'data':data})

def stationaddmissingresponse(request):
        compid=request.GET.get("id")
        st="not approved"
        p="select * from missingitem  where missid='"+str(compid)+"'"
        c.execute(p)
        data=c.fetchall()
        if 'missingitemsolved' in request.POST:
        
            station=request.POST.get("ctype")
            des1=request.POST.get("ipc")
            st="solved"
            vb="update missingitem set status='"+str(st)+"',reply='"+str(des1)+"' where missid='"+str(station)+"'"
            c.execute(vb)
            con.commit()
            return HttpResponseRedirect("/stationviewcomplaint")

        if 'missingitempending' in request.POST:
            
            station=request.POST.get("ctype")
            des1=request.POST.get("ipc")
            st="pending"
            vb="update missingitem set status='"+str(st)+"',reply='"+str(des1)+"' where missid='"+str(station)+"'"
            c.execute(vb)
            con.commit()
            return HttpResponseRedirect("/stationviewcomplaint")

        if 'missingitemreject' in request.POST:
            
            station=request.POST.get("ctype")
            des1=request.POST.get("ipc")
            st="rejected"
            vb="update missingitem set status='"+str(st)+"',reply='"+str(des1)+"' where missid='"+str(station)+"'"
            c.execute(vb)
            con.commit()
            return HttpResponseRedirect("/stationviewcomplaint")

        return render(request,'stationaddmissingstatus.html',{'data':data})
def adminviewcriminal(request):
    if 'searchcr' in request.POST:   
        cr=request.POST.get("search")
        # ad=request.session["cid"]
        
        p="select * from criminaldetails where name='"+str(cr)+"' or nickname='"+str(cr)+"' or moperation='"+str(cr)+"' or identification='"+str(cr)+"'"
        c.execute(p)
        print(p)
        data=c.fetchall()
        return render(request,'adminsearchcriminal.html ',{'data':data})
    return render(request,'adminsearchcriminal.html ')

def adminaddauthority(request):
    if 'sub' in request.POST:   
        cr=request.POST.get("dis")
        un=request.POST.get("uname")
        pw=request.POST.get("pass")
        st="approved"
        # ad=request.session["cid"]
        
        p="insert into login(username,password,type,status) values('"+str(un)+"','"+str(pw)+"','"+str(cr)+"','"+str(st)+"')"
        c.execute(p)
        print(p)
        con.commit()
        return render(request,'adminaddauthority.html ')
    return render(request,'adminaddauthority.html ')