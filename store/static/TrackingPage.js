var trackingNumber = document.getElementById("trackingNumberInput")
var clickButton  = document.getElementById("submitButton")

clickButton.addEventListener('click', sendTracking)

function sendTracking(e)
{
	e.preventDefault();
	if(trackingNumber.value != "")
	{
		var trackNumber = trackingNumber.value;
	console.log("in sendTracking " + trackingNumber.value);
    //window.location.href = "track";
	console.log("sending trackNumber to server....");
   $.ajax({
        url : "./post_tracking", // the endpoint
        type : "GET", // http method
        data : { tNumber : trackNumber,
            'csrfmiddlewaretoken': '{{ csrf_token }}'
         }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            $('#trackingNumberInput').val(''); // remove the value from the input
            console.log("tracking number sent back by server",json); // log the returned json to the console
            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error : function(err)
        {
        	console.log("data could not be sent to server");
        }
        
    });

	}
	else 
	{	
	console.log("no input");
	}
	
}
