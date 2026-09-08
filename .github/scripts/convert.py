import sys
import os
from playwright.sync_api import sync_playwright

def main():
    if len(sys.argv) < 3:
        print("Usage: python convert.py <input_html> <output_pdf>")
        sys.exit(1)

    html_path = os.path.abspath(sys.argv[1])
    pdf_path = os.path.abspath(sys.argv[2])

    with sync_playwright() as p:
        browser = p.chromium.launch(args=["--no-sandbox", "--disable-setuid-sandbox"])
        page = browser.new_page()
        page.goto(f"file://{html_path}", wait_until="networkidle")
        page.emulate_media(media="screen")
        page.pdf(
            path=pdf_path,
            format="A4",
            print_background=True,
            margin={"top": "12mm", "bottom": "12mm", "left": "12mm", "right": "12mm"}
        )
        browser.close()

    print(f"Successfully generated {pdf_path}")

if __name__ == "__main__":
    main()
