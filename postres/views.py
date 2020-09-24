from django.shortcuts import render
from django.views.generic import View

import firebase_admin

from firebase_admin import credentials
from firebase_admin import db

class Postres( View ):
    template_name = 'index.html'
    cred = credentials.Certificate('./fir-django-edfdb-firebase-adminsdk-nqz49-77a1d24e82.json')
    firebase_admin.initialize_app(cred,
        {'databaseURL': 'https://fir-django-edfdb.firebaseio.com'}
    )

    ref = db.reference('postres')

    datos = ref.get()

    def get(self ,request):
        return render(request ,self.template_name , {"productos":self.datos})

