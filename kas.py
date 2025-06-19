import asyncio
from playwright.async_api import async_playwright

FAUCET_URL = "https://app.kaspafinance.io/faucets"
TESTNET_ADDRESS = "kaspa:qqxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # Replace with your Kasplex testnet address

async def claim_kasplex_faucet():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)  # Set headless=False to see the browser
        page = await browser.new_page()

        await page.goto(FAUCET_URL)

        # Wait for the address input field to appear
        await page.wait_for_selector('input[type="text"]')

        # Fill in the testnet address
        await page.fill('input[type="text"]', TESTNET_ADDRESS)

        # Click the claim/request button (adjust selector if needed)
        await page.click('button:has-text("Request")')

        # Wait for a success message or timeout after 10 seconds
        try:
            await page.wait_for_selector('text=Success', timeout=10000)
            print("Faucet claim successful!")
        except:
            print("No success message detected. Please verify manually.")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(claim_kasplex_faucet())
