import time
import unittest
from django.test import TestCase
from django.contrib.messages import get_messages
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from . models import Friend, Requests, Like, Comment, Media, Shared
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login_func(driver, username, password):
    username_id = "username"
    password_id = "password"
    button_id = "submit"
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, username_id))
    )
    username_field = driver.find_element(By.ID, username_id)
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, password_id))
    )
    password_field = driver.find_element(By.ID, password_id)
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, button_id))
    )
    button = driver.find_element(By.ID, button_id)

    username_field.send_keys(username)
    password_field.send_keys(password)
    button = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, button_id))
    )
    button.click()

# class LoginTestCase(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username='testuser', password='testpassword')
#         self.login_url = reverse('login')

#     # Test that a user can log in with valid credentials
#     def test_login_successful(self):
#         response = self.client.post(self.login_url, {'username': 'testuser', 'password': 'testpassword'})
#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(response, reverse('index'))
#         # Check if the user is now logged in
#         user_is_authenticated = self.client.login(username='testuser', password='testpassword')
#         self.assertTrue(user_is_authenticated)

#     # Test that login fails with invalid credentials
#     def test_login_unsuccessful(self):
#         response = self.client.post(self.login_url, {'username': 'testuser', 'password': 'wrongpassword'})
#         self.assertEqual(response.status_code, 302)
#         messages = [m.message for m in get_messages(response.wsgi_request)]
#         self.assertIn('Invalid credentials', messages)

#         # Check if the user is not logged in
#         user_is_authenticated = self.client.login(username='testuser', password='wrongpassword')
#         self.assertFalse(user_is_authenticated)

# class RegistrationTestCase(TestCase):
#     def setUp(self):
#         print('setup')
#         self.register_url = reverse('register')
#         User.objects.create_user(username='existing_user', password='t', email='existing@gmail.com')

#         with open("C:/Users/user/Pictures/Screenshots/c1.png", 'rb') as file:
#             file_content = file.read()

#         with open("C:/Users/user/Videos/vid.mkv", 'rb') as file:
#             file_content2 = file.read()
#         self.correct_file = SimpleUploadedFile('c1.png', file_content)
#         self.incorrect_file = SimpleUploadedFile('vid.mkv', file_content2)

#     def test_successful_with_everything(self):
#         response = self.client.post(self.register_url,
#         {'name': 'test', 'surname': 'testov', 'username': 'test', 'password': 't', 'password2': 't', 'email': 'test@gmail.com', 'inputFile': self.correct_file})
#         self.assertEqual(response.status_code, 302)
#         user_is_authenticated = self.client.login(username='test', password='t')
#         self.assertTrue(user_is_authenticated)

#     def test_successful_without_profile_image_file(self):
#         response = self.client.post(self.register_url,
#         {'name': 'test', 'surname': 'testov', 'username': 'test', 'password': 't', 'password2': 't', 'email': 'test@gmail.com'})
#         self.assertEqual(response.status_code, 302)
#         user_is_authenticated = self.client.login(username='test', password='t')
#         self.assertTrue(user_is_authenticated)

#     def test_unmatching_passwords_with_space(self):
#         response = self.client.post(self.register_url,
#         {'name': 'test', 'surname': 'testov', 'username': 'test', 'password': 't', 'password2': 'wrong t', 'email': 'test@gmail.com'})
#         self.assertEqual(response.status_code, 302)
#         messages = [m.message for m in get_messages(response.wsgi_request)]
#         self.assertIn('Passwords did not match or contains spaces', messages)
#         user_is_authenticated = self.client.login(username='test', password='t')
#         self.assertFalse(user_is_authenticated)

#     def test_with_errors(self):
#         response = self.client.post(self.register_url,
#         {'name': ' ', 'surname': '', 'username': ' test', 'password': ' t', 'password2': 'wrong t', 'email': 'testgmail.com'})
#         self.assertEqual(response.status_code, 302)
#         messages = [m.message for m in get_messages(response.wsgi_request)]
#         self.assertEqual(len(messages), 5)
#         user_is_authenticated = self.client.login(username='test', password='t')
#         self.assertFalse(user_is_authenticated)
    
#     def test_with_incorrect_profile_image_file(self):
#         response = self.client.post(self.register_url,
#         {'name': 'test', 'surname': 'testov', 'username': 'test', 'password': 't', 'password2': 'wrong t', 'email': 'test@gmail.com', 'inputFile': self.incorrect_file})
#         self.assertEqual(response.status_code, 302)
#         messages = [m.message for m in get_messages(response.wsgi_request)]
#         self.assertIn('Profile Image is not supported upload one of the followings: jpg, png, jpeg', messages)
#         user_is_authenticated = self.client.login(username='test', password='t')
#         self.assertFalse(user_is_authenticated)
    
#     def test_existing_user(self):
#         response = self.client.post(self.register_url,
#         {'name': 'test', 'surname': 'testov', 'username': 'existing_user', 'password': 't', 'password2': 't', 'email': 'existing@gmail.com'})
#         self.assertEqual(response.status_code, 302)
#         messages = [m.message for m in get_messages(response.wsgi_request)]
#         self.assertIn('Username already exists', messages)
#         self.assertIn('Email already registered', messages)
#         self.assertEqual(len(messages), 2)
#         user_is_authenticated = self.client.login(username='test', password='t')
#         self.assertFalse(user_is_authenticated)

# class ProfileTestCase(TestCase):
#     def setUp(self):
#         self.user1 = User.objects.create_user(username='tes1', password='t')
#         self.user2 = User.objects.create_user(username='tes2', password='t')
#         self.login_url = reverse('login')
#         self.logout_url = reverse('logout')
#         self.profile_url = reverse('profile', kwargs={'username':'tes2'})
#         self.profile_url2 = reverse('profile', kwargs={'username':'tes1'})

#     def test_unfollowed_user(self):
#         response = self.client.post(self.login_url, {'username': 'tes1', 'password': 't'})
#         response = self.client.post(self.profile_url, {'button_action': 'add_friend'})
#         self.assertEqual(response.status_code, 302)
#         redirected_response = self.client.get(response.url)
#         self.assertIn("Unfollow", redirected_response.content.decode())
    
#     def test_followed_user(self):
#         response = self.client.post(self.login_url, {'username': 'tes1', 'password': 't'})
#         response = self.client.post(self.profile_url, {'button_action': 'add_friend'})
#         response = self.client.post(self.logout_url)
#         response = self.client.post(self.login_url, {'username': 'tes2', 'password': 't'})
#         response = self.client.get(self.profile_url2)
#         html_content = response.content.decode('utf-8')
#         self.assertEqual(response.status_code, 200)
#         self.assertIn("Accept", html_content)
#         self.assertNotIn("Follow", html_content)
#         self.assertNotIn("Unfollow", html_content)
#         self.assertNotIn("Your profile!", html_content)

#     def test_user_itself(self):
#         response = self.client.post(self.login_url, {'username': 'tes1', 'password': 't'})
#         response = self.client.post(self.profile_url, {'button_action': 'add_friend'})
#         response = self.client.post(self.logout_url)
#         response = self.client.post(self.login_url, {'username': 'tes2', 'password': 't'})
#         response = self.client.get(self.profile_url)
#         html_content = response.content.decode('utf-8')
#         self.assertEqual(response.status_code, 200)
#         self.assertNotIn("Follow", html_content)
#         self.assertNotIn("Unfollow", html_content)
#         self.assertIn("Your profile!", html_content)
    
#     def test_user_both_accepted(self):
#         response = self.client.post(self.login_url, {'username': 'tes1', 'password': 't'})
#         response = self.client.post(self.profile_url, {'button_action': 'add_friend'})
#         response = self.client.post(self.logout_url)
#         response = self.client.post(self.login_url, {'username': 'tes2', 'password': 't'})
#         response = self.client.post(self.profile_url2, {'button_action': 'add_friend'})
#         self.assertEqual(response.status_code, 302)
#         redirected_response = self.client.get(response.url)
#         self.assertIn("Unfollow", redirected_response.content.decode())
#         self.assertNotIn("Follow", redirected_response.content.decode())
#         self.assertNotIn("Accept", redirected_response.content.decode())
#         self.assertNotIn("Your profile!", redirected_response.content.decode())
#         self.assertIn('"write_message">Message</button>', redirected_response.content.decode())

# class UploadTestCase(TestCase):
#     def setUp(self):
#         self.upload_url = reverse('upload')
#         self.login_url = reverse('login')
#         User.objects.create_user(username='user', password='t', email='user@gmail.com')

#         with open("C:/Users/user/Pictures/Screenshots/c1.png", 'rb') as file:
#             file_content = file.read()

#         with open("C:/Users/user/Videos/vid.mkv", 'rb') as file:
#             file_content2 = file.read()
#         self.correct_file = SimpleUploadedFile('c1.png', file_content)
#         self.incorrect_file = SimpleUploadedFile('vid.mkv', file_content2)

#     # Succesfull upload with everything!
#     def test_upload_image(self):
#         response = self.client.post(self.login_url, {'username': 'user', 'password': 't'})
#         response = self.client.post(self.upload_url,
#         {'inputFile': self.correct_file, 'description_text': 'This is test description!'})
#         self.assertEqual(response.status_code, 302)
#         messages = [m.message for m in get_messages(response.wsgi_request)]
#         self.assertEqual(len(messages), 0)

#     # Succesfull upload without image!
#     def test_successful_without_profile_image_file(self):
#         response = self.client.post(self.login_url, {'username': 'user', 'password': 't'})
#         response = self.client.post(self.upload_url,
#         {'description_text': 'This is test description!'})
#         self.assertEqual(response.status_code, 302)
#         messages = [m.message for m in get_messages(response.wsgi_request)]
#         self.assertEqual(len(messages), 0)

#     # Succesfull upload without description!
#     def test_correct_file(self):
#         response = self.client.post(self.login_url, {'username': 'user', 'password': 't'})
#         response = self.client.post(self.upload_url,
#         {'inputFile': self.correct_file})
#         self.assertEqual(response.status_code, 302)
#         messages = [m.message for m in get_messages(response.wsgi_request)]
#         self.assertEqual(len(messages), 0)

#     # Unsuccesfull file issue!
#     def test_incorrect_file(self):
#         response = self.client.post(self.login_url, {'username': 'user', 'password': 't'})
#         response = self.client.post(self.upload_url,
#         {'inputFile': self.incorrect_file})
#         messages = [m.message for m in get_messages(response.wsgi_request)]
#         print(messages)
#         self.assertIn('Incorrect format!', messages)

class SeleniumRequestsTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        if User.objects.filter(username='tes1').exists() is False:
            self.user1 = User.objects.create_user(username='tes1', password='correctone')
        else:
            self.user1 = User.objects.get(username='tes1')

        if User.objects.filter(username='tes2').exists() is False:
            self.user2 = User.objects.create_user(username='tes2', password='correctone')
        else:
            self.user2 = User.objects.get(username='tes2')
        self.driver.get("http://localhost:8000/requests")
    
    def test_accept_request(self):
        Requests.objects.create(from_user=self.user1, to_user=self.user2)
        login_func(self.driver, 'tes2', 'correctone')
        self.driver.get("http://localhost:8000/requests")
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "tes1"))
        )
        button = self.driver.find_element(By.NAME, 'accept')
        button.click()
        self.driver.get("http://localhost:8000")
        self.assertFalse(Requests.objects.filter(from_user=self.user1, to_user=self.user2).exists())


    def test_remove_request(self):
        Requests.objects.create(from_user=self.user1, to_user=self.user2)
        self.driver.get("http://localhost:8000/")
        login_func(self.driver, 'tes2', 'correctone')
        self.driver.get("http://localhost:8000/requests")
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "tes1"))
        )
        button = self.driver.find_element(By.NAME, 'remove')
        button.click()
        self.driver.get("http://localhost:8000")
        self.assertFalse(Requests.objects.filter(from_user=self.user1, to_user=self.user2).exists())

    def test_empty_request(self):
        self.driver.get("http://localhost:8000/")
        login_func(self.driver, 'tes2', 'correctone')
        self.driver.get("http://localhost:8000/requests")
        found = False
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "tes1"))
            )
            found = True
        except Exception:
            found = False
        self.driver.get("http://localhost:8000")
        self.assertFalse(found)

    def tearDown(self):
        self.driver.quit()

# class SeleniumPeopleTestCase(TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#         self.driver.get("http://localhost:8000/")
    
#     def test_existing_user(self):
#         login_func(self.driver, 'tes1', 't')
#         self.driver.get("http://localhost:8000/people")
#         WebDriverWait(self.driver, 3).until(
#             EC.presence_of_element_located((By.ID, "searches"))
#         )
#         search_input = self.driver.find_element(By.ID, "searches")
#         search_input.send_keys('ad')
#         try:
#             WebDriverWait(self.driver, 3).until(
#                 EC.presence_of_element_located((By.ID, "ad"))
#             )
#         except Exception:
#             pass
#         self.assertIn('admin', self.driver.page_source)

#     def test_not_existing_user(self):
#         login_func(self.driver, 'tes1', 't')
#         self.driver.get("http://localhost:8000/people")
#         WebDriverWait(self.driver, 3).until(
#             EC.presence_of_element_located((By.ID, "searches"))
#         )
#         search_input = self.driver.find_element(By.ID, "searches")
#         search_input.send_keys('rty')
#         try:
#             WebDriverWait(self.driver, 5).until(
#                 EC.presence_of_element_located((By.ID, 'rty'))
#             )
#         except Exception:
#             pass
        
#         self.assertNotIn('admin', self.driver.page_source)

#     def tearDown(self):
#         self.driver.quit()

# class SeleniumChatViewTestCase(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#         self.driver.get("http://localhost:8000/")
#         self.user1 = User.objects.get(username='tes1')
#         self.user2 = User.objects.get(username='tes2')
#         Requests.objects.filter(from_user=self.user1, to_user=self.user2).delete()
    
#     def test_empty_chat_view(self):
#         login_func(self.driver, 'tes2', 't')
#         self.driver.get("http://localhost:8000/chatting")
#         found = False
#         try:
#             WebDriverWait(self.driver, 3).until(
#                 EC.presence_of_element_located((By.TAG_NAME, "img"))
#             )
#             found = True
#         except Exception:
#             found = False
            
#         self.assertFalse(found)
    
#     def test_remove_request(self):
#         self.driver.get("http://localhost:8000/")
#         Friend.objects.create(user1=self.user1, user2=self.user2)
#         Friend.objects.create(user1=self.user2, user2=self.user1)
#         login_func(self.driver, 'tes2', 't')
#         self.driver.get("http://localhost:8000/chatting")
#         try:
#             WebDriverWait(self.driver, 3).until(
#                 EC.presence_of_element_located((By.TAG_NAME, "img"))
#             )
#             found = True
#         except Exception:
#             found = False
        
#         Friend.objects.get(user1=self.user1, user2=self.user2).delete()
#         Friend.objects.get(user1=self.user2, user2=self.user1).delete()
#         self.assertTrue(found)

#     def tearDown(self):
#         self.driver.quit()

# class SeleniumMainPageTestCase(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#         self.driver.get("http://localhost:8000")
#         self.user1 = User.objects.get(username='tes1')
#         login_func(self.driver, 'tes1', 't')
#         self.driver.get("http://localhost:8000/")
    
    # def test_like(self):
    #     Like.objects.filter(user=self.user1).delete()
    #     self.driver.get("http://localhost:8000")
    #     WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable((By.NAME, "like*admin*admin*2023-11-22 14:44:14+0000"))
    #     )
    #     like_button = self.driver.find_element(By.NAME, 'like*admin*admin*2023-11-22 14:44:14+0000')
    #     self.driver.execute_script("arguments[0].click();", like_button)
    #     icon = like_button.find_element(By.TAG_NAME, 'i')
    #     self.assertIn('fas', icon.get_attribute('class'))
    #     self.assertEqual(len(Like.objects.filter(user=self.user1)), 1)

    # def test_dislike(self):
    #     WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable((By.NAME, "like*admin*admin*2023-11-22 14:44:14+0000"))
    #     )
    #     like_button = self.driver.find_element(By.NAME, 'like*admin*admin*2023-11-22 14:44:14+0000')
    #     self.driver.execute_script("arguments[0].click();", like_button)
    #     icon = like_button.find_element(By.TAG_NAME, 'i')
    #     self.assertIn('far', icon.get_attribute('class'))
    #     self.assertEqual(len(Like.objects.filter(user=self.user1)), 0)

    # def test_repost(self):
    #     self.driver.get("http://localhost:8000")
    #     WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable((By.NAME, "share*admin*admin*2023-11-22 14:44:14+0000"))
    #     )
    #     share_button = self.driver.find_element(By.NAME, 'share*admin*admin*2023-11-22 14:44:14+0000')
    #     self.driver.execute_script("arguments[0].click();", share_button)
    #     icon = share_button.find_element(By.TAG_NAME, 'i')
    #     self.assertIn('fas', icon.get_attribute('class'))
    #     self.driver.get("http://localhost:8000/login")
    #     self.assertEqual(len(Shared.objects.filter(user=self.user1)), 1)
    #     Media.objects.filter(reposter=self.user1).delete()
    #     Shared.objects.filter(user=self.user1).delete()

    # def test_comment(self):
    #     WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable((By.NAME, "comment*admin*admin*2023-11-22 14:44:14+0000"))
    #     )
    #     comment_button = self.driver.find_element(By.NAME, 'comment*admin*admin*2023-11-22 14:44:14+0000')
    #     self.driver.execute_script("arguments[0].click();", comment_button)
    #     WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='admin*admin*2023-11-22 14:44:14+0000']"))
    #     )
    #     comment_input = self.driver.find_element(By.CSS_SELECTOR, "input[name='admin*admin*2023-11-22 14:44:14+0000']")
    #     comment_input.send_keys("Test comment!")
    #     WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable((By.NAME, "submit*admin*admin*2023-11-22 14:44:14+0000"))
    #     )
    #     submit_input = self.driver.find_element(By.NAME, "submit*admin*admin*2023-11-22 14:44:14+0000")
    #     submit_input.click()
    #     self.driver.get("http://localhost:8000")
    #     self.assertEqual(len(Comment.objects.filter(user=self.user1)), 1)
    #     Comment.objects.filter(user=self.user1).delete()

    # def tearDown(self):
    #     self.driver.quit()