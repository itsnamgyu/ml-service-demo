from PIL import Image
from django.http import JsonResponse, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, CreateView
from torchvision import transforms

from core.models import Post
from ml.models import load_default_model

classifier = load_default_model()
transform = transforms.Compose([
    transforms.Resize([256, 256]),
    transforms.ToTensor(),
])


def predict(image):
    image = Image.open(image).convert("RGB")
    image = transform(image)
    image = image.unsqueeze(0)
    prediction = classifier(image)
    prediction_index = prediction.argmax()
    return prediction_index


class HomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        return context


class PostCreateView(TemplateView):
    template_name = "core/post_create.html"
    success_url = reverse_lazy("home")

    def post(self, request, *args, **kwargs):
        image = request.FILES.get("image")
        if image is None:
            return HttpResponseBadRequest()
        prediction_index = predict(image)  # run ml model

        post = Post(image=image)
        if prediction_index == 0:
            post.prediction = Post.CAT
        else:
            post.prediction = Post.DOG
        post.save()

        return HttpResponseRedirect(self.success_url)


class AppView(TemplateView):
    template_name = "index.html"  # app/build/index.html


class PostListApiView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        posts = map(lambda post: {
            "id": post.id,
            "prediction": post.prediction,
            "image_url": post.image.url,
        }, posts)
        posts = list(posts)
        return JsonResponse(posts, safe=False)

    def post(self, request, *args, **kwargs):
        return HttpResponseNotFound()


@method_decorator(csrf_exempt, name='dispatch')
class PostCreateApiView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponseNotFound()

    def post(self, request, *args, **kwargs):
        image = request.FILES.get("image")
        if image is None:
            return HttpResponseBadRequest()

        self.object = Post(image=image)
        prediction_index = predict(self.object.image)  # run ml model

        post = Post(image=image)
        if prediction_index == 0:
            post.prediction = Post.CAT
        else:
            post.prediction = Post.DOG
        post.save()

        return JsonResponse({"success": True})
