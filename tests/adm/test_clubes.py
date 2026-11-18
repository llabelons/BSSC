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
    page.wait_for_timeout(500)

    #1. Dirigirse a clubes
    page.get_by_role("navigation").get_by_role("link", name="Clubes", exact=True).click()

    #2. Buscar por cuit
    buscador = page.get_by_placeholder("Nombre, razon social o cuit")
    buscador.fill("20725169737")
    buscador.press("Enter")
    page.get_by_role("button", name="Buscar", exact=True).click()
    buscador = page.get_by_placeholder("Nombre, razon social o cuit")
    buscador.fill("20000000001")
    buscador.press("Enter")
    page.get_by_role("button", name="Buscar", exact=True).click()
    buscador = page.get_by_placeholder("Nombre, razon social o cuit")
    buscador.fill("30715800574")
    buscador.press("Enter")
    page.get_by_role("button", name="Buscar", exact=True).click()
    buscador = page.get_by_placeholder("Nombre, razon social o cuit")
    buscador.fill("30491622683")
    buscador.press("Enter")
    page.get_by_role("button", name="Buscar", exact=True).click()

    #3. Clic en "Editar empresa"
    buscador = page.get_by_placeholder("Nombre, razon social o cuit")
    buscador.fill("30491622683")
    buscador.press("Enter")
    page.get_by_role("button", name="Buscar", exact=True).click()
    #clic en editar
    page.get_by_role("button", name="Editar empresa", exact=True).click()
    #guardar y despues cancelar
    page.get_by_role("button", name="Guardar empresa", exact=True).click()
    page.get_by_role("button", name="Cancelar", exact=True).click()

    #4. Clic en "Administradores"
    page.get_by_role("button", name="Administradores", exact=True).click()
    buscador = page.get_by_placeholder("Nombre, apellido o email")
    #buscamos por mail
    buscador.fill("leo@leo.com")
    buscador.press("Enter")
    page.get_by_role("button", name="Editar", exact=True).click()
    page.get_by_role("button", name="Cancelar", exact=True).click()

    #5. Clic en "Entrar al club"
    page.get_by_role("button", name="Entrar al club", exact=True).click()
    page.get_by_role("button", name="Ingresar", exact=True).click()
    #buscamos en sidebar
    page.get_by_role("navigation").get_by_role("link", name="Volver a SYSADMIN", exact=True).click()




