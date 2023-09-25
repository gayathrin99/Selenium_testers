import bs4
from bs4 import BeautifulSoup
import requests
import pandas as pd
import selenium
from selenium import webdriver
import django
from django.shortcuts import render
from django.http import HttpResponse
def say_hello(request):
    return HttpResponse('Hello World')