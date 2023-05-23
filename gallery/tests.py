from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import date
from .models import Image


class ImageDetailViewTest(TestCase):
    def test_image_detail_view(self):
        # Create a sample Image object for testing
        image = Image.objects.create(
            title='Test Image',
            image=SimpleUploadedFile('test_image.jpg', b'content'),
            created_date=date.today(),
            age_limit=18
        )
        url = reverse('image_detail', kwargs={'pk': image.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'image_detail.html')
        self.assertEqual(response.context['image'], image)
