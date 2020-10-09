from django.http import JsonResponse
from mdeditor.views import UploadView
from common.qiniuyun import QiniuYun


# 图片上传七牛云
class UploadQiniuyunView(UploadView):

    def post(self, request, *args, **kwargs):
        file = request.FILES.get("editormd-image-file", None)

        if not file:
            return JsonResponse({
                'success': 0,
                'message': "未获取到要上传的图片",
                'url': ""
            })

        # 图片上传七牛云
        qny = QiniuYun()
        imgData = file.read()
        imgUrl = qny.upload(imgData)

        return JsonResponse({
                'success': 1,
                'message': "上传成功！",
                'url': imgUrl,
            })