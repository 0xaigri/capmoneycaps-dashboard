import asyncio
from playwright.async_api import async_playwright
import csv
from datetime import date
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        total_caps = 0
        seen_pages = set()

        async def handle_response(response):
            nonlocal total_caps
            if "api.cap.app/v1/caps/leaderboard" in response.url:
                try:
                    data = await response.json()
                    page_num = data.get("pagination", {}).get("current")
                    if page_num not in seen_pages:
                        seen_pages.add(page_num)
                        subtotal = sum(int(e["caps"]) for e in data.get("entries", []))
                        total_caps += subtotal
                        print(f"Page {page_num} → +{subtotal} (total = {total_caps})")
                except:
                    pass

        page.on("response", handle_response)

        await page.goto("https://cap.app/caps")
        await page.wait_for_timeout(3000)

        while True:
            next_button = page.locator("button:has(span:has-text('Go to next page'))")

            if not await next_button.is_visible() or not await next_button.is_enabled():
                break

            await next_button.click()
            await page.wait_for_timeout(3000)

        print("TOTAL FINAL :", total_caps)
        await browser.close()

        # --- Ajout étape 1 : écrire l’historique toujours à côté du script ---
        script_dir = os.path.dirname(os.path.abspath(__file__))  # dossier du script
        csv_path = os.path.join(script_dir, "caps_history.csv")

        with open(csv_path, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([date.today(), total_caps])

# Lancer le script
asyncio.run(main())
