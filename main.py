from pyscript import document

def compute(event):

    num1 = float(document.querySelector("#input1").value)
    num2 = float(document.querySelector("#input2").value)
    operation = document.querySelector("#operations").value


    if operation == "add":

        result = num1 + num2
    elif operation == "subtract":
   
        result = num1 - num2
    elif operation == "multiply":
 
        result = num1 * num2
    elif operation == "divide":

        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    else:
        result = "Invalid operation"

    document.querySelector("#output").innerText = f"Result: {result}" 
