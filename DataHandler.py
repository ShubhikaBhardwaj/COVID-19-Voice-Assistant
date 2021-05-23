import requests
import json
import threading
import time
import os
from VoiceRecognition import *

# Setting environment variables
API_KEY = os.environ['API_KEY']
PROJECT_TOKEN = os.environ['PROJECT_TOKEN']
RUN_TOKEN = os.environ['RUN_TOKEN']


class DataHandler:
    """Data Handler is responsible for getting, updating and manipulating data that was extracted from the
    webscraping-tool,ParseHub"""

    def __init__(self, api_key, project_token):
        """Initialising the API key and Project token"""
        self.api_key = api_key
        self.project_token = project_token

        # Setting up Authentication
        self.params = {
            "api_key": self.api_key
        }

        # Most recent run
        self.data = self.get_data()

        # Initialising COVID-19 Bot
        self.covid_bot = VoiceAssistant()

    @staticmethod
    def get_data():
        """Getting COVID-19 data from the last run of the webscraping-tool """
        response = requests.get(f'https://www.parsehub.com/api/v2/projects/{PROJECT_TOKEN}/last_ready_run/data',
                                params={
                                    "api_key": API_KEY})  # Authentication for the get request
        data = json.loads(response.text)
        return data

    @staticmethod
    def get_recent_data():
        """Getting recent COVID-19 data from the webscraping-tool """
        response = requests.post(f'https://www.parsehub.com/api/v2/projects/{PROJECT_TOKEN}/run',
                                 params={"api_key": API_KEY})
        data = json.loads(response.text)
        return data

    def poll(self):
        """Comparing the latest data from the web with the old data available"""
        time.sleep(0.1)
        old_data = self.data
        while True:
            latest_data = self.get_recent_data()
            if latest_data != old_data:  # Check if old data equals new data every 5 seconds
                self.data = latest_data
                print("Data Updated!")
                break
            time.sleep(5)

    def update_data(self):
        """Concurrently updating data to the latest values from the web"""

        # Run the voice assistant on one thread and update the information on another
        new_thread = threading.Thread(target=self.poll)
        new_thread.start()

    def get_country_data(self, country):
        countries_list = self.data['country']
        country_data = {}
        for country_details in countries_list:
            if country_details['name'].lower() == country.lower():
                country_data = country_details
                break
        return country_data

    def get_world_data(self):
        world_data = self.data['total']
        return world_data

    def get_list_of_countries(self):
        countries_list = []
        for country_details in self.data['country']:
            countries_list.append(country_details['name'].lower())
        return countries_list

    def get_country_cases(self, country):
        """Gives the total number of cases in a country
        : param country: name of the country"""
        country_data = self.get_country_data(country)
        count = country_data['total_cases']
        self.covid_bot.speak("The total number of cases in this country are %s" % count)

    def get_country_deaths(self, country):
        """Gives the total number of deaths in a country
        : param country: name of the country"""
        country_data = self.get_country_data(country)
        count = country_data['total_deaths']
        self.covid_bot.speak("The total number of deaths in this country are %s" % count)

    def get_country_recovered(self, country):
        """Gives the total number of recovered cases in a country
        : param country: name of the country"""
        country_data = self.get_country_data(country)
        count = country_data['total_recovered']
        self.covid_bot.speak("The total number of recovered cases in this country are %s" % count)

    def get_country_active_cases(self, country):
        """Gives the number of active cases in a country
        : param country: name of the country"""
        country_data = self.get_country_data(country)
        count = country_data['active_cases']
        self.covid_bot.speak("The number of active cases in this country are %s" % count)

    def get_total_cases(self):
        """Gives the total number of cases in the world"""
        world_data = self.get_world_data()
        count = world_data['total_cases']
        self.covid_bot.speak("The total number of cases in the world are %s" % count)

    def get_total_deaths(self):
        """Gives the total number of deaths in the world"""
        world_data = self.get_world_data()
        count = world_data['total_deaths']
        self.covid_bot.speak("The total number of deaths in the world are %s" % count)

    def get_total_recovered(self):
        """Gives the total number of recovered cases in the world"""
        world_data = self.get_world_data()
        count = world_data['total_recovered']
        self.covid_bot.speak("The total number of recovered cases in the world are %s" % count)

    def get_total_active_cases(self):
        """Gives the number of active cases in the world"""
        world_data = self.get_world_data()
        count = world_data['active_cases']
        self.covid_bot.speak("The number of active cases in the world are %s" % count)
