// Function Ready
$(document).ready(function(){
    showImage()
});

function showImage(){
    // Get Data & Append
    $.ajax({
        type: "GET",
        url : "/quotes/get_image",
        success: function(response){
            // Preventing Duplicate
            $("#board").empty();
            // Debug
            console.log(response.data);
            let datas = response.data
            console.log(response.data[0])
            for (let data of datas){
                let title = data.fields.title;
                let image = data.fields.image;
                let uploader = data.fields.user;
                let id    = data.pk;

                // Account Related
                let request_user = data.who; // who is login right now
                let admin_stat = data.admin_stat; // is current user is admin

                console.log(response.data[0])

                // Check apakah user punya akses menghapus
                let delete_access = "";
                if (admin_stat){
                    delete_access = '<a class="btn btn-outline-danger" id="delete-button" href="/quotes/delete_image/' + id + '" role="button"> Hapus </a>'
                } else if (request_user === uploader){
                    delete_access = '<a class="btn btn-outline-danger" id="delete-button" href="/quotes/delete_image/' + id + '" role="button"> Hapus </a>'
                } else {
                    delete_access = '<div></div>'
                }

                appendImage(title, image, id, uploader, delete_access);
            }
            layout()
        },
        // Debug
        error: function(){
            alert("ERROR | get_image failure");
        }
    });
}

// Append HTML Element
function appendImage(title, image, pk, username, delete_button){
    $("#board").append(`
        <div class="grid-item" id="image-${pk}">
            <img src="${image}" alt="${title}" data-bs-toggle="modal" data-bs-target="#modal-${pk}">
        </div>
        
       <div class="modal fade"
             id="modal-${pk}"
             tabindex="-1"
             aria-labelledby="exampleModalLabel"
             aria-hidden="true">
            <div class="modal-dialog" id="image-modal-dialog">
                <div class="modal-content">
                    <div class="modal-body" id="image-modal-body">
                        <div id="imageFrame">
                            <img src="${image}" alt="${title}">
                        </div>
                        <div class="row">
                            <h1> ${title} </h1>
                            <h5> By ${username} </h5>
                            <center>
                                ${delete_button}                   
                            </center>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `)
}

// Run Masonry Layout
function layout() {
    let $grid = $('#board').masonry({
        itemSelector: '.grid-item',
        columnWidth: 0,
    });

    $grid.imagesLoaded().progress(function () {
        $grid.masonry('layout');
        console.log("running masonry")
    });
}

// Image Preview on Modal
$(document).on('click', '#promptAdd', function(){
    $("#imageurl").on('input', function() {
        console.log("test")
        // Adding img html to Modal
        $("#imageFrame").html('<img id="imagePreview"  class="rounded mx-auto d-block" src="" alt="Not a Valid Image">')

        // Change src attr to input url
        let url = $("#imageurl").val();
        $("#imagePreview").attr("src", url);
    });
});


// Async add Image
$(document).on('submit', '#add_quote', function(event) {
    event.preventDefault();
    $.ajax({
        type    : "POST",
        url     : "/quotes/ajax_add_quote",
        data    : $("form#add_quote").serialize(),
        success: function(){
            console.log("you have accessed ajax add")
            window.location.reload();
            },
        // Debug
        error: function(){
            alert("ERROR | add_quote failure");
        }
    });
})

