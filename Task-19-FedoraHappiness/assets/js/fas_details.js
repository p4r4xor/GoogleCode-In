$(function() {
  /*
  Place the button inside input field
  */
  $("#id_fasid").after($("#search_fasid"));

  /*
  Making the input fields clear when the page reloads
  */
  $("#id_fasid").val("");
  $("#id_recipient_name").val("");
  $("#id_recipient_email").val("");

  $("#search_fasid").click(function() {
    let fasid = $("#id_fasid").val();
    $("#server-error").remove();

    if (!fasid) {
      console.log("!fasid");
      return;
    }
    $("#id_recipient_name").attr("placeholder", "");
    $("#id_recipient_name").val("");
    $("#id_recipient_email").val("");
    $("#id_fasid").prop("disabled", true);
    $("#no-fas-id-error").remove();
    $("#server-error").remove();
    if (!$('#fas_username_check_message').length) {
      $("#div_id_fasid").after(
        '<p class="searching-text" id="fas_username_check_message">Searching for FAS Username...</p>'
      );
    }
    
    email = $.ajax({
      type: "GET",
      url: "/send/search?fasid=" + encodeURIComponent(fasid),
      success: function(data) {
        console.log(data);
        $(".error").remove();
        $(".searching-text").remove();
        $("#id_fasid").prop("disabled", false);
        if (data["privacy"]) {
          $("#id_recipient_name").attr(
            "placeholder",
            "Privacy is Set! Type Name Manually"
          );
        } else {
          $("#id_recipient_name").val(data["name"]);
        }

        $("#id_recipient_email").val(data["email"]);
      },
      statusCode: {
        404: function(data) {
          console.log(data);
          $("#no-fas-id-error").remove();
          $("#id_fasid").prop("disabled", false);
          $(".searching-text").remove();
          $("#div_id_fasid").after(
            '<p class="error" id="no-fas-id-error">Sorry! No such FAS Username exist</p>'
          );
          $("#no-fas-id-error").fadeIn("slow", function() {
            $("#no-fas-id-error")
              .delay(2700)
              .fadeOut();
          });
          $("#id_fasid").val("");
        },
        500: function(data) {
          console.log(data);
          $("#id_fasid").val("");
          $("#server-error").remove();
          $(".searching-text").remove();
          $("#id_fasid").prop("disabled", false);
          $("#div_id_fasid").after(
            '<p class="error" id="server-error" >Internal Server Error Occured! Enter Name and Email manually!</p>'
          );
          $("#server-error").fadeIn("slow", function() {
            $("#server-error")
              .delay(3000)
              .fadeOut();
          });
        }
      }
    });
  });
});
