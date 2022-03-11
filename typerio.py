import time
import pyautogui
import argparse
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager 

if __name__ == "__main__":
    parser=argparse.ArgumentParser(description="This is script to type faster on typer.io.")
    parser.add_argument("-t",default=20,type=int,help="Time delay in second(Default=20sec)")
    parser.add_argument("-u",help="Enter your URL(Default=typer.io)",default="https://typer.io/")
    parser.add_argument("-s",default=0.05,help="Enter your interval to do speed typing(Default=0.05sec)")

    args=parser.parse_args()
    speed=float(args.s)
    URL=args.u
    TIM=args.t

    # Downloading and setting path for chrome Driver
    options=webdriver.ChromeOptions()
    chrome_driver_path=ChromeDriverManager().install()
    driver=webdriver.Chrome(chrome_driver_path,options=options)
    
    # options=webdriver.FirefoxOptions()
    # firefox_driver_path=GeckoDriverManager().install()
    # driver=webdriver.Firefox(firefox_driver_path,options=options)
   
    driver.get(URL)

    time.sleep(TIM)

    i=0
    for i in range(200):
        word=driver.find_elements_by_id("word-" +str(i)+"")
        for letter in word:
            letters=letter.text
            pyautogui.typewrite(letters,interval=speed)
            pyautogui.press('space')
        i=i+1






