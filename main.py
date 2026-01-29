from pyscript import document, display
def show_team(e): #define function show_team to show intramurals team based on selected grade and section
    grade = int(document.getElementById("grade_level_dropdown").value)
    section = str(document.getElementById("section_dropdown").value)
    registered = document.querySelector('input[name="registered"]:checked')
    medical = document.querySelector('input[name="medical"]:checked')

    if grade == 7 and registered == "Yes" and medical == "Yes":
        if section == "Ruby":
            message = "Your intramurals team is the Yellow Tigers!"
        elif section == "Sapphire":
            message = "Your intramurals team is the Red Bulldogs!"
        elif section == "Emerald":
            message = "Your intramurals team is the Blue Bears!"
        elif section == "Topaz":
            message = "Your intramurals team is the Green Hornets!"
        elif section == "Jade":
            message = "Invalid Grade & Section."

    elif grade == 8 and registered == "Yes" and medical == "Yes":
        if section == "Ruby":
            message = "Your intramurals team is the Red Bulldogs!"
        elif section == "Sapphire":
            message = "Your intramurals team is the Green Hornets!"
        elif section == "Emerald":
            message = "Your intramurals team is the Yellow Tigers!"
        elif section == "Topaz":
            message = "Your intramurals team is the Blue Bears!"
        elif section == "Jade":
            message = "Your intramurals team is the Blue Bears!"

    elif grade == 9 and registered == "Yes" and medical == "Yes":
        if section == "Ruby":
            message = "Your intramurals team is the Blue Bears!"
        elif section == "Sapphire":
            message = "Your intramurals team is the Yellow Tigers!"
        elif section == "Emerald":
            message = "Your intramurals team is the Green Hornets!"
        elif section == "Topaz":
            message = "Your intramurals team is the Red Bulldogs!"
        elif section == "Jade":
            message = "Your intramurals team is the Jade Green Hornets!"

    elif grade == 10 and registered == "Yes" and medical == "Yes":
        if section == "Ruby":
            message = "Your intramurals team is the Green Hornets!"
        elif section == "Sapphire":
            message = "Your intramurals team is the Yellow Tigers!"
        elif section == "Emerald":
            message = "Your intramurals team is the Red Bulldogs!"
        elif section == "Topaz":
            message = "Your intramurals team is the Blue Bears!"
        elif section == "Jade":
            message = "Invalid Grade & Section."

    else:
        message = f"Please finish the online registration and/or get medical clearance from the clinic before signing up."

    display(message, target="team_message")