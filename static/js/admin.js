function enableEdit() {
    console.log("editing");
    var textboxes = document.getElementsByClassName("bike-pos-input");
    var i = 0;

    for (i = 0; i < textboxes.length; i++) {
        textboxes[i].disabled ^= true;
    }

    var editButton = document.getElementById("edit-button");
    var editStatus = editButton.textContent;

    if(editStatus == "Enable Edit"){
        editButton.textContent = "Disable Edit";
    }

    if(editStatus == "Disable Edit"){
        editButton.textContent = "Enable Edit";
    }
}