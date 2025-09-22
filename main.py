from pyscript import document, display

def generate_msg(e):
    
    name = str(document.getElementById("name").value) #string
    age = str(document.getElementById("age").value) #string
    school = str(document.getElementById("school").value) #string
    
    notes = '''This is name. She's currently age year old, and studies at school.
    \nThis information was retrieved via input fields and displayed \nusing a 
    multiline string in Python via PyScript
    '''
    notes = notes.replace("name", name).replace("age", age).replace("school", school) 
    
    display(f"Name: {name}", target="name1") #name
    display(f"Age: {age}", target="age1") #age
    display(f"School: {school}", target="school1") #school
    display(notes, target="notes") 


