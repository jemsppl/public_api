from django.urls import reverse

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.

from django.db import models

# Create your models here.

from bs4 import BeautifulSoup
import requests
import re


def get_status(case_id):
    id = case_id
    result = []
    g_query = "https://www.mohfw.gov.in/"
    # print(g_query)

    # file1 = open("sysn.txt", "a", encoding="utf-8")

    page = requests.get(g_query)
    dataSet_bs = page.content
    soup = BeautifulSoup(dataSet_bs, 'html.parser')

    for a in soup.find_all('div', {'class': 'site-stats-count'}):
        ac = a.get_text()
        ac_no = re.findall(r'[0-9]+', ac)
        result.append(ac_no)
        # print(result)

    if id == "AC":
        return ac_no[0]
    elif id == "CD":
        return ac_no[1]
    elif id == "D":
        return ac_no[2]
    elif id == "M":
        return ac_no[3]
    else:
        return "COVID-19"


def active_count(request):
    count = get_status('AC')
    return HttpResponse(count, content_type='text/plain')


# def active_count(request):
#     count = get_status('AC')
#     return HttpResponse(count, content_type='text/plain')
#
#
# def active_count(request):
#     count = get_status('AC')
#     return HttpResponse(count, content_type='text/plain')
#
#
# def active_count(request):
#     count = get_status('AC')
#     return HttpResponse(count, content_type='text/plain')
