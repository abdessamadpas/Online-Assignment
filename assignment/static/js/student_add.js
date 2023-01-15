// store csrf token in a variable cookie


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

//  add new student

$(document).ready(function() {
    $("#submit_add_student").click(function(e) {
        console.log("u entered");
        e.preventDefault()

        var name = document.getElementById('student_name').value
        var email = document.getElementById('student_email').value
        var groupe = document.getElementById('groupe').value
        var matiere = document.getElementById('matiere').value
        console.log(name, email, groupe, matiere);



        var url = 'http://127.0.0.1:8000/dashboard/students/add_list_Student/'

        fetch(url, {
            method: 'POST',
            headers: {
                'Content-type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({
                'name': name,
                'email': email,
                'group_id': groupe,
                'matiere': matiere
            })
        }).then(function(response) {
            console.log('response', response)
        })


    })
})


// # delete student

$(document).ready(function() {
    $("#submit_deleteStudent").click(function(e) {
        console.log("u entered");
        e.preventDefault()

        var student_id = document.getElementById('id of student').value
        console.log(student_id);



        var url = 'http://127.0.0.1:8000/dashboard/students/fordelete'

        fetch(url, {
            method: 'DELETE',
            headers: {
                'Content-type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({

            })
        }).then(function(response) {
            console.log('response', response)
        })


    })
})