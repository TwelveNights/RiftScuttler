/**
 * Created by Stephanie on 11/4/2016.
 */
// https://gist.github.com/emptyhammond/1603144

function addData() {
    /*var elements = document.getElementsByClassName("attr");
    if (elements.length >= 1) {
        for (var i = 0; i < elements.length; i++) {
            var firstItem = elements[0];
        }
    }*/


}

var elSubmit = document.getElementById('submit');
elSubmit.addEventListener('submit', addData, false);

// click

var form = $('#add');
form.submit(function() {
    $.ajax({
        type: form.attr('method'),
        url: form.attr('action'),
        data: form.serialize(),
        success: function (data) {
            console.log("success");
        },
        error: function(data) {
            console.log("something went wrong!");
        }
    });
    return false;
});