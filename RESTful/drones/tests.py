from django.urls import reverse
from django.utils.http import urlencode
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from drones import views
from drones.models import Pilot, DroneCategory


class DroneCategoryTests(APITestCase):

    def post_drone_category(self, name):
        print('1')
        url = reverse('drones:' + views.DroneCategoryList.name)
        print(url)
        print('2')
        data = {'name': name}
        response = self.client.post(url, data, format='json')
        return response

    def test_post_and_get_drone_category(self):
        """ Ensure that we can create a new DroneCategory and retrieve it"""
        new_drone_category_name = 'Hexacopter'
        response = self.post_drone_category(new_drone_category_name)
        print(f'pk {DroneCategory.objects.get().pk}')
        assert response.status_code == status.HTTP_201_CREATED
        assert DroneCategory.objects.count() == 1
        assert DroneCategory.objects.get().name == new_drone_category_name

    def test_post_existing_drone_category_name(self):
        """ Ensure that we can`t create DroneCategory with an existing name"""
        url = reverse('drones:' + views.DroneCategoryList.name)
        new_drone_category_name = 'Duplicated Copter'
        data = {'name': new_drone_category_name}
        response1 = self.post_drone_category(new_drone_category_name)
        assert response1.status_code == status.HTTP_201_CREATED
        response2 = self.post_drone_category(new_drone_category_name)
        assert response2.status_code == status.HTTP_400_BAD_REQUEST

    def test_filter_drone_category_by_name(self):
        """ Ensure than we can filter a drone caregory by name """
        drone_category_name_1 = 'Hexacopter'
        self.post_drone_category(drone_category_name_1)
        drone_category_name_2 = 'Octocopter'
        self.post_drone_category(drone_category_name_2)
        filter_by_name = {'name': drone_category_name_1}
        url = '{0}?{1}'.format(
            reverse('drones:' + views.DroneCategoryList.name),
            urlencode(filter_by_name))
        print(url)
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        # Make sure we receive only one element in the response
        assert response.data['count'] == 1
        assert response.data['results'][0]['name'] == drone_category_name_1

    def test_get_drone_categories_collection(self):
        """ Ensure we can retrieve the drone categories collection """
        new_drone_category_name = 'Super Copter'
        self.post_drone_category(new_drone_category_name)
        url = reverse('drones:' + views.DroneCategoryList.name)
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        # Make sure we receive only one element in the response
        assert response.data['count'] == 1
        assert response.data['results'][0]['name'] == new_drone_category_name


class PilotTests(APITestCase):
    def post_pilot(self, name, gender, races_count):
        url = reverse('drones:' + views.PilotList.name)
        data = {
            'name': name,
            'gender': gender,
            'races_count': races_count,
        }
        response = self.client.post(url, data)
        return response

    def create_user_and_set_token_credentials(self):
        user = User.objects.create_user('user01', 'user01@example.com', 'user01P4ssw0rD')
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')

    def test_post_and_get_pilots(self):
        """
        Ensure we can create a new Pilot and then retrieve it
        Ensure we cannot retrieve the persisted pilot without a token
        """
        self.create_user_and_set_token_credentials()
        new_pilot_name = 'Gatson'
        new_pilot_gender = Pilot.MALE
        new_pilot_races_count = 5
        response = self.post_pilot(new_pilot_name, new_pilot_gender, new_pilot_races_count)
        assert response.status_code == status.HTTP_201_CREATED
        assert Pilot.objects.count() == 1
        saved_pilot = Pilot.objects.get()
        assert saved_pilot.name == new_pilot_name
        assert saved_pilot.gender == new_pilot_gender
        assert saved_pilot.races_count == new_pilot_races_count
        url = reverse('drones:' + views.PilotDetail.name, None, {saved_pilot.pk})
        authorized_get_response = self.client.get(url, format='json')
        assert authorized_get_response.status_code == status.HTTP_200_OK
        assert authorized_get_response.data['name'] == new_pilot_name
        # Clean up credentials
        self.client.credentials()
        unauthorized_get_response = self.client.get(url, format='json')
        assert unauthorized_get_response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_try_to_post_pilot_without_token(self):
        new_pilot_name = 'Unauthorized Pilot'
        new_pilot_gender = Pilot.MALE
        new_pilot_races_count = 5
        response = self.post_pilot(new_pilot_name, new_pilot_gender, new_pilot_races_count)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert Pilot.objects.count() == 0
