from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import csv
import os


def main():
    driver = get_driver()


def get_driver():
    # set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    # options.add_argument("--incognito")

    url = "http://itaxhelp.kra.go.ke/itaxhelp/scp/tickets.php?id="

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    # input username
    # userName = driver.find_element("id", "name")
    try:
        userName = driver.find_element("xpath", '//*[@id="name"]')
    except NoSuchElementException:
        userName = driver.find_element("id", "name")

    # input password
    # password = driver.find_element("id", "pass")
    password = driver.find_element(by="xpath", value='//*[@id="pass"]')

    # click log In button
    # logIn_button = driver.find_element("name", "submit")
    logIn_button = driver.find_element(by="xpath", value='//*[@id="loginBox"]/form/fieldset/input[3]')

    # enter username
    userName.send_keys("T35829707")

    # enter password
    password.send_keys("@Oliverkra")

    # click log in
    # logIn_button.click()
    logIn_button.send_keys(Keys.RETURN)

    ticket_numbers = [62527,62621,62654,62729,62774,62794,62837,62880,62915,62930,62971,62983,62995,63129,63229,63262,63267,63272,63278,63294,63447,63655,63760,
    63831,63856,64007,64014,64038,64047,64178,64213,64215,64236,64239,64249,64348,64362,64363,64459,64496,64499,64563,64586,64640,64711,64757,
    64847,64855,64938,65004,65011,65023,65044,65048,65086,65088,65145,65161,65170,65175]

    for ticket in ticket_numbers:

    # for ticket in range(67664, 67679):
        
        url = 'http://itaxhelp.kra.go.ke/itaxhelp/scp/tickets.php?id=' + str(ticket)
        driver.get(url)

        try:
            ticket = driver.find_element('xpath', '/html/body/div[1]/div[2]/div/table[1]/tbody/tr/td[1]/h2/a').text
            status = driver.find_element('xpath', '/html/body/div[1]/div[2]/div/table[2]/tbody/tr/td[1]/table/tbody/tr[1]/td').text
            create_date = driver.find_element('xpath', '/html/body/div[1]/div[2]/div/table[2]/tbody/tr/td[1]/table/tbody/tr[4]/td').text
            subject = driver.find_element('xpath', '/html/body/div[1]/div[2]/div/h2').text
            officer_assigned = driver.find_element('xpath', '/html/body/div[1]/div[2]/div/table[3]/tbody/tr/td[1]/table/tbody/tr[1]/td').text
            issue_category = driver.find_element('xpath', '/html/body/div[1]/div[2]/div/table[3]/tbody/tr/td[2]/table/tbody/tr[1]/td').text
            closed_date = driver.find_element('xpath', '/html/body/div[1]/div[2]/div/table[3]/tbody/tr/td[1]/table/tbody/tr[3]/td').text

            status = status.upper()

            folder_path = "D:\python\WebScraping\job_scripts"

            if status == 'OPEN':
                file_path = os.path.join(folder_path, "scraped.csv")
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                with open(file_path, "a" , newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([ticket[8:], status, create_date[:10], subject, officer_assigned, issue_category])
            elif status == 'CLOSED':
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                with open(file_path, "a" , newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([ticket[8:], status, closed_date[:10], subject, officer_assigned, issue_category])

        except NoSuchElementException:
            file_path = os.path.join(folder_path, "unscraped.csv")
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            with open(file_path, "a" , newline='') as file:
                writer = csv.writer(file)
                writer.writerow([ticket])

    return driver


if __name__ == "__main__":
    main()



