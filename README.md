# Workflow Automation Scripts

## 1. Overview

This collection of Python scripts provides templates to automate various workflow steps, from UI interaction and web navigation to running other scripts. They are designed as starting points and **require customization** to fit your specific environment, applications, and credentials.

## 2. General Setup

Before using these scripts, ensure you have the following:

*   **Python 3**: These scripts are written for Python 3. Download and install it from [python.org](https://www.python.org/downloads/).
*   **pip**: Python's package installer, usually included with Python 3. Used to install necessary libraries. You can upgrade pip with `python -m pip install --upgrade pip`.

## 3. Script-Specific Instructions

Each script has its own purpose and requirements:

---

### `navigate_files.py`

*   **Purpose**: Simulates user interactions for file navigation within a generic media player application using GUI automation.
*   **Key Libraries**: `pyautogui`
*   **Required Installations**:
    ```bash
    pip install pyautogui
    ```
*   **Crucial Customizations**:
    *   **Screen Coordinates**: If using absolute click positions (e.g., `pyautogui.click(X, Y)`), these coordinates are specific to your screen resolution and application window placement. Use `pyautogui.displayMousePosition()` in a Python console to find correct coordinates.
    *   **Image Recognition**: For more robust automation, replace coordinate-based clicks with image recognition (e.g., `pyautogui.locateCenterOnScreen('button.png')`). This requires taking screenshots of UI elements.
    *   **UI Interaction Logic**: The sequence of key presses (`'down'`, `'enter'`) and clicks must match your media player's controls.
    *   **Hotkeys**: The script uses `Ctrl+O` as an example to open files. Adjust this if your application uses a different shortcut.
    *   **Timings**: `time.sleep()` values may need adjustment based on your system's and application's responsiveness.

---

### `review_wiki_doc.py`

*   **Purpose**: Opens a specified URL in a Chrome browser using Selenium, intended for reviewing a document.
*   **Key Libraries**: `selenium`
*   **Required Installations**:
    ```bash
    pip install selenium
    ```
*   **Crucial Customizations**:
    *   **`DOCUMENT_URL`**: Update the `DOCUMENT_URL` variable with the actual URL of the document you wish to review.
    *   **ChromeDriver Path**: If ChromeDriver is not in your system PATH, you must set the `CHROME_DRIVER_PATH` variable in the script to the location of your `chromedriver.exe` (Windows) or `chromedriver` (macOS/Linux) executable. See section "4. ChromeDriver (for Selenium scripts)" below.

---

### `access_groupware.py`

*   **Purpose**: Simulates logging into a web-based groupware system and navigating its menus using Selenium.
*   **Key Libraries**: `selenium`
*   **Required Installations**:
    ```bash
    pip install selenium
    ```
*   **Crucial Customizations**:
    *   **`GROUPWARE_URL`**: Set this to the exact login URL of your groupware.
    *   **`USERNAME`**, **`PASSWORD`**: **Replace placeholder credentials with your actual login details.** (See Security Warning section).
    *   **`LOCATOR_*` Variables**: These are **critical**. You must identify the correct Selenium locators (e.g., `By.ID`, `By.XPATH`, `By.NAME`, `By.CSS_SELECTOR`) for:
        *   Username input field
        *   Password input field
        *   Login button
        *   Any menu items you intend to interact with (`LOCATOR_MENU_ITEM_1`, etc.)
        Use browser developer tools ("Inspect Element") to find these. Locators are highly specific to the groupware's web interface.
    *   **ChromeDriver Path**: Set `CHROME_DRIVER_PATH` if ChromeDriver is not in your system PATH.

---

### `run_task_mining_script.py`

*   **Purpose**: Executes another Python script (`task_mining.py`) using the `subprocess` module.
*   **Key Libraries**: `subprocess`, `sys` (standard libraries, no separate install needed)
*   **Required Installations**: None beyond Python itself.
*   **Crucial Customizations**:
    *   **`task_mining_script_path`**: If `task_mining.py` is not in the same directory as `run_task_mining_script.py`, update this variable to the full path of `task_mining.py`.
    *   **Dummy `task_mining.py`**: If `task_mining.py` is not found when `run_task_mining_script.py` is executed, it will attempt to create a dummy `task_mining.py` for demonstration. Replace this dummy script with your actual `task_mining.py`.

---

### `update_cafe24.py`

*   **Purpose**: Simulates logging into a Cafe24 e-commerce admin panel, navigating to a product, and updating its information using Selenium.
*   **Key Libraries**: `selenium`
*   **Required Installations**:
    ```bash
    pip install selenium
    ```
*   **Crucial Customizations**: This script requires extensive and careful customization.
    *   **`CAFE24_ADMIN_URL`**: Set this to your specific Cafe24 admin login URL.
    *   **`ADMIN_USERNAME`**, **`ADMIN_PASSWORD`**: **Replace placeholder credentials with your actual Cafe24 admin login details.** (See Security Warning section).
    *   **`LOCATOR_*` Variables**: **This is the most complex part.** Cafe24's admin panel structure is intricate and uses iframes extensively. You MUST use browser developer tools to find the correct locators for:
        *   Login iframe, username field, password field, login button.
        *   Product management menu links.
        *   Product selection elements (e.g., search fields, edit buttons in a product list).
        *   Product editing iframe (if any).
        *   Specific fields to update (e.g., product description, price).
        *   Save/confirm buttons.
        The example locators are placeholders and **will not work** without modification. Pay close attention to `<iframe>` elements; you may need to use `driver.switch_to.frame()` and `driver.switch_to.default_content()`.
    *   **Product Identifier**: `PRODUCT_IDENTIFIER_FOR_SELECTION` needs to be set to a real product name/ID if you use the example product selection logic.
    *   **Data to Update**: Modify `new_description_data`, `new_price_data` with the actual information you want to set.
    *   **ChromeDriver Path**: Set `CHROME_DRIVER_PATH` if ChromeDriver is not in your system PATH.

---

## 4. ChromeDriver (for Selenium scripts)

Selenium requires a WebDriver executable to interface with the chosen browser. For Chrome, this is ChromeDriver.

*   **Why it's needed**: ChromeDriver acts as a bridge between Selenium's commands and the Chrome browser, allowing Selenium to control Chrome.
*   **Download**: Download the version of ChromeDriver that matches **your installed Chrome browser version** from the official site: [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads).
*   **Setup**:
    1.  **Add to System PATH (Recommended)**: Extract `chromedriver.exe` (Windows) or `chromedriver` (macOS/Linux) and place it in a directory that is part of your system's PATH environment variable. This allows Selenium to find it automatically.
    2.  **Specify Path in Script**: If you don't add ChromeDriver to PATH, you must uncomment and set the `CHROME_DRIVER_PATH` variable in the Selenium-based scripts (`review_wiki_doc.py`, `access_groupware.py`, `update_cafe24.py`) to the full path of the ChromeDriver executable.

## 5. Identifying UI Element Locators (for Selenium scripts)

To tell Selenium which elements to interact with (e.g., buttons to click, fields to type into), you need to provide locators.

*   **How to find locators**:
    1.  Open the web page in Chrome.
    2.  Right-click on the UI element you want to interact with (e.g., a username field).
    3.  Select "Inspect" or "Inspect Element" from the context menu. This opens the browser's developer tools.
    4.  The HTML code for the selected element will be highlighted. Look for attributes like:
        *   `id`: Often the best and most unique locator (e.g., `By.ID, "username"`).
        *   `name`: Common for form elements (e.g., `By.NAME, "password"`).
        *   `class`: Can be used, but classes are often not unique (e.g., `By.CLASS_NAME, "login-button"`).
        *   Link text: For `<a>` tags (e.g., `By.LINK_TEXT, "Dashboard"`).
    5.  If no unique `id` or `name` is available, you might need to use:
        *   **CSS Selectors**: (e.g., `By.CSS_SELECTOR, "button[type='submit']"`).
        *   **XPath**: A more powerful but complex way to navigate the HTML structure (e.g., `By.XPATH, "//div[@id='main-content']//button"`).

## 6. Error Handling and Debugging

*   **Basic Error Handling**: The scripts include basic `try-except` blocks to catch common exceptions and print error messages.
*   **Tracebacks**: When an error occurs, Python prints a traceback. Read this carefully to understand where the error happened and why.
*   **Print Statements**: The scripts include print statements to show progress. You can add more `print()` calls to track variable values or execution flow during debugging.
*   **GUI Automation Issues (`pyautogui`)**:
    *   **Screen Resolution**: Coordinate-based actions are sensitive to screen resolution changes.
    *   **Window Focus**: `pyautogui` controls the currently active window. Ensure the target application window is in focus before the script attempts to interact with it. The scripts often include a `time.sleep()` at the beginning to allow you to switch windows.
    *   **Permissions (macOS)**: On macOS, you may need to grant accessibility permissions to your terminal or IDE for `pyautogui` to control the mouse and keyboard.
*   **Selenium Issues**:
    *   **Timing**: Web pages load dynamically. Use `WebDriverWait` and `expected_conditions` (as shown in the scripts) to wait for elements to be present/clickable before interacting. Avoid fixed `time.sleep()` calls for waiting for elements, except for brief pauses or observation.
    *   **Stale Elements**: If the page structure changes after an element is found, you might get a `StaleElementReferenceException`. Re-locate the element if this happens.
    *   **Incorrect Locators**: The most common issue. Double-check your locators using developer tools.

## 7. Security Warning

**Credentials Handling**: The scripts for `access_groupware.py` and `update_cafe24.py` include placeholder variables for usernames and passwords. Hardcoding sensitive information directly into scripts is a security risk, especially if the code is shared or version-controlled.

For better security, consider using:
*   **Environment Variables**: Store credentials in environment variables and access them in the script using `os.environ.get('YOUR_PASSWORD_ENV_VAR')`.
*   **Configuration Files**: Store credentials in a separate configuration file (e.g., `.ini`, `.yaml`, `.env`) that is not committed to version control (add it to `.gitignore`). Load them at runtime.
*   **Secrets Management Tools**: For more advanced scenarios, use tools like HashiCorp Vault or cloud provider secret managers.

The provided scripts **do not implement these advanced methods** for simplicity but be aware of the risks.

## 8. Disclaimer

These scripts are provided as examples and "as-is". You are solely responsible for their use, any modifications you make, and ensuring they comply with the terms of service of any websites or applications they interact with. Always test automation scripts responsibly and be mindful of the systems you are interacting with.
The user is responsible for their use and any modifications. Ensure you understand what each script does before running it, especially those that interact with live accounts or systems.
