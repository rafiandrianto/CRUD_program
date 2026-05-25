# Python CRUD Application for Automotive Dealership

A comprehensive Python application for managing managing high value collector vehicle data with Create, Read, Update, and Delete (CRUD) operations.

## Business Understanding

This project caters to the Automotive Dealership & Vehicle Brokerage industry, specifically addressing the need to manage specialized high value automobile inventories (JDM, USDM, and EDM variants). Vehicle inventory management plays a crucial role in maintaining showroom logistics, ensuring correct asset pricing, tracking vehicle availability, and avoiding costly duplicate registry entries for multi-million and multi-billion Rupiah assets.

**Benefits:**

* Automated ID generation (JDM-XXX, USD-XXX, EDM-XXX) eliminates manual indexing overlap
* Real time data filtration and keyword lookups let sales operators isolate vehicle specs instantly during client inquiries
* Localized trap loops combined with try except data validation that ensures alphabetical strings never corrupt decimal fields
* Employs raw ANSI codes for terminal color styling, allowing the system to run on any machine without installing packages

**Target Users:**

This application is designed for Showroom Inventory Managers, Luxury Car Brokers, and Dealership Operators within the organization to facilitate their daily data maintenance tasks, price adjustment processing, and client inventory lookups related to available vehicles

## Features

* **Create:**
    * Add new vehicle entries with details like Category, Model Name, Assembly Year, Engine Series, and Retail Price
    * Automatically evaluates current database records to assign the next sequential primary key identifier
    * Features localized validation loops to guarantee category (JDM, USD, EDM) and numerical type validation for years and pricing

* **Read:**
    * Displays a colored and structured tabular dashboard featuring comma separated thousands formatting for financial clarity
    * Search and isolate specific vehicle records via a complete primary key ID match
    * Filter inventory sheets instantly by distinct geographical regions (JDM, USD, EDM)
    * Executes case insensitive partial keyword scans across both model names and engine codes simultaneously (ex: searching "RS" or "2JZ")

* **Update:**
    * Modify individual attributes of an existing vehicle record without forcing the re-entry of untouched parameters
    * Localized string validation (Available, Reserved, Sold)
    * Includes terminal confirmation steps (Y/N) before writing changes into memory

* **Delete:**
    * Removes unwanted or mistakenly added vehicle records from the memory registry

* **Optimizations:**
    * Allows operators to input 0 at primary prompts to immediately cancel execution flows and return safely to the dashboard
    * Implements UI color (Green for success, Red for errors/deletions, Yellow for warnings, Cyan for borders, Blue for options) using standard ANSI sequences
    

## Installation

1. **Prerequisites:**
    * Python version 3.6 or higher (required for formatted f-strings and standard dictionary ordering)
    * Terminal environment supporting standard ANSI Escape Sequences

2. **Installation:**
    ```bash
    git clone https://github.com/rafiandrianto/CRUD_program.git
    cd <your-repo-name>
    ```

3. **Database Setup (if applicable):**
    This system utilizes an in memory nested dictionary initialized with six iconic placeholder vehicles upon startup. No relational database connections or structural migrations are required to run the environment

## Usage

1. **Run the application:**
    ```bash
    python main.py
    ```

2. **CRUD Operations:**
    * **Create:** Navigate to Option 2. Provide the desired asset category (ex: JDM), let the system generate your unique sequential ID, input model parameters, review the visual summary, and confirm the write command.
    * **Read:** Navigate to Option 1. Select whether to print the complete showroom grid, filter by a distinct category, lookup a standalone record, or use the partial search engine to look for model name or engine type.
    * **Update:** Navigate to Option 3. Input your target vehicle's ID, view its current parameters, pick an attribute number to adjust, define the new field parameter, and save.
    * **Delete:** Navigate to Option 4. Input the vehicle ID to drop, review the deletion alert banner, and confirm to permanently delete the vehicle out of the system.

## Data Model
This project utilizes a Python Nested Dictionary (dict) structure to represent vehicular data. The structure assigns a distinct alphanumeric token string as the primary key mapped to an internal dictionary object containing the following data fields:
   * kategori: (str) - The regional classification tag of the vehicle; strictly limited to "JDM", "USDM", or "EDM" (for now)
   * nama_mobil: (str) - The official commercial name of the vehicle
   * tahun: (int) - The manufacturing or assembly year of the vehicle (bounded between 1900 and 2026)
   * mesin: (str) - The specific internal combustion engine code or variant designator
   * harga: (float) - The calculated retail value of the unit represented in Indonesian Rupiah (IDR)
   * status_unit: (str) - The trade state of the asset; limited to "Available", "Reserved", or "Sold"


