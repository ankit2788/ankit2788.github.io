#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 19:20:23 2019

@author: ankitgupta
"""

import pandas as pd

from bokeh.plotting import show


from FDynamics.Visualizations import BokehVisuals

pathdata = "/Users/ankitgupta/Documents/git/anks/github_page/data/correlation/"
outputpath = "/Users/ankitgupta/Documents/git/anks/github_page/data/bokeh/"



#---------UFO vs Superheros-----------
file = "superhero_ufo.csv"

data = pd.read_csv(pathdata + file)
boka = BokehVisuals(data)
p = boka.createPlot(outputpath + "ufo.html", 
                imagetitle = "UFOs and our Superheroes",
                XAxisDetails={"LABEL": "Year", "COL_NAME": "year"},
                PrimaryAxisDetails={"LABEL": "SuperheroMovies", "COL_NAME": "superhero_movies", "HOVER":"@superhero_movies"},
                SecondaryAxis=True,
                SecondaryAxisDetails={"LABEL": "UFO sightings", "COL_NAME": "UFO_sightings", "HOVER":"@UFO_sightings"}
                )
show(p)



#---------UFO vs Superheros-----------
            





