
$(document).ready(function(){
    $("#refresh_data").click(function(){
        $.get("/com_events/json_all/", function(data) {
            $("#title").empty();
            $("#main_div").empty();
            $("#title").append('List Of Events');
              for(var i = 0 ; i < data.length; i++){
                const date = new Date(data[i].fields.date)
                  $("#main_div").append(`
                <div class="modal fade" id="modal_confirm-${data[i].pk}" tabindex="-1" aria-labelledby="mainModalLabel" aria-hidden="true">
                    <div class="modal-dialog">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h1 class="modal-title fs-5" id="mainModalLabel">
                                    Are You Sure?
                                </h1>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close" id="close_confirm-${data[i].pk}"></button>
                            </div>
                            <div class="modal-body">
                            </div>
                            <div class="modal-footer">
                                <button type="button" data-bs-dismiss="modal">Go Back</button>
                                <button type="submit" class="btn btn-primary" data-pk='${data[i].pk}' id="confirm-${data[i].pk}">Confirm</button>
                            </div>
                        </div>
                    </div>
                </div>
                  <div id='item-${data[i].pk}'>
                  <h1>${data[i].fields.name}</h1>
                      <div>${date}
                        <p>
                          ${data[i].fields.description}
                        </p>
                      </div>
                        <button data-bs-toggle="modal" data-bs-target="#modal_confirm-${data[i].pk}">
                            Join
                        </button>
                  </div>
                  `
                  )
                  $(`#confirm-${data[i].pk}`).click(function(){
                    const id_item = $(this).attr("data-pk")
                    $.get(`/com_events/join_event/${id_item}`);
                    $(`#close_confirm-${id_item}`).click();
                    setTimeout(function(){$("#refresh_data").click();}, 200);
                }); 
            }
        });
    });
    
});


    
