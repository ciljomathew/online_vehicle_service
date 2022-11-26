from django.test import TestCase
from django.urls import reverse
from core import models as core_models
from core import forms as core_forms
from django.contrib.auth import get_user_model
from django.utils.timezone import now


class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse("core:home")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)


class AboutTests(TestCase):
    def test_about_view_status_code(self):
        url = reverse("core:about")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)


# feedback


class FeedbackTests(TestCase):
    def create_feedback(
        self,
        name="Ciljo",
        email="onlinevservice.ciljo@gmail.com",
        subject="Some Test",
        message="Some message",
    ):
        feedback_object = core_models.FeedbackModel.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )

        return feedback_object

    def test_feedback_create_view_get_status_code(self):
        url = reverse("core:feedback_create")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_feedback_create_view_post_status_code(self):
        url = reverse("core:feedback_create")
        data = {
            "name": "Ciljo",
            "email": "onlinevservice.ciljo@gmail.com",
            "subject": "Some Test",
            "message": "Some message",
        }
        response = self.client.post(url, data=data)
        self.assertEquals(response.status_code, 302)

    # send
    def test_feedback_send(self):
        url = reverse("core:feedback_create")
        data = {
            "name": "Ciljo",
            "email": "onlinevservice.ciljo@gmail.com",
            "subject": "Some Test",
            "message": "Some message",
        }
        response = self.client.post(url, data=data)
        self.assertEquals(response.status_code, 302)

    # feedbacklist
    def test_feedback_list_view_status_code(self):
        url = reverse("core:feedback_list")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    # model
    def test_feedback_model_object_create(self):
        feedback_object = self.create_feedback()
        self.assertTrue(isinstance(feedback_object, core_models.FeedbackModel))

    def test_feedback_model_object_detail(self):
        feedback_object = self.create_feedback()
        f_id = feedback_object.id
        f_obj = core_models.FeedbackModel.objects.get(id=f_id)
        self.assertEqual(feedback_object, f_obj)

    def test_feedback_model_object_list(self):
        feedback_object = self.create_feedback()
        feedback_object_list = core_models.FeedbackModel.objects.all()
        self.assertIn(feedback_object, feedback_object_list)

    def test_feedback_model_object_update(self):
        feedback_object = self.create_feedback()
        feedback_object.name = "New name"
        feedback_object.save()
        self.assertTrue(isinstance(feedback_object, core_models.FeedbackModel))

    def test_feedback_model_object_delete(self):
        feedback_object = self.create_feedback()
        f_id = feedback_object.id
        feedback_object = feedback_object.delete()
        self.assertTrue(feedback_object[0] == f_id)

    # Form
    def test_feedback_create_form_valid(self):
        data = {
            "name": "Ciljo",
            "email": "onlinevservice.ciljo@gmail.com",
            "subject": "Some Test",
            "message": "Some message",
        }
        form = core_forms.FeedbackForm(data=data)
        self.assertTrue(form.is_valid())

    def test_feedback_create_form_invalid(self):
        data = {
            "name": "",
            "email": "",
            "subject": "Some Test",
            "message": "Some message",
        }
        form = core_forms.FeedbackForm(data=data)
        self.assertFalse(form.is_valid())


# class BookServiceTests(TestCase):
#     def test_about_view_status_code(self):
#         url = reverse("core:book_service")
#         response = self.client.get(url)
#         self.assertEquals(response.status_code, 200)


# class AboutTests(TestCase):
#     def test_about_view_status_code(self):
#         url = reverse("core:about")
#         response = self.client.get(url)
#         self.assertEquals(response.status_code, 200)


# class CheckoutTests(TestCase):
#     def test_checkout_view_status_code(self):
#         url = reverse("core:checkout",kwargs={"pk":1})
#         response = self.client.get(url)
#         self.assertEquals(response.status_code, 200)


# class ServiceTests(TestCase):
#     def test_service_view_status_code(self):
#         url = reverse("core:delivery")
#         response = self.client.get(url)
#         self.assertEquals(response.status_code, 302)


# class ServiceTests(TestCase):
#     def test_service_view_status_code(self):
#         url = reverse("core:service_history")
#         response = self.client.get(url)
#         self.assertEquals(response.status_code, 302)


# class PaymentTests(TestCase):
#     def test_payment_view_status_code(self):
#         url = reverse("core:payment")
#         response = self.client.get(url)
#         self.assertEquals(response.status_code, 302)


# class PaymentCompletedTests(TestCase):
#     def test_paymentcompleted_view_status_code(self):
#         url = reverse("core:payment_completed", kwargs={"pk":1})
#         response = self.client.get(url)
#         self.assertEquals(response.status_code, 200)
#         self.assertRaises(reverse("core:payment_completed", kwargs={"pk":1}))


# class PaymentTests(TestCase):
#     def test_payment_view_status_code(self):
#         url = reverse("core:payment_list")
#         response = self.client.get(url)
#         self.assertEquals(response.status_code, 200)


# bookservice


# vehilcemodel
class VehicleModelTests(TestCase):
    def create_vehiclemodel(
        self,
        name="car",
        model="car",
        type="car",
    ):
        vehicle_object = core_models.VehicleModel.objects.create(
            name=name,
            model=model,
            type=type,
        )

        return vehicle_object


# servicetype
class ServiceTypeModelTests(TestCase):
    def create_vehiclemodel(
        self,
        name="car",
        model="car",
        type="cr",
    ):
        vehicle_object = core_models.VehicleModel.objects.create(
            name=name,
            model=model,
            type=type,
        )

        return vehicle_object

    def create_servicetypemodel(
        self,
        name="car",
        cost=100.0,
    ):
        servicetype_object = core_models.ServiceTypeModel.objects.create(
            name=name,
            cost=cost,
        )

        return servicetype_object


# servicemodel
class ServiceModelTests(TestCase):
    def create_vehiclemodel(
        self,
        name="car",
        model="car",
        type="cr",
    ):
        vehicle_object = core_models.VehicleModel.objects.create(
            name=name,
            model=model,
            type=type,
        )

        return vehicle_object

    def create_servicetypemodel(
        self,
        name="Change Engine Oil",
        cost=100.0,
    ):
        servicetype_object = core_models.ServiceTypeModel.objects.create(
            name=name,
            cost=cost,
        )

        return servicetype_object

    def get_user(self):
        user, created = get_user_model().objects.get_or_create(
            username="user_1", password="p@55w0rd", email="user_1@email.com"
        )
        return user

    def create_servicemodel(
        self,
        user="ciljo",
        type="painting",
        vehicle="car",
        cost="amount",
        date="date",
        delivery_time="time",
        is_delivered="delivered",
    ):
        user = self.get_user()
        service_type = self.create_servicetypemodel()
        vehicle = self.create_vehiclemodel()
        service_object = core_models.ServiceModel.objects.create(
            user=user,
            type=service_type,
            vehicle=vehicle,
            cost=100.0,
            date=now(),
            delivery_time=now(),
            is_delivered=False,
        )

        return service_object

    def test_book_service_view_get_status_code(self):
        url = reverse("core:book_service")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)


    # model
    def test_service_model_object_create(self):
        service_object = self.create_servicemodel()
        self.assertTrue(isinstance(service_object, core_models.ServiceModel))

    def test_service_model_object_detail(self):
        service_object = self.create_servicemodel()
        f_id = service_object.id
        f_obj = core_models.ServiceModel.objects.get(id=f_id)
        self.assertEqual(service_object, f_obj)

    def test_service_model_object_list(self):
        service_object = self.create_servicemodel()
        service_object_list = core_models.ServiceModel.objects.all()
        self.assertIn(service_object, service_object_list)

    def test_service_model_object_update(self):
        service_object = self.create_servicemodel()
        service_object.name = "New name"
        service_object.save()
        self.assertTrue(isinstance(service_object, core_models.ServiceModel))

    def test_service_model_object_delete(self):
        service_object = self.create_servicemodel()
        f_id = service_object.id
        service_object = service_object.delete()
        self.assertTrue(service_object[0] == f_id)

    # Form
    def test_service_create_form_valid(self):
        service = self.create_servicetypemodel()
        vehicle = self.create_vehiclemodel()
        user = self.get_user()
        date = now()
        data = {
            "type": service.id,
            "vehicle": vehicle.id,
            "user": user.id,
            "date": date,
        }
        form = core_forms.ServiceForm(data=data)
        self.assertTrue(form.is_valid())

    def test_service_create_form_invalid(self):
        data = {
            "type": "",
            "vehicle": "",
            "date": "Some message",
        }
        form = core_forms.ServiceForm(data=data)
        self.assertFalse(form.is_valid())




#checkout

class CheckoutTests(TestCase):
    def test_checkout_view_status_code(self):
        url = reverse("core:checkout", kwargs={"pk":0})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)


#history

class BookServiceListTests(TestCase):
    def test_bookservicelist_view_status_code(self):
        url = reverse("core:service_history")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)



#payment completed
        

class PaymentCompletedTests(TestCase):
    def test_payment_completed_view_status_code(self):
        url = reverse("core:payment_completed", kwargs={"pk":0})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

