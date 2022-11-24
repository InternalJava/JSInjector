"""
       _______ ____        _           __            
      / / ___//  _/___    (_)__  _____/ /_____  _____
 __  / /\__ \ / // __ \  / / _ \/ ___/ __/ __ \/ ___/  - JSInjector
/ /_/ /___/ // // / / / / /  __/ /__/ /_/ /_/ / /      - Tools to inject javascript
\____//____/___/_/ /_/_/ /\___/\___/\__/\____/_/       @Java#0032
                    /___/                            
"""

# Import required libraries
from bin.function import JS
import os

# Extra functions
def read_banner(file_location : str):
    file = open(file_location, "r")
    content = file.read()
    print(content)
    file.close()

# Main functions
def main(): 
    os.system("cls")
    read_banner("assets/banner.txt")
    console = input("Browser: ")
    website = input("Website: ")
    inject_script = input("Script: ")
    if console == "1":
        browser_type = "Chrome"
        injected = JS.Inject(browser_type, website, inject_script)
        print(injected)
    if console == "2":
        browser_type = "Firefox"
        injected = JS.Inject(browser_type, website, inject_script)
        print(injected)

# Start the function
if __name__ == "__main__":
    main()