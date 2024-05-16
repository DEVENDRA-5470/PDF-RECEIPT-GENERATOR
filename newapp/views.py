from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.shortcuts import redirect, render
from .models import Image, Student_data
from django.db.models import Q


# Create your views here.

def recents(request):
   q=request.GET.get('query_set') if request.GET.get('query_set') != None else ''
   print(str(q.count))
   print(0x000001878D2DCD70)
   stu=Student_data.objects.filter(Q(s_name__icontains=q))
   print(stu)
   context={'stu':stu ,'q':q}
   return render(request,'recents.html',context)


def dashboard(request):
    return render(request,'dashboard.html')

# def logo(request):
#     print(logo)
#     return render(request,'student_pdf.html')

def new_reg(request):
    if request.method == 'POST':
        # student detail
        s_name=request.POST.get('sn')
        s_mobile=request.POST.get('sm')
        s_email=request.POST.get('se')
        s_address=request.POST.get('sa')
        # course detail
        c_desc=request.POST.get('cd')
        c_amt=request.POST.get('ca')
        c_rec_amt=request.POST.get('cra')
        c_rec_amt_word=request.POST.get('craw')
        c_pen_amt=request.POST.get('cpa')
        c_due_date=request.POST.get('cdd')
        data=Student_data( s_name=s_name,s_mobile=s_mobile,s_email=s_email,s_address=s_address,
                          c_desc=c_desc,c_amt=c_amt,c_rec_amt=c_rec_amt,c_rec_amt_word=c_rec_amt_word,c_pen_amt=c_pen_amt,c_due_date=c_due_date)
        data.save()
        return redirect('recents')
    return render(request,'new_reg.html')

# 
def student_pdf(request,*args,**kwargs):
    pk=kwargs.get('pk')
    stu=get_object_or_404(Student_data,pk=pk)
    print(stu)
    img=Image.objects.all()
    reg=Student_data.objects.all()
    template_path = 'student_pdf.html'
    context = {'stu': stu,'img':img,'reg':reg}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Reciept.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(
       html, dest=response)
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response 