def clean_amount(text):
    """৳ আর কমা সরিয়ে সংখ্যায় ফেরত।"""
    return float(text.strip().replace("৳", "").replace(",", ""))


def taka(amount):
    """সংখ্যাকে টাকার format-এ ফেরত।"""
    return f"৳{amount:.2f}"


def read_lines(path):
    """ফাইল পড়ে লাইনগুলোর list ফেরত দিন।"""
    with open(path, encoding="utf-8") as fh:
        return fh.read().strip().split("\n")

if __name__ == "__main__":
    print(clean_amount(" ৳ 1,240.50 "))
    print(taka(1240.5))