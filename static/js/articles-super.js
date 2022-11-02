$(document).ready(function() {
    ajax_get()
});

function ajax_get() {

    $.get('/articles/json-artc', function(articles) {
        $('#articles_cards').empty()
        articles.map((atc) => {
            $('#articles_cards').append(
                `
                <div class="card" >
                    <div class="card-body d-flex flex-column">
                        <h4 class="card-title" style="font-size:large"> ${atc.fields.title} </h4>
                        <h6 class="card-subtitle mb-2 text-muted">• ${atc.fields.date}</h6>
                        <hr style="color:white"></hr>
                        <p class="card-text" style="font-size:medium"> ${atc.fields.content.substring(0,50)}...</p>

                        <div class="flex justify-between gap-3" style="position: absolute; bottom: 15px;">
                            <div class="flex flex-col justify-center rounded" >
                                <a type="button" class="btn" style="background-color: #613FE5; margin-left: 15px; font-weight: bold; color: white;" 
                                href="/articles/read/${atc.pk}">Read More</a>
                                <a type="button" class="btn" style="background-color: #9D1325; margin-left: 10px; font-weight: bold; color: white;" 
                                href="/articles/delete-articles/${atc.pk}">X</a>
                            </div>
                        </div>
                    </div>
                </div>
                `
            )
        })
    })
}

