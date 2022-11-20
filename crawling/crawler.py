import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from utils import find_element, find_elements, waiting_element, save_csv


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()


def main():
    base_path = lambda page: f"https://www.chotot.com/mua-ban-do-dien-tu?page={page}"
    posts = list()
    sellers = list()
    done = list()

    for page in range(1, 2):
        driver.get(base_path(page))
        waiting_element(driver, "#__next")

        elem_post = find_elements(driver, ".AdItem_adItem__USIDA")
        post_links = [e.get_attribute('href') for e in elem_post]

        for link in post_links:
            driver.get(link)
            waiting_element(driver, "#__next")

            try:
                layers = find_element(driver, "#layers")
                if layers:
                    layers.click()
            except:
                pass

            # get user profile
            username = find_element(driver, ".SellerProfile_nameDiv__utFTB").text

            elem_phone_number = waiting_element(driver, ".sc-EHOje")
            elem_phone_number.click()
            phone_number = find_element(driver, ".sc-ifAKCX").text

            address = find_element(driver, ".AdParam_address__my_OK").text

            user = {
                "username": username,
                "phone_number": phone_number,
                "address": address
            }
            sellers.append(user)

            # get post info
            title = find_element(driver, ".AdDecription_adTitle__8l66m").text
            price = find_element(driver, ".AdDecription_price__pr_W7").text
            desc = find_element(driver, ".AdDecription_adBody__Ab_tS").text

            elem_imgs = find_elements(driver, 'img[role="presentation"]')
            imgs = list(set([e.get_attribute('src') for e  in elem_imgs]))

            post = {
                "title": title,
                "price": price,
                "imgs": imgs,
                "desc": desc,
            }
            posts.append(post)

            print("[DONE]", link)
            done.append(link)

            time.sleep(2)

    save_csv(sellers, "./data/sellers.csv")
    save_csv(posts, "./data/posts.csv")

    with open("./data/page.log", "w", encoding='utf-8') as f:
        f.write('\n'.join(done))


if __name__ == "__main__":
    main()