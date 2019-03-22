# Program that takes an input from the user and grabs information from the specified IP using this url: https://whatismyipaddress.com/ip/[INPUT])

from tkinter import *
import requests
from bs4 import BeautifulSoup
import lxml.html
import lxml
from lxml import etree
import json
import os


root = Tk()
root.title('IP Lookup')

banner = PhotoImage(file="banner.png")
Label (root, image=banner, bg="black") .grid(row=0, column=0, sticky=W)

def search_for_city(*args):
	ip_search = "https://ipapi.co/" + ip_input_entry.get() + "/city"
	city_return = requests.get(ip_search).text
	return city_return

def search_for_postal(*args):
	ip_search = "https://ipapi.co/" + ip_input_entry.get() + "/postal"
	postal_return = requests.get(ip_search).text
	return postal_return

def search_for_continent(*args):
	ip_search = "https://ipapi.co/" + ip_input_entry.get() + "/continent_code"
	continent_return = requests.get(ip_search).text
	return continent_return

def search_for_ip(*args):
	ip_search = "https://ipapi.co/" + ip_input_entry.get() + "/ip"
	ip_return = requests.get(ip_search).text
	return ip_return

def search_for_isp(*args):
	ip_search = "https://ipapi.co/" + ip_input_entry.get() + "/org"
	org_return = requests.get(ip_search).text
	return org_return

def search_for_latitude(*args):
	ip_search = "https://ipapi.co/" + ip_input_entry.get() + "/latitude"
	latitude_return = requests.get(ip_search).text
	return latitude_return

def search_for_longitude(*args):
	ip_search = "https://ipapi.co/" + ip_input_entry.get() + "/longitude"
	longitude_return = requests.get(ip_search).text
	return longitude_return


def search_for_currency(*args):
	ip_search = "https://ipapi.co/" + ip_input_entry.get() + "/currency"
	currency_return = requests.get(ip_search).text
	return currency_return


def search_for_country(*args):
	ip_search = "https://ipapi.co/" + ip_input_entry.get() + "/country_name"
	country_return = requests.get(ip_search).text
	return country_return

def search_for_region(*args):
	ip_search = "https://ipapi.co/" + ip_input_entry.get() + "/region"
	region_return = requests.get(ip_search).text
	return region_return

def ip_search():

	ip_summary = "IP: " + search_for_ip()
	continent_summary = "Continent: " + search_for_continent()
	country_summary = "Country: " + search_for_country()
	region_summary = "Region: " + search_for_region()
	city_summary = "City: " + search_for_city()
	postal_summary = "Postal Code: " + search_for_postal()
	currency_summary = "Currency: " + search_for_currency()
	latitude_summary = "Latitude: " + search_for_latitude()
	longitude_summary = "Longitude: " + search_for_longitude()
	isp_summary = "ISP: " + search_for_isp()

	ip_label = Label(root, text=ip_summary)
	ip_label.grid(row=4, column=0, sticky=W)

	divider_label = Label(root)
	divider_label.grid(row=5, column=0, sticky=W)
	

	continent_label = Label(root, text=continent_summary)
	continent_label.grid(row=6, column=0, sticky=W)

	country_label = Label(root, text=country_summary)
	country_label.grid(row=7, column=0, sticky=W)

	region_label = Label(root, text=region_summary)
	region_label.grid(row=8, column=0, sticky=W)

	city_label = Label(root, text=city_summary)
	city_label.grid(row=9, column=0, sticky=W)

	postal_label = Label(root, text=postal_summary)
	postal_label.grid(row=10, column=0, sticky=W)

	currency_label = Label(root, text=currency_summary)
	currency_label.grid(row=11, column=0, sticky=W)

	latitude_label = Label(root, text=latitude_summary)
	latitude_label.grid(row=12, column=0, sticky=W)

	longitude_label = Label(root, text=longitude_summary)
	longitude_label.grid(row=13, column=0, sticky=W)

	isp_label = Label(root, text=isp_summary)
	isp_label.grid(row=14, column=0, sticky=W)


ip_input_label = Label(root, text="Enter IP Address to lookup: ")
ip_input_label.grid(row=1, column=0, sticky=W)


ip_input_entry = Entry(root)
ip_input_entry.grid(row=1, column=0, sticky=W, padx=180)

button_search = Button(text="Lookup IP", command=ip_search)
button_search.grid(row=3, column=0, sticky=W)

root.maxsize(340, 375)


root.mainloop()
