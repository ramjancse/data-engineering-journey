#!/usr/bin/env python3
"""
অ্যাসাইনমেন্ট ৫ — শুরু করার ফাইল

ভয় পাবেন না। এই ফাইলটা এখনই চলে — চালিয়ে দেখুন:

    python3 module-03/assignments/class-05-starter.py

শূন্য দেখাবে। আপনার কাজ ওই শূন্যগুলোকে আসল সংখ্যায় বদলানো।

তিনটা লেভেল আছে। লেভেল ১ সবার জন্য। ওটুকু হলেই জমা দিতে পারবেন।
পারলে ২, তারপর ৩।
"""

import os
import my_tools

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(
    BASE_DIR, "..", "..",
    "ostad-de-bootcamp", "module-02", "data", "raw_sales.txt"
)


# def clean_amount(text):
#     """৳ আর কমা সরিয়ে সংখ্যায় ফেরত।"""
#     return float(text.strip().replace("৳", "").replace(",", ""))


# def taka(amount):
#     """সংখ্যাকে টাকার format-এ ফেরত।"""
#     return f"৳{amount:.2f}"


# def read_lines(path):
#     """ফাইল পড়ে লাইনগুলোর list ফেরত দিন।"""
#     with open(path, encoding="utf-8") as fh:
#         return fh.read().strip().split("\n")

    
# ============================================================
#  লেভেল ১ — শুধু bkash
#  লক্ষ্য:  bkash  3টা  ৳2484.00
# ============================================================
def calculate_totals(lines):
    totals = {}

    for raw in lines:
        parts = raw.split(";")

        amount = my_tools.clean_amount(parts[5])
        payment = parts[6].strip().lower()
        status = parts[7].strip().lower()

        if status == "cancelled":
            continue

        if payment not in totals:
            totals[payment] = {
                "count": 0,
                "total": 0.0
            }

        totals[payment]["count"] += 1
        totals[payment]["total"] += amount

    return totals
# ============================================================
#  লেভেল ২ — আরো দুইটা যোগ করুন
#  লক্ষ্য:  nagad  2টা  ৳908.00
#           card   1টা  ৳812.00
# ============================================================
#
# উপরের loop-টাই কাজে লাগবে। শুধু:
#   - উপরে আরো চারটা ঘর বানান (nagad_total, nagad_count, card_total, card_count)
#   - loop-এর ভেতরে if-এর পরে elif যোগ করুন:
#
#       if payment == "bkash":
#           ...
#       elif payment == "nagad":
#           ...
#       elif payment == "card":
#           ...

# TODO ৩


# ============================================================
#  লেভেল ৩ — বাকি দুইটা
#  লক্ষ্য:  rocket            1টা  ৳232.25
#           cash on delivery  2টা  ৳661.50
# ============================================================
#
# rocket-এর জন্য আরেকটা elif.
# আর cash on delivery-র জন্য শেষে else — কারণ ফাইলে ওটা দুই বানানে আছে।
#
# শেষে মিলিয়ে দেখুন:  সব মিলিয়ে ৳5097.75

# TODO ৪


# ============================================================
#  বোনাস — যাঁরা তিনটা লেভেলই শেষ করেছেন
# ============================================================
#
# কোন তারিখে সবচেয়ে বেশি টাকার অর্ডার হয়েছে?
# পাঁচটা তারিখ: 2026-10-07 থেকে 2026-10-11
# নিয়ম একই — পাঁচটা ঘর, আর if/elif দিয়ে ঠিক ঘরে যোগ।
#
# (হ্যাঁ, এটা ক্লান্তিকর। সোমবার dictionary শিখলে এই পুরোটা তিন লাইনে নামবে।)

# TODO ৫
def main():
    lines = my_tools.read_lines(PATH)
    totals = calculate_totals(lines)

    print("payment ধরে হিসাব (বাতিল বাদে)")
    print()

    for payment, data in totals.items():
        print(f"{payment:<18} {data['count']}টা   {my_tools.taka(data['total'])}")

    grand_total = sum(data["total"] for data in totals.values())
    print()
    print(f"সব মিলিয়ে: {my_tools.taka(grand_total)}")

if __name__ == "__main__":
    main()