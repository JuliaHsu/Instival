$(function () {
    $('#FileUpload1').change(function () {
        $('#Image1').hide();
        var reader = new FileReader();
        reader.onload = function (e) {
            $('#Image1').show();
            $('#Image1').attr("src", e.target.result);
            $('#Image1').Jcrop({
                boxWidth: 600,
                boxHeight: 600,
                onChange: SetCoordinates,
                onSelect: SetCoordinates,
                setSelect: [0, 160, 160, 0],// you have set proper proper x and y coordinates here
                aspectRatio: 1
            });
        }
        reader.readAsDataURL($(this)[0].files[0]);
    });
 
    $('#btnCrop').click(function () {
        var x1 = $('#imgX1').val();
        var y1 = $('#imgY1').val();
        var width = $('#imgWidth').val();
        var height = $('#imgHeight').val();
        var canvas = $("#canvas")[0];
        var context = canvas.getContext('2d');
        var img = new Image();
        img.onload = function () {
            $('#btnSubmit').show();
            canvas.height = width;
            canvas.width = width;
            context.drawImage(img, x1, y1, width, height, 0, 0, width, height);
            context.scale(0.5,0.5);
            $('#imgCropped').val(canvas.toDataURL());
            var dataURL = canvas.toDataURL();
            document.getElementById("saveimage").src = dataURL;
        };
        
        img.src = $('#Image1').attr("src");
    });
});
function SetCoordinates(c) {
    $('#imgX1').val(c.x);
    $('#imgY1').val(c.y);
    $('#imgWidth').val(c.w);
    $('#imgHeight').val(c.h);
    $('#btnCrop').show();
};