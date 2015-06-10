# make some simple store function

receipts = [
    {"id": 1, "datetime": "1/1/2001 12:39"},
    {"id": 2, "datetime": "2/2/2001 22:39"}
]

items = [
    {"id": 1, "name": "widget", "price": 1.00},
    {"id": 2, "name": "sling-a-rang", "price": 10.01}
]

lines = [
    {"id": 1, "qty": 3, "item_id": 1, "receipt_id": 1},
    {"id": 2, "qty": 2, "item_id": 2, "receipt_id": 1},
    {"id": 2, "qty": 2, "item_id": 2, "receipt_id": 2}
]

def print_all_receipts_totals():
    for r in receipts:
        total = 0
        for line in lines:
            # does tis belong to this receipt
            if line["receipt_id"] == r["id"]:

                # item = get_item(line["item_id"])
                # this line above can be replaced by the for loop below, but is more clunky

                # find item that this line points to
                for i in items:
                    # is this the item this line points to via item id
                    if i["id"] == line["item_id"]:
                        # its a match
                        item = i
                        # adding the word break makes it as efficient as the other function
                        # stops the for i in items loop
                        break
                total += line["qty"] * item["price"]
        print r["id"], r["datetime"], total

#nest data or
hierarchical_receipts = [
    {
        "id": 1,
        "datetime": "1/1/2001 12:39",
        "lines": [
                    {
                        "id": 1,
                        "qty": 3,
                        "item_id": 1,
                        "receipt_id": 1
                    },
                    {
                        "id": 2,
                        "qty": 2,
                        "item_id": 2,
                        "receipt_id": 1
                    }
                ]
    },
    {
        "id": 2,
        "datetime": "2/2/2001 22:39",
        "lines": [
            {
                "id": 2,
                "qty": 2,
                "item_id": 2,
                "receipt_id": 2
            }
        ]
    }
]


def hierarchical_print_all_receipt_totals():
    for i in hierarchical_receipts:
        total = 0
        for line in r.lines:
            item = line["item"]
            total += line["qty"] * item["price"]
        print r["id"], r["datetime"], total



def get_item(item_id):
    for i in items:
        if i["id"] == item_id:
            return i
    return None



print print_all_receipts_totals()
print hierarchical_receipts()






