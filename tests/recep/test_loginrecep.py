import os
import pytest
from playwright.sync_api import Page
from dotenv import load_dotenv

load_dotenv()

def test_login_bsports(page: Page):
    page.goto("https://stg.blueopendata.com/bsports-club/login")
    page.get_by_text("Prefer", exact=False).click()
    
    # Forzamos el uso exclusivo de RECEP_EMAIL y RECEP_PASSWORD
    page.get_by_placeholder("Email o usuario").fill(os.getenv("RECEP_EMAIL"))
    page.locator("input[type='password']").fill(os.getenv("RECEP_PASSWORD"))
    
    page.get_by_role("button", name="INGRESAR").click()
    page.wait_for_timeout(500)
