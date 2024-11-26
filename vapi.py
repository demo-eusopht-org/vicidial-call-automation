import requests

def create_vapi_call(customer_number, customer_name, customer_email):
    if not customer_number or customer_number.strip() == "":
        print("Customer number is empty") 
        return {"message": "Customer number is empty", "error": ""}
    url = "https://api.vapi.ai/call"
    headers = {"Authorization": "Bearer 20808f42-f66c-4f01-8675-9c9d7f6e74ff","Content-Type": "application/json"}
    body = {
        "assistantId": "de0203b2-c5a3-4aab-a7c0-2869d04b3eb6",
        "assistantOverrides": {"firstMessage": f"Hello {customer_name}, this is Abid from Symmetry.I am calling you from Sales and Promotions department.How are you doing today ?","variableValues": {"email": customer_email}},
        "phoneNumberId": "49855077-f83e-4e21-8f03-80a7c452df6d",
        "customer": {"number": customer_number}
    }
        
    try:
        response = requests.post(url, json=body, headers=headers)
        response_data = response.json()
        print("API Response:", response_data)
        return response_data
    except Exception as e:
        print("Error in vAPI call:", e)
        return {"message": "Error in API call", "error": str(e)}

def make_call():
    customer_number = "+923422793234"
    customer_name = "Talha"
    customer_email = "talhahaider074@gmail.com"
    
    if not customer_number or customer_number.strip() == "": print({"message": "Customer number is missing", "error": ""})
    else: 
        create_call_res = create_vapi_call(customer_number, customer_name, customer_email)
        print("Response:", create_call_res)


make_call()


# Hi. This is Abid calling you from ____________ (Company Name) Sales and Promotions department. How are you doing today sir/mam?
# Reason for this call is that we are offering a wonderful discount for our loyal and existing customers in which we are offering you each pair of jeans in just 1900 only.
# I believe you are spending more than that.
# If customer is okay till now then ask them that how much are they spending monthly on clothing and for how many items?
# If they say a number higher than 1900 per item, say something like thats really high number.
# Well we can surely provide you discount on your next purchase. Please confirm me the number(209xxxxxxx) which is showing on my screen is that your landline or mobile phone number.
# And then say let me just transfer this call to my supervisor he will guide you better regarding this.