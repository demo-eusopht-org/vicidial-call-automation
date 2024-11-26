# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import Select
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# import time
# import requests

# # AUTO ENABLE MICROPHONE 
# chrome_options = Options()
# chrome_options.add_argument("--use-fake-ui-for-media-stream")


# #VAPI CALLING FEATURE
# def create_vapi_call(customer_number, customer_name, customer_email):
#     if not customer_number or customer_number.strip() == "":
#         print("Customer number is empty") 
#         return {"message": "Customer number is empty", "error": ""}
#     url = "https://api.vapi.ai/call"
#     headers = {"Authorization": "Bearer 20808f42-f66c-4f01-8675-9c9d7f6e74ff","Content-Type": "application/json"}
#     body = {
#         "assistantId": "de0203b2-c5a3-4aab-a7c0-2869d04b3eb6",
#         "assistantOverrides": {"firstMessage": f"Hello {customer_name}, this is Emily from Symmetry. I have an opportunity that I want to discuss with you. Do you have some time to talk?","variableValues": {"email": customer_email}},
#         "phoneNumberId": "49855077-f83e-4e21-8f03-80a7c452df6d",
#         "customer": {"number": customer_number}
#     }
        
#     try:
#         response = requests.post(url, json=body, headers=headers)
#         response_data = response.json()
#         print("API Response:", response_data)
#         return response_data
#     except Exception as e:
#         print("Error in vAPI call:", e)
#         return {"message": "Error in API call", "error": str(e)}

# def make_call():
#     customer_number = "+923422793234"
#     customer_name = "Talha"
#     customer_email = "talhahaider074@gmail.com"
    
#     if not customer_number or customer_number.strip() == "": print({"message": "Customer number is missing", "error": ""})
#     else: 
#         create_call_res = create_vapi_call(customer_number, customer_name, customer_email)
#         print("Response:", create_call_res)


# # SELENIUM AUTMOATION
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
# driver.get('https://ahucommunications.dialerlab.com:446/login.php')
# driver.maximize_window()
# wait = WebDriverWait(driver, 10)

# try:
#     username_field = wait.until(EC.element_to_be_clickable((By.ID, 'Jzr87Cp8XqJY')))
#     password_field = wait.until(EC.element_to_be_clickable((By.ID, 'WNK1WOrAvT1I')))
#     username_field.send_keys('6010')
#     password_field.send_keys('U97QvPF17')
#     login_button = wait.until(EC.element_to_be_clickable((By.NAME, 'submit')))
#     login_button.click()
#     anchor_tag = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Click Here']")))
#     anchor_tag.click()
#     agent_login_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Agent Login']")))
#     agent_login_link.click()
#     phone_login_feild_1 = wait.until(EC.element_to_be_clickable((By.NAME, 'phone_login')))
#     phone_login_feild_2 = wait.until(EC.element_to_be_clickable((By.NAME, 'phone_pass')))
#     phone_login_feild_1.send_keys('6010')
#     phone_login_feild_2.send_keys('U97QvPF17')
#     submit_button = wait.until(EC.element_to_be_clickable((By.ID, 'login_sub')))
#     submit_button.click()
#     campaign_login_feild_1 = wait.until(EC.element_to_be_clickable((By.NAME, 'VD_login')))
#     campaign_login_feild_2 = wait.until(EC.element_to_be_clickable((By.NAME, 'VD_pass')))
#     campaign_login_feild_1.send_keys('6010')
#     campaign_login_feild_2.send_keys('U97QvPF17')
#     click_select_box = wait.until(EC.element_to_be_clickable((By.ID, 'LogiNCamPaigns')))
#     click_select_box.click()
#     open_select_element = wait.until(EC.visibility_of_element_located((By.ID, 'VD_campaign')))
#     open_select_element.click()
#     time.sleep(3)
#     select_element = wait.until(EC.visibility_of_element_located((By.ID, 'VD_campaign')))
#     select = Select(select_element)
#     select.select_by_visible_text("Outbound - USA Outbound")
#     submit_capaign_button = wait.until(EC.element_to_be_clickable((By.ID, 'login_sub')))
#     submit_capaign_button.click()

#     try:
#         ok_anchor_tag = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "OK")))
#         ok_anchor_tag.click()
#         call_agent_webphone_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Call Agent Webphone ->")))
#         call_agent_webphone_link.click()
        
#     except:
#         call_agent_webphone_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Call Agent Webphone ->")))
#         call_agent_webphone_link.click()
#     time.sleep(2)

# finally:
#     input("Press Enter to close the browser...")
#     # driver.quit()



# CALLING 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

# AUTO ENABLE MICROPHONE 
chrome_options = Options()
chrome_options.add_argument("--use-fake-ui-for-media-stream")

# SELENIUM AUTOMATION
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get('https://ahucommunications.dialerlab.com:446/login.php')
driver.maximize_window()
wait = WebDriverWait(driver, 10)

def inject_js_for_button_click():
    # js_script = """
    # document.getElementById('dial').onclick = function() {
    #     const url = "https://api.vapi.ai/call";
    #     const headers = {
    #         "Authorization": "Bearer 20808f42-f66c-4f01-8675-9c9d7f6e74ff",
    #         "Content-Type": "application/json"
    #     };
    #     const body = JSON.stringify({
    #         "assistantId": "de0203b2-c5a3-4aab-a7c0-2869d04b3eb6",
    #         "assistantOverrides": {
    #             "firstMessage": "Hello Talha, this is Emily from Symmetry. I have an opportunity that I want to discuss with you. Do you have some time to talk?",
    #             "variableValues": {"email": "talhahaider074@gmail.com"}
    #         },
    #         "phoneNumberId": "49855077-f83e-4e21-8f03-80a7c452df6d",
    #         "customer": {"number": "+923422793234"}
    #     });

    #     fetch(url, {
    #         method: "POST",
    #         headers: headers,
    #         body: body
    #     })
    #     .then(response => response.json())
    #     .then(data => console.log("API Response:", data))
    #     .catch(error => console.error("Error in API call:", error));
    # };
    # console.log("Custom click handler injected for the 'dial' button.");
    # """
    js_script = """
    const dialButton = document.getElementById('dial');

    if (dialButton) {
        dialButton.addEventListener('click', function() {

            const url = "https://api.vapi.ai/call";
            const headers = {
                "Authorization": "Bearer 20808f42-f66c-4f01-8675-9c9d7f6e74ff",
                "Content-Type": "application/json"
            };
            const body = JSON.stringify({
                "assistantId": "de0203b2-c5a3-4aab-a7c0-2869d04b3eb6",
                "assistantOverrides": {
                    "firstMessage": "Hello Talha, this is Emily from Symmetry. I have an opportunity that I want to discuss with you. Do you have some time to talk?",
                    "variableValues": {"email": "talhahaider074@gmail.com"}
                },
                "phoneNumberId": "49855077-f83e-4e21-8f03-80a7c452df6d",
                "customer": {"number": "+923422793234"}
            });

            fetch(url, {
                method: "POST",
                headers: headers,
                body: body
            })
            .then(response => response.json())
            .then(data => console.log("API Response:", data))
            .catch(error => console.error("Error in API call:", error));

            console.log("API call triggered by button click.");
        });
    }
    """
    driver.execute_script(js_script)

# Automate login and navigate to the button
try:
    username_field = wait.until(EC.element_to_be_clickable((By.ID, 'Jzr87Cp8XqJY')))
    password_field = wait.until(EC.element_to_be_clickable((By.ID, 'WNK1WOrAvT1I')))
    username_field.send_keys('6010')
    password_field.send_keys('U97QvPF17')
    login_button = wait.until(EC.element_to_be_clickable((By.NAME, 'submit')))
    login_button.click()

    anchor_tag = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Click Here']")))
    anchor_tag.click()
    agent_login_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Agent Login']")))
    agent_login_link.click()

    phone_login_field_1 = wait.until(EC.element_to_be_clickable((By.NAME, 'phone_login')))
    phone_login_field_2 = wait.until(EC.element_to_be_clickable((By.NAME, 'phone_pass')))
    phone_login_field_1.send_keys('6010')
    phone_login_field_2.send_keys('U97QvPF17')
    submit_button = wait.until(EC.element_to_be_clickable((By.ID, 'login_sub')))
    submit_button.click()

    campaign_login_field_1 = wait.until(EC.element_to_be_clickable((By.NAME, 'VD_login')))
    campaign_login_field_2 = wait.until(EC.element_to_be_clickable((By.NAME, 'VD_pass')))
    campaign_login_field_1.send_keys('6010')
    campaign_login_field_2.send_keys('U97QvPF17')
    click_select_box = wait.until(EC.element_to_be_clickable((By.ID, 'LogiNCamPaigns')))
    click_select_box.click()

    open_select_element = wait.until(EC.visibility_of_element_located((By.ID, 'VD_campaign')))
    open_select_element.click()
    time.sleep(3)

    select_element = wait.until(EC.visibility_of_element_located((By.ID, 'VD_campaign')))
    select = Select(select_element)
    select.select_by_visible_text("Outbound - USA Outbound")
    submit_campaign_button = wait.until(EC.element_to_be_clickable((By.ID, 'login_sub')))
    submit_campaign_button.click()

    try:
        ok_anchor_tag = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "OK")))
        ok_anchor_tag.click()
        call_agent_webphone_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Call Agent Webphone ->")))
        call_agent_webphone_link.click()
    except:
        call_agent_webphone_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Call Agent Webphone ->")))
        call_agent_webphone_link.click()

    # Inject the JavaScript to handle the button click
    # inject_js_for_button_click()
    print("JavaScript injected to replace button functionality.")

finally:
    input("Press Enter to close the browser...")
    driver.quit()
