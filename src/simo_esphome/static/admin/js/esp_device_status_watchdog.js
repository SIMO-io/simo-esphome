(function($) {
    function check_firmware_status(){
        $.ajax({
            url: '/esphome/firmware-status/' + object_id + '/',
            success: function(content){
                $('.field-firmware_status .readonly').html(content.firmware);
                $('.field-connected .readonly').html(content.connected);
                $('.field-install_button .readonly').html(content.webusb);
            }
        });
    }
    $(document).ready(function(){
        check_firmware_status();
        setInterval(check_firmware_status, 3000);
        $(document).click(function(e){
            if (e.target.id === 'rebuild-firmware'){
                e.preventDefault();
                $.post('/esphome/rebuild-firmware/' + object_id + '/');
            }
            if (e.target.id === 'wifi-update'){
                e.preventDefault();
                $.post('/esphome/wifi-update/' + object_id + '/');
            }
        });
    });
})(django.jQuery);
