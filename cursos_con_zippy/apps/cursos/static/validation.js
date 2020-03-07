$(document).ready(function(){

// function ValidateEmail(mail) {
//     var mailformat = /\S+@\S+\.\S+/;
//     if(mail.value.matc(mailformat)){
//         return true;
//     }
//     else{
//         return false;
//     }
// }

$('#email').keyup(function(){

        console.log("KeyUP**********")
        $.ajax({
            method:"GET",
            url: "/username",
            data : {'email': $("#email").val()}
            
        })
        .done(function(res){
            $('#usernameMsg').html(res)
            console.log(res)
            })
        }
)})
