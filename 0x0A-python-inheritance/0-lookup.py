def order_pizza(pizza_type, Extra_topping):
    pizza = "make a pizza " + pizza_type + " with " + Extra_topping + "."
    return pizza
first_pizza = order_pizza("pepperoni", "slice")
print(first_pizza)
second_pizza = order_pizza("pepp", "sluce")
print(second_pizza)
