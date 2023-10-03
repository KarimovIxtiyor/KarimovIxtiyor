from  .models import Movie
from django.test import TestCase,Client

class TestMovieViewSet(TestCase):
     def setUp(self) -> None:
         self.movie = Movie.objects.create(title="Test Movie")
         self.movie1 = Movie.objects.create(title="alijon")
         self.client = Client()

     # def test_get_all_movie(self):
     #     response=self.client.get('/movie/')
     #     data=response.data
     #
     #     self.assertEqual(response.status_code,200)
     #     self.assertEqual(len(data),1)
     #     self.assertIsNotNone(data[0]["id"])
     #     self.assertEqual(data[0]['title'], 'Test Movie')



     def test_search(self):
         response=self.client.get('/movie/?search=Test')
         data=response.data

         # self.assertEqual((response.status_code,200))
         self.assertEqual(len(data),1)
         self.assertIsNotNone(data[0]["id"])
         self.assertEqual(data[0]['title'], 'Test Movie')



class TestMovieViewSetOrdering(TestCase):
    def setUp(self) -> None:
        self.movie1 = Movie.objects.create(title="Test Movie1",imdb=11)
        self.movie2 = Movie.objects.create(title="Test Movie2",imdb=8)
        self.movie3 = Movie.objects.create(title="Test Movie3",imdb=15)
        self.client = Client()

    def test_ordering(self):
        response = self.client.get("/movie/?ordering=-imbd")
        print(response.data)
        ordered = Movie.objects.order_by('-imdb')
        print(ordered)

        # self.assertEqual((response.status_code,200))
        # self.assertEqual(len(data), 2)
        # self.assertIsNotNone(data[0]["id"])
        # self.assertIsNotNone(data[1]["id"])
        # self.assertEqual(data[0]['title'], 'Test Movie2')
        # self.assertEqual(data[1]['title'], 'Test Movie1')
        # self.assertEqual(data[0]['imdb'], 8)
        # self.assertEqual(data[1]['imdb'], 11)
