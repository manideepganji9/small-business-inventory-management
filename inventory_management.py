# SMALL BUSINESS INVENTORY MANAGEMENT SYSTEM
# Beginner-friendly version using dictionaries, lists, loops and conditions.

products = {}
sales = []

while True:
    print("\n===== SMALL BUSINESS INVENTORY SYSTEM =====")
    print("1. Add Product")
    print("2. View All Products")
    print("3. Search Product")
    print("4. Update Stock")
    print("5. Record Sale")
    print("6. Low Stock Alert")
    print("7. View Inventory Value")
    print("8. View Sales Report")
    print("9. Exit")

    choice = input("Enter your choice: ").strip()

    # 1. Add Product
    if choice == "1":
        product_id = input("Enter Product ID: ").strip()

        if not product_id:
            print("Product ID cannot be empty.")
        elif product_id in products:
            print("Product ID already exists!")
        else:
            name = input("Enter Product Name: ").strip()
            cost_text = input("Enter Purchase Price: ").strip()
            selling_text = input("Enter Selling Price: ").strip()
            stock_text = input("Enter Initial Stock: ").strip()
            minimum_text = input("Enter Minimum Stock Level: ").strip()

            # Validate numeric inputs before converting them.
            if (not cost_text.replace(".", "", 1).isdigit()
                    or not selling_text.replace(".", "", 1).isdigit()
                    or not stock_text.isdigit()
                    or not minimum_text.isdigit()):
                print("Enter valid positive numbers for prices and quantities.")
            elif not name:
                print("Product name cannot be empty.")
            else:
                cost_price = float(cost_text)
                selling_price = float(selling_text)
                stock = int(stock_text)
                minimum_stock = int(minimum_text)

                if cost_price < 0 or selling_price < 0:
                    print("Prices cannot be negative.")
                else:
                    products[product_id] = {
                        "name": name,
                        "cost_price": cost_price,
                        "selling_price": selling_price,
                        "stock": stock,
                        "minimum_stock": minimum_stock
                    }
                    print("Product added successfully!")
                    if selling_price < cost_price:
                        print("Note: Selling price is below purchase price.")

    # 2. View All Products
    elif choice == "2":
        if not products:
            print("No products available.")
        else:
            print("\nID | Product | Purchase Price | Selling Price | Stock | Min Stock")
            print("-" * 72)
            for product_id, product in products.items():
                print(
                    product_id, "|", product["name"], "| ₹",
                    format(product["cost_price"], ".2f"), "| ₹",
                    format(product["selling_price"], ".2f"), "|",
                    product["stock"], "|", product["minimum_stock"]
                )

    # 3. Search Product
    elif choice == "3":
        product_id = input("Enter Product ID to search: ").strip()

        if product_id in products:
            product = products[product_id]
            print("\nProduct Found!")
            print("Product ID:", product_id)
            print("Name:", product["name"])
            print("Purchase Price: ₹", format(product["cost_price"], ".2f"))
            print("Selling Price: ₹", format(product["selling_price"], ".2f"))
            print("Available Stock:", product["stock"])
            print("Minimum Stock Level:", product["minimum_stock"])
        else:
            print("Product not found!")

    # 4. Update Stock
    elif choice == "4":
        product_id = input("Enter Product ID: ").strip()

        if product_id in products:
            quantity_text = input("Enter quantity received: ").strip()
            if quantity_text.isdigit() and int(quantity_text) > 0:
                quantity = int(quantity_text)
                products[product_id]["stock"] += quantity
                print("Stock updated successfully!")
                print("New Stock:", products[product_id]["stock"])
            else:
                print("Quantity must be a positive whole number.")
        else:
            print("Product not found!")

    # 5. Record Sale
    elif choice == "5":
        product_id = input("Enter Product ID: ").strip()

        if product_id in products:
            quantity_text = input("Enter quantity sold: ").strip()
            if not quantity_text.isdigit() or int(quantity_text) <= 0:
                print("Quantity must be a positive whole number.")
            else:
                quantity = int(quantity_text)
                product = products[product_id]

                if quantity > product["stock"]:
                    print("Insufficient stock! Sale was not recorded.")
                else:
                    product["stock"] -= quantity
                    revenue = quantity * product["selling_price"]
                    cost = quantity * product["cost_price"]
                    profit = revenue - cost

                    sales.append({
                        "product_id": product_id,
                        "name": product["name"],
                        "quantity": quantity,
                        "revenue": revenue,
                        "cost": cost,
                        "profit": profit
                    })

                    print("\nSale Successful!")
                    print("Product:", product["name"])
                    print("Quantity Sold:", quantity)
                    print("Total Sale: ₹", format(revenue, ".2f"))
                    print("Gross Profit: ₹", format(profit, ".2f"))
                    print("Remaining Stock:", product["stock"])
        else:
            print("Product not found!")

    # 6. Low Stock Alert
    elif choice == "6":
        found = False
        print("\n===== LOW STOCK PRODUCTS =====")

        for product_id, product in products.items():
            if product["stock"] <= product["minimum_stock"]:
                print(
                    product["name"], "(ID:", product_id + ")",
                    "- Remaining:", product["stock"],
                    "- Minimum:", product["minimum_stock"]
                )
                found = True

        if not found:
            print("All products have sufficient stock.")

    # 7. View Inventory Value
    elif choice == "7":
        total_value = 0
        for product in products.values():
            total_value += product["stock"] * product["cost_price"]

        print("Total Inventory Value (purchase cost): ₹", format(total_value, ".2f"))

    # 8. View Sales Report
    elif choice == "8":
        total_revenue = 0
        total_cost = 0
        total_profit = 0
        total_items_sold = 0

        print("\n===== SALES REPORT =====")

        if not sales:
            print("No sales recorded yet.")
        else:
            print("Product | Quantity | Revenue | Cost | Gross Profit")
            print("-" * 58)
            for sale in sales:
                print(
                    sale["name"], "|", sale["quantity"], "| ₹",
                    format(sale["revenue"], ".2f"), "| ₹",
                    format(sale["cost"], ".2f"), "| ₹",
                    format(sale["profit"], ".2f")
                )
                total_revenue += sale["revenue"]
                total_cost += sale["cost"]
                total_profit += sale["profit"]
                total_items_sold += sale["quantity"]

            print("\nTotal Items Sold:", total_items_sold)
            print("Total Revenue: ₹", format(total_revenue, ".2f"))
            print("Total Cost of Goods Sold: ₹", format(total_cost, ".2f"))
            print("Total Gross Profit: ₹", format(total_profit, ".2f"))

    # 9. Exit
    elif choice == "9":
        print("Thank you for using the Inventory Management System!")
        break

    else:
        print("Invalid choice! Please select a number from 1 to 9.")
