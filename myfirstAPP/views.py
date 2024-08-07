from django.shortcuts import render
from django.views.generic import TemplateView 

import geemap
import ee
import pandas as pd 
import folium
import geemap.foliumap as geemap

Map=geemap.Map()


# Create your views here.
# Logic: Functions or classes

class Facebook(TemplateView):

    
    template_name = "index.html"
     


class insta(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        Map=folium.Map()
        figure=folium.Figure()

        

        return{"insta":figure}
    

    

    






    