$(document).ready(function(){
    console.log("loaded");
    $.material.init();
    $(document).on("submit", "#register-form", function(e){
        e.preventDefault()
        var form = $('#register-form').serialize();
        $.ajax({
            url : '/postregistration',
            type: 'POST',
            data: form,
            success: function(response){
                console.log(response);
                window.location.href = '/login';

            }
        });
    });
    $(document).on("submit", "#login-form", function(e){
        e.preventDefault()
        var form = $(this).serialize();
        $.ajax({
            url : '/check-login',
            type: 'POST',
            data: form,
            success: function(res){
                if (res=="error"){
                    alert("Could not login");
                }
                else{
                     window.location.href = '/';
                     console.log("login in as",res);




                }
            }
        });
    });

    $(document).on("click", "#logout-link", function(e){
        e.preventDefault()
        $.ajax({
            url : '/logout',
            type: 'GET',
            success: function(resp){
                if (resp=="success"){
                    window.location.href='/login';
                }
                else{
                    alert("Something went wrong");
                }


            }
        });
    });
    $(document).on("submit", "#post-activity", function(e){
        e.preventDefault()
        var form = $('#post-activity').serialize();
        $.ajax({
            url: '/post-activity',
            type: 'POST',
            data: form,
            success: function(res){
                console.log(res);
                window.location.href = '/';

            }
        });
    });
    $(document).on("submit", ".comment-form", function(e){
        e.preventDefault()
        console.log("helo");
        var form = $(this).serialize();
        $.ajax({
            url: '/submit-comment',
            type: 'POST',
            data: form,

            success: function(res ){
                window.location.href = '/';
                console.log(res);


            }
        });
    });
});
