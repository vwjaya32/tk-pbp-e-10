
$(document).ready(function(){
    $("#refresh_data_user").click(function(){
        $.get("/com_events/json_all/", function(_data) {
            const data = _data.data
            $("#title").empty();
            $("#main_div").empty();
            $("#title").append('List Of All Events Available');
              for(var i = 0 ; i < data.length; i++){
                const date = new Date(data[i].fields.date).toDateString()
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
                            Do you want to join ${data[i].fields.name} ?
                            </div>
                            <div class="modal-footer">
                                <button type="button" data-bs-dismiss="modal">Go Back</button>
                                <button type="submit" class="btn btn-primary" data-pk='${data[i].pk}' id="confirm-${data[i].pk}">Confirm</button>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="modal fade" id="details-${data[i].pk}" tabindex="-1" aria-labelledby="mainModalLabel" aria-hidden="true">
                    <div class="modal-dialog">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h1 class="modal-title fs-5" id="mainModalLabel">
                                ${data[i].fields.name}
                                </h1>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close" id="close_confirm-${data[i].pk}"></button>
                            </div>
                            <div class="modal-body">
                            <p><u>
                            Description:</u></p>
                            <p>
                            ${data[i].fields.description}
                            </p>
                            <p><u>
                            Users that participate in this event:</u></p>
                            <p>
                            ${data[i].fields.attendees}
                            </p>
                            </div>
                            <div class="modal-footer">
                                <button type="button" data-bs-dismiss="modal">Go Back</button>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="card">
                    <div>
                        <h2 id='item-${data[i].pk}'>${data[i].fields.name}</h2>
                            <div>
                                <p>EVENT DATE: ${date}</p>
                            </div>
                            <button class="join-btn" data-bs-toggle="modal" data-bs-target="#modal_confirm-${data[i].pk}">
                                Join
                            </button>
                            <button class="details-btn" data-bs-toggle="modal" data-bs-target="#details-${data[i].pk}">
                                Details
                            </button>
                    </div>
                </div>
                <br>
                  `
                  )
                  $(`#confirm-${data[i].pk}`).click(function(){
                    const id_item = $(this).attr("data-pk")
                    $.get(`/com_events/join_event/${id_item}`);
                    $(`#close_confirm-${id_item}`).click();
                    setTimeout(function(){$("#refresh_data_user").click();}, 200);
                }); 
            }
        });
    });
    $("#refresh_my_events").click(function(){
        $.get("/com_events/json_user/", function(_data) {
            const data = _data.data
            $("#title").empty();
            $("#main_div").empty();
            $("#title").append('My Events');
              for(var i = 0 ; i < data.length; i++){
                const date = new Date(data[i].fields.date).toDateString()
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
                            Do you want to remove ${data[i].fields.name} ?
                            </div>
                            <div class="modal-footer">
                                <button type="button" data-bs-dismiss="modal">Go Back</button>
                                <button type="submit" class="btn btn-primary" data-pk='${data[i].pk}' id="confirm-${data[i].pk}">Confirm</button>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="modal fade" id="details-${data[i].pk}" tabindex="-1" aria-labelledby="mainModalLabel" aria-hidden="true">
                    <div class="modal-dialog">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h1 class="modal-title fs-5" id="mainModalLabel">
                                ${data[i].fields.name}
                                </h1>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close" id="close_confirm-${data[i].pk}"></button>
                            </div>
                            <div class="modal-body">
                            <p><u>
                            Description:</u></p>
                            <p>
                            ${data[i].fields.description}
                            </p>
                            <p><u>
                            Users that participate in this event:</u></p>
                            <p>
                            ${data[i].fields.attendees}
                            </p>
                            </div>
                            <div class="modal-footer">
                                <button type="button" data-bs-dismiss="modal">Go Back</button>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="card">
                    <div id='item-${data[i].pk}'>
                        <h2>${data[i].fields.name}</h2>
                        <div>
                        <p>EVENT DATE: ${date}</p>
                        </div>
                        <button class="unjoin-btn" data-bs-toggle="modal" data-bs-target="#modal_confirm-${data[i].pk}">
                            Unjoin
                        </button>
                        <button class="details-btn" data-bs-toggle="modal" data-bs-target="#details-${data[i].pk}">
                            Details
                        </button>
                    </div>
                </div>
                <br>
                  `
                  )
                  $(`#confirm-${data[i].pk}`).click(function(){
                    const id_item = $(this).attr("data-pk")
                    $.get(`/com_events/unjoin_event/${id_item}`);
                    $(`#close_confirm-${id_item}`).click();
                    setTimeout(function(){$("#refresh_my_events").click();}, 200);
                }); 
            }
        });
    });
    $("#submit_event").click(function(){
        $.post("/com_events/add/", $('#modal_form').serialize());
        $("#close_modal").click();
        setTimeout(function(){$("#refresh_data_admin").click();}, 200);
    }); 
    $("#refresh_data_admin").click(function(){
        $.get("/com_events/json_all/", function(_data) {
            const data = _data.data
            $("#title").empty();
            $("#main_div").empty();
            $("#title").append('List Of Events');
              for(var i = 0 ; i < data.length; i++){
                const date = new Date(data[i].fields.date).toDateString()
                  $("#main_div").append(`
                  <div class="card">
                  <div id='item-${data[i].pk}'>
                  <h2>${data[i].fields.name}</h2>
                      <div>
                      <p>EVENT DATE: ${date}</p>
                      </div>
                        <button class="delete-btn" data-pk="${data[i].pk}" id="delete-${data[i].pk}">
                            Delete
                        </button>
                  </div>
                  </div>
                  <br>
                  `
                  ) 
                $(`#delete-${data[i].pk}`).click(function(){
                    const id_item = $(this).attr("data-pk")
                    $.get(`/com_events/delete/${id_item}`);
                    setTimeout(function(){$("#refresh_data_admin").click();}, 200);
                })
            }
        });
    });
});


    
