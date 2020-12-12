# moving
def left(): return "a"
def right(): return "d"
def up(): return "w"
def down(): return "s"
def bail_out(): return "bailOut"

# digging collecting placing
def dig(): return "dig"
def bury(): return "bury"
def collect(): return "collect"
def drop_part(part_id): return "dropPart-" + part_id
def swap_part(part_id): return "swapPart-" + part_id
def place_trap(): return "trap"


# buying and selling
def buy_potion(): return "buy-potion"
def use_potion(): return "usePotion"
def buy_trap(): return "buy-trap"
def buy_part(part_id): return "buy-" + part_id
def sell_part(part_id): return "sell-" + part_id
def trade_parts(give_part_id, take_part_id): return "trade-" + give_part_id + "-" + take_part_id
def sell_part_with_curse(part_id): return "sellPartWithCurse-" + part_id
def trade_parts_with_curse(give_part_id, take_part_id): return "tradeWithCurse-" + give_part_id + "-" + take_part_id
def sell_totem(): return "sellTotem"
