from django.shortcuts import render

def list(request):
    return render(request, 'document/list.html')

def form(request):
    if request.GET:
        if request.GET.id:
            return  render(request, 'member/form.html')
        else:
            return render(request, 'member/form.html')
    else:
        pass

def store(request):
    if request.POST:
        if request.POST.id:
            return render(request, 'member/form.html')
        else:
            return render(request, 'member/form.html')
    else:
        pass

def search(request):
    pass

def pdf(request):
    return render(request, 'document/pdf.html')