var map, geocoder;
var marker;
var fullAddress = "Avenida España 1680, Valparaíso, Valparaíso, Chile"
var MARKER_PATH = 'https://maps.gstatic.com/intl/en_us/mapfiles/marker_green.png';

function initialize() {
var mapOptions = {
  zoom: 10,
  center: new google.maps.LatLng(-33.0360358,-71.5985076),
  mapTypeControl: false,
  panControl: false,
  zoomControl: false,
  streetViewControl: false,
  draggable: false,
};
geocoder = new google.maps.Geocoder();
map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
setMapByAddress(fullAddress);
  }

  function setMapByAddress(mAddress) {
geocoder.geocode({ 'address': mAddress}, function(results, status) {
  if (status == google.maps.GeocoderStatus.OK) {
    map.setCenter(results[0].geometry.location);
    map.panTo(results[0].geometry.location);
    map.setZoom(16);
    clearMarkers();
    addMarker(results[0].geometry.location);
  }
});
  }

  function addMarker(location) {
var markerIcon = MARKER_PATH;
marker = new google.maps.Marker({
  position: location,
  animation: google.maps.Animation.DROP,
  title: "Valparaíso Mobile Conf",
  icon: MARKER_PATH
});
marker.setMap(map);
  }

  function clearMarkers() {
if(marker==null)
  return;
marker.setMap(null);
  }

google.maps.event.addDomListener(window, 'load', initialize);

$(document).ready(function(){

    $(function() {
      $('a[href*="#"]:not([href="#"])').click(function() {
        if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
          var target = $(this.hash);
          target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
          if (target.length) {

            $('html,body').animate({
              scrollTop: target.offset().top
            }, 700);
            return false;
          }
        }
      });
    });


    $('#sponsorForm').submit(function(event){
      event.preventDefault();
      var actionURL =  $(this).attr("action");
      var postData = $(this).serialize();
      $.ajax({
        type: "POST",
        url: actionURL,
        data: postData,
        success: function(response) {
          alertify.success('Mensaje enviado correctamente', 5);
          $('#sponsorsModal').modal('hide');
        },
        error: function (jqXHR, textStatus, errorThrown) {
            var response = jqXHR.responseJSON;
            $.each(response, function(key, value) {
                if( key != 'status' ) {
                    var fieldId = '#sponsor_' + key + '_error';
                    $(fieldId).html(value[0]);
                }
            });
        }
      }).fail(function(){
          alertify.error('No se pudo enviar el mensaje', 5);
      });
    });


    $('#speakerForm').submit(function(event){
      event.preventDefault();
      var actionURL = $(this).attr("action");
      var postData = $(this).serialize();
      $.ajax({
        type: "POST",
        url: actionURL,
        data: postData,
        success: function(response) {
          alertify.success('Mensaje enviado correctamente', 5);
          $('#speakersModal').modal('hide');
        },
        error: function (jqXHR, textStatus, errorThrown) {
            var response = jqXHR.responseJSON;
            $.each(response, function(key, value) {
                if( key != 'status' ) {
                    var fieldId = '#speaker_' + key + '_error';
                    $(fieldId).html(value[0]);
                }
            });
        }
      }).fail(function(){
          alertify.error('No se pudo enviar el mensaje', 5);
      });
    });

  });