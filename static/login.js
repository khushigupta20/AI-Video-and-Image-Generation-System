$(document).ready(function(){
    
    $('#btnLogin').click(function(){
        let password = $('#loginpass').val();
        let email = $('#loginemail').val();
                
        // Make sure the code isn't empty
        if (!email.trim()) {
            alert("Please enter Email.");
            return;
        }

        // Make sure the code isn't empty
        if (!password.trim()) {
            alert("Please enter Password.");
            return;
        }

        // Send POST request to the /optimize endpoint
        $.ajax({
            url: "/token", // Replace with your API endpoint URL
            type: "POST",
            //contentType: "application/json",
            data: { username: email, password: password, grant_type: "password"  },
            //data: JSON.stringify({ email: email, password: password }),
            success: function (response) {
                // Assuming the server responds with { "token": "your-jwt-token" }
                //console.log(response);
                const token = response.access_token;

                // Store the token in Session Storage
                sessionStorage.setItem("jwtToken", token);
                // Set cookie
                Cookies.set('MY_TOKEN', token, { expires: 30 / 1440 }); // Cookie expires in 7 days

                document.location = "/jobs";
            },
            error: function (xhr, status, error) {
                // Handle errors
                console.error("Error:", error);
                alert("An error occurred: " + xhr.responseText || error);
            }
        });

    });

});