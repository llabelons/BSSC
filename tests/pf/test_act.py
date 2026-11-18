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

    # 1. Dirigirse a la sección "Mis ACtividades" de la sidebar
    page.get_by_role("navigation").get_by_role("link", name="Mis actividades", exact=True).click(force=True)

    #2. Ver una actt
    page.locator("table tbody tr").first.get_by_role("button", name="Ver actividad", exact=True).click(force=True)
    page.get_by_role("button", name="Cerrar", exact=True).click(force=True)