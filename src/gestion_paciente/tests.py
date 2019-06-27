#import unittest
from django.test import TestCase
from django.contrib.auth.models import User
#from django.contrib.auth import get_user_model
from .forms import *
from .models import *

# Create your tests here.
class Paciente_Form_Test(TestCase):

    """def create_user(self):
        return User.objects.create_user(username="John", email="asd@mail.com")"""

    def setUp(self):
        #user = get_user_model().objects.create_user('zoidberg')
        usr = User.objects.create(
            password='sha1$6efc0$f93efe9fd7542f25a7be94871ea45aa95de57161',
            is_superuser=False, username='testclient',
            first_name='Test', last_name='Client', email='testclient@example.com', is_staff=False, is_active=True
            
            )
        self.paciente=Paciente.objects.create(user=usr, estado=estado_civil.objects.get(estado="Soltero"))

    def test_init(self):
        PacienteForm(paciente=self.paciente)

    def test_init_without_entry(self):
        with self.assertRaises(KeyError):
                PacienteForm()

    def test_valid_data(self):
        form = PacienteForm({
            'nombre': "Benito",
            'apellido_paterno':"Camelo",
            'apellido_materno':"Golosa",
            'run':"1234567-1",
            'fecha_nacimiento':"1996-01-19",
            'escolaridad':"Basica completa",
            'ocupacion':"Profesor",
            'domicilio':"Av arlegui",
            'ciudad':"Viña del mar",
            'telefono':1234124,
            'prevision':"Isapre",

         }, paciente=self.paciente)
        self.assertTrue(form.is_valid())
        comment = form.save()
        self.assertEqual(comment.nombre, "Benito")
        self.assertEqual(comment.apellido_paterno, "Camelo")
        self.assertEqual(comment.apellido_materno, "Golosa")
        self.assertEqual(comment.run, "1234567-1")
        self.assertEqual(comment.fecha_nacimiento, "1996-01-19")
        self.assertEqual(comment.escolaridad, "Basica completa")
        self.assertEqual(comment.ocupacion, "Profesor")
        self.assertEqual(comment.domicilio, "Av arlegui")
        self.assertEqual(comment.ciudad, "Viña del mar")
        self.assertEqual(comment.telefono, 1234124)
        self.assertEqual(comment.prevision, "Isapre")

        self.assertEqual(comment.paciente, self.paciente)

    def test_blank_data(self):
        form = PacienteForm({}, paciente=self.paciente)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'nombre': ['required'],
            'apellido_paterno':['required'],
            'apellido_materno':['required'],
            'run':['required'],
            'fecha_nacimiento':['required'],
            'escolaridad':['required'],
            'ocupacion':['required'],
            'domicilio':['required'],
            'ciudad':['required'],
            'telefono':['required'],
            'prevision':['required'],    	

            })

        