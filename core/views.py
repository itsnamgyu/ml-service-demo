from PIL import Image
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from torchvision import transforms

from core.models import Post
from ml.models import load_default_model


classifier = load_default_model()
print(classifier.fc._parameters)
transform = transforms.Compose([
    transforms.Resize([256, 256]),
    transforms.ToTensor(),
])


class HomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        return context


class PostCreateView(CreateView):
    template_name = "core/post_create.html"
    success_url = reverse_lazy("home")

    model = Post
    fields = ["image"]

    def form_valid(self, form):
        self.object: Post = form.save(commit=False)
        image = Image.open(self.object.image)
        image.save("image.jpeg")
        image = transform(image)
        image = image.unsqueeze(0)

        prediction = classifier(image)
        prediction_index = prediction.argmax()

        print(prediction)

        if prediction_index == 0:
            self.object.prediction = Post.CAT
        else:
            self.object.prediction = Post.DOG

        self.object.save()

        return super().form_valid(form)

