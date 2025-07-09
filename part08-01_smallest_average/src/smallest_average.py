# Write your solution here
def smallest_average(person1: dict, person2: dict, person3: dict):
    avg1 = (person1["result1"] + person1["result2"] + person1["result3"]) / 3
    avg2 = (person2["result1"] + person2["result2"] + person2["result3"]) / 3
    avg3 = (person3["result1"] + person3["result2"] + person3["result3"]) / 3
    reslut = [
        (avg1, person1),
        (avg2, person2),
        (avg3, person3),
    ]
    
    smallest = min(reslut, key=lambda x:x[0])
    return smallest[1]