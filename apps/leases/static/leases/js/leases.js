$(document).ready(function() {});

function mytoggle(id) {
    var x = document.getElementById(id);
    if (x.style.display == "none") {
        x.style.display = "";
    } else {
        x.style.display = "none";
    }
};

function show_create_lease() {
    mytoggle('add-lease');
    mytoggle('new-button');
    mytoggle('create-buttons');
};