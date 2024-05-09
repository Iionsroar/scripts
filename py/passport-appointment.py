# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
from selenium import webdriver
import os
import time


FF_PROFILE_DIR = r"C:\Users\halloween\AppData\Local\Programs\Python\Python39\Scripts"
FF_PROFILE = webdriver.FirefoxProfile(profile_directory=FF_PROFILE_DIR)

browser = webdriver.Firefox()
# browser = webdriver.Firefox(FF_PROFILE, service_log_path=r"C:\Users\halloween\AppData\Local\Programs\Python\Python39\Scripts\geckodriver.log")

AREA_VALUES = {'malolos': '489',
			'novaliches': '423',
			'manila-aseana': '4',
			'baguio': '12',
			'pangasinan': '16',
			'pampanga-1': '10',
			'pampanga-2': '27',
			'sm-manila' :'9'}

def schedule(office_code, group=True):
	while True:
		try:
			if group:
				browser.get("https://www.passport.gov.ph/appointment/individual/site")
			else:
				browser.get("https://www.passport.gov.ph/appointment")
			break
		except:
			continue


	# if group:
		# time.sleep(10)
		# tc = browser.find_element_by_id("agree")
		# tc.click()
		# START_INDIV_APP_TEXT_KEYS = ['Start Individual', 'Start individual', 'START INDIVIDUAL', 'start individual']
		# START_GROUP_APP_TEXT_KEYS = ['Start Group', 'Start group', 'START GROUP', 'start group']
		# keys = START_GROUP_APP_TEXT_KEYS if group else START_INDIV_APP_TEXT_KEYS

		# start = None
		# for text_key in keys:
		# 	try:
		# 		start = browser.find_element_by_partial_link_text(text_key)
		# 		break
		# 	except:
		# 		continue 
		# start.click()

		# time.sleep(3)
		# num_applicants = browser.find_element_by_id("numberOfApplicants")
		# num_applicants.send_keys("3")
		# submit = browser.find_element_by_css_selector("div.col-sm-6:last-child button")
		# submit.click()

	time.sleep(3)
	while True:
		print("ye yo stuck")
		try:
			dfa_center = browser.find_element_by_css_selector(f"#SiteID option[value='{office_code}']")
			dfa_center.click()
			submit = browser.find_element_by_css_selector("button[value='next']")
			submit.click()
			break
		except:
			browser.quit()
			browser = webdriver.Firefox(FF_PROFILE, service_log_path=r"C:\Users\halloween\AppData\Local\Programs\Python\Python39\Scripts\geckodriver.log")
			browser.get("https://www.passport.gov.ph/appointment/individual/site")
			continue


	time.sleep(3)
	available = browser.find_element_by_id("earliest-available")
	if not 'No available date' in available.text:
		os.chdir(r"C:\Users\halloween\AppData\Local\Programs\Python\Python39\Scripts\gmail_scripts")
		os.system("python gmail_quickstart.py") 
		time.sleep(420)

	return available.text

for i in range(100):
	print('\n')
	for area in AREA_VALUES.keys():
		print(f'{area.capitalize()}: {schedule(AREA_VALUES[area], group=False)}')
	print('\n')
	time.sleep(60)

browser.quit()

# print('\n')
# for area in AREA_VALUES.keys():
# 	print(f'{area.capitalize()}: {schedule(AREA_VALUES[area])}')
# print('\n')
