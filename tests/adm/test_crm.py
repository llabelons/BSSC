import os
from playwright.sync_api import Page
from dotenv import load_dotenv

load_dotenv()

def test_amen_recep(page: Page):
    #0. Login en stg
    page.goto("https://stg.blueopendata.com/bsports-club/login")
    page.get_by_text("Prefer", exact=False).click()
    page.get_by_placeholder("Email o usuario").fill(os.getenv("ADM_EMAIL"))
    page.locator("input[type='password']").fill(os.getenv("ADM_PASSWORD"))
    page.get_by_role("button", name="INGRESAR").click()

    #1. Dirigirse a clubes
    page.get_by_role("navigation").get_by_role("link", name="CRM Manager", exact=True).click()

     #2. Buscar por cuit
    buscador = page.get_by_role("searchbox", name="Buscar club")
    buscador.fill("20725169737")
    buscador.press("Enter")
    page.get_by_role("button", name="Buscar", exact=True).click()
    buscador = page.get_by_role("searchbox", name="Buscar club")
    buscador.fill("20000000001")
    buscador.press("Enter")
    page.get_by_role("button", name="Buscar", exact=True).click()
    buscador = page.get_by_role("searchbox", name="Buscar club")
    buscador.fill("30715800574")
    buscador.press("Enter")
    page.get_by_role("button", name="Buscar", exact=True).click()
    buscador = page.get_by_role("searchbox", name="Buscar club")
    buscador.fill("23477930859")
    buscador.press("Enter")
    page.get_by_role("button", name="Buscar", exact=True).click()

    #3. Clic en "Cambiar plan"
    buscador = page.get_by_role("searchbox", name="Buscar club")
    buscador.fill("23477930859")
    buscador.press("Enter")
    page.get_by_role("button", name="Buscar", exact=True).click()
    page.get_by_role("button", name="Cambiar plan", exact=True).click()
    page.get_by_text("Aplicar descuento temporal a la suscripción").scroll_into_view_if_needed()
    page.get_by_role("checkbox", name="Aplicar descuento temporal a la suscripción").click()
    page.get_by_role("button", name="Cancelar", exact=True).click(force=True)

    #4. Clic en "Dar de baja"
    page.get_by_role("button", name="Dar de baja", exact=True).click()
    page.get_by_role("button", name="Cancelar", exact=True).click()
