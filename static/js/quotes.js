// Function Ready
$(function(){
    showImage()
});

function showImage(){
    // Preventing Duplicate
    $("#board").empty();

    // Get Data & Append
    $.ajax({
        type: "GET",
        url : "/quotes/get_image",
        success: function(response){
            // Debug
            console.log("Below is the data");
            console.log(response);

            $("#board").empty();
            let Array = response.images

            for (let key in Array){
                let title = Array[key].title;
                let image = Array[key].image;

                appendImage(title, image);
            }
        },
        // Debug
        error: function(){
            alert("ERROR | get_image failure");
        }
    });
}

// Append HTML Element
function appendImage(title, image){
    $("#board").append(`
        <div class="grid-item">
            <img src="/media/${image}" alt="${title}"/>
        </div>
    `)
}

// // Submit Event
// $(document).on('submit', '#add_quote', function(event) {
//     event.preventDefault();
//     console.log('Adding Image')
//     $.ajax({
//         type    : "POST",
//         url     : "quotes/add_quote",
//         dataType: 'json',
//         data    : $("form#add_quote").serialize(),
//         success: function(data){
//             document.getElementById("add_quote").reset();
//             console.log(data);
//             showImage();
//         },
//         // Debug
//         error: function(){
//             alert("ERROR | add_quote failure");
//         }
//     });
// });