#!/usr/bin/env python

from .models import University
from .forms import UniversityForm
from django.test import TestCase, Client
from django.urls import reverse

class UniversityModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        University.objects.create(name='Test University', description='Just a test')

    def test_name_label(self):
        university = University.objects.get(id=1)
        field_label = university._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_description_content(self):
        university = University.objects.get(id=1)
        expected_object_description = f'{university.description}'
        self.assertEquals(expected_object_description, 'Just a test')





class UniversityListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_universities = 5
        for university_num in range(number_of_universities):
            University.objects.create(
                name=f'University {university_num}',
                description=f'Sample description {university_num}',
            )

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/universities/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('university_list'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('university_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'university/university_list.html')

    def setUpTestData(cls):
        number_of_universities = 5
        for university_num in range(number_of_universities):
            University.objects.create(
                name=f'University {university_num}',
                description=f'Sample description {university_num}',
                price=10000 + university_num,
                address=f'Address {university_num}',
                telephone=f'123456{university_num}',
                email=f'info{university_num}@university.edu',
                website=f'http://university{university_num}.edu'
            )

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/universities/')
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('university_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'university/university_list.html')




class UniversityFormTest(TestCase):

    def test_university_form_valid_data(self):
        form = UniversityForm(data={
            'name': "Test University",
            'description': "Just a test",
            'price': 1000,
            # інші поля
        })
        self.assertTrue(form.is_valid())

    def test_university_form_no_data(self):
        form = UniversityForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)




class UniversityModelTest2(TestCase):

    @classmethod
    def setUpTestData(cls):
        University.objects.create(
            name='Dnipro University',
            description='A leading university in Dnipro',
            price=10000,
            address='Some address',
            telephone='123456789',
            email='info@dnipro-uni.edu',
            website='http://dnipro-uni.edu'
        )

    def test_university_content(self):
        university = University.objects.get(id=1)
        expected_object_name = f'{university.name}'
        expected_object_description = f'{university.description}'
        expected_object_price = university.price
        self.assertEquals(expected_object_name, 'Dnipro University')
        self.assertEquals(expected_object_description, 'A leading university in Dnipro')
        self.assertEquals(expected_object_price, 10000)



class UniversityDetailViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        University.objects.create(
            name='Test University',
            description='A test university',
            price=20000,
            address='Test address',
            telephone='987654321',
            email='contact@testuniversity.com',
            website='http://testuniversity.com'
        )

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/universities/1/')
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('university_detail', args=[1]))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'university/university_detail.html')

    def test_view_displays_correct_university_info(self):
        resp = self.client.get(reverse('university_detail', args=[1]))
        self.assertContains(resp, 'Test University')
        self.assertContains(resp, 'A test university')

class UniversityFormTest2(TestCase):

    def test_university_form_valid_data(self):
        form_data = {
            'name': 'New University',
            'description': 'A new university',
            'price': 25000,
            'address': 'New address',
            'telephone': '123123123',
            'email': 'info@newuniversity.com',
            'website': 'http://newuniversity.com'
        }
        form = UniversityForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_university_form_no_data(self):
        form = UniversityForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 7)



class UniversityCreateViewTest(TestCase):

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('university_new'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('university_new'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'university/university_form.html')

    def test_form_error_for_blank_fields(self):
        resp = self.client.post(reverse('university_new'), {})
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.context['form'].errors)


class UniversityUpdateViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        University.objects.create(name='Old University', description='Old description')

    def test_view_url_accessible_by_name(self):
        university = University.objects.get(name='Old University')
        resp = self.client.get(reverse('university_edit', kwargs={'pk': university.pk}))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        university = University.objects.get(name='Old University')
        resp = self.client.get(reverse('university_edit', kwargs={'pk': university.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'university/university_form.html')


class UniversityDeleteViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        University.objects.create(name='Delete University', description='To be deleted')

    def test_view_url_accessible_by_name(self):
        university = University.objects.get(name='Delete University')
        resp = self.client.get(reverse('university_delete', kwargs={'pk': university.pk}))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        university = University.objects.get(name='Delete University')
        resp = self.client.get(reverse('university_delete', kwargs={'pk': university.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'university/university_confirm_delete.html')

if __name__ == '__main__':
    print(UniversityDeleteViewTest)
    print(UniversityUpdateViewTest)
    print(UniversityCreateViewTest)
    print(UniversityFormTest)
    print(UniversityFormTest2)
    print(UniversityDetailViewTest)
    print(UniversityModelTest)
    print(UniversityModelTest2)
    print(UniversityListViewTest)
