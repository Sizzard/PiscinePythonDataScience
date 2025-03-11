from time import time
from datetime import datetime

ft_month = {
    1: "Jan",
    2: "Feb",
    3: "Mar",
    4: "Apr",
    5: "May",
    6: "Jun",
    7: "Jul",
    8: "Aug",
    9: "Sept",
    10: "Oct",
    11: "Nov",
    12: "Dec",
}

x = datetime.now()

timestamp = time()

print(f"Seconds since January 1, 1970: {timestamp:,.4f} or {timestamp:.2e} in scientific notation")
print(f"{ft_month[x.month]} {x.day} {x.year}")