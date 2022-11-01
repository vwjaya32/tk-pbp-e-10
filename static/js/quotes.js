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

            let Array = response.images

            for (let key in Array){
                let title = Array[key].title;
                let image = Array[key].image;

                appendImage(title, image);
            }

            // Run this after appending Image
            layout();
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
            <img src="${image}" alt="${title}"/>
        </div>
    `)
}

// Run Masonry Layout
function layout() {
    console.log("loaded");
    var $grid = $('#board').masonry({
        itemSelector: '.grid-item',
        columnWidth: 0,
    });

    $grid.imagesLoaded().progress(function () {
        $grid.masonry('layout');
    });
}

// Image Preview on Modal
$(document).on('click', '#promptAdd', function(){
    $("#imageurl").on('input', function() {
        console.log("test")
        // Adding img html to Modal
        $("#imageFrame").html("<img id='imagePreview' src='' alt='Not a Valid Image'>")

        // Change src attr to input url
        let url = $("#imageurl").val();
        $("#imagePreview").attr("src", url);
    });
});

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