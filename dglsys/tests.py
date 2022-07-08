from django.test import TestCase
from dglsys.views import MainPage
from .models import Submisyon
class HomePageTest(TestCase):
	def test_mainpage_as_seen_client(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'mainpage.html')

	def test_save_POST_request(self):
		response = self.client.post('/',{'firstn': 'jeremiah',
			'lastn': 'encluna',
			'email': 'jejeje@gmail.com',
			'sex': 'Male',
			'mgabansa': 'Philippines',
			'descript': 'Because I need to earn money'})
		
		self.assertEqual(Submisyon.objects.count(), 1)
		nData = Submisyon.objects.first()

		self.assertEqual(nData.fnam, 'jeremiah')
		self.assertEqual(nData.lnam, 'encluna')
		self.assertEqual(nData.emayl, 'jejeje@gmail.com')
		self.assertEqual(nData.seks, 'Male')
		self.assertEqual(nData.countri, 'Philippines')
		self.assertEqual(nData.descr, 'Because I need to earn money')

	def test_save_POST_redirect(self):
		response = self.client.post('/', {'firstn': 'jeremiah',
			'lastn': 'encluna',
			'email': 'jejeje@gmail.com',
			'sex': 'Male',
			'mgabansa': 'Philippines',
			'descript': 'Because I need to earn money'})

		self.assertEqual(response.status_code, 302)
		self.assertEqual(response["location"], '/')

	def test_only_saves_items_if_necessary(self):
		self.client.get('/')
		self.assertEqual(Submisyon.objects.count(), 0)

class ORMTEST(TestCase):
    def test_saving_retriv(self):
        
        ple1 = Submisyon()
        ple1.fnam = 'jeremiah'
        ple1.lnam = 'encluna'
        ple1.emayl = 'jejeje@gmail.com'
        ple1.seks = 'Male'
        ple1.countri = 'Philippines'
        ple1.descr = 'Because I need to earn money'
        ple1.save()

        ple2 = Submisyon()
        ple2.fnam = 'ste'
        ple2.lnam = 'ven'
        ple2.emayl = 'steven@gmail.com'
        ple2.seks = 'Male'
        ple2.countri = 'Philippines'
        ple2.descr = 'Because I need to earn money2'
        ple2.save()

        Submisyons = Submisyon.objects.all()
        self.assertEqual(Submisyons.count(), 2)

        sub1 = Submisyons[0]
        sub2 = Submisyons[1]

        self.assertEqual(sub1.fnam, 'jeremiah')
        self.assertEqual(sub1.lnam, 'encluna')
        self.assertEqual(sub1.emayl, 'jejeje@gmail.com')
        self.assertEqual(sub1.seks, 'Male')
        self.assertEqual(sub1.countri, 'Philippines')
        self.assertEqual(sub1.descr, 'Because I need to earn money')

        self.assertEqual(sub2.fnam, 'ste')
        self.assertEqual(sub2.lnam, 'ven')
        self.assertEqual(sub2.emayl, 'steven@gmail.com')
        self.assertEqual(sub2.seks, 'Male')
        self.assertEqual(sub2.countri, 'Philippines')
        self.assertEqual(sub2.descr, 'Because I need to earn money2')

    def test_template_display_list(self):
    	Submisyon.objects.create(fnam='la', 
    		lnam='le',
    		emayl='lale@gmail.com',
    		seks='Male',
    		countri='Philippines',
    		descr='Because' )

    	Submisyon.objects.create(fnam='ba', 
    		lnam='be',
    		emayl='babe@gmail.com',
    		seks='Male',
    		countri='Philippines',
    		descr='Because2' )

    	resp = self.client.get('/')
    	self.assertIn('Entry 1: la, le, lale@gmail.com, Male, Philippines, Because', resp.content.decode())
    	self.assertIn('Entry 2: ba, be, babe@gmail.com, Male, Philippines, Because2', resp.content.decode())
