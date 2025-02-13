function onPageLoad() {
    $.get("/get_location_names", function (data) {
        if (data.locations) {
            let locationsDropdown = $("#uiLocations");
            locationsDropdown.empty();
            locationsDropdown.append(new Option("Choose a Location", "", true, true));
            data.locations.forEach((location) => {
                locationsDropdown.append(new Option(location, location));
            });
        }
    });
}

function onClickedEstimatePrice() {
    let sqft = $("#uiSqft").val();
    let bhk = $("#uiBHK").val();
    let bath = $("#uiBathrooms").val();
    let location = $("#uiLocations").val();

    if (!sqft || !bhk || !bath || !location) {
        alert("Please enter all details");
        return;
    }

    // Show progress bar
    $("#progressBar").show();
    $(".progress").css("width", "0%"); // Reset progress bar
    setTimeout(() => $(".progress").css("width", "100%"), 500); // Animate progress bar

    let requestData = {
        total_sqft: parseFloat(sqft),
        bhk: parseInt(bhk),
        bath: parseInt(bath),
        location: location
    };

    $.ajax({
        url: "/predict_home_price",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify(requestData),
        success: function (response) {
            $("#uiEstimatedPrice").html("<h2>Estimated Price: ₹" + response.estimated_price + " Lakhs</h2>");
        },
        error: function () {
            $("#uiEstimatedPrice").html("<h2>Could not fetch the estimated price.</h2>");
        },
        complete: function () {
            setTimeout(() => $("#progressBar").fadeOut(), 500); // Hide progress bar after completion
        }
    });
}

$(document).ready(function () {
    onPageLoad();
});
