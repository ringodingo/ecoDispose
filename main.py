#python3 -m venv .venv in directory
#source .venv/bin/activate (EVERY TIME LOADING IN TO CONSOLE)
#pip install uk_postcodes_parsing

import re
import time
from datetime import datetime, date, timedelta
import uk_postcodes_parsing.ukpostcode as pcparsenval
import uk_postcodes_parsing.postcode_database as pcdist

EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

def get_valid_date(prompt="Enter a date (DD-MM-YYYY): "):
    while True:
        date_input = input(prompt).strip()
        try:
            # Parse the string matching the specific format
            valid_date = datetime.strptime(date_input, "%d-%m-%Y").date()
            return valid_date
        except ValueError:
            print("❌ Invalid date or format. Please use DD-MM-YYYY (e.g., 28-09-2026).")

#welcomenote
print("Welcome to greenTech EcoDispose, we follow the WEEE Directive and are here to provide more information")
#GDPR
print("The personal information shared with us is held only for localised data processing and stored securely, we do not share or sell information, you can contact us at privacy@greentech.org to request data removal, for our more detailed privacy policy please access https://www.greentech.org/privacypolicy")
#softwareuse
print("By using this software you affirm you are doing so safely and securely and confirm you abide to our terms of use, available at https://www.greentech.org/ecotos\n")
#Name input
print("Your name is only used for this local session if you do not have an account with us and are not logged in.\n")
name=input("Please enter your name:")
if name.isalpha():
    #need to add name loop
    #print("\nThanks for visiting " + name.upper() + "!")
    print("\nThanks for visiting " + name.capitalize() + "!")
else:
    print("\nYou entered " + name.capitalize() + ", please check and try again, if you are having issues, please contact us on 01234 567890, we do not manually process quotes over the phone.")
    exit()

age=int(input("What is your age? "))

#should add validation error message regarding wrong data being entered instead of numerical
print("\nYou are " + str(age))
if age >= int("70") and age <= int("104"):
    print("\nPlease give us a call on 01223 477652")
    exit()
elif age >= int("105"):
    print("You're past a centennial, impressive, please call us on 01223 477652")
    exit()
elif age <= int("17"):
    print("\nSorry you are too young to use this service on your own, please speak to a parent or guardian")
    exit()

region=input("Please enter your full postcode? ")
pc=pcparsenval.parse_from_corpus(region)
if not pcparsenval.is_in_ons_postcode_directory(region):
    print("\nYou did not enter a valid postcode, " + region.upper() + ", Please try again")
    exit()
for pc2 in pc:
    location=pcdist.lookup_postcode(pc2.postcode)
    if location:
        #future planning for these is to integrate what3words for easier positioning and also wire in the uk_postcodes_parsing co-ordinates - future proofing opportunity for web ui display would be to link out via QR code for phone to scan and open on map too
        print(f"\nGreat we have you as in {location.county}, within the {location.district} district")
        print("\nWe have dedicated recycling points within the " +location.district.capitalize() + " area")
        if location.county == "Essex":
            print(f"\n{location.county} County Council' waste and recycling scheme is known as Love Essex; greenTech exceed their conformity levels when it comes to WEEE recycling")
            print(f"\nLove Essex hold a partnership between all their districts, further information can be found at https://www.loveessex.org/waste-strategy-essex/essex-waste-partnership")
            print(f"\nYou can find recycling centres within the Essex Area at https://www.loveessex.org/find-recycling-centre")
            if location.district == "Maldon":
                print(f"\nOur hub can be accessed Mon - Fri between 10am - 3pm at CM9 5HZ | W3W address ///issues.backtrack.mentions")
                print(f"\n{location.district} Council have a recycling facility at Park Drive, CM9 5UR | W3W - ///compliant.enveloped.winded")
                # future proofing here would be to webscrape opening and closing times with auto-update, Maldon council site has varying times for Summer and Winter so would add variables per etc.
                print(f"\n{location.district} Councils opening times are currently 9am - 5pm you can find out more information and book to access at https://www.loveessex.org/find-recycling-centre/maldon-recycling-centre")
            elif location.district == "Colchester":
                print(f"\nOur dedicated hub can be accessed Mon - Fri between 10am - 3pm at CM9 5HZ | W3W ///issues.backtrack.mentions")
                print(f"\n{location.district} Council have a recycling facility at 221 Shrub End Road, CO3 4RN | W3W - ///appeal.trunk.zips")
                # future proofing here would be to webscrape opening and closing times with auto-update, Maldon council site has varying times for Summer and Winter so would add variables per etc.
                print(f"\n{location.district} Council opening times are currently 9am - 5pm you can find out more information and book to access at https://www.loveessex.org/find-recycling-centre/colchester-recycling-centre")
            elif location.district == "Basildon":
                print(f"\nOur hub can be accessed Mon - Fri between 10am - 3pm at CM9 5HZ | W3W address ///issues.backtrack.mentions")
                print(f"\n{location.district} Council have a recycling facility at Pitsea Hall Lane, SS16 4UH | W3W - ///finest.flies.lazy")
                # future proofing here would be to webscrape opening and closing times with auto-update, Maldon council site has varying times for Summer and Winter so would add variables per etc.
                print(f"\n{location.district} Council' opening times are currently 9am - 5pm you can find out more information and book to access at https://www.loveessex.org/find-recycling-centre/pitsea-recycling-centre")
    else:
        print("\nSorry we don't seem to recognise your area, not to worry we can still help, please continue to enter your details below. If you only need recycling points, call us on 01223 456553")

#need to change this to a loop
email=input("\nWhat is your email address? ")
if re.match(EMAIL_REGEX, email):
    print("\nThanks, your email is " +email)
else:
    print("\nThere seems to be an error in how you have input email, please try again " +name+ ", you entered: " +email)
    exit()
#must include the 'Print' function, either .lower, .upper or .capitalise. Also the use of a variable and also If, elif or else function. You can use 
#For loop and While loop as extra functions as a challenge addition to your computer program. You must include information about the WEEE Directive, 
# GDPR statement and some form of health and safety guidance such as the safe recycling of batteries perhaps.

#Item Questions
Q1=input("\nDo you have items that you want to see if there is possible resale value? Yes / No ")
#Q3=input("Please confirm the item type and quantity")
count=0
addingdays=6
if Q1.lower()=="no":
    #should look to simplify repetition here too
    Q3=input("\nOK, what kind of disposal method do you want? Enter 1 for a WEEE Skip (8 Yards Due to Max Weight) | 2 for a Compactor (No Bulky Items i.e. Fridges / CRT televisions, NO PRODUCTS CONTAINING GASES) | 3 for a Dust Cart - Best for large items, boxed items etc. | 4 for Bags & Boxes to be provided ")
    if Q3=="1":
        deldate= get_valid_date(f"\nPlease Enter Your Required Delivery Date (we need min 5 days to schedule, your earliest date will be {date.today() + timedelta(days=addingdays):%B %d, %Y}, if this is an issue, please call on 01234 567890) ")
        print("\nThanks, give us a few hours to review and get a price back to you")
    elif Q3=="2":
        deldate= get_valid_date(f"\nPlease Enter Your Required Delivery Date (we need min 5 days to schedule, your earliest date will be {date.today() + timedelta(days=addingdays):%B %d, %Y}, if this is an issue, please call on 01234 567890) ")
        print("\nThanks, give us a few hours to review and get a price back to you")
    elif Q3=="3":
        deldate= get_valid_date(f"\nPlease Enter Your Required Delivery Date (we need min 5 days to schedule, your earliest date will be {date.today() + timedelta(days=addingdays):%B %d, %Y}, if this is an issue, please call on 01234 567890) ")
        print("\nThanks, give us a few hours to review and get a price back to you")
    elif Q3=="4":
        deldate= get_valid_date(f"\nPlease Enter Your Required Delivery Date (we need min 5 days to schedule, your earliest date will be {date.today() + timedelta(days=addingdays):%B %d, %Y}, if this is an issue, please call on 01234 567890) ")
        print("\nhanks, give us a few hours to review and get a price back to you")
    else:
        print("\n Please enter a value between 1 - 4")
    #q2/q3
elif Q1.lower()=="yes":
    print("\nOK, we will ask next whether items are non-working or working separately ")
    while Q1.lower:
        Q2=input("Item/'s broken or working, please enter 1 for broken or 2 for working? ")
        while Q2=="1":
            while count < 5:
                print("\n Thanks for confirming you have broken items, we will ask you what type of items now, max. of 5, if bulk please input a quantity of them too - include brand and model if available")
                input("What type of item? ")
                count += 1
                print (f"Item infilled: {count}/5")
            break
        while Q2=="2":
            while count < 5:
                print("\n Thanks for confirming you have working items, we will ask you what type of items now, max. of 5, if bulk please input a quantity of them too - include brand and model if available")
                input("What type of item? ")
                count += 1
                print (f"Item infilled: {count}/5")
                #print("Thanks, items listed and sent over to us, give us a few hours to review and get a price back to you")
            break
        print("Thanks, items listed and sent over to us, give us a few hours to review and get a price back to you, your reference is " + str(time.time()) + ", please note this down for any communication with us")
        break

else:
    print("Please answer yes or no")
