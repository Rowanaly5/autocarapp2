$('#id_line_one_quantity, #id_line_one_unit_price, #id_line_two_quantity, #id_line_two_unit_price, #id_line_three_quantity, #id_line_three_unit_price, #id_line_four_quantity, #id_line_four_unit_price, #id_line_five_quantity, #id_line_five_unit_price, #id_line_six_quantity, #id_line_six_unit_price, #id_line_seven_quantity, #id_line_seven_unit_price, #id_line_eight_quantity, #id_line_eight_unit_price #id_line_nine_quantity, #id_line_nine_unit_price, #id_line_ten_quantity, #id_line_ten_unit_price').keyup(function(){
    var service_one_price = $('#id_line_one_unit_price').val();

    var service_two_price = $('#id_line_two_unit_price').val();

    var service_three_price = $('#id_line_three_unit_price').val();
    
    var service_four_price = $('#id_line_four_unit_price').val();

    var service_five_price = $('#id_line_five_unit_price').val();

    var service_six_price = $('#id_line_six_unit_price').val();

    var service_seven_price = $('#id_line_seven_unit_price').val();

    var service_eight_price = $('#id_line_eight_unit_price').val();

    var service_nine_price = $('#id_line_nine_unit_price').val();

    var service_ten_price = $('#id_line_ten_unit_price').val();

    var Total = service_one_price + service_two_price + service_three_price + service_four_price + service_five_price+ service_six_price + service_seven_price + service_eight_price + service_nine_price + service_ten_price

    $('#id_line_one_total_price').val(service_one_price);
    $('#id_line_two_total_price').val(service_two_price);
    $('#id_line_three_total_price').val(service_three_price);
    $('#id_line_four_total_price').val(service_four_price);
    $('#id_line_five_total_price').val(service_five_price);
    $('#id_line_six_total_price').val(service_six_price);
    $('#id_line_seven_total_price').val(service_seven_price);
    $('#id_line_eight_total_price').val(service_eight_price);
    $('#id_line_nine_total_price').val(service_nine_price);
    $('#id_line_ten_total_price').val(service_ten_price);
    $('#id_total').val(Total);
});