$(function(){

    // save profile
    $("#profile-form").submit(function(e){
        e.preventDefault();
        saveProfile();
    });

    // update profile
    $("#profile-update-form").submit(function(e){
        e.preventDefault();
        updateProfile();
    });

    // save pattern
    $("#pattern-form").submit(function(e){
        e.preventDefault();
        savePattern();
    });

    // update pattern
    $("#pattern-update-form").submit(function(e){
        e.preventDefault();
        updatePattern();
    });

    // eventlistener on create profile save btn 
    $("button#create-profile").on("click", createProfile);

    // eventlistener on create pattern save btn
    $("button#create-pattern").on("click", createPattern);

});

function createProfile() {
    var HTML = '<form id="profile-form">' +

    '<div class="row">' +
    '<div class="col-sm">' +

    '<div class="form-group">' +
    '<label for="inputMeta">Meta</label>' +
    '<input type="text" name="meta" class="form-control form-control-sm" id="meta" aria-describedby="metaHelp" placeholder="Enter meta">' +
    '<small id="metaHelp" class="form-text text-muted">Please enter some description.</small>' +
    '</div>' +

    '<div class="form-group">' +
    '<label for="inputType1">Type</label>' +
    '<input type="number" name="type" class="form-control form-control-sm" id="inputType1" placeholder="Type">' +
    '</div>' +

    '<div class="form-group">' +
    '<label for="inputDirection">Direction</label>' +
    '<input type="number" min="0" name="direction" max="1" class="form-control form-control-sm" id="inputDirection" placeholder="Direction">' +
    '</div>' +

    '<div class="form-group">' +
    '<label for="inputinterval">interval</label>' +
    '<input type="number" min="0" max="6000" name="interval" class="form-control form-control-sm" id="inputinterval" placeholder="interval">' +
    '</div>' +

    '<div class="form-group">' +
    '<label for="inputmax_time">max_time</label>' +
    '<input type="number" min="0" max="6000" name="max_time" class="form-control form-control-sm" id="inputmax_time" placeholder="max_time">' +
    '</div>' +

    '<div class="form-group">' +
    '<label for="inputType1">deep_depth</label>' +
    '<input type="number" min="0" max="6000" name="deep_depth" class="form-control form-control-sm" id="inputdeep_depth" placeholder="deep_depth">' +
    '</div>' +

    '<div class="form-group">' +
    '<label for="inputdeep_window">deep_window</label>' +
    '<input type="number" min="0" max="6000" class="form-control form-control-sm" name="deep_window" id="inputdeep_window" placeholder="deep_window">' +
    '</div>' +

    '<div class="form-group">' +
    '<label for="inputshallow_depth">shallow_depth</label>' +
    '<input type="number" min="0" max="6000" class="form-control form-control-sm" id="inputshallow_depth" name="shallow_depth"  placeholder="shallow_depth">' +
    '</div>' +

    '<div class="form-group">' +
    '<label for="inputshallow_window">shallow_window</label>' +
    '<input type="number" min="0" max="6000" class="form-control form-control-sm" id="inputshallow_window" name="shallow_window" placeholder="shallow_window">' +
    '</div>' +

    '<div class="form-group">' +
    '<label for="inputstall_timeout">stall_timeout</label>' +
    '<input type="number" min="0" max="6000" class="form-control form-control-sm" id="inputstall_timeout"  name="stall_timeout" placeholder="stall_timeout">' +
    '</div>' +

    '<div class="form-group">' +
    '<label for="inputramp_time">ramp_time</label>' +
    '<input type="number" min="0" max="6000" class="form-control form-control-sm" name="inputramp_time" id="inputramp_time" placeholder="ramp_time">' +
    '</div>' +

    '<div class="form-group">' +
    '<label for="inputstop_check">stop_check</label>' +
    '<input type="number" min="0" max="6000" class="form-control form-control-sm" name="stop_check" id="inputstop_check"  placeholder="stop_check">' +
    '</div>' +

    '<div class="form-group">' +
    '<label for="inputType1">backtrack_time</label>' +
    '<input type="number" min="0" max="6000" class="form-control form-control-sm" name="backtrack_time" id="inputbacktrack_time" placeholder="backtrack_time">' +
    '</div>' +

    '<div class="form-group">' +
    '<label for="inputbacktrack_count">backtrack_count</label>' +
    '<input type="number" min="0" max="6000" class="form-control form-control-sm" name="backtrack_count" id="inputbacktrack_count" placeholder="backtrack_count">' +
    '</div>' +

    '<div class="form-group">' +
    '<label for="inputctd_warmup_time">ctd_warmup_time</label>' +
    '<input type="number" min="0" max="6000" name="ctd_warmup_time" class="form-control form-control-sm" id="inputctd_warmup_time" placeholder="ctd_warmup_time">' +
    '</div>' +

    '<div class="form-group">' +
    '<label for="inputdpdt_threshold">dpdt_threshold</label>' +
    '<input type="number" min="0" max="6000" name="dpdt_threshold" class="form-control form-control-sm" id="inputdpdt_threshold" placeholder="dpdt_threshold">' +
    '</div>' +

    '</div>' +
    '</div>' +

    '<button type="submit" id="create-profile" class="btn btn-warning">Save Profile</button>' +
    '</form>';

    $("#profile-form").html(HTML);

}

function createPattern() {
  var HTML = '<form id="pattern-form">' +

    '<div class="clearfix"></div>' +
    '<div class="row mb-5">' +
        '<h5>Create a New Pattern</h4>' +
    '</div>' +
    '<div class="clearfix"></div>' +

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

    '<button type="submit" id="create-pattern" class="btn btn-warning">Save Pattern</button>' +
    '</form>';

    $("#pattern-form").html(HTML);

}

function deleteProfile(profile){
    var url = "/deleteProfile/" + profile;
    $.get(url, function(data){
        $("#message").html(data);
        alert(data);
        location.reload();
    });
}

function editProfile(profile){
    var url = "/profile/edit/" + profile;
    $.get(url, function(data) {
        $("#message").html(data);
        alert(data);
        location.reload();
    });
}

function deletePattern(pattern){
    var url = "/deletePattern/" + pattern;
    $.get(url, function(data) {
        $("#message").html(data);
        alert(data);
        location.reload();
    });
}

function saveProfile() {
    // Stop form from submitting normally
    //event.preventDefault();
    // Get some values from elements on the page:
    var $form = $('#profile-form'),
    meta = $form.find("input[name='meta']").val(),
    type = $form.find("input[name='type']").val(),
    direction = $form.find("input[name='direction']").val(),
    interval = $form.find("input[name='interval']").val(),
    max_time = $form.find("input[name='max_time']").val(),
    deep_depth = $form.find("input[name='deep_depth']").val(),
    deep_window = $form.find("input[name='deep_window']").val(),
    shallow_depth = $form.find("input[name='shallow_depth']").val(),
    shallow_window = $form.find("input[name='shallow_window']").val(),
    stall_timeout = $form.find("input[name='stall_timeout']").val(),
    ramp_time = $form.find("input[name='ramp_time']").val(),
    stop_check = $form.find("input[name='stop_check']").val(),
    backtrack_time = $form.find("input[name='backtrack_time']").val(),
    backtrack_count = $form.find("input[name='backtrack_count']").val(),
    ctd_warmup_time = $form.find("input[name='ctd_warmup_time']").val(),
    dpdt_threshold = $form.find("input[name='dpdt_threshold']").val(),
    url = '/createProfile';

    // Send the data using post
    var posting = $.post( url, {
        meta: meta,
        type: type,
        direction: direction,
        interval: interval,
        max_time: max_time,
        deep_depth: deep_depth,
        deep_window: deep_window,
        shallow_depth: shallow_depth,
        shallow_window: shallow_window,
        stall_timeout: stall_timeout,
        ramp_time: ramp_time,
        stop_check: stop_check,
        backtrack_time: backtrack_time,
        backtrack_count: backtrack_count,
        ctd_warmup_time: ctd_warmup_time,
        dpdt_threshold: dpdt_threshold
    });

    // Put the results in a div
    posting.done(function(data) {
        alert(data);
        var content = $(data);
        $("#message").append(content);
    });
    location.reload();
}

function updateProfile() {
    // Stop form from submitting normally
    //event.preventDefault();
    // Get some values from elements on the page:
    var $form = $('#profile-update-form'),
    meta = $form.find("input[name='meta']").val(),
    type = $form.find("input[name='type']").val(),
    direction = $form.find("input[name='direction']").val(),
    interval = $form.find("input[name='interval']").val(),
    max_time = $form.find("input[name='max_time']").val(),
    deep_depth = $form.find("input[name='deep_depth']").val(),
    deep_window = $form.find("input[name='deep_window']").val(),
    shallow_depth = $form.find("input[name='shallow_depth']").val(),
    shallow_window = $form.find("input[name='shallow_window']").val(),
    stall_timeout = $form.find("input[name='stall_timeout']").val(),
    ramp_time = $form.find("input[name='ramp_time']").val(),
    stop_check = $form.find("input[name='stop_check']").val(),
    backtrack_time = $form.find("input[name='backtrack_time']").val(),
    backtrack_count = $form.find("input[name='backtrack_count']").val(),
    ctd_warmup_time = $form.find("input[name='ctd_warmup_time']").val(),
    dpdt_threshold = $form.find("input[name='dpdt_threshold']").val(),
    url = document.location.href;

    // Send the data using post
    var posting = $.post( url, {
        meta: meta,
        type: type,
        direction: direction,
        interval: interval,
        max_time: max_time,
        deep_depth: deep_depth,
        deep_window: deep_window,
        shallow_depth: shallow_depth,
        shallow_window: shallow_window,
        stall_timeout: stall_timeout,
        ramp_time: ramp_time,
        stop_check: stop_check,
        backtrack_time: backtrack_time,
        backtrack_count: backtrack_count,
        ctd_warmup_time: ctd_warmup_time,
        dpdt_threshold: dpdt_threshold
    });

    // Put the results in a div
    posting.done(function(data) {
        alert(data);
        var content = $(data);
        $("#message").append(content);
    });

    // similar behavior as clicking on a link
    window.location.href = "/profile";
}

function savePattern() {
    // Stop form from submitting normally
    //event.preventDefault();
    // Get some values from elements on the page:
    var $form = $('#pattern-form'),
    meta = $form.find("input[name='meta']").val(),
    start_dt = $form.find("input[name='start_dt']").val(),
    stop_dt = $form.find("input[name='stop_dt']").val(),
    sequence = $form.find("input[name='sequence']").val(),
    type = $form.find("input[name='type']").val(),
    status = $form.find("input[name='status']").val(),
    url = '/createPattern';

    // Send the data using post
    var posting = $.post( url, {
        meta: meta,
        start_dt: start_dt,
        stop_dt: stop_dt,
        sequence: sequence,
        type: type,
        status: status
    });

    // Put the results in a div
    posting.done(function(data) {
        alert(data);
        var content = $(data);
        $("#message").append(content);
    });
    location.reload();
}

function updatePattern() {
    // Stop form from submitting normally
    //event.preventDefault();

    // Get some values from elements on the page:
    var $form = $('#pattern-update-form'),
    meta = $form.find("input[name='meta']").val(),
    start_dt = $form.find("input[name='start_dt']").val(),
    stop_dt = $form.find("input[name='stop_dt']").val(),
    sequence = $form.find("input[name='sequence']").val(),
    type = $form.find("input[name='type']").val(),
    status = $form.find("input[name='status']").val(),
    profiles = $form.find("select[name='profile_list']").val(),
    url = document.location.href;
    //alert($form.find("select[name='profile_list']").val());
    // Send the data using post
    var posting = $.post( url, {
        meta: meta,
        start_dt: start_dt,
        stop_dt: stop_dt,
        sequence: sequence,
        type: type,
        status: status,
        profiles: profiles
    });

    // Put the results in a div
    posting.done(function(data) {
        alert(data);
        var content = $( data );
        $("#message").append(content);
    });

    // similar behavior as clicking on a link
    window.location.href = "/pattern";
}
