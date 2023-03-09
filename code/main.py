# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 16:21:02 2023

@author: abiga
"""

import quarto
import os

def renderAsDoc(qmd_folder, qmd_file, output_format):
    # this is just my function around the quarto.render() function
    os.chdir(qmd_folder)
    quarto.render(input=qmd_file, output_format=output_format)
    
qmd_folder=r"C:\Users\abiga\OneDrive\Documents\PythonScripts\linear_equations\qmd"
qmd_file="linear_equations.qmd"
    
renderAsDoc(qmd_folder, qmd_file, "html")