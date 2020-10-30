uri = "mongodb://localhost:27017"
dbname = "Coding"
is_active = 0
new_sheet_name = "Main"
is_groupby = 0
group_by = "function_name"
collection_name = "collection"
collection_name_alias = "Stats"
sender = "sarvidigilocker@gmail.com"
reciever = ["18eucs100@skcet.ac.in"]
password = "digintern"
debug_mode = 0
flag = 1


configuration_count = {
    "stats_for_1": {
        "name": "Stats with filter",
        "uri": uri,
        "dbname": dbname,
        "is_groupby": 1,
        "group_by": {"name": "$name"},
        "field_name": "created_date",
        "is_active": 1,
        "new_sheet_name": "My Sheet",
        "collection_name": "collection",
        "interval_mode": "day",
        "interval_date": "2020-10-06",
        "interval_time": "00:00:00",
        "filter": {"name": "Pascal"},
    },
    "stats_for_2": {
        "name": "sarvi with filter",
        "uri": uri,
        "dbname": dbname,
        "is_groupby": 1,
        "group_by": {"name": "$name"},
        "field_name": "created_date",
        "is_active": 1,
        "new_sheet_name": "My Sheet",
        "collection_name": "collection",
        "interval_mode": "day",
        "interval_date": "2020-10-25",
        "interval_time": "00:00:00",
        "filter": {"name": "Java"},
    },
}