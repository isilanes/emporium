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

async function create_lease(csrf_token) {
    let template_element = document.getElementById("latex-template");
    let owner_element = document.getElementById("owner");
    let resident_element = document.getElementById("resident");

    let payload = {
        "template_id": template_element.value,
        "owner_id": owner_element.value,
        "resident_id": resident_element.value,
    };

    let response;
    response = await fetch(
        "/api/leases/lease/create_lease/",
        {
            method: "POST",
            headers: {
                "X-CSRFToken": csrf_token,
                "Content-Type": 'application/x-www-form-urlencoded',
            },
            body: "payload=" + JSON.stringify(payload),
        }
    );
};