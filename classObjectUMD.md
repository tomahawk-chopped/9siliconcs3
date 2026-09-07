# SG4 - Understanding Classes and Objects
# MANGAOANG, KARL - IX-SILICON - 09/07/2026
## Sports - Equipment
## Represents any item or gear used by players during training or a game, such as a ball, bat, or protective gear. It tracks essential details like equipment type, condition, and availability.
## Properties
| Property | Data Type | Description |
| itemName | string	| The name or title of the equipment (e.g., "ShoheiOhtani-09062026-baseballbat") |
| quantity | int | The total number of units available in stock |
| unitPrice | double | The rental or replacement cost per item |
| isAvailable | boolean | Indicates whether the item is currently available for use |
## Methods
| Method | Description |
| borrowItem() | Sets isAvailable to false when the item is checked out |
| updateQuantity(amount: int) | Updates the stored total quantity by adding or subtracting the given integer amount |
| displayDetails() | Prints out the current properties and status of the equipment item |
## Class Diagram
+------------------------------------+
|             Equipment              |
+------------------------------------+
| - itemName: string                 |
| - quantity: int                    |
| - unitPrice: double                |
| - isAvailable: boolean             |
+------------------------------------+
| + borrowItem(): void               |
| + updateQuantity(amount: int): void|
| + displayDetails(): void           |
+------------------------------------+
## Design Explination
### It is because I like sports and I decided to add it to my UML.
### Property: itemName. Because I love to name unique names to an item. Example: ShoheiOhtani-09062026-baseballbat
### Method: displayDetails(). Sets out a good background of that item. Example: The bat was made in El Paso, Texas in 2024
