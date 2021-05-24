# Coronavirus Voice Assistant

This app makes use of [ParseHub](https://www.parsehub.com/) which is a powerful web-scraping tool.

The data is extracted from the very popular website [Worldometers](https://www.worldometers.info/coronavirus/) that provides the accurate information about the COVID19 disease worldwide.

---

Steps to be followed:

1. Download [ParseHub](https://www.parsehub.com/quickstart).
2. Start a New Project and paste the link 'https://www.worldometers.info/coronavirus/'.
3. Select the items that you would like to scrape from the page and assign unique tags to each one of them. Get the data.
4. Set the api key, project token and run token as the environment variables in your IDE.
5. Install the required python modules mentioned in **requirements.txt**
6. Execute **runVoiceAssistant.py file**

---

Steps to run the application:

1. Execute the command "runVoiceAssistant.py"
2. Ask the assistant for "number of recovered cases in India", "total cases in India", etc.
3. For updating the information, say "update" and wait for a while.
4. Say "bye" to exit the application.

---


