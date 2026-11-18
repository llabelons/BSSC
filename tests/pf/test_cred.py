import os
from playwright.sync_api import Page
from dotenv import load_dotenv

load_dotenv()

def test_eventos_recep(page: Page):
    #0. Login en stg
    page.goto("https://stg.blueopendata.com/bsports-club/login")
    page.get_by_text("Prefer", exact=False).click()
    page.get_by_placeholder("Email o usuario").fill(os.getenv("PROF_EMAIL"))
    page.locator("input[type='password']").fill(os.getenv("PROF_PASSWORD"))
    page.get_by_role("button", name="INGRESAR").click()
    page.wait_for_timeout(500)

    # 1. Dirigirse a la sección "Eventos" de la sidebar
    page.get_by_role("navigation").get_by_role("link", name="Mi credencial", exact=True).click(force=True)
    page.wait_for_timeout(500)

    #2. Ver qr
    page.get_by_role("button", name="Ver dorso del carnet", exact=False).click()
    page.wait_for_timeout(500)