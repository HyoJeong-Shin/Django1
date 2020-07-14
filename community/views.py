from django.shortcuts import render
from community.forms import *
# Create your views here.
def write(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid(): #form에 있는 데이터가 유효하다면,
            form.save() # 데이터베이스에 필드가 저장됨
    else:
        form = Form()
    return render(request, 'write.html', {'form':form})

def list(request):
    articleList = Article.objects.all() # Article이라는 데베 테이블에 있는 모든 컬럼을 가져와 articleList에 저장함
    return render(request, 'list.html', {'articleList':articleList})

def view(request, num='1'):
    article = Article.objects.get(id=num)   # article이라는 모델의 object중에 아이템을 가져옴 # 모델 생성시 모델에 대한 아이디 생성됨
    return render(request, 'view.html', {'article':article})