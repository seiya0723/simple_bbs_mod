from django.shortcuts import render,redirect
from django.views import View

from .models import Topic
from .forms import TopicForm

import datetime

class BbsView(View):

    def get(self, request, *args, **kwargs):

        topics  = Topic.objects.all().order_by("-dt")
        #topics  = Topic.objects.all().order_by("name")
        
        #filterで条件を指定して絞り込みができる。
        #topics  = Topic.objects.filter(id=10).order_by("-dt")
        #topics  = Topic.objects.filter(name="AAA").order_by("-dt")

        """
        topics = [ {"id": "1", "comment": "あああああ"},
                   {"id": "2", "comment": "こんにちは"},
                   {"id": "3", "comment": "Hello"},
                   {"id": "4", "comment": "あああ"},
                   ]
        """

        if "search" in request.GET:
            print(request.GET["search"],"で検索されました")


        context = { "topics":topics }

        return render(request,"bbs/index.html",context)

    def post(self, request, *args, **kwargs):

        form    = TopicForm(request.POST)

        if form.is_valid():
            print("バリデーションOK")
            form.save()
        else:
            print("バリデーションNG")


        """
        if "comment" in request.POST:
            print(request.POST["comment"])

            posted  = Topic( comment=request.POST["comment"] )
            posted.save()

        else:
            print("commentがありません")
        """

        #POST文は基本的にredirectをreturnする。
        #"app_name:name"の文字列を
        #return render(request, "bbs/index.html")
        return redirect("bbs:index")

index   = BbsView.as_view()


class BbsEditView(View):
    
    def get(self, request, pk, *args, **kwargs):

        topic   = Topic.objects.filter(id=pk).first()
        context = { "topic":topic }

        return render(request, "bbs/edit.html", context)

    def post(self, request, pk, *args, **kwargs):

        #対象のトピックを特定
        topic   = Topic.objects.filter(id=pk).first()

        #instanceに特定したトピックを指定、これで編集ができる。
        form    = TopicForm(request.POST,instance=topic)
        
        if form.is_valid():
            print("バリデーションOK")
            form.save()

        return redirect("bbs:index")

edit    = BbsEditView.as_view()


class BbsDeleteView(View):

    def post(self, request, pk, *args, **kwargs):

        #対象のトピックを特定して削除する。
        topic   = Topic.objects.filter(id=pk).first()
        topic.delete()

        return redirect("bbs:index")

delete  = BbsDeleteView.as_view()

