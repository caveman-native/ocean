document.addEventListener("DOMContentLoaded", function(){
    console.log("DOM Loaded! Plain Javascript...");
});
$(function(){
  console.log("Helloworld! Good Old jQuery...");

$("#profileForm").submit(function(e){
     e.preventDefault();
     saveProfile();
  });



$("#profileUpdateForm").submit(function(e){
     e.preventDefault();
     updateProfile();
  });


$("#patternUpdateForm").submit(function(e){
     e.preventDefault();
     updatePattern();
  });

$("#patternForm").submit(function(e){
     e.preventDefault();
     savePattern();
  });

$( "button#createProfile" ).on( "click", createProfile );

$( "button#createPattern" ).on( "click", createPattern );


});


function createProfile() {
  var HTML = '<form id="profileForm">' +
    '<div class="form-group">' +
    '<label for="inputMeta">Meta</label>' +
    '<input type="text" name="meta" class="form-control" id="meta" aria-describedby="metaHelp" placeholder="Enter meta">' +
    '<small id="metaHelp" class="form-text text-muted">Please enter some description.</small>' +
  '</div>' +
  '<div class="form-group">' +
    '<label for="inputType1">Type</label>' +
    '<input type="number" name="type" class="form-control" id="inputType1" placeholder="Type">' +
  '</div>' +
    '<div class="form-group">' +
    '<label for="inputDirection">Direction</label>' +
    '<input type="number" min="0" name="direction" max="1" class="form-control" id="inputDirection" placeholder="Direction">' +
  '</div>' +
    '<div class="form-group">' +
    '<label for="inputinterval">interval</label>' +
    '<input type="number" min="0" max="6000" name="interval" class="form-control" id="inputinterval" placeholder="interval">' +
  '</div>' +
    '<div class="form-group">' +
    '<label for="inputmax_time">max_time</label>' +
    '<input type="number" min="0" max="6000" name="max_time" class="form-control" id="inputmax_time" placeholder="max_time">' +
  '</div>' +
    '<div class="form-group">' +
    '<label for="inputType1">deep_depth</label>' +
    '<input type="number" min="0" max="6000" name="deep_depth" class="form-control" id="inputdeep_depth" placeholder="deep_depth">' +
  '</div>' +

    '<div class="form-group">' +
    '<label for="inputdeep_window">deep_window</label>' +
    '<input type="number" min="0" max="6000" class="form-control" name="deep_window" id="inputdeep_window" placeholder="deep_window">' +
  '</div>' +

    '<div class="form-group">' +
    '<label for="inputshallow_depth">shallow_depth</label>' +
    '<input type="number" min="0" max="6000" class="form-control" id="inputshallow_depth" name="shallow_depth"  placeholder="shallow_depth">' +
  '</div>' +

    '<div class="form-group">' +
    '<label for="inputshallow_window">shallow_window</label>' +
    '<input type="number" min="0" max="6000" class="form-control" id="inputshallow_window" name="shallow_window" placeholder="shallow_window">' +
  '</div>' +

    '<div class="form-group">' +
    '<label for="inputstall_timeout">stall_timeout</label>' +
    '<input type="number" min="0" max="6000" class="form-control" id="inputstall_timeout"  name="stall_timeout" placeholder="stall_timeout">' +
  '</div>' +

    '<div class="form-group">' +
    '<label for="inputramp_time">ramp_time</label>' +
    '<input type="number" min="0" max="6000" class="form-control" name="inputramp_time" id="inputramp_time" placeholder="ramp_time">' +
  '</div>' +

    '<div class="form-group">' +
    '<label for="inputstop_check">stop_check</label>' +
    '<input type="number" min="0" max="6000" class="form-control" name="stop_check" id="inputstop_check"  placeholder="stop_check">' +
  '</div>' +

    '<div class="form-group">' +
    '<label for="inputType1">backtrack_time</label>' +
    '<input type="number" min="0" max="6000" class="form-control" name="backtrack_time" id="inputbacktrack_time" placeholder="backtrack_time">' +
  '</div>' +

      '<div class="form-group">' +
    '<label for="inputbacktrack_count">backtrack_count</label>' +
    '<input type="number" min="0" max="6000" class="form-control" name="backtrack_count" id="inputbacktrack_count" placeholder="backtrack_count">' +
  '</div>' +

    '<div class="form-group">' +
    '<label for="inputctd_warmup_time">ctd_warmup_time</label>' +
    '<input type="number" min="0" max="6000" name="ctd_warmup_time" class="form-control" id="inputctd_warmup_time" placeholder="ctd_warmup_time">' +
  '</div>' +

   '<div class="form-group">' +
    '<label for="inputdpdt_threshold">dpdt_threshold</label>' +
    '<input type="number" min="0" max="6000" name="dpdt_threshold" class="form-control" id="inputdpdt_threshold" placeholder="dpdt_threshold">' +
  '</div>' +

  ' <button type="submit" id="saveProfile" class="btn btn-warning"> Submit </button>' +
'</form>';

$("#profileForm").html(HTML);

}


function createPattern() {
  var HTML = '<form id="patternForm">' +
    '<div class="form-group">' +
    '<label for="inputMeta">Meta</label>' +
    '<input type="text" name="meta" class="form-control" id="meta" aria-describedby="metaHelp" placeholder="Enter meta">' +
    '<small id="metaHelp" class="form-text text-muted">Please enter some description.</small>' +
  '</div>' +
  '<div class="form-group">' +
    '<label for="inputStartDate">start_dt</label>' +
    '<input type="date" name="start_dt" class="form-control" id="inputStartDate" placeholder="start_dt">' +
  '</div>' +
    '<div class="form-group">' +
    '<label for="inputstop_dt">stop_dt</label>' +
    '<input type="date" name="stop_dt" class="form-control" id="inputstop_dt" placeholder="inputstop_dt">' +
  '</div>' +
    '<div class="form-group">' +
    '<label for="inputsequence">sequence</label>' +
    '<input type="number"  min="0" max="6000" name="sequence" class="form-control" id="inputsequence" placeholder="sequence">' +
   '</div>' +
   '<div class="form-group">' +
    '<label for="inputType1">type</label>' +
    '<input type="number" min="0" max="6000" name="type" class="form-control" id="inputType1" placeholder="type">' +
  '</div>' +

    '<div class="form-group">' +
    '<label for="inputstatus">status</label>' +
    '<input type="number" min="0" max="6000" class="form-control" name="status" id="inputstatus" placeholder="status">' +
  '</div>' +

  ' <button type="submit" id="saveProfile" class="btn btn-warning"> Submit </button>' +
'</form>';

$("#patternForm").html(HTML);

}





function deleteProfile(profile){

var url = "/deleteProfile/" + profile;
$.get( url, function( data ) {
  $( "#message" ).html( data );
  alert( data );
  location.reload();
});
}

function editProfile(profile){

var url = "/profile/edit/" + profile;
$.get( url, function( data ) {
  $( "#message" ).html( data );
  alert( data );
  location.reload();
});
}


function deletePattern(pattern){

var url = "/deletePattern/" + pattern;
$.get( url, function( data ) {
  $( "#message" ).html( data );
  alert( data );
  location.reload();
});
}


function saveProfile() {
  // Stop form from submitting normally
  //event.preventDefault();
  // Get some values from elements on the page:
  var $form = $( '#profileForm' ),
    meta = $form.find( "input[name='meta']" ).val(),
    type = $form.find( "input[name='type']" ).val(),
    direction = $form.find( "input[name='direction']" ).val(),
    interval = $form.find( "input[name='interval']" ).val(),
    max_time = $form.find( "input[name='max_time']" ).val(),
    deep_depth = $form.find( "input[name='deep_depth']" ).val(),
    deep_window = $form.find( "input[name='deep_window']" ).val(),
    shallow_depth = $form.find( "input[name='shallow_depth']" ).val(),
    shallow_window = $form.find( "input[name='shallow_window']" ).val(),
    stall_timeout = $form.find( "input[name='stall_timeout']" ).val(),
    ramp_time = $form.find( "input[name='ramp_time']" ).val(),
    stop_check = $form.find( "input[name='stop_check']" ).val(),
    backtrack_time = $form.find( "input[name='backtrack_time']" ).val(),
    backtrack_count = $form.find( "input[name='backtrack_count']" ).val(),
    ctd_warmup_time = $form.find( "input[name='ctd_warmup_time']" ).val(),
    dpdt_threshold = $form.find( "input[name='dpdt_threshold']" ).val(),
    url = '/createProfile';
  // Send the data using post
  var posting = $.post( url, { meta: meta, type :type, direction: direction,interval : interval,
                               max_time : max_time, deep_depth : deep_depth, deep_window : deep_window,
                               shallow_depth : shallow_depth, shallow_window: shallow_window,
                               stall_timeout: stall_timeout, ramp_time :ramp_time, stop_check :stop_check,
                               backtrack_time : backtrack_time, backtrack_count:backtrack_count ,
                               ctd_warmup_time: ctd_warmup_time, dpdt_threshold :dpdt_threshold} );
  // Put the results in a div
  posting.done(function( data ) {
    alert(data);

    var content = $( data );
    $( "#message" ).append( content );
  });
   location.reload();
}


function updateProfile() {
  // Stop form from submitting normally
  //event.preventDefault();
  // Get some values from elements on the page:
  var $form = $( '#profileUpdateForm' ),
    meta = $form.find( "input[name='meta']" ).val(),
    type = $form.find( "input[name='type']" ).val(),
    direction = $form.find( "input[name='direction']" ).val(),
    interval = $form.find( "input[name='interval']" ).val(),
    max_time = $form.find( "input[name='max_time']" ).val(),
    deep_depth = $form.find( "input[name='deep_depth']" ).val(),
    deep_window = $form.find( "input[name='deep_window']" ).val(),
    shallow_depth = $form.find( "input[name='shallow_depth']" ).val(),
    shallow_window = $form.find( "input[name='shallow_window']" ).val(),
    stall_timeout = $form.find( "input[name='stall_timeout']" ).val(),
    ramp_time = $form.find( "input[name='ramp_time']" ).val(),
    stop_check = $form.find( "input[name='stop_check']" ).val(),
    backtrack_time = $form.find( "input[name='backtrack_time']" ).val(),
    backtrack_count = $form.find( "input[name='backtrack_count']" ).val(),
    ctd_warmup_time = $form.find( "input[name='ctd_warmup_time']" ).val(),
    dpdt_threshold = $form.find( "input[name='dpdt_threshold']" ).val(),
    url = document.location.href;
  // Send the data using post
  var posting = $.post( url, { meta: meta, type :type, direction: direction,interval : interval,
                               max_time : max_time, deep_depth : deep_depth, deep_window : deep_window,
                               shallow_depth : shallow_depth, shallow_window: shallow_window,
                               stall_timeout: stall_timeout, ramp_time :ramp_time, stop_check :stop_check,
                               backtrack_time : backtrack_time, backtrack_count:backtrack_count ,
                               ctd_warmup_time: ctd_warmup_time, dpdt_threshold :dpdt_threshold} );
  // Put the results in a div
  posting.done(function( data ) {
    alert(data);

    var content = $( data );
    $( "#message" ).append( content );
  });
   // similar behavior as clicking on a link
   window.location.href = "/profile";
}


function savePattern() {
  // Stop form from submitting normally
  //event.preventDefault();
  // Get some values from elements on the page:
  var $form = $( '#patternForm' ),
    meta = $form.find( "input[name='meta']" ).val(),
    start_dt = $form.find( "input[name='start_dt']" ).val(),
    stop_dt = $form.find( "input[name='stop_dt']" ).val(),
    sequence = $form.find( "input[name='sequence']" ).val(),
    type = $form.find( "input[name='type']" ).val(),
    status = $form.find( "input[name='status']" ).val(),
    url = '/createPattern';
  // Send the data using post
  var posting = $.post( url, { meta: meta, start_dt :start_dt, stop_dt: stop_dt,sequence : sequence,
                               type : type, status : status } );
  // Put the results in a div
  posting.done(function( data ) {
    alert(data);

    var content = $( data );
    $( "#message" ).append( content );
  });
   location.reload();
}


function updatePattern() {
  // Stop form from submitting normally
  //event.preventDefault();
  // Get some values from elements on the page:
  var $form = $( '#patternUpdateForm' ),
    meta = $form.find( "input[name='meta']" ).val(),
    start_dt = $form.find( "input[name='start_dt']" ).val(),
    stop_dt = $form.find( "input[name='stop_dt']" ).val(),
    sequence = $form.find( "input[name='sequence']" ).val(),
    type = $form.find( "input[name='type']" ).val(),
    status = $form.find( "input[name='status']" ).val(),
    url = document.location.href;
  // Send the data using post
  var posting = $.post( url, { meta: meta, start_dt :start_dt, stop_dt: stop_dt,sequence : sequence,
                               type : type, status : status } );
  // Put the results in a div
  posting.done(function( data ) {
    alert(data);

    var content = $( data );
    $( "#message" ).append( content );
  });
    // similar behavior as clicking on a link
   window.location.href = "/pattern";
}