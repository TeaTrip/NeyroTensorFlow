$(document).ready(function(){


    function get_season_id(action){
        if (action == 'winter') {
            return 1
        } else if (action == 'spring'){
            return 2
        } else if (action == 'summer') {
            return 3
        } else if (action == 'autumn'){
            return 4 
        } //else {
        //     throw new error("Input errorr")
        // }
    }


    $('#onSubmit').click(function() {       
        let student_id = $('#id').val();
        let season_id = get_season_id($('#season_info').val());
        let arr = {"student_id": student_id, "season_id": season_id}
        $.ajax({
            url: "api/get_student",
            type: 'POST',
            data: JSON.stringify(arr),
            dataType: 'json',
            contentType: 'application/json',
            success: function(response) {
                if (response < 30) {
                    $('.output').css('background-color', '#4aff53');
                } else if (response > 30 && response < 70) {
                    $('.output').css('background-color', '#fff130');
                } else {
                    $('.output').css('background-color', '#ff4d29');
                }
                $('#output').text(response + "h");
                console.log(response)
            },
            error: function(response) {
//                console.log("err")
//
//                $('.output').css('background-color', 'black')
            }
        })
    })

})