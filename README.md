# CalendarTW, Taiwan Calendar, 台灣行事曆
Provides the `list` and `dict` format of Taiwan Calendar.

Please note that the list data format is came from [TaiwanCalendar](https://github.com/ruyut/TaiwanCalendar)

Simply type `python transfer.py` to transfer from list to dict format


(Note) We shoud use `encoding="utf-8-sig"`

------------------------
因為想要一個以日期當key的dict行事曆所以就自己做了一個, 
./data裡面的json檔案是從[TaiwanCalendar](https://github.com/ruyut/TaiwanCalendar)這邊來的
開檔案的時候注意 `encoding="utf-8-sig"`

------------------------
LIST
```
[
  {
    "date": "20200101",
    "week": "三",
    "isHoliday": true,
    "description": "開國紀念日"
  },
  {
    "date": "20200102",
    "week": "四",
    "isHoliday": false,
    "description": ""
  },
  ...
]
```
DICT
```
{
    "20170101": {week: ..., isHoliday: ..., description: ...},
    ...
}
```
