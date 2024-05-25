import json


def get_records(filename):
    with open(filename, "r") as json_file:
        json_list = list(json_file)
        json_objects = [
            json.loads(json.loads(json.dumps(json_str))) for json_str in json_list
        ]
    return json_objects


def analyze_brand_codes():
    brand_codes = set()
    count_test_brand_codes = 0
    count_records_missing_brand_code = 0
    count_records_missing_top_brand = 0
    number_of_top_brands = 0
    brands_json_records = get_records("data-sources/brands.jsonl")

    for rec in brands_json_records:
        brand_code = rec.get("brandCode")
        top_brand = rec.get("topBrand")

        if brand_code:
            brand_codes.add(brand_code)
            if "@" in brand_code or "TEST" in brand_code:
                count_test_brand_codes += 1
        else:
            count_records_missing_brand_code += 1

        if top_brand:
            if top_brand == True:
                number_of_top_brands += 1
        else:
            count_records_missing_top_brand += 1

    # print(f"Brand Codes: {brand_codes}")
    print(
        f"Percentage of unique brands in file: {len(brand_codes)/len(brands_json_records) * 100} %"
    )
    print(
        f"Percentage of test brands in file: {count_test_brand_codes/len(brands_json_records) * 100} %"
    )
    print(
        f"Percentage of top brands in file: {number_of_top_brands/len(brands_json_records) * 100} %"
    )
    print(
        f"Percentage of entries missing brand codes: {count_records_missing_brand_code/len(brands_json_records) * 100} %"
    )
    print(
        f"Percentage of entries missing top brand flag: {count_records_missing_top_brand/len(brands_json_records) * 100} %"
    )


def analyze_receipts_data():
    receipt_json_records = get_records("data-sources/receipts.jsonl")
    statuses_count_hashmap = {
        status: 0
        for status in ["FLAGGED", "SUBMITTED", "REJECTED", "PENDING", "FINISHED"]
    }
    number_of_items = 0
    number_of_receipts_with_one_item = 0
    number_of_receipts_without_items = 0

    for rec in receipt_json_records:
        status = rec.get("rewardsReceiptStatus")
        items = rec.get("rewardsReceiptItemList")
        if items:
            number_of_items += len(items)
            if len(items) == 1:
                number_of_receipts_with_one_item += 1
        else:
            number_of_receipts_without_items += 1
        statuses_count_hashmap[status] += 1
    print(statuses_count_hashmap)
    print(
        f"Average number of items purchased by consumers: {number_of_items/len(receipt_json_records)}"
    )
    print(
        f"Percentage of receipts with just one item: {number_of_receipts_with_one_item/len(receipt_json_records) * 100} %"
    )
    print(
        f"Percentage of receipts with zero items: {number_of_receipts_without_items/len(receipt_json_records) * 100} %"
    )


if __name__ == "__main__":
    analyze_brand_codes()
    analyze_receipts_data()
