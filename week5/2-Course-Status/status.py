def status_count(students):
    arr = {"finalized":[],
           "not_finalized":[]}
    for student in students:
        if student["status"] == "finalized":
            arr["finalized"] += [student["name"]]
        else:
            arr["not_finalized"] += [student["name"]]
    return arr




students = [{
              "name": "RadoRado",
              "status": "not_finalized"
            }, {
              "name": "Ivo",
              "status": "finalized"
            }, {
              "name": "Genadi",
              "status": "finalized"
            }]

print(status_count(students))
