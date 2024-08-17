import phonenumbers
from phonenumbers import timezone, carrier,geocoder

#Enter your phone Number with country code

number=input("Enter Number:")

phone=phonenumbers.parse(number)

time=timezone.time_zones_for_number(phone)
carrier_name=carrier.name_for_number(phone,"en")
location=geocoder.description_for_number(phone,"en")

print("you want information:",number)
print("\n Time Zone :",time)
print("\n Carrier name:",carrier_name)
print("\n The number belong location:",location)