// Function Ready
$(function(){
    showImage()
    layout()
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