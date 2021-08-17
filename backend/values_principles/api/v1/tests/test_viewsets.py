from rest_framework import status
from rest_framework.test import APITestCase

from django.urls import reverse


class ValuesViewSetTestCase(APITestCase):
    def test_get_value(self):
        response = self.client.get(reverse("values_principles-v1:value-list"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_value_detail(self):
        response = self.client.get(
            reverse("values_principles-v1:value-detail", kwargs={"pk": 1})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_value(self):
        data = {"title": "Test title", "description": "Test description"}

        response = self.client.post(
            reverse("values_principles-v1:value-list"), data=data
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_value(self):
        response = self.client.delete(
            reverse("values_principles-v1:value-detail", kwargs={"pk": 1})
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_patch_value(self):
        data = {"title": "Test title", "description": "Test description"}
        response = self.client.patch(
            reverse("values_principles-v1:value-detail", kwargs={"pk": 1}),
            data=data,
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class PrincipleViewSetTestCase(APITestCase):
    def test_get_principle(self):
        response = self.client.get(reverse("values_principles-v1:principle-list"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_principle_detail(self):
        response = self.client.get(
            reverse("values_principles-v1:principle-detail", kwargs={"pk": 1})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_principle(self):
        data = {"title": "Test title", "description": "Test description"}

        response = self.client.post(
            reverse("values_principles-v1:principle-list"), data=data
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_principle(self):
        response = self.client.delete(
            reverse("values_principles-v1:principle-detail", kwargs={"pk": 1})
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_patch_principle(self):
        data = {"title": "Test title", "description": "Test description"}
        response = self.client.patch(
            reverse("values_principles-v1:principle-detail", kwargs={"pk": 1}),
            data=data,
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
