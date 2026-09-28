from django.test import TestCase
from .models import Student


class PageTests(TestCase):
	def test_home_page_renders(self):
		response = self.client.get('/')

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Student Project')

	def test_student_page_renders(self):
		response = self.client.get('/student/')

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Students')

	def test_student_can_be_added(self):
		response = self.client.post('/student/', {
			'name': 'Mira Patel',
			'email': 'mira@example.com',
			'course': 'Python',
		})

		self.assertRedirects(response, '/student/')
		self.assertTrue(Student.objects.filter(name='Mira Patel').exists())

	def test_student_name_is_required(self):
		response = self.client.post('/student/', {'name': '   '})

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Please enter a student name.')
		self.assertEqual(Student.objects.count(), 0)
