from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView

from blog.models import Article


class BlogListView(ListView):
    """Контроллер для просмотра списка статей"""
    model = Article
    extra_context = {"title": "Главная страница"}
    template_name = "article_list.html"
    context_object_name = "object_list"

    def get_queryset(self):
        # Получаем только опубликованные объекты
        return Article.objects.filter(is_published=True)


class BlogDetail(DetailView):
    """Контроллер для просмотра конкретной статьи"""
    model = Article
    template_name = "article_detail.html"
    context_object_name = "object"

    def get_object(self, queryset=None):
        """Метод подсчета количества просмотров"""
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogCreate(CreateView):
    """Контроллер для создания статьи"""
    model = Article
    fields = ["title", "description", "preview", "is_published"]
    template_name = "blog_item.html"
    success_url = reverse_lazy("blog:article_list")


class BlogUpdate(UpdateView):
    """Контроллер для редактирования статьи"""
    model = Article
    fields = ["title", "description", "preview", "is_published"]
    template_name = "blog_item.html"
    success_url = reverse_lazy("blog:article_list")


class BlogDelete(DeleteView):
    """Контроллер для удаления статьи"""
    model = Article
    template_name = "blog_confirm_delete.html"
    success_url = reverse_lazy("blog:article_list")


class ContactView(TemplateView):
    """Контроллер для страницы контакты и обратной связи"""

    template_name = "contact.html"
    extra_context = {"title": "Контакты"}

    def get_context_data(self, **kwargs):
        if self.request.method == "POST":
            name = self.request.POST.get("name")
            email = self.request.POST.get("email")
            message = self.request.POST.get("message")
            print(f"You have new message from {name}({email}): {message}")
        return super().get_context_data(**kwargs)
