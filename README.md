# Overview

This custom :contentReference[oaicite:0]{index=0} module extends the Sales Order functionality by adding additional business fields and customizing the Sales Order PDF report.

It integrates Sales Orders with HR employees and introduces dynamic field logic for order tracking and reporting.

---

# Features

## Responsible Employee

- Adds required field `responsible_employee_id`
- Links Sales Order to an HR employee
- Used for tracking responsibility in order processing

---

## Dynamic Field (`new_field`)

Automatically generates a value based on order data:

### Behavior:
- If no order lines exist → generates a random 10-character string
- If order has order lines → generates a formatted string: date_order + amount_total


### Validation:
- Maximum length: 30 characters

---

## Custom Sales Order Report

Extends standard Odoo report: sale.report_saleorder_document

### Modifications:
- Adds a custom block before the order table
- Displays:
  - `new_field` if available
  - fallback message if empty:
    ```
    Поле New Field пустое!!!
    ```

---

# Dependencies

- `sale` → Sales Order functionality
- `hr` → Employee model integration

---

# Installation

1. Copy module into the Odoo addons directory
2. Restart Odoo server
3. Update Apps list
4. Install **Odoo Gfis Module**
