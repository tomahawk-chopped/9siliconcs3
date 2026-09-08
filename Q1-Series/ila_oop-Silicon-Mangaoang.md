MANGAOANG, KARL IX - SILICON

1. Encapsulation
Encapsulation bundles product properties—such as productName, price, and stockQuantity—together into a single Product class while restricting direct external modification of critical attributes. By setting data attributes to private and exposing public methods like updateStock() or sellItem(), the system prevents unintended data corruption, such as setting a negative stock value or a negative price. This keeps the sari-sari store inventory data secure, self-contained, and consistent across all operations.

2. Abstraction
Abstraction hides the complex internal calculations and database operations involved in managing stock, exposing only simplified interfaces to the user or cashier. For instance, an Inventory class might provide a straightforward method named processSale(itemCode, quantity), hiding low-level details like updating database records, calculating remaining inventory, and printing receipts. This organizes the codebase cleanly by separating what the system does from how it performs the action under the hood.

3. Inheritance
Inheritance allows a general Product class to serve as a base class, while specific item categories derive from it to share common attributes like name and price. Specialized classes, such as PerishableProduct (with an added expiryDate property) or SachetProduct (with a unitsPerBundle property), can inherit from Product without re-writing basic code. This hierarchy reduces code duplication and streamlines system updates when adding new product types to the sari-sari store.

4. Polymorphism
Polymorphism enables different product types to implement the same method call in ways tailored to their specific behaviors. For example, both StandardProduct and PerishableProduct can share a calculateDiscount() method, but PerishableProduct can override it to automatically apply a discount if the item is near its expiration date. The main inventory system can invoke item.calculateDiscount() uniformly across an entire array of items without needing to check each item's specific class type beforehand.

Reflection
Among the four pillars, Encapsulation is the most crucial for improving the sari-sari store inventory system. In a small retail environment where inventory data is constantly updated during fast-paced manual sales, protecting data integrity is vital. Encapsulation ensures that critical product variables, such as stock levels and prices, cannot be modified accidentally or corrupted by external functions without going through validated methods like deductStock(). By bundling state and behavior securely, the application becomes reliable, bug-free, and easy to maintain as store operations scale.
