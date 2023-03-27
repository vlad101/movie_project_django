$(function(){
    
  // Initialize the Datepicker plugin
  $('#movie_year').datepicker({
    format: 'yyyy',  // Set the format to year only
    viewMode: 'years',  // Set the view mode to year only
    minViewMode: 'years',  // Set the minimum view mode to year only
  }).on('keydown', function(event) {
    // Get the key code of the pressed key
    var keyCode = event.keyCode || event.which;

    // Allow only digits (0-9), backspace (8), delete (46), and numlock digits (96-105) keys
    if (keyCode < 48 || keyCode > 57) {
        if (keyCode < 96 || keyCode > 105) {
            if (keyCode != 8 && keyCode != 46) {
                // Prevent default behavior for non-digit keys
                event.preventDefault();
            }
        }
    }
  }).on('changeDate', function(event) {
    // Hide the Datepicker when a year is selected
    $(this).datepicker('hide');
    
    // Get the selected year
    var selectedYear = event.date.getFullYear();

    // Get the current year
    var currentYear = new Date().getFullYear();

    // Validate the selected year to be within the valid range (not negative and not exceeding the current year)
    if (selectedYear < 0 || selectedYear > currentYear) {
        // Reset the input value and show an error message
        $(this).val('');
    }
  });

  // Initialize the autocomplete plugin
  $('#movie_name').autocomplete({
    source: function(request, response) {
      // Make an AJAX request to the server to get the autocomplete suggestions
      $.getJSON('/movie/autocomplete-movie-search', {
          q: request.term
      }, function(data) {
          // Pass the suggestions to the autocomplete plugin
          response(data);
      });
    },
    minLength: 2, // Only show suggestions after the user has typed at least 2 characters
    select: function(event, ui) {
      // Remove the year from the label
      var label = ui.item.label.replace(/\s\(\d{4}\)$/, '');
      // Set the value of the input field to the label of the selected item
      $('#movie_name').val(label);
      // Set the value of the hidden field to the ID of the selected item
      $('#movie_id').val(ui.item.id);
      return false; // Prevent the form from submitting
    }
  }).autocomplete('instance')._renderItem = function(ul, item) {
    // Create a <li> element to hold each suggestion
    var li = $("<li>").appendTo(ul);
    // Create a <div> element to hold the text and image
    var div = $("<div>").appendTo(li);
    // Create an <img> element for the image
    $("<img>").attr("src", item.image_url).appendTo(div);
    // Create a <span> element for the label text
    $("<span>").text(item.label).appendTo(div);
    // Add pixels of margin to the right side of the image
    div.find("img").css({"margin-right":"10px","width":"50px","height": "70px"});
    // Close the <li> element
    return li;
  };
});

// Get the "Check All" and "Uncheck All" checkboxes and all the other checkboxes
const checkAllCheckbox = document.getElementById("check-all");
const uncheckAllCheckbox = document.getElementById("uncheck-all");
const infoCheckboxes = document.querySelectorAll(".info-checkbox");

// Add event listeners to the "Check All" and "Uncheck All" checkboxes
checkAllCheckbox.addEventListener("change", function() {
  for (let i = 0; i < infoCheckboxes.length; i++) {
    infoCheckboxes[i].checked = true;
  }
  uncheckAllCheckbox.checked = false;
});

uncheckAllCheckbox.addEventListener("change", function() {
  for (let i = 0; i < infoCheckboxes.length; i++) {
    infoCheckboxes[i].checked = false;
  }
  checkAllCheckbox.checked = false;
});

// Add event listener to the other checkboxes
for (let i = 0; i < infoCheckboxes.length; i++) {
  infoCheckboxes[i].addEventListener("change", function() {
    let allChecked = true;
    for (let j = 0; j < infoCheckboxes.length; j++) {
      if (!infoCheckboxes[j].checked) {
        allChecked = false;
        break;
      }
    }
    checkAllCheckbox.checked = allChecked;
    uncheckAllCheckbox.checked = false;
  });
}
