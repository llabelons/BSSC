import os
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

    #1. Dirigirse a la sección "Ingresos" de la sidebar
    page.get_by_role("navigation").get_by_role("link", name="Ingresos", exact=True).click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Nuevo movimiento", exact=True).click(force=True)
    page.wait_for_timeout(500)

    #2. Buscar por fecha
    #Escribir en el campo de Mes (MM)
    page.get_by_placeholder("MM").fill("9")
    page.get_by_placeholder("AAAA").fill("2026")
    page.wait_for_timeout(1000)
    
    #3. Buscar por tipo y fecha
    page.locator("app-select[etiqueta='Tipo'] button").click()
    page.get_by_role("listbox").get_by_text("Ingreso", exact=True).click(force=True)
    page.wait_for_timeout(1000)
    page.locator("app-select[etiqueta='Tipo'] button").click()
    page.get_by_role("listbox").get_by_text("Egreso", exact=True).click(force=True)
    page.wait_for_timeout(1000)


