class employee:
    def __init__(self):
        print("Started executing data")
        self.id=123
        self.salary=60000
        self.designation="SDE"
        print("Finished executed data")
    def travel(self,destination):
        return f"Employeee is now travelling too {destination}"


sam=employee()


print(sam.id)
print(sam.salary)
print(sam.designation)
print(sam.travel("bangladesh"))
