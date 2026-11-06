# Skill Test
from pyscript import display, document

def OrderSummary(e):
    document.getElementById("result").innerHTML = ""

    item1 = document.getElementById("item1")
    item2 = document.getElementById("item2")
    item3 = document.getElementById("item3")
    item4 = document.getElementById("item4")
    item5 = document.getElementById("item5") 
    item6 = document.getElementById("item6")
    item7 = document.getElementById("item7")
    

    subtotal = float(item1.value) * item1.checked #calculate the subtotal using the selected values

    #add the current value of the items to the subtotal
    # .checked adds the selected item only
    subtotal += float(item2.value) * item2.checked
    subtotal += float(item3.value) * item3.checked
    subtotal += float(item4.value) * item4.checked
    subtotal += float(item5.value) * item5.checked
    subtotal += float(item6.value) * item6.checked
    subtotal += float(item7.value) * item7.checked

    tax = subtotal * 0.12 #multiplied by 0.12 for tax
    total = subtotal + tax

    display(f"Subtotal: ₱{subtotal:.2f}", target="result") 
    display(f"Tax: ₱{tax:.2f}", target="result")
    display(f"Total: ₱{total:.2f}", target="result")