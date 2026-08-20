MANGAOANG, KARL   IX - SILICON

PART I & II
The main problem: Catastrophic crowd and slow service during lunch breaks due to  inefficiencies in ordering, payment and inventory management.

Sub-Problem 1 (Ordering Friction): Delays caused by students deciding what to buy while already at the front of the line.

Sub-Problem 2 (Manual Checkout): Slow checkout times due to manual calculation of totals and change.

Sub-Problem 3 (Inventory Visibility): Lack of real-time tracking for food stock levels, leading to unexpected sell-outs.

Sub-Problem 4 (Crowd Flow): Bottlenecks caused by ordering, payment, and food pickup happening at the exact same physical spot.

PART III
Decomposition	
Splitting the canteen workflow into 3 distinct modules: Digital Pre-ordering (App/Kiosk), Automated Point of Sale (POS), and Real-time Inventory Management.

Pattern Recognition	
Identifying peak traffic hours (12:00 PM – 1:00 PM) and high-demand menu items to prepare fast-selling meals in advance.

Abstraction	
Focusing only on essential transaction details (Item ID, Price, Quantity, Wallet Balance) while ignoring non-essential details (e.g., ingredients, brand of cash register).

Algorithm Design
Creating step-by-step logic for processing orders, updating stock levels, and processing digital payments automatically.

PART IV
BEGIN CanteenOrderingSystem

    // Step 1: Initialize System Data
    DISPLAY MenuWithPrices
    DISPLAY CurrentInventoryStatus

    // Step 2: Student Order Input
    INPUT StudentID
    INPUT SelectedItemsList

    TotalCost = 0
    OrderValid = TRUE

    // Step 3: Verify Inventory and Calculate Total
    FOR EACH Item IN SelectedItemsList DO
        IF Item.StockQuantity > 0 THEN
            TotalCost = TotalCost + Item.Price
        ELSE
            DISPLAY "Sorry, " + Item.Name + " is out of stock."
            OrderValid = FALSE
        END IF
    END FOR

    // Step 4: Process Payment and Update Inventory
    IF OrderValid IS TRUE THEN
        DISPLAY "Your total is: " + TotalCost
        INPUT StudentBalance

        IF StudentBalance >= TotalCost THEN
            // Process Transaction
            NewBalance = StudentBalance - TotalCost
            DISPLAY "Payment Successful! Remaining Balance: " + NewBalance

            // Deduct Stock (Inventory Tracking)
            FOR EACH Item IN SelectedItemsList DO
                Item.StockQuantity = Item.StockQuantity - 1
                IF Item.StockQuantity < LowStockThreshold THEN
                    SEND AlertToKitchen("Restock required for: " + Item.Name)
                END IF
            END FOR

            // Generate Order Token for Pickup
            GeneratePickupTicket(OrderID, SelectedItemsList)

        ELSE
            DISPLAY "Insufficient funds. Transaction canceled."
        END IF
    END IF

END CanteenOrderingSystem
