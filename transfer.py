import json
from pathlib import Path
from collections import defaultdict
def from_list_to_dict(org_file: str, new_file: str):
    """
    to transfer the list format to dict(date as key) format
    e.g:
    LIST
    [
      {
        "date": "20170101",
        "week": "日",
        "isHoliday": true,
        "description": "開國紀念日"
      },
      {
        "date": "20170102",
        "week": "一",
        "isHoliday": true,
        "description": "補假"
      },
    ]

    DICT
    {
        "20170101": {week: ..., isHoliday: ..., description: ...},
        ...
    }
    :param org_file: the original list file format
    :param new_file: make the date as key
    """
    target_dict = defaultdict(dict)
    key_to_keep = ["week", "isHoliday", "description"]
    main_key = "date"
    with open(org_file, 'r', encoding="utf-8-sig") as f:
        data = json.load(f)
        for item in data:
            target_dict[item[main_key]] = {k:item[k] for k in key_to_keep}

    with open(new_file, "w", encoding="utf-8-sig") as f:
        json.dump(target_dict, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    list_dir = Path("./data")
    target_dir = Path("data_dict")
    for org_file in list(list_dir.glob("*.json")):
        new_file = target_dir / (org_file.name + ".txt")
        from_list_to_dict(str(org_file), str(new_file))
