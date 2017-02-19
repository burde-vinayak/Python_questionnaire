import json
from Tkinter import *

class Application(Frame):
    def cities(self):
        city_list = [x['name'] for x in self.city_info]
        return tuple(sorted(city_list))

    def get_info(self, city_name):
        info = [x for x in self.city_info if x['name'] == city_name]
        return info[0]

    def updated(self, value):
        info = self.get_info(value)
        self.county_value.set(info['county_name'])
        self.latitude_value.set(info['primary_latitude'])
        self.longitude_value.set(info['primary_longitude'])


    def createWidgets(self):
        self.frame1 = Frame(self)
        self.frame1.pack(fill=X)
        self.city = Label(self.frame1, text="City")
        self.city.pack(side=LEFT)
        self.city_value = StringVar()
        city_list = self.cities()
        self.city_value.set(city_list[0])
        self.city_field = OptionMenu(*(tuple([self.frame1, self.city_value]) + city_list), command=self.updated)
        self.city_field.pack(fill=X)

        self.frame2 = Frame(self)
        self.frame2.pack(fill=X)
        self.county = Label(self.frame2, text="County")
        self.county.pack(side=LEFT)
        self.county_value = StringVar()
        self.county_value.set(self.get_info(city_list[0])['county_name'])
        self.county_field = Entry(self.frame2, textvariable=self.county_value)
        self.county_field.pack(side=RIGHT)

        self.frame3 = Frame(self)
        self.frame3.pack(fill=X)
        self.latitude = Label(self.frame3, text="Latitude")
        self.latitude.pack(side=LEFT)
        self.latitude_value = StringVar()
        self.latitude_value.set(self.get_info(city_list[0])['primary_latitude'])
        self.latitude_field = Entry(self.frame3, textvariable=self.latitude_value)
        self.latitude_field.pack(side=RIGHT)

        self.frame4 = Frame(self)
        self.frame4.pack(fill=X)
        self.longitude = Label(self.frame4, text="Longitude")
        self.longitude.pack(side=LEFT)
        self.longitude_value = StringVar()
        self.longitude_value.set(self.get_info(city_list[0])['primary_longitude'])
        self.longitude_field = Entry(self.frame4, textvariable=self.longitude_value)
        self.longitude_field.pack(side=RIGHT)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title = "City Information"
        self.city_info = None
        with open('ca.json', 'r') as in_file:
            self.city_info = json.load(in_file)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
