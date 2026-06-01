# creating waiter class :
class waiter:
    # attributes
    def __init__(self, names, is_busy, tables):
        self.names = names
        self.is_busy = is_busy
        self.tables = tables

    # methods
    def get_order(self, tables, order):
        out = f"table {tables} has ordered {order}.Hurry up!! "
        self.is_busy = True
        self.tables.append(tables)
        return out

    def check(self, tables, cost):
        out = f" table {tables} Hello .Your cost is {cost} dollar ,"
        self.tables = False
        return out


# Examples
waiter1 = waiter("mary", True, [1, 2, 3])
waiter2 = waiter("mahsa", False, [])

print(waiter2.tables, waiter2.is_busy)
print(waiter2.get_order(4, "esperso"))
print(waiter2.tables, waiter2.is_busy)
