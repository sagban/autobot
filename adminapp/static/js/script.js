
function addTodoItem() {

    var form = $("#todo-list-item").html();

  $("#todo-list").append("<li id='todo-list-item' class='card'>"+ form +

                         " <button class='todo-item-delete btn waves-effect amber lighten-2'>"+
                         "<i class=\"material-icons amber lighten-2\">delete</i></button></li>"+
                            "<script>$('select').material_select();</script>");

 $("#new-todo-item").val("");
}

function deleteTodoItem(e, item) {
  e.preventDefault();
  $(item).parent().fadeOut('slow', function() {
    $(item).parent().remove();
  });
}


$(function(){

   $("#add-todo-item").on('click', function(e){
     e.preventDefault();
     addTodoItem();
   });

  $("#todo-list").on('click','.todo-item-delete', function(e){
    var item = this;
    deleteTodoItem(e, item)
  });

  $(".button-collapse").sideNav();

$('.datepicker').pickadate({
    selectMonths: true, // Creates a dropdown to control month
    selectYears: 15, // Creates a dropdown of 15 years to control year,
    today: 'Today',
    clear: 'Clear',
    close: 'Ok',
    closeOnSelect: false // Close upon selecting a date,
    // ex. 'body' will append picker to body
  });

//Time Picker:
  $('.timepicker').pickatime({
    default: 'now', // Set default time: 'now', '1:30AM', '16:30'
    fromnow: 0,       // set default time to * milliseconds from now (using with default = 'now')
    twelvehour: false, // Use AM/PM or 24-hour format
    donetext: 'OK', // text for done-button
    cleartext: 'Clear', // text for clear-button
    canceltext: 'Cancel', // Text for cancel-button,
    container: undefined, // ex. 'body' will append picker to body
    autoclose: false, // automatic close timepicker
    ampmclickable: true, // make AM PM clickable
    aftershow: function(){} //Function for after opening timepicker
  });

  $(document).ready(function() {
    $('select').material_select();
  });


});

