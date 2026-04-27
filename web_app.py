"""
Веб-версия парсера Avito
Запуск: python web_app.py
Доступ: http://localhost:8550
"""

from AvitoParser import main
import flet as ft


if __name__ == "__main__":
    ft.app(
        target=main,
        assets_dir="assets",
        port=8550,
        host="0.0.0.0",
        view=ft.AppView.WEB_BROWSER,
    )
