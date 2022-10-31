
$(document).ready(function(){
    $("#refresh_data").click(function(){
        $.get("/com_events/json_all/", function(data) {
            $("#main_div").empty();
              for(var i = 0 ; i < data.length; i++){
                  $("#main_div").append(`
                  <div>
                  <h1>${data[i].fields.name}</h1>
                      <div>${data[i].fields.date}
                        <p>
                          ${data[i].fields.description}
                        </p>
                      </div>
                  </div>
                  `
                  );
            }
        });
    });
});

$(document).ready(function(){
    $("#submit_event").click(function(){
        $.post("/com_events/add/", $('#modal_form').serialize());
        $("#close_modal").click();
        setTimeout(function(){$("#refresh_data").click();}, 200);
    }); 
});