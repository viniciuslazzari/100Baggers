from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


def start_driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver


def click_input(driver):
    widgetFieldDateRange = driver.find_element_by_xpath(
        '//*[@id="widgetFieldDateRange"]')
    widgetFieldDateRange.click()


def populate_date(driver):
    startDate = driver.find_element_by_xpath(
        '//*[@id="startDate"]')

    startDate.clear()
    startDate.send_keys("01/01/2002")


def submit(driver):
    applyBtn = driver.find_element_by_xpath(
        '//*[@id="applyBtn"]')

    applyBtn.click()


def return_max(driver):
    maxLabel = driver.find_element_by_xpath(
        '//*[@id="placehereresult2"]/tbody/tr/td[1]/span')

    max = maxLabel.text
    return max


def return_min(driver):
    minLabel = driver.find_element_by_xpath(
        '//*[@id="placehereresult2"]/tbody/tr/td[2]/span')

    min = minLabel.text
    return min


def return_title(driver):
    title = driver.find_element_by_xpath(
        '//*[@class="instrumentHeader"]/h2').text
    return title


def main():
    with open('links.txt') as f:
        lines = f.readlines()

        lines[-1] = lines[-1] + ' '

        arr = []

        for line in lines:
            arr.append(line[:-1] + "-historical-data")

        f.close()

    with open('prices.txt', 'w') as f:
        driver = start_driver()

        for line in arr:
            driver.get(line)

            try:
                click_input(driver)

                populate_date(driver)

                submit(driver)

                time.sleep(5)

                alta = return_max(driver)
                baixa = return_min(driver)
                title = return_title(driver)

                text = title[0: 5] + " " + baixa + " " + alta + "\n"

                f.write(text)
            except Exception as err:
                print(err)

        driver.quit()


if __name__ == "__main__":
    main()
