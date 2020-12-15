from django.shortcuts import render
# from django.http import HttpResponse
from .models import ZufangInfo
# Create your views here.


# render(request, 返回的页面，字典)
# HttpResponse('字符串')
# JsonResponse(字典)，专门生成json编码的响应，发给前端ajax
def test(request):
    zufang_info = ZufangInfo.objects.all()
    rr = []
    res = zufang_info.distinct('community')
    i = 0
    while i < 500:
        item = res[i]
        rr.append(item)
        i = i+1
    length = len(res)
    context = {
        'count': length,
        'wenzi':  rr
    }
    return render(request, 'test.html', context)
