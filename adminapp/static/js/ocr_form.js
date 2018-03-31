$(document).ready(function() {
    var $imageInput = $("[data-js-image-input]");
    var $imageContainer = $("[data-js-image-container]");
    var $resultContainer = $("[data-js-result-container]");
    $imageInput.change(function(event) {
        event.stopPropagation();
        event.preventDefault();
        var file = event.target.files[0];
        console.log(event.target.files);
        var fileReader = new FileReader();
        fileReader.onload = (function(theFile) {
            return function(event) {
                $imageContainer.html('<img class="image" src="' + event.target.result + '">');
            };
        })(file);
        fileReader.readAsDataURL(file);
    });
    // $(document).ready(function() {
    // var $imageInput2 = $("[data-js-image-input-upload]");
    // var $imageContainer2 = $("[data-js-image-container-upload]");
    // $imageInput2.change(function(event) {
    //     event.stopPropagation();
    //     event.preventDefault();
    //     var file = event.target.files[0];
    //     console.log(event.target.files);
    //     var fileReader = new FileReader();
    //     fileReader.onload = (function(theFile) {
    //         return function(event) {
    //             $imageContainer2.html('<img class="image" src="' + event.target.result + '">');
    //         };
    //     })(file);
    //     fileReader.readAsDataURL(file);
    // });
    $("[data-js-go-button]").click(function(event) {
        event.stopPropagation();
        event.preventDefault();
        data = new FormData();
        data.append('image', $imageInput[0].files[0]);
        $.post({
            url: "/upload-image/",
            data: data,
            cache: false,
            contentType: false,
            processData: false
        }).done(function(data) {
            console.log(data);
            $resultContainer.removeClass("result-default result-error");
            $resultContainer.addClass("result-success");
            $resultContainer.html(data.utf8_text);
            /*var $imageResult = $resultContainer.parents();
            var $filePath = $imageResult.parents();
            var $form = $filePath.parents();
            var $input = $form.find('#icon_prefix');
            $input.prop("disabled",true);*/

        })
        .fail(function(jqXHR) {
            $resultContainer.removeClass("result-default result-success");
            $resultContainer.addClass("result-error");
            $resultContainer.html('Cannot Process Image. Enter Manually');
           /* var $imageResult = $resultContainer.parents();
            var $filePath = $imageResult.parents();
            var $form = $filePath.parents();
            var $input = $form.find('#icon_prefix');
            $input.prop("disabled",false);*/
        });
    });
});