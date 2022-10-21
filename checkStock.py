import requests
import json
from scrap import WebDriver

# SKU for PS5 Disc is 15689336 , digital is 15689335

checkAllPS5Stock='https://www.bestbuy.ca/ecomm-api/availability/products?accept=application%2Fvnd.bestbuy.simpleproduct.v1%2Bjson&accept-language=en-CA&locations=62%7C931%7C927%7C977%7C203%7C617%7C965%7C237%7C57%7C943%7C956%7C932%7C938%7C200%7C937%7C202%7C795%7C916%7C544%7C910%7C954%7C207%7C926%7C223%7C233%7C930%7C622%7C925%7C985%7C245%7C949%7C990%7C959&postalCode=M4P1S2&skus=15689336%7C15689335'
ItemAvailableInStore='https://www.bestbuy.ca/ecomm-api/availability/products?accept=application%2Fvnd.bestbuy.standardproduct.v1%2Bjson&accept-language=en-CA&locations=62%7C931%7C927%7C977%7C203%7C617%7C965%7C237%7C57%7C943%7C956%7C932%7C938%7C200%7C937%7C202%7C795%7C916%7C544%7C910%7C954%7C207%7C926%7C223%7C233%7C930%7C622%7C925%7C985%7C245%7C949%7C990%7C959&postalCode=M4P1S2&skus=15689336'
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'} 
webhook ="YOUR DISCORD WEBHOOK HERE"

response = requests.get(checkAllPS5Stock,headers = header)

PS5_DIGIT = {"sku":"15689335","url":"https://www.bestbuy.ca/en-ca/product/playstation-5-digital-edition-console/15689335"}
PS5_DISC = {"sku":"15689335","url":"https://www.bestbuy.ca/en-ca/product/playstation-5-console/15689336"}

decoded_data=response.text.encode().decode('utf-8-sig') 
data = json.loads(decoded_data)

for i in data['availabilities']:
    if i['pickup']['status'] == "InStock" and i['pickup']['purchasable'] == True:
        resp = requests.get(ItemAvailableInStore,headers=header)
        decoded_resp = resp.text.encode().decode('utf-8-sig')
        stock = json.loads(decoded_resp)
        for j in stock['availabilities'][0]['pickup']['locations']:
            if j['hasInventory'] == True:
                # Inform user in discord about the store and stock  

                webhookHeader = {'Content-Type':'application/json'}
                body = {'attachments':[],'content':f"Restock Alert!!!!, {j['name']} is available in store now with quantity of {j['quantityOnHand']}!!",'embeds':None}
                jsonbody = json.dumps(body)
                discordResp = requests.post(webhook, headers=webhookHeader, data=jsonbody)             

    # use selenium to purchase the ps5 if it is available online
    if i['shipping']['status'] == "InStock" and i['shipping']['purchasable'] == True:
        if __name__ == '__main__':    
            
            if i['sku'] == PS5_DIGIT['sku']:
                    webdriver = WebDriver(PS5_DIGIT['url'])
                    webdriver.openDriver()
                    break
                    
            else:
                    webdriver = WebDriver(PS5_DISC['url'])
                    webdriver.openDriver()
                    break