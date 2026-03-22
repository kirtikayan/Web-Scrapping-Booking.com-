from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
import random

mumbai = 'https://www.booking.com/searchresults.en-gb.html?ss=Mumbai&ssne=New+Delhi&ssne_untouched=New+Delhi&label=gen173nr-1BCAEoggI46AdIM1gEaGyIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4AueF3b0GwAIB0gIkMjFkYTVhYTMtZWM5ZC00ZmYyLTkzMDktZjUxN2IxMzVjZTdk2AIF4AIB&sid=e926d54c76bc20f9416c4f573131702a&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=searchresults&dest_id=-2092174&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=bb7575c39e5206d2&ac_meta=GhBiYjc1NzVjMzllNTIwNmQyIAAoATICZW46Bk11bWJhaUAASgBQAA%3D%3D&checkin=2025-04-01&checkout=2025-04-02&group_adults=2&no_rooms=1&group_children=0&flex_window=1'


def scrape_booking(url, filename):
    driver = webdriver.Chrome()
    driver.get(url)

    print("Opening browser...")
    num = random.randint(3,7)
    time.sleep(num)  

    hotels = driver.find_elements(By.XPATH, '//div[@data-testid="property-card"]')

    with open(f"{filename}.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Hotel Name", "Price", "Rating", "Link"])

        for hotel in hotels:
            try:
                name = hotel.find_element(By.XPATH, './/div[@data-testid="title"]').text
            except:
                name = "NA"

            try:
                price = hotel.find_element(By.XPATH, './/span[@data-testid="price-and-discounted-price"]').text
            except:
                price = "NA"

            try:
                rating = hotel.find_element(By.XPATH, './/div[@data-testid="review-score"]').text
            except:
                rating = "NA"

            try:
                link = hotel.find_element(By.XPATH, './/a').get_attribute("href")
            except:
                link = "NA"

            writer.writerow([name, price, rating, link])

    print("Scraping done!")
    driver.quit()


if __name__ == "__main__":
    url = input("Enter URL: ")
    filename = input("Enter file name: ")

    scrape_booking(url, filename)