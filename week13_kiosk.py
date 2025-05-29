# open api : wttr.in (weather info)
import kiosk as kk
import requests

if __name__ == "__main__":
    url = f"https://wttr.in/suwon?format=%C+%t&lang=ko"
    response = requests.get(url)
    print(response.text.strip())# 습관적으로 .strip() 하는게 좋음
    kk.run()
    kk.print_receipt()
    kk.print_ticket_number()

