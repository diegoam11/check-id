from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from unidecode import unidecode
import time
from src.database.tables.student import Student

class WebScraper:
    def __init__(self, student_id):
        self.student_id = student_id
        self.web_side = 'http://websecgen.unmsm.edu.pe/carne/carne.aspx'
        self.driver_path = '../../chromedriver.exe'
        self.options = Options()
        self.driver = None

    def initialize_driver(self):
        service = Service(self.driver_path)
        self.driver = webdriver.Chrome(service=service, options=self.options)

    def scrape_student_data(self):
        self.driver.get(self.web_side)
        time.sleep(2)

        self.driver.execute_script(f"document.querySelector('#ctl00_ContentPlaceHolder1_txtUsuario').value='{self.student_id}';")
        self.driver.execute_script("document.querySelector('#ctl00_ContentPlaceHolder1_cmdConsultar').click();")
        time.sleep(2)

        faculty = unidecode(self.driver.execute_script("return document.querySelector('#ctl00_ContentPlaceHolder1_txtFacultad').value;"))
        if faculty != "":
            program = unidecode(self.driver.execute_script("return document.querySelector('#ctl00_ContentPlaceHolder1_txtPrograma').value;"))
            student_name = unidecode(self.driver.execute_script("return document.querySelector('#ctl00_ContentPlaceHolder1_txtAlumno').value;"))
            student = Student(self.student_id, student_name, program)
            return student

    def close_driver(self):
        if self.driver is not None:
            self.driver.quit()
