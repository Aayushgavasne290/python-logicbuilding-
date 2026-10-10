students ={101:{"name": "aditi","scores":[90, 85, 92]},
           102:{"name": "bob","scores":[88, 92, 89]},
           103:{"name": "charlie","scores":[95, 90, 93]},
           104:{"name": "david","scores":[80, 85, 88]},
           105:{"name": "priya","scores":[45,78,98]}
           }
for sid, details in students.items():
    avg = sum(details["scores"]) / len(details["scores"])
    details["avrage"] = avg
    details["passed"] = avg >= 30

print("students who are passed:")
for sid ,details in students.items():
    if details["passed"]:
        