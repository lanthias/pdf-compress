#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
{{ scaffold.name | capitalize }} Service
"""
import stackhut
import sh

class DefaultService:
    def __init__(self):
        pass

    def compress(self, pdfUrl) :
    	in_file = stackhut.download_file(pdfUrl)
    	out_file = "out_{}".format(in_file)

    	output = sh.gs("-sDEVICE=pdfwrite", "-dCompatibilityLevel=1.4", "-dPDFSETTINGS=/ebook", "-dNOPAUSE", "-dQUIET", "-dBATCH", "-sOutputFile={}".format(out_file), in_file)
    	
    	print(output)
    	return stackhut.put_file(out_file)

# export the services
SERVICES = {"Default": DefaultService()}
