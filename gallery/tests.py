from django.test import TestCase, RequestFactory
from django.urls import reverse
from .models import Image
from .views import image_detail
# Create your tests here.


class ImageDetail(TestCase):
    def setUp(self) -> None:
        self.image = Image.objects.create(name='Test Image', url='test.jpg')

    def test_image_detail(self):
        factory = RequestFactory()
        request = factory.get(reverse('image_detail', args=[self.image.pk]))

        # Call the view function
        response = image_detail(request, self.image.pk)
        self.assertEqual(response.status_code, 200)

        # Check if the rendered template is correct
        self.assertTemplateUsed(response, 'image_detail.html')

        # Check if the image object is passed to the template context
        self.assertEqual(response.context['image'], self.image)