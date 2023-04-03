import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#TODO: replace time elements with a variable for click, type, etc and have a random range


def browser_bot(row):
    first_name = row[0]
    last_name = row[1]
    email_address = row[9]
    phone_home = str(row[2])
    address = row[3]
    city = row[4]
    state = row[5]
    zip_code = str(row[6])

    # Create a Service object with the path to the chromedriver executable
    service = Service('./chromedriver111.exe')

    # Launch the Chrome browser with the Service object
    driver = webdriver.Chrome(service=service)

    try:


        # Navigate to Google
        driver.get('https://Ready4solar.com')

        time.sleep(2)

        # Find the zipcode input element by id
        zip_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'zip_code'))
        )

        # Enter a zipcode value
        zip_input.send_keys(zip_code)
        time.sleep(1.23)

        # Locate the First Continue Button
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div[2]/div/div[2]/div/form/div[2]/input'))
        )
        button.click()
        time.sleep(2)

        driver.get('https://ready4solar.com/start-now/?zip_code=${zip_code}&campaign_id=&lp_request_id=&utm_source=&utm_medium=&utm_campaign=&utm_term=&utm_content=&fb_page_id=&fb_ad_id=&fb_ad_name=&fb_adset_id=&fb_adset_name=&fb_campaign_id=&fb_campaign_name=&fb_form_id=')

        # Locate the Family House Yes radio button and click it
        input_element = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div[2]/div/form/div[2]/div[1]/label/input')
        input_element.click()
        time.sleep(1.23)

        #Approximate shading of roof option select open
        input_element = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div[2]/div/form/div[2]/div[3]/div[1]/select/option[1]')
        input_element.click()
        time.sleep(4)

        #Continue Button
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div/div/div[2]/div/form/div[2]/div[3]/div[2]/input'))
        )
        button.click()
        time.sleep(3)



        # Locate the average monthly electric bill select : $101~200
        input_element = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div[2]/div/form/div[3]/div[1]/select/option[2]')
        input_element.click()
        time.sleep(1.23)

        # Locate the Name of Electric Utility Company : 4 Change
        input_element = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div[2]/div/form/div[3]/div[2]/select/option[2]')
        input_element.click()
        time.sleep(1.23)

        # Locate the Continue Button
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div/div/div[2]/div/form/div[3]/div[3]/input'))
        )
        button.click()
        time.sleep(3)

        ################# Contact Info pg 1 ##########################
        # Find the first name input element by id
        first_name_input = driver.find_element(By.ID, 'first_name')
        first_name_input.send_keys(first_name)
        time.sleep(1.23)

        # Find the last name input element by id
        last_name_input = driver.find_element(By.ID, 'last_name')
        last_name_input.send_keys(last_name)
        time.sleep(1.23)

        # Find the email input element by id
        email_address_input = driver.find_element(By.ID, 'email_address')
        email_address_input.send_keys(email_address)
        time.sleep(1.23)

        # Find the last name input element by id
        address_input = driver.find_element(By.ID, 'address')
        address_input.send_keys(address)
        time.sleep(1.23)

        # Find the email input element by id
        city_input = driver.find_element(By.ID, 'city')
        city_input.send_keys(city)
        time.sleep(1.23)

        # Find the state
        select_element = driver.find_element(By.ID, 'state')
        state_select = Select(select_element)
        state_select.select_by_value(state)
        time.sleep(1.23)
        
        # Find the first name input element by id
        phone_home_input = driver.find_element(By.ID, 'phone_home')
        phone_home_input.send_keys(phone_home)

        # Zipcode is already defaulted from prior input

        # Locate the Submit Button
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div/div/div[2]/div/form/div[4]/div[9]/input'))
        )
        button.click()
        time.sleep(3)


        ################ Waiting for thank-you page load ###############
        start_time = time.time()
        while (time.time() - start_time) < 60:
            try:
                element = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, '//div[@class="header"][contains(text(), "Related Topics (Ads)")]')))
                # If element is found, do something
                # print("Element found!")
                status = True
                break
            except:
                # If element is not found, continue checking
                # print("Element not found, checking again...")
                time.sleep(1)

        # If the timer expires, end the program
        else:
            print("Timer expired, element not found.")
            status = False


        ################ End Browser Bot ###############
        time.sleep(20)
    except Exception as e:
        print(f"error: {e}")
        status = False

    try:
        # Close the browser
        driver.quit()
    except:
        print("error closing driver")

    return status
