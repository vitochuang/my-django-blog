from django.shortcuts import render

def index(request):
    posts = []  # 🌟 關鍵：這裡暫時給它一個空列表，完美繞過資料庫連線！
    return render(request, 'blog/index.html', {'posts': posts})
