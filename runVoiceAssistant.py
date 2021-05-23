from VoiceRecognition import *
from DataHandler import *
import re

covid_bot = VoiceAssistant()
welcome_prompt = "Welcome to COVID-19 Voice Assistance!"
update_phrase = "update"
end_phrase = ["no", "bye", "stop", "quit", "close", "thank you", "thanks"]

covid_bot.speak(welcome_prompt)

data_handler = DataHandler(API_KEY, PROJECT_TOKEN)
country_list = data_handler.get_list_of_countries()

# Look for REGEX patterns in the voice
WorldPatterns = {
    re.compile("[\w\s]+ total[\w\s]+ cases"): data_handler.get_total_cases,
    re.compile("[\w\s]+ total[\w\s]+ deaths"): data_handler.get_total_deaths,
    re.compile("[\w\s]+ total[\w\s]+ recovered"): data_handler.get_total_recovered,
    re.compile("[\w\s]+ total[\w\s]+ active[\w\s]+ cases"): data_handler.get_total_active_cases,
}

CountryPatterns = {
        re.compile("[\w\s]+ cases [\w\s]+"): lambda country: data_handler.get_country_cases(country),
        re.compile("[\w\s]+ deaths [\w\s]+"): lambda country: data_handler.get_country_deaths(country),
        re.compile("[\w\s]+ recovered [\w\s]+"): lambda country: data_handler.get_country_recovered(country),
        re.compile("[\w\s]+ active+[\w\s]+cases[\w\s]+"): lambda country: data_handler.get_country_active_cases(country)
}

while True:
    print("Listening...")
    input_text = covid_bot.get_audio()
    print(input_text)

    for phrase in end_phrase:
        if input_text.find(phrase) != -1:
            covid_bot.speak("Stay safe! Bye")
            print("Turning off Voice Assistant! ")
            exit(0)

    for pattern, func in CountryPatterns.items():
        if pattern.match(input_text):
            words = set(input_text.split(" "))
            for country in country_list:
                if country in words:
                    result = func(country)
                    break

    for pattern, func in WorldPatterns.items():
        if pattern.match(input_text):
            result = func()
            break

    if input_text == update_phrase:
        update_prompt = "COVID-19 data is being updated. Please wait! The updation process may take a while."
        covid_bot.speak(update_prompt)
        data_handler.update_data()
    covid_bot.speak('Do you have any more questions for me? Please ask ..')






